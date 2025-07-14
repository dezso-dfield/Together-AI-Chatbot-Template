import os
from dotenv import load_dotenv
from together import Together
import gradio as gr


load_dotenv()
API_KEY = os.getenv("TOGETHER_API_KEY")

client = Together(api_key=API_KEY)

def load_prompt(path="prompt.txt"):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        raise RuntimeError("Missing {path}. Create \"prompt.txt\".")
    
SYSTEM_PROMPT = load_prompt()

def chat(message, history):
    if history is None:
        history = []
        
    history.append({"role": "user", "content": message})
    
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + history
    
    response = client.chat.completion.create(
        model = "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages = messages
    )
    
    assistant_messages = response.choices[0].message.content
    
    history.append({"role": "assistant", "content": assistant_messages})
    
    return history, history

css = """
    body { background:#ffffff;font-family: Arial, sans-serif; }
    .container { max-width:800px; margin:auto; }
    .message.user { background: #ffffff; border: 1px solid #000000; color: #000000; }
    .message.assistant { background: #0000ff; border: 1px solid #0000ff; color: #ffffff; }
    .message { border-radius: 8px; padding: 10px; margn: 5px 0px; }
    .chatbot { border-radius: 12px; padding: 10px; }
    .textbox { border-radius: 12px; padding: 10px; width: 100%; }
    .button { background: #0000ff; color: white; border-radius: 6px; padding: 10px; cursor: pointer; }
    button:disabled { background: #999999; cursor: not-allowed; }
"""

def main():
    with gr.Blocks(css=css) as demo:
        gr.Markdown("## Chatbot")
        
        chatbot = gr.Chatbot(type="messages", elem_classes="chatbot", height=500)
        
        user_input = gr.Textbox(placeholder="Type your message here...", elem_classes="textbox", interactive=True)
        
        send_button = gr.Button("Send", elem_classes="button")
        
        send_button.click(chat, [user_input, chatbot], [chatbot, chatbot])
        user_input.submit(chat, [user_input, chatbot], [chatbot, chatbot])
        
        gr.Markdown("Type \"exit\" or \"quit\" to end the chat.")
        
        demo.launch()
    
if __name__ == '__main__':
    main()
