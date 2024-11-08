import os
from openai import AzureOpenAI
import streamlit as st
import json
import time
from dotenv import load_dotenv

from azure.ai.inference import ChatCompletionsClient
from azure.core.credentials import AzureKeyCredential
from azure.ai.inference.models import (
    SystemMessage,
    UserMessage,
    TextContentItem,
    ImageContentItem,
    ImageUrl,
    ImageDetailLevel,
)

#Use GitHub Token to access the Azure OpenAI service
load_dotenv()
token = os.getenv("GITHUB_TOKEN")
if not token:
    raise ValueError("GITHUB_TOKEN environment variable is not set")
#token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"

model_name = "gpt-4o"

client = ChatCompletionsClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(token),
)

def get_completion(prompt): 
    response = client.complete(
        messages=[
            SystemMessage(content="You are a marketing professional."),
            UserMessage(content= prompt),
        ],
        model=model_name,
        # Optional parameters
        temperature=0,
        stream=True
    )
    for chunk in response:
        if chunk.choices and chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content
            time.sleep(0.01)


###app

st.title("Intelligent Marketing Writer")
st.caption("From idea and bullet points to a complete marketing copy")

content = st.text_area("Please input your ideas, bullet points or product spec, etc.")

product_value = st.multiselect(
    "Product value to promote",
    [
    "High efficiency",
    "Innovation",
    "Environmentally friendly",
    "User friendly",
    "Safe and reliable",
    "Cost-effective",
    "Beautiful",
    "Easy",
    "Intelligent",
    "Mental health"
    ],
    [])

emotion_value = st.multiselect(
    "Emotion value to highlight",
    [
    "Comfort",
    "Relax",
    "Refreshing",
    "Happiness",
    "Confidence",
    "Sweet",
    "Novelty",
    "Security",
    "Advanced sense",
    "Belonging"
    ],
    [])

age = st.slider(
    "Audience age range",
    0, 100, (18, 60))

number = st.number_input("How many words do you want to generate?", min_value=1, step=1)

# Language selection
languages = {
    'English': 'English',
    'Chinese': 'Chinese',
    'Japanese': 'Japanese',
    'Korean': 'Korean'
}

# 创建单选按钮，默认值为英语
selected_language = st.radio(
    "Select a language:",
    options=list(languages.values()),
    index=0  # 默认选择第一个选项，即英语
)

if st.button("Start Write", type="primary"):
    if content and product_value and emotion_value and age and number:
        prompt = f"""
        Think step by step and create an engaging piece of writing. The following requirements must be followed:
        ###
        - According to the product description **{content}**, you must reflect on the characteristics of the product.
        - Content must amplify the value of the product:**{product_value}**.
        - Content must inspire emotional value:**{emotion_value}**.
        - The product is aimed at the **{age}** age range.
        - add appropriate emoticons and symbols.
        - no less than **{number}** words。
        - Must output in {selected_language}.
        """
        with st.spinner("Just a moment, the AI is writing..."):
            completion = st.write_stream(get_completion(prompt))
        print(completion)
        #st.write(completion)
    else:
        st.error("Please fill in all the information.")

