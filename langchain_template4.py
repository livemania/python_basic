from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
)
from langchain_core.messages import SystemMessage, HumanMessage
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate

from langchain_google_genai import ChatGoogleGenerativeAI

#from langchain_classic.chains import LLMChain

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template("당신은 {country} 요리 전문가 입니다."),
    HumanMessagePromptTemplate.from_template("다음 요리의 레시피를 생각해 주세요.\n\n요리 : {dish}")
])

messages = chat_prompt.format_messages(country="중국", dish="마라탕")

print(messages)

class Recipe(BaseModel):
    ingredients: list[str] = Field(description="ingredient of the dish")
    steps: list[str] = Field(description = "steps to make the dish")

# 위에서 생성한 Recipe 클래스를 넘겨서 PydanticoutputParser 를 생성함.

parser = PydanticOutputParser(pydantic_object=Recipe)
format_instructions = parser.get_format_instructions()
print(format_instructions)

# 포맷팅이된 프롬프트를 생성해 봄. 이 PromptTemplate 에 입력에 대한 예시로 "마라탕"을 추가해 봄.
template = """
    다음 요리의 레시피를 생각해 주세요.

    {format_instructions}

    요리 : {dish}
"""

prompt = PromptTemplate(
    template = template,
    input_variables = ["dish"],
    partial_variables = {"format_instructions" : format_instructions},
)

formatted_prompt = prompt.format(dish="마라탕")
print(formatted_prompt)

# Recipe 의 클래스의 정의에 따라 출력형식을 지정하는 프롬프트가 내장되었음. 이 텍스트를 입력해서 LLM 을 실행해 봄.
chat = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0)
messages = [HumanMessage(content=formatted_prompt)]
output = chat.invoke(messages)
#print(output)

# 위의 응답을 Pydantic 의 클래스로 변환해서 사용하면 편함.
# PydanticOutputParser 를 사용하면 그 변환과정도 간단함.
# output.content 에서 실제 텍스트만 꺼내서 파싱해야 함. 
if isinstance(output.content, list):
    text_response = output.content[0].get("text","")
else:
    text_response = output.contetn

# parser.parse()는 순수 문자열을 기대하기 때문에 list로 넘어오면 Pydantic 이 "string이 아니고 list다" 라고 에러를 냄.
#recipe = parser.parse(text_response)
#print(type(recipe))
#print(recipe)

# LangChain 이라는 단어의 의미에서 보이는 것처럼 LLM 에 단순하게 입력해서 출력을 얻고 끝나는 것이 아니라 처리를 연속적으로 연결할 수 있음.
# 아래 코드는 LLMChain 을 사용하는 코드임. OutputParser, PromptTemplate, Language Model 을 준비함.

chain = prompt | chat | parser

recipe = chain.invoke("짬뽕")

print(type(recipe))
print(recipe)