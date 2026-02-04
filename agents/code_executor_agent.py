
from autogen_agentchat.agents import CodeExecutorAgent
import asyncio
from autogen_agentchat.messages import TextMessage
from autogen_core import CancellationToken
from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor

def GetCodeExecutorAgent(code_executor):

    code_executor_agent = CodeExecutorAgent(
        name='CodeExecutor',
        code_executor = code_executor
    )
    
    return code_executor_agent

async def main():
    docker= DockerCommandLineCodeExecutor(
    work_dir='temp',
    timeout=120
)

    await docker.start()

    code_executor_agent = GetCodeExecutorAgent(docker)

    task = TextMessage(
        content=''' Here is the python code which you have to run
```python
print('Hello World')
``` 
    ''',
source='user'
    )

    try:
        res = await code_executor_agent.on_messages(
            messages=[task],
            cancellation_token=CancellationToken()
        )
        print('result is:',res)
    except Exception as e:
        print('Exception:',e)
    finally:
        await docker.stop()


if (__name__ == '__main__'):
    asyncio.run(main())







