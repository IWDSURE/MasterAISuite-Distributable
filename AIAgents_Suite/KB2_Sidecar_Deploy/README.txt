# KB2 Sidecar Portable Deployment

This folder contains everything needed to run the KB2 Embedding Sidecar.

## Contents
1. `START_SIDECAR.bat`: Cleans port 5002 and launches the sidecar.
2. `STOP_SIDECAR.bat`: Stops the sidecar on port 5002.
3. `kb2_embed_server.py`: The sidecar server code.
4. `kb2_gateway.py`: The KB2 logic required by the server.

## Instructions
1. Copy this entire folder (`KB2_Sidecar_Deploy`) to any location on your machine.
2. Double-click `START_SIDECAR.bat` to launch the server.
3. Wait for the new window to show "Model ready" (approx. 30 seconds).
4. Use `STOP_SIDECAR.bat` when you are finished.

## Port
- **Sidecar**: Port 5002 (Required for semantic search in KB2).
