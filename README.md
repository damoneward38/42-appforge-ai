# AppForge local rebuild

This is an independent development copy on the feature branch `feature/cybersecurity-workbench-both`. The original AppForge checkout and Base44 publication are not modified.

## Run locally

```bash
./start-local.sh
```

Open http://127.0.0.1:43101 for the existing AppForge generator, or http://127.0.0.1:43101/cybersecurity for the new Cybersecurity Workbench.

The server binds only to loopback. Do not expose it with a tunnel, router port-forward, or public deployment.

## Current functionality

- Preserves the recovered static AppForge generator at `index.html`.
- Adds a dedicated Cybersecurity Workbench page.
- Provides live TCP reachability checks for NeuralCore gateway/orchestrator, Sapphire port, and Ollama.
- Discovers installed Ollama models through the local Ollama tags API.
- Sends user prompts to Ollama's local chat API.
- Provides opt-in browser speech recognition and speech synthesis when supported.

## Not yet integrated

- Sapphire browser/computer-use API: port reachability is not proof of a working adapter.
- NeuralCore authenticated task/job API.
- Security tool registry, dispatcher, execution, audit trail, cancellation, and evidence pipeline.
- Authenticated public broker or multi-user deployment.

Tool execution is intentionally disabled. No host shell or Docker socket is exposed. Do not treat the dashboard as a completed security assessment platform.
