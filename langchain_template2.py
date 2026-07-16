from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

chat = ChatGoogleGenerativeAI(model="gemini-3.5-flash")

chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "이 시스템은 여행 전문가입니다."),
    ("user", "{user_input}"),
])

chain = chat_prompt | chat

response = chain.invoke({"user_input":"한국인이 방문하기에ㅐ 좋은 라오스의 3군데 관광지를 추천해 주세요."})

print(response.content)
