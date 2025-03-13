import os
import gradio as gr
from modules import script_callbacks

# This function is called when the "Restart" button is clicked.
def restart_app():
    # Immediately exits the application
    os._exit(0)

def on_ui_tabs():
    print("Restart extension on_ui_tabs() called")
    with gr.Blocks() as zrestart_ui:
        gr.Markdown("## 重启WebUI应用程序")
        gr.Markdown("点击重启, WebUI 会退出, 切换到GPU的详情页面,可以查看启动的日志.<br/> 如果出现 *Running on local URL:  http://0.0.0.0:3000* 字样, 就代表启动成功,可以刷新页面,重启完成 <br/> \n\n---\n\n  请注意观察运行日志,重启完成后才可以刷新页面, 否则会出现白屏")
        gr.Button("重启").click(fn=lambda: os._exit(0), inputs=[], outputs=[])
    return (zrestart_ui, "退出WebUI", "zrestart_ui"),


script_callbacks.on_ui_tabs(on_ui_tabs)

