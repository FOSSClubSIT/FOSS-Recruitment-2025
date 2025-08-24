import streamlit as st

st.title("Talk2PDF 💬")
st.write("Upload a PDF and chat with it!")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    st.success("File uploaded! You can now start chatting.")
    st.session_state.pdf_uploaded = True  # A flag to control UI flow

if "pdf_uploaded" in st.session_state:
    st.divider() # A horizontal line for visual separation

    user_question = st.text_input("Ask a question about your document:")

    if user_question:
        # This is where the AI magic will happen tomorrow!
        st.write("Processing your request...") # A temporary message

        # Placeholder for the final answer
        st.info("Answer will appear here. Stay tuned!")