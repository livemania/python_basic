from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

prompt = ChatPromptTemplate.from_template("You are export in UI/UX Answer the question. <Question>: {input}")

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

chain = prompt | llm

response = chain.invoke({"input": "최근 아이폰의 UX에 대해서 설명해줘"})

print(response.content)