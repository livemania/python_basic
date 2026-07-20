from langchain_classic import hub
from langsmith import Client
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0)

tools = [DuckDuckGoSearchRun()]

#랭체인(LangChain) 허브에서 원격 프롬프트를 풀(hub.pull)해올 때 발생하는 보안 강화로 인한 오류가 발생하는 것을 막기 위해 dangerously_pull_public_promt 옵션을 사용.
# 그러나 hub.pull 에서는 해당 옵션을 사용할 수 없음
#prompt = hub.pull("hwchase17/openai-tools-agent", dangerously_pull_public_prompt=True)
client = Client()
prompt = client.pull_prompt("hwchase17/openai-tools-agent", dangerously_pull_public_prompt=True)

agent = create_tool_calling_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

result = agent_executor.invoke({"input":"방콕의 현재 날씨를 알려줘"})
print(result["output"]);