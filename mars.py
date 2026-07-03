import streamlit as st

#take a user import\
st.title("take the input")
name=st.text_input("enter your name")

if st.button("submit"):
  st.write(f"print the name:{name}")
