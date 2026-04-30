import streamlit as st
import random

st.set_page_config(page_title="感情ラベリング", page_icon="🧠", layout="centered")

# タイトルのフォントサイズを調整
st.markdown("""
<style>
.custom-title {
    font-size: 1.8rem; /* 約 18pt 相当 */
    font-weight: 700;
}
.blue-box {
    padding: 18px;
    border-radius: 10px;
    background-color: #e8f4ff;
    border: 1px solid #bcdfff;
    font-size: 1.1rem;
    line-height: 1.6;
    margin-bottom: 20px; /* ← リセットボタンとの間に余白 */
}
.blue-title {
    font-weight: bold;
    margin-bottom: 8px;
    font-size: 1.15rem;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="custom-title">🧠 感情ラベリング</div>', unsafe_allow_html=True)
st.write("今の気持ちをすべて選んでね")

emotions = [
    "寂しい",
    "悲しい",
    "不安",
    "怒り",
    "虚しい",
    "苦しい",
    "モヤモヤ",
]

selected = st.multiselect(
    "いまの感情を選択",
    emotions,
    placeholder="タップして選んでね"
)

messages = [
    "大波のあとは凪になって落ち着くよ",
    "今はしんどいけど、自分のペースで大丈夫",
    "抱えすぎないで、肩の力を抜いてみよ",
    "ちゃんと頑張ってるの、わかってるよ。",
    "あなたの気持ちはちゃんと意味があるよ。",
    "今は曇りでも、いつかちゃんと晴れるからね。",
    "一回深呼吸して、間をあけてみよう",
    "今日は優しく自分を扱ってあげてね",
]

if selected:
    message = random.choice(messages)
    st.markdown(
        f"""
        <div class="blue-box">
            <div class="blue-title">🍀そっと寄り添うひとこと🍀</div>
            {message}
        </div>
        """,
        unsafe_allow_html=True
    )

if st.button("リセット"):
    st.experimental_rerun()
