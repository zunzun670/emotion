import streamlit as st
import random

st.set_page_config(page_title="感情ラベリング", page_icon="🧠", layout="centered")

st.title("🧠 感情ラベリング")
st.write("今の気持ちをすべて選んでください。")

emotions = [
    "寂しい",
    "悲しい",
    "不安",
    "怒り",
    "虚しい",
    "苦しい",
]

selected = st.multiselect(
    "感情を選択",
    emotions,
    placeholder="タップして選んでください"
)

# 優しい一言リスト
messages = [
    "波はいつか凪になって落ち着くよ。",
    "今はしんどいけど、あなたのペースで大丈夫だよ。",
    "抱えすぎなくていいよ、少し休んでいいんだよ。",
    "ちゃんと頑張ってるの、わかってるよ。",
    "あなたの気持ちはちゃんと意味があるよ。",
    "今は曇りでも、いつかちゃんと晴れるからね。",
    "ひとりで全部やらなくていいよ。",
    "今日は少し優しく自分を扱ってあげてね。",
]

# CSS（薄い青枠）
st.markdown("""
<style>
.blue-box {
    padding: 16px;
    border-radius: 8px;
    background-color: #e8f4ff;
    border: 1px solid #bcdfff;
    font-size: 1.1rem;
}
</style>
""", unsafe_allow_html=True)

if selected:
    message = random.choice(messages)
    st.markdown(f'<div class="blue-box">{message}</div>', unsafe_allow_html=True)

if st.button("リセット"):
    st.experimental_rerun()
