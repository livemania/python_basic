from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

#print(os.getenv("GOOGLE_API_KEY"))

# Google Gemini 모델 연결.
llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

response = llm.invoke("한국인이 한달 살기를 할 수 있는 동남아 도시 3개를 추천해 줘")

print(response.content)