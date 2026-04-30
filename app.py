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

if selected:
    st.subheader("🌱 そっと寄り添うひとこと")
    st.write(random.choice(messages))

if st.button("リセット"):
    st.experimental_rerun()
