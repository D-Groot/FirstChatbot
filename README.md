# FirstChatbot
# FRIENDly 🤝
Students often hesitate to ask questions related to career, mental health, or academics. FRIENDly acts as a companion chatbot that answers in a supportive, simple, and concise manner.

The project offers:

A web-based interface built with Streamlit.

Interactive chat-like experience with session memory.

Customizable design (light sky-blue chat bubbles for readability).

# Features

Acts as a student-friendly buddy

Provides short and supportive answers (≤ 150 characters)

Clean and simple chat interface

Maintains chat history within a session

Powered by Google Gemini 2.5 Flash model

Environment variable support for secure API key storage

# Demo

Once deployed, you can access FRIENDly via a browser.

Run it locally and open:

http://localhost:8501


You’ll see:

Input field to ask questions

Chat history displayed like a messaging app

Bot responses with a typing indicator

# Installation
1. Clone the repository
git clone https://github.com/D-Groot/Firstchatbot.git
cd FirstChatbot

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Set up environment variables

Create a .env file in the project root and add your Google Gemini API key:

GEMINI_API_KEY=your_api_key_here

5. Run the app
streamlit run app.py



# Tech Stack

Python – Core language

Streamlit – Interactive UI framework

Google Gemini API – AI model for chat

python-dotenv – Environment variable management

Rich – Console styling (optional, for fallback mode)

# Future Enhancements

Add sidebar controls (reset chat, theme switch, quick prompts)

Support for multi-language conversations

Deploy to Streamlit Cloud / Hugging Face Spaces

Save chat history across sessions in a database

# Contributing

Contributions are welcome!

Fork the project

Create a new branch (feature/your-feature)

Commit your changes

Push to the branch

Open a Pull Request

# License

This project is licensed under the MIT License.
You’re free to use, modify, and distribute it with attribution.

Made with care to support students everywhere.
