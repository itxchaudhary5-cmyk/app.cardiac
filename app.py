import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="Cardiac Care",
    page_icon="🫀"
)

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

st.title("🫀 Cardiac Care")
st.write("Heart Health Awareness & Emergency Support")

st.info(
    "This app provides educational information and does not "
    "diagnose or replace professional medical care."
)

st.header("🤖 AI Heart Health Assistant")

question = st.text_area(
    "Ask a general heart health question:"
)

if st.button("Ask AI"):

    if question.strip():

        response = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a heart health education assistant. "
                        "Give general educational information only. "
                        "Do not diagnose or prescribe treatment. "
                        "For possible emergencies, advise the user "
                        "to seek immediate professional medical help."
                    )
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        st.write(response.choices[0].message.content)

    else:
        st.warning("Please enter a question.")
