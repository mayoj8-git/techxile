import streamlit as st
import openai

# OpenAI APIキーの設定
openai.api_key = st.secrets["OPENAI_API_KEY"]

def get_wine_recommendations(product, occasion, recipient, budget):
    # ChatGPT 4を使用したワインのレコメンド
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # GPT-4モデルを指定
        messages=[
            {"role": "system", "content": "あなたはワインの専門家です。日本語で回答してください。"},
            {"role": "user", "content": f"Please recommend 5 wines for a {occasion} gift to a {recipient} with a budget of {budget}. "
                                        f"For each wine, provide the name, price, and a brief description (less than 300 characters) of its story or background."}
        ],
        max_tokens=700  # GPT-4では、出力の精度が高いので少し多めに
    )
    
    return response.choices[0].message.content

# Streamlitアプリの設定
st.title('ワインギフトレコメンドアプリ')

st.write('贈る相手や目的に応じて、ワインギフトを5つ提案します。')

# ユーザー入力
product = st.text_input('商品', 'ワイン')
occasion = st.text_input('目的', '昇進祝のプレゼント')
recipient = st.text_input('プレゼント相手', '女性の上司')
budget = st.text_input('金額', '50-100USD')

if st.button('レコメンドを表示'):
    # GPT-4 APIを呼び出してレコメンドを取得
    recommendations = get_wine_recommendations(product, occasion, recipient, budget)
    
    # レコメンドの表示
    st.subheader('おすすめのワイン')
    st.text(recommendations)
