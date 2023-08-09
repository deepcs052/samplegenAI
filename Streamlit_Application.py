import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
os.environ["OPENAI_API_KEY"] = "sk-"
llm = OpenAI(temperature=0.7,model_name="gpt-3.5-turbo")
st.header("Test Scenario Generation using GenAI ")
option = st.sidebar.selectbox("Output Type", ("Decision Table", "Use cases"))
req = st.text_input("Type your requirement here:", key="req")
#st.session_state.req

st.sidebar.write("Application Modes")
appflow1 = st.sidebar.checkbox("Intake")
appflow2 = st.sidebar.checkbox("RAC")
appflow3 = st.sidebar.checkbox("Renewals")

if appflow1:
    appflow1 = "Intake"
else:
    appflow1 = None
if appflow2:
    appflow2 = "RAC"
else:
    appflow2 = None
if appflow3:
    appflow3 = "Renewals"
else:
    appflow3 = None

if option and req:
    st.write("--**--Below are the scenarios--**--")
    prompt = PromptTemplate(input_variables=["outputtype", "req", "appflow1", "appflow2", "appflow3"],
                            template="create {outputtype} for requirement {req}. Consider different application flows as {appflow1},{appflow2},{appflow3}")
    #st.write(prompt.format(outputtype=option, req=req))
    scenario = llm(prompt.format(outputtype=option, req=req, appflow1=appflow1, appflow2=appflow2, appflow3=appflow3))
    st.write(scenario)
