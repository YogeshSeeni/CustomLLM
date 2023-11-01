import time
import pathlib
import streamlit as st
from functions import add_website, initialize_vector_database, pass_prompt, add_pdf, initialize_llm
# Custom image for the app icon and the assistant's avatar
company_logo = 'https://www.app.nl/wp-content/uploads/2019/01/Blendle.png'

# Configure Streamlit page
st.set_page_config(
    page_title="CustomLLM",
    page_icon=company_logo
)

# Initialize LLM chain
llm = initialize_llm()
db = initialize_vector_database()

tmp_directory = "D:/Projects/Custom Large Language Models/tmp"

# Initialize chat history
if 'messages' not in st.session_state:
    # Start with first message from assistant
    st.session_state['messages'] = [{"role": "assistant", "content": "Welcome to CustomLLM! Upload documents or websites for more informed response, and ask away!"}]

if 'trained_files' not in st.session_state:
    st.session_state['trained_files'] = []

def display_trained_files():
    if st.session_state.trained_files:
        st.title("Trained Items:")
        for file_name in st.session_state.trained_files:
            st.write(file_name)
    else:
        st.write("No trained items available.")

with st.sidebar:
    with st.form("my-form", clear_on_submit=True):
        uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True, type=["pdf"])
        url = st.text_input('Enter URL')

        if st.form_submit_button("Train"):
            for uploaded_file in uploaded_files:
                save_path = pathlib.Path(tmp_directory, uploaded_file.name)

                with open(save_path, mode="wb") as w:
                    w.write(uploaded_file.getvalue())

                if save_path.suffix == ".pdf":
                    add_pdf(str(save_path), db)

                pathlib.Path.unlink(save_path)

                st.session_state.trained_files.append(uploaded_file.name)

        if len(url) > 0:
            add_website(url, db)
            st.session_state.trained_files.append(url)

        display_trained_files()


# Display chat messages from history on app rerun
# Custom avatar for the assistant, default avatar for user
for message in st.session_state.messages:
    if message["role"] == 'assistant':
        with st.chat_message(message["role"], avatar=company_logo):
            st.markdown(message["content"])
    else:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat logic
if query := st.chat_input("Ask me anything"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": query})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant", avatar=company_logo):
        message_placeholder = st.empty()
        # Send user's question to our chain
        response = pass_prompt(llm, query, db)
        full_response = ""

        # Simulate stream of response with milliseconds delay
        for chunk in response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)

    # Add assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})