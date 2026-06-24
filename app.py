
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage

# Page Config
st.set_page_config(
    page_title="Groq Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI Chatbot")
st.write("Powered by Groq + LangChain")

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize LLM
llm = ChatGroq(
    groq_api_key="ur_secret_api_key",
    model_name="llama-3.3-70b-versatile",
    temperature=0.3
)

# Display Previous Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
user_input = st.chat_input("Type your message here...")

if user_input:

    # Store User Message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Display User Message
    with st.chat_message("user"):
        st.markdown(user_input)

    # Convert Chat History to LangChain Messages
    chat_history = []

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            chat_history.append(HumanMessage(content=msg["content"]))
        else:
            chat_history.append(AIMessage(content=msg["content"]))

    # Get Response
    response = llm.invoke(chat_history)

    bot_response = response.content

    # Store Assistant Response
    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )

    # Display Assistant Response
    with st.chat_message("assistant"):
        st.markdown(bot_response)
