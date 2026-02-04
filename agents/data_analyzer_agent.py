from autogen_agentchat.agents import AssistantAgent
from agents.prompts.DataAnalyzerAgentprompt import DATA_ANALYZER_MSG


def GetDataAnalyzerAgent(model_client):
    data_analyzer_agent = AssistantAgent(
        name='Data_Analyzer_Agent',
        model_client=model_client,
        system_message=DATA_ANALYZER_MSG
    )

    return data_analyzer_agent
