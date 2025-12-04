import streamlit as st

from agents.technical_agent import TechnicalAgent
from agents.behavioral_agent import BehavioralAgent
from agents.scenario_agent import ScenarioAgent

# Page Setup
st.set_page_config(page_title="Interview Question Generator Suite", layout="wide")

st.title("🎯 Interview Question Generator Suite")
st.subheader("Powered by Ollama + Python + Streamlit")
st.markdown("---")

role = st.text_input("Enter the job role (e.g., Backend Engineer, Data Scientist):")

model = st.selectbox(
    "Choose Ollama Model",
    ["llama3", "mistral", "gemma", "llama2", "mixtral"]
)

st.markdown("---")

col1, col2, col3 = st.columns(3)

# Agents
tech_agent = TechnicalAgent(model)
beh_agent = BehavioralAgent(model)
sc_agent = ScenarioAgent(model)

# Technical Questions
with col1:
    st.header("🔵 Technical Questions")
    if st.button("Generate Technical Questions"):
        if role.strip():
            questions = tech_agent.generate(role)
            st.write(questions)
        else:
            st.error("Please enter a role.")

# Behavioral STAR Questions
with col2:
    st.header("🟢 Behavioral (STAR) Questions")
    if st.button("Generate Behavioral Questions"):
        questions = beh_agent.generate()
        st.write(questions)

# Scenario-Based Questions
with col3:
    st.header("🔴 Scenario-Based Questions")
    if st.button("Generate Scenario Questions"):
        if role.strip():
            questions = sc_agent.generate(role)
            st.write(questions)
        else:
            st.error("Please enter a role.")
