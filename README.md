# ngrokWifiTelemetrySnapshot
This application demonstrates to capture snapshots from from any mobile controlled using limit switch, to demonstrate WIFI and RF 900 communications.

## Remote Camera Snapshot with Limit Switch and Long-Range Telemetry
In this demonstration project, a limit switch is connected to an Arduino microcontroller. The primary function of the limit switch is to remotely trigger a snapshot from a camera connected to a server, using a two-step communication process:
- **Long-Range Telemetry (30 km Line-of-Sight):**
  - When the limit switch is pressed, the Arduino sends a trigger signal over a 30 km LOS (Line-of-Sight) telemetry link.
  - This link ensures reliable, low-latency communication between the remote Arduino and the ground server, even over large distances.
- **Server and Gradio Web Application:**
  - The server hosts a Python-based Gradio application.
  - The server runs locally, but is exposed to the public internet using NGROK, which generates a secure, shareable public URL.
  - Any user, anywhere in the world, can access the Gradio app via the NGROK URL to monitor the camera status and view snapshots.
### Snapshot Capture and Storage:
- Upon receiving the trigger signal from the limit switch (via the telemetry link and server), the Gradio app activates the camera to capture a snapshot.
- The captured photos are automatically saved in the application’s directory for later review or download.
### Key Features
- Remote physical triggering (via limit switch and Arduino)
- Reliable long-range wireless communication (up to 30 km LOS telemetry)
- Global web access (Gradio + NGROK public URL)
- Automated photo capture and storage on the server
### Typical Use Cases
- Remote equipment monitoring
- Security and surveillance
- Environmental research (wildlife, weather, etc.)
- Industrial automation snapshots

Demonstration
