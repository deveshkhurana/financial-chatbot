import streamlit as st
import requests

# Your Endpoint Details 
endpoint_url = "https://vkvtumyy7shq53yv.us-east-1.aws.endpoints.huggingface.cloud"
advisor_context = """Assume the role of a seasoned financial advisor with a strong understanding of investment strategies, 
budgeting, and retirement planning and answer the questions asked by a young adults who has just started earning. Make sure the response is designed for 
general purpose use case, talk about benefits of stock investments, dividends, fixed deposits, mutual funds, etc.
ask questions to the user like what is their income, if they have not provided, how much are they willing to invest, how much risk they want in their investment etc. Be proactive 
and try to help the user who is asking the question as a friendly financial advisor """  

# Streamlit Title
st.title("Financial Chatbot Assistant") 

# User Input
user_input = st.text_input("Ask your financial question: ")

# Interaction Logic
if user_input: 
    st.write("Bot: Thinking...") 

    # Construct the payload 
    payload = {"inputs": advisor_context + user_input}

    # Send the request 
    response = requests.post(endpoint_url, json=payload)

    # Extract and display the response
    if response.status_code == 200:
        bot_response = response.json()["generated_text"]  # Adjust if needed 
        st.write("Bot:", bot_response)
    else:
        st.write("Bot: There seems to be an error. Please try again.") 
