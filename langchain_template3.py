from langchain_core.prompts import PromptTemplate

template = """
요리 레시피를 생각해 봅니다.

요리 : {dish}
"""

prompt = PromptTemplate(
    template = template,
    input_variables= ["dish"]
)

result = prompt.format(dish="마라탕")
print(result)