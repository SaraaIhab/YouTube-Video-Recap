import gradio as gr
from backend import app, get_transcript, add_transcript_to_app

def random_response(message, history):
        return app.query(message)

with gr.Blocks() as demo:
    gr.Markdown("# 🎥 YouTube Transcript Chat")

    with gr.Row():
        video_input = gr.Textbox(label="Enter YouTube Video ID (e.g., dQw4w9WgXcQ)")
        load_button = gr.Button("Load Transcript")

    transcript_status = gr.Textbox(label="Status", interactive=False)

    load_button.click(fn=add_transcript_to_app, inputs=video_input, outputs=transcript_status)

    gr.Markdown("---")

    chatbot = gr.ChatInterface(fn=random_response)

demo.launch()
