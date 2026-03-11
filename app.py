import streamlit as st
from dotenv import load_dotenv
import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# .env の読み込み
load_dotenv()

# APIキー取得
api_key = os.getenv("OPENAI_API_KEY")

# LLM設定
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    openai_api_key=api_key
)

# ---- LLMを呼び出す関数 ----
def get_llm_response(user_input, expert_type):

    if expert_type == "料理の専門家":
        system_prompt = "あなたはプロの料理研究家です。料理に関する質問にわかりやすく答えてください。"

    elif expert_type == "旅行の専門家":
        system_prompt = "あなたは経験豊富な旅行ガイドです。旅行に関する質問に具体的にアドバイスしてください。"

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]

    response = llm.invoke(messages)

    return response.content


# ---- Streamlit UI ----

st.title("専門家AIアドバイスアプリ")

st.write("""
このアプリでは、入力した質問に対してAIが専門家として回答します。

使い方  
1. 専門家の種類を選択してください  
2. 質問を入力してください  
3. 送信するとAIが回答します
""")

# ラジオボタン
expert = st.radio(
    "専門家の種類を選択してください",
    ("料理の専門家", "旅行の専門家")
)

# 入力フォーム
user_text = st.text_input("質問を入力してください")

# 送信ボタン
if st.button("送信"):

    if user_text:
        answer = get_llm_response(user_text, expert)

        st.subheader("AIの回答")
        st.write(answer)

    else:
        st.warning("質問を入力してください。")