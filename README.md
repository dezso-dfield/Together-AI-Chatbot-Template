Usage
Follow these steps to get your Together AI Chatbot up and running:

1. Obtain Your Together AI API Key

Register/Log In: Visit the Together AI website and log in or create an account.

Generate Key: Navigate to your API Keys section (usually in your dashboard or settings) and generate a new API key.

Copy Key: Copy the generated API key.

2. Configure Your .env File

Create .env: In the root directory of your project, create a file named .env.

Add API Key: Open .env and add your API key:

TOGETHER_API_KEY=YOUR_TOGETHER_AI_API_KEY

Replace YOUR_TOGETHER_AI_API_KEY with the key you copied.

3. Define Your Chatbot's Persona in prompt.txt

Create prompt.txt: In the same directory as your Python script, create a file named prompt.txt.

Insert Prompt: Paste your desired chatbot persona and instructions (like the "Coach Max" prompt) into this prompt.txt file. This content will define your chatbot's behavior and tone.

4. Run the Chatbot

Install Dependencies: Make sure you have the necessary Python libraries installed:

pip install -r requirements.txt

Execute Script: Run your main Python script from your terminal:

python3 main.py

(Replace your_chatbot_script_name.py with the actual name of your Python file, e.g., app.py or main.py).

Your Gradio chatbot interface will then launch in your web browser, allowing you to interact with your AI assistant!

