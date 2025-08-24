import streamlit as st
import PyPDF2
import faiss

# This function extracts all text from a PDF file
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    return text

# This function splits a large text into smaller, overlapping chunks
def get_text_chunks(text, chunk_size=1000, chunk_overlap=200):
    chunks = []
    current_index = 0
    while current_index < len(text):
        chunk = text[current_index:current_index + chunk_size]
        chunks.append(chunk)
        current_index += chunk_size - chunk_overlap
    return chunks


from sentence_transformers import SentenceTransformer
import faiss

# This function creates and saves the vector database (FAISS index)
def create_and_save_vector_db(text_chunks, db_name="faiss_index"):
    # Load the sentence transformer model (runs offline)
    embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Create embeddings for all the text chunks
    embeddings = embedding_model.encode(text_chunks)
    
    # Create a FAISS index from the embeddings
    vector_db = faiss.IndexFlatL2(embeddings.shape[1])
    vector_db.add(embeddings)
    
    # Save the index to a file
    faiss.write_index(vector_db, db_name)
    print(f"Vector DB saved as {db_name}")

    return vector_db, embedding_model



st.title("Talk2PDF 💬")
st.write("Upload a PDF and chat with it!")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file:
    with st.spinner("Processing PDF..."):
        text = extract_text_from_pdf(uploaded_file)
        if text:
            chunks = get_text_chunks(text, chunk_size=1000, chunk_overlap=200)
            
            # Create and save the vector DB for the chunks
            db, model = create_and_save_vector_db(chunks)
            
            st.session_state.chunks = chunks
            st.session_state.db = db
            st.session_state.model = model
            st.success("File processed! You can now start chatting.")
            st.session_state.pdf_uploaded = True
        else:
            st.error("Could not extract text from the PDF. Please try a different file.")

if "pdf_uploaded" in st.session_state:
    st.divider() # A horizontal line for visual separation

    user_question = st.text_input("Ask a question about your document:")

    if user_question:
        st.write("Processing your request...") # A temporary message

        # Placeholder for the final answer
        st.info("Answer will appear here. Stay tuned!")