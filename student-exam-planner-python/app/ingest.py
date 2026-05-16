from dotenv import load_dotenv
load_dotenv()
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

loader = PyPDFLoader("./data/os.pdf")
pages = loader.load()
print(f"Loaded {len(pages)} pages")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = splitter.split_documents(pages)
print(f"Total chunks: {len(chunks)}")

db = Chroma.from_documents(
    documents=chunks,
    collection_name="student_docs",
    persist_directory="./chroma_db"
)

print(f"Ingestion complete. Total documents stored: {db._collection.count()}")
