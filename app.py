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
st.title('🍷ワインギフトレコメンドアプリ🍷')

st.write('贈る相手や目的に応じて、ワインギフトを5つ提案します。')


# 3列レイアウト作成
col1, col2, col3 = st.columns([1, 2, 1])

# 左側にユーザー入力欄
with col1:
    st.header('🎁 ユーザー入力')
    with st.form(key='user_input_form'):
        product = st.text_input('商品', 'ワイン')
        occasion = st.text_input('目的', '昇進祝のプレゼント')
        recipient = st.text_input('プレゼント相手', '女性の上司')
        budget = st.text_input('金額', '50-100USD')
        
        submit_button = st.form_submit_button(label='レコメンドを表示')

# 中央にレコメンド結果
with col2:
    if submit_button:
        st.header('🍾 レコメンド結果')
        recommendations = get_wine_recommendations(product, occasion, recipient, budget)

        st.markdown(
            f"""
            <div style='background-color: black; color: white; padding: 10px; border-radius: 10px;'>
                {recommendations.replace('\n', '<br>')}
            </div>
            """, 
            unsafe_allow_html=True
        )

# 右側に空白スペースや追加情報
with col3:
    st.header('📚 購入先')
    st.info("購入先情報をここに表示します。")
