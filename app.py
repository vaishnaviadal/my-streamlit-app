import streamlit as st

st.title("Hello, Streamlit!")
x = st.slider("Select a value", 0, 100, 50)
st.write(f"The square of {x} is {x * x}")
