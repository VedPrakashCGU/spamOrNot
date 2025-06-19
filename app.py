import streamlit as st
import pandas as pd
import pickle
model=pickle.load(open("model.pkl",'rb'))
vector=pickle.load(open("vector.pkl",'rb'))
def check(msg):
    user_vector=vector.transform([msg]).toarray()
    spamOrNot=model.predict(user_vector)
    return spamOrNot
    
    
st.title("Spam or NOt")
user_input = st.text_area("Enter your message here:")
if st.button("Check"):
    if user_input.strip()=="":
        st.warning("Enter the message")
    else:
        yesOrNot=check(user_input)
        if yesOrNot[0]==1:
            st.error("Message Spam")
        else:
            st.success("Message is not Spam")