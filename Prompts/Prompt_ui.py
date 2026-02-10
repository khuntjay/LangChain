from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

# Load Key
load_dotenv()

# Load Model
model = ChatOpenAI()


# Create Streamlit app 
st.header("Type Your Text")
input  = st.text_area("enter text")


if st.button("Summarize"):
    result = model.invoke(input)
    st.write(result.content)
