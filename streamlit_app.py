import streamlit as st
import asyncio
import os

from config.openai_utilities import get_model_client
from team.analyzer_gpt import get_analyzer_gpt_team
from config.docker_utils import (
    getDockerCommandLineExecutor,
    start_docker_container,
    stop_docker_container,
)

from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult


# -----------------------------
# UI SETUP
# -----------------------------
st.title("Analyzer GPT - Digital Data Analyzer")

upload_file = st.file_uploader("Upload the CSV file", type="csv")
task = st.chat_input("Enter your task")


# -----------------------------
# SESSION STATE
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "autogen_team_state" not in st.session_state:
    st.session_state.autogen_team_state = None


# -----------------------------
# AGENT AVATARS / LABELS
# -----------------------------
AGENT_AVATARS = {
    "user": "👤",
    "Data_Analyzer_Agent": "📊",
    "Code_Executor_Agent": "⚙️",
    "Planner_Agent": "🧠",
}

AGENT_LABELS = {
    "Data_Analyzer_Agent": "Data Analyst",
    "Code_Executor_Agent": "Code Executor",
    "Planner_Agent": "Planner",
}


# -----------------------------
# RE-RENDER CHAT ON RERUN
# -----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar=msg["avatar"]):
        if msg.get("label"):
            st.markdown(f"**{msg['label']}**")
        st.markdown(msg["content"])


# -----------------------------
# CORE ASYNC RUNNER
# -----------------------------
async def run_analyzer_gpt(docker, openai_model_client, task):
    try:
        await start_docker_container(docker)
        team = get_analyzer_gpt_team(docker, openai_model_client)

        if st.session_state.autogen_team_state is not None:
            await team.load_state(st.session_state.autogen_team_state)

        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                role = "user" if message.source == "user" else "assistant"
                avatar = AGENT_AVATARS.get(message.source, "🤖")
                label = AGENT_LABELS.get(message.source)

                chat_msg = {
                    "role": role,
                    "avatar": avatar,
                    "label": label,
                    "content": message.content,
                }

                st.session_state.messages.append(chat_msg)

                with st.chat_message(role, avatar=avatar):
                    if label:
                        st.markdown(f"**{label}**")
                    st.markdown(message.content)

            elif isinstance(message, TaskResult):
                system_msg = {
                    "role": "system",
                    "avatar": "🛑",
                    "content": f"Stop Reason: {message.stop_reason}",
                }

                st.session_state.messages.append(system_msg)

                with st.chat_message("system", avatar="🛑"):
                    st.markdown(f"**Stop Reason:** {message.stop_reason}")

            st.session_state.autogen_team_state = await team.save_state()

        return None

    except Exception as e:
        return e

    finally:
        await stop_docker_container(docker)


# -----------------------------
# EXECUTION TRIGGER
# -----------------------------
if task:
    if upload_file is None:
        st.warning("Please upload the CSV file")
        st.stop()

    os.makedirs("temp", exist_ok=True)

    with open("temp/data.csv", "wb") as f:
        f.write(upload_file.getbuffer())

    openai_model_client = get_model_client()
    docker = getDockerCommandLineExecutor()

    error = asyncio.run(run_analyzer_gpt(docker, openai_model_client, task))

    if error:
        st.error(f"An error occurred: {error}")

    if os.path.exists("temp/output.png"):
        st.image("temp/output.png", caption="Analysis Output")
