import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from rich.prompt import Prompt
from rich.console import Console
import streamlit as st

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
console = Console()


system_instruction = ("You are friendly buddy for the students from schooling to undergraduation."
                      "ask clarifying questions what ever they ask and keep answers concise (<= 150)."
)

chat = client.chats.create(
model="gemini-2.5-flash",
config=types.GenerateContentConfig(
system_instruction=system_instruction,
temperature=0.6,
),
history=[],
)


st.set_page_config(page_title="FRIENDly  - Your AI Friend", layout="centered")
st.markdown(
    """
    <style>
    .stChatMessage {
        background-color: #E6F7FF !important; /* very light sky blue */
        border-radius: 12px;
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("FRIENDly")
st.markdown("### Your friendly buddy for **career, health, and academics**.")
# Chat history container
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# User input box
if user_input := st.chat_input("Ask me anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    # Get response from Prendly
    response = chat.send_message(user_input)

    # Add assistant response
    bot_reply = response.text
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.chat_message("assistant").markdown(bot_reply)



console.print("[bold green]FRIENDly ready. Type 'exit' to quit.[/bold green]")
while True:
    user_msg = Prompt.ask("[bold cyan] You [/bold cyan]")
    if user_msg.strip().lower() in {"exit", "quit"}:
        break
    resp = chat.send_message(user_msg)
    console.print(f"[bold yellow] FRIENDly [/bold yellow]: {resp.text}\n")
