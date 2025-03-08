import streamlit as st
import openai

# Initialize OpenAI API Key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Set the chatbot title
st.title("Elephant ChatBot")  # Change this to your preferred chatbot name

# Initialize chat history with system message for context
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are an expert assistant who ONLY talks about elephants. If asked anything else, politely redirect the conversation to elephants."}
    ]

# Display chat history
for message in st.session_state.messages:
    if message["role"] != "system":  # Hide system messages
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User input box
user_input = st.chat_input("Type your message...")

# Function to get response from OpenAI
def get_response(conversation):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    return response["choices"][0]["message"]["content"]

# Handle user input
if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get assistant response
    response = get_response(st.session_state.messages)

    # Append assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(response)
