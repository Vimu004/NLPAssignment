import streamlit as st
import requests
import uuid  

st.set_page_config(page_title="SL Chatbot")

def generate_new_session_id():
    return str(uuid.uuid4())  

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to Sri Lanka's SL Chatbot."},  
    ]
    st.session_state.session_id = generate_new_session_id()  

def send_message_to_api(message):
    try:
        response = requests.post(
            "http://127.0.0.1:5000/predict",
            json={"message": message}
        )
        response.raise_for_status()
        return response.json().get("answer", "Sorry, I didn't understand that.") 
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err}"
    except requests.exceptions.ConnectionError:
        return "Connection error. Please check if the server is running."
    except requests.exceptions.Timeout:
        return "The request timed out. Please try again."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def reset_conversation():
    st.session_state.messages = [
        {"role": "assistant", "content": "Welcome to Sri Lanka's SL Chatbot."} 
    ]
    st.session_state.session_id = generate_new_session_id()  

if st.button("Reset Chat"):
    reset_conversation()  

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if prompt := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = send_message_to_api(prompt)  

            if response:
                response_lines = response.split("\n")
                for line in response_lines:
                    st.write(line)
            else:
                st.write("Sorry, I didn't receive a valid response.")

    message = {"role": "assistant", "content": response}
    st.session_state.messages.append(message)
