#!/usr/bin/env python3
"""Loopback-only AppForge gateway with a deliberately narrow action allowlist."""
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from pathlib import Path
import json, socket, os, time

ROOT = Path(__file__).resolve().parent
OLLAMA = os.environ.get("OLLAMA_URL", "http://127.0.0.1:11434")
SERVICES = {"NeuralCore gateway": ("127.0.0.1", 8766), "NeuralCore orchestrator": ("127.0.0.1", 8765), "Sapphire HTTPS": ("127.0.0.1", 3080), "Ollama": ("127.0.0.1", 11434)}
ACTIONS = {"check_local_services": "Read-only reachability check for the four configured local services."}

def probe(host, port, timeout=0.6):
    try:
        with socket.create_connection((host, port), timeout=timeout): return True
    except OSError: return False

def service_report():
    return {name: {"reachable": probe(*addr), "address": f"{addr[0]}:{addr[1]}"} for name, addr in SERVICES.items()}

class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs): super().__init__(*args, directory=str(ROOT), **kwargs)
    def send_json(self, code, data):
        raw = json.dumps(data).encode()
        self.send_response(code); self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(raw))); self.send_header("Cache-Control", "no-store")
        self.end_headers(); self.wfile.write(raw)
    def read_body(self, limit=20000):
        size = int(self.headers.get("Content-Length", "0"))
        if size < 2 or size > limit: raise ValueError("Invalid request size")
        return json.loads(self.rfile.read(size))
    def do_GET(self):
        if self.path == "/api/status":
            states = service_report(); models = []
            if states["Ollama"]["reachable"]:
                try:
                    with urlopen(OLLAMA + "/api/tags", timeout=2) as resp:
                        models = [m.get("name") for m in json.load(resp).get("models", [])]
                except Exception: pass
            self.send_json(200, {"services": states, "ollama_models": models,
                "computer_use": "Not connected: Sapphire adapter requires authenticated browser session",
                "tool_dispatch": "Only the read-only local service diagnostic is enabled",
                "server": "AppForge local development gateway", "binding": "127.0.0.1",
                "actions": ACTIONS}); return
        if self.path == "/": self.path = "/index.html"
        if self.path == "/cybersecurity": self.path = "/cybersecurity/workbench.html"
        return super().do_GET()
    def do_POST(self):
        if self.path == "/api/actions/run":
            try: body = self.read_body(4096)
            except Exception as e: return self.send_json(400, {"error": str(e)})
            action = body.get("action")
            if action not in ACTIONS: return self.send_json(403, {"error": "Action is not in the server allowlist"})
            result = {"action": action, "description": ACTIONS[action], "checked_at": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "services": service_report(), "execution": "read-only"}
            print("AUDIT action=" + action + " result=completed")
            return self.send_json(200, result)
        if self.path != "/api/chat": return self.send_json(404, {"error": "Not found"})
        if not probe("127.0.0.1", 11434): return self.send_json(503, {"error": "Ollama is not reachable"})
        try:
            body = self.read_body()
            prompt = str(body.get("prompt", "")).strip(); model = str(body.get("model", "")).strip()
            if not prompt or len(prompt) > 12000 or not model: return self.send_json(400, {"error": "A model and prompt of at most 12000 characters are required"})
            payload = json.dumps({"model": model, "messages": [
                {"role": "system", "content": "You are the local AppForge assistant. Give defensive, authorized cybersecurity guidance. Do not claim to execute tools or control a browser. Tool execution is not available through chat."},
                {"role": "user", "content": prompt}], "stream": False}).encode()
            req = Request(OLLAMA + "/api/chat", data=payload, headers={"Content-Type": "application/json"})
            with urlopen(req, timeout=120) as resp: data = json.load(resp)
            self.send_json(200, {"response": data.get("message", {}).get("content", ""), "model": model, "provider": "Ollama local"})
        except HTTPError as e: self.send_json(502, {"error": f"Ollama returned HTTP {e.code}"})
        except Exception as e: self.send_json(502, {"error": f"Local model request failed: {type(e).__name__}"})
    def log_message(self, fmt, *args): print("%s - %s" % (self.client_address[0], fmt % args))

if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 43101), Handler)
    print("AppForge local server: http://127.0.0.1:43101 (loopback only)")
    server.serve_forever()
