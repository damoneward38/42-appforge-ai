#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"
if lsof -nP -iTCP:43101 -sTCP:LISTEN >/dev/null 2>&1; then
  echo "Port 43101 is already in use. Check http://127.0.0.1:43101"
  exit 1
fi
exec python3 server.py
