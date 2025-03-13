import os
import gradio as gr
from modules import script_callbacks

# This function is called when the "Restart" button is clicked.
def restart_app():
    # Immediately exits the application
    os._exit(0)

def on_ui_tabs():
    print("Restart extension on_ui_tabs() called")
    with gr.Blocks() as restart_ui:
        gr.Markdown("## Restart Application")
        gr.Button("Restart").click(fn=lambda: os._exit(0), inputs=[], outputs=[])
    return (restart_ui, "Restart", "restart_ui"),


script_callbacks.on_ui_tabs(on_ui_tabs)

