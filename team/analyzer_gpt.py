from agents.code_executor_agent import GetCodeExecutorAgent
from agents.data_analyzer_agent import GetDataAnalyzerAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination

def get_analyzer_gpt_team(docker,model_client):

    code_executor_agent = GetCodeExecutorAgent(docker)

    data_analyzer_agent = GetDataAnalyzerAgent(model_client)
    text_mention_termination = TextMentionTermination('STOP')

    team = RoundRobinGroupChat(
        participants=[data_analyzer_agent, code_executor_agent],
        max_turns=15,
        termination_condition=text_mention_termination
    )

    return team



    