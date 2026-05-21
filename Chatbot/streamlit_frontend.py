import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

CONFIG = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

#loading the conversation hostory
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
            st.text(message['content'])

user_input = st.chat_input("Ask a question")

if user_input:
    #first add message to history
    st.session_state['message_history'].append({'role':'user', 'content': user_input})
    with st.chat_message('user'):
        st.text(user_input)

    #then send the request to chatbot
    response = chatbot.invoke({'messages': [HumanMessage(content=user_input)]}, config=CONFIG)

    ai_message = response['messages'][-1].content
    #fisrt add message to message_histoy

    st.session_state['message_history'].append({'role':'assistant', 'content': ai_message})
    with st.chat_message('assistant'):
        st.text(ai_message)