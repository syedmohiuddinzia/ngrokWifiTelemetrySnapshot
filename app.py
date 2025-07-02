import gradio as gr
import numpy as np
import threading
import serial
import time
import cv2
from datetime import datetime
import os

latest_frame = None
last_saved_filename = None

def update_latest_frame(frame):
    global latest_frame
    if frame is not None and np.mean(frame) > 10:
        latest_frame = frame
        print("Got a frame! Mean pixel value:", np.mean(frame))
    return frame

def save_snapshot():
    global latest_frame, last_saved_filename
    if latest_frame is not None and np.mean(latest_frame) > 10:
        filename = f"snapshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        cv2.imwrite(filename, cv2.cvtColor(latest_frame, cv2.COLOR_RGB2BGR))
        last_saved_filename = filename
        print("Photo saved to", filename)
    else:
        print("No valid frame to save.")

def monitor_serial():
    try:
        ser = serial.Serial('/dev/ttyUSB0', 57600, timeout=1)
        print("[Serial] Connected to /dev/ttyUSB0!")
        while True:
            data = ser.read()
            if data == b'c':
                print("[Serial] Received 'c' from serial, attempting to save photo...")
                save_snapshot()
            time.sleep(0.05)
    except Exception as e:
        print("[Serial] Connection error:", e)

def get_last_snapshot():
    global last_saved_filename
    if last_saved_filename and os.path.exists(last_saved_filename):
        return last_saved_filename
    else:
        return None

with gr.Blocks() as demo:
    img = gr.Image(
        sources=["webcam"], type="numpy", streaming=True, 
        label="Webcam Stream (should be live)",
        height=240, width=320
    )
    img.stream(update_latest_frame, inputs=img, outputs=img)
    gr.Image
    gr.Markdown("### Last Saved Photo (Click Refresh Below)")
    snapshot_img = gr.Image(label="Last Snapshot", interactive=False)
    refresh_btn = gr.Button("Refresh Last Snapshot")
    refresh_btn.click(get_last_snapshot, inputs=None, outputs=snapshot_img)

threading.Thread(target=monitor_serial, daemon=True).start()
demo.launch()

