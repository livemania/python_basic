from langchain_community.document_loaders import GitLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

def file_filter(file_path):
    return file_path.endswith(".md")

loader = GitLoader(
    clone_url = "https://github.com/langchain-ai/langchain",
    repo_path = "./langchain",
    branch = "master",
    file_filter = file_filter,
)

raw_docs = loader.load()
#print(raw_docs)

# 문서 변환.
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

docs = text_splitter.split_documents(raw_docs)

#len(docs)

#embeddings = GoogleGenerativeAIEmbeddings(model="text-embeding-004")
# text-embedding-004 는 이전 모델로 지원 중단. gemini-emgedding-2 를 사용.
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2")

#query = "AWS S3에서 데이터를 불러올 수 있는 DocumentLoader 가 있나요?"
#vector = embeddings.embed_query(query)
#print("==="*10,"len(vector)")
#print(len(vector))
#print("---"*10, "vector")
#print(vector)

# 청크로 분할한 문서와 Text embedding model 을 기반으로 벡터 스토어를 초기화 함.
db = Chroma.from_documents(docs, embeddings)

# 벡터 스토어에서는 사용자의 입력과 관련된 문서를 가져오는 작업을 실행함.
# LangChain 에서 텍스트와 관련되 문서를 가져오는 인터페이스를 Retriever 라고 함.
retriever = db.as_retriever()

# Retriever 를 사용해서 "AWS S3 에서 데이터를 불러오는 DocumentLoader가 있나요?"라는 질문과 유사한 문서를 검색해 봄.
query = "AWS S3 에서 데이터를 불러올 수 있는 DocumentLoader 가 있나요?"
context_docs = retriever.get_relevant_documents(query)

print(f"len= {len(context_docs)}")

first_doc = context_docs[0]
print(f"metadata = {first_doc.metadata}")
print(first_doc.page_content)