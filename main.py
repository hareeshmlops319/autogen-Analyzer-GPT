import asyncio
from team.analyzer_gpt import get_analyzer_gpt_team
from agents.data_analyzer_agent import GetDataAnalyzerAgent
from agents.code_executor_agent import GetCodeExecutorAgent
from config.openai_utilities import get_model_client
from config.docker_utils import getDockerCommandLineExecutor,start_docker_container,stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

async def main():
    openai_model_client=get_model_client()
    docker=getDockerCommandLineExecutor()
    
    team = get_analyzer_gpt_team(docker,openai_model_client)

    try:
        task = 'can you give me a graph of survived and died in my data data.csv and save it as output.png'

        await start_docker_container(docker)

        async for message in team.run_stream(task=task):
            print('='*40)
            if isinstance(message,TextMessage):
                print(message.source, ":", message.content)
            elif isinstance(message,TaskResult):
                print("stop Reason :" , message.stop_reason)
    except Exception as e:
        print(e)
    finally:
        await stop_docker_container(docker)





if (__name__=='__main__'):
    asyncio.run(main())