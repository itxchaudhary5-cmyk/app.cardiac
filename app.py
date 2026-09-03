import streamlit as st

st.set_page_config(
    page_title="Cardiac Care",
    page_icon="🫀"
)

st.title("🫀 Cardiac Care")
st.write("Heart Health Awareness & Emergency Support")

st.info(
    "This app provides educational information and does not "
    "diagnose or replace professional medical care."
)

st.header("🚨 Emergency Symptom Checker")

st.write("Select the symptoms the person is experiencing:")

chest_pain = st.checkbox("Chest pain or pressure")
breathing = st.checkbox("Difficulty breathing")
fainting = st.checkbox("Fainting or loss of consciousness")
palpitations = st.checkbox("Very fast or irregular heartbeat")
weakness = st.checkbox("Sudden severe weakness")

if st.button("Check Symptoms"):

    emergency_symptoms = [
        chest_pain,
        breathing,
        fainting
    ]

    if any(emergency_symptoms):
        st.error(
            "⚠️ These symptoms may require urgent medical attention. "
            "Seek emergency medical care immediately."
        )

    elif palpitations or weakness:
        st.warning(
            "⚠️ Medical assessment is recommended, especially if "
            "symptoms are new, severe, or getting worse."
        )

    else:
        st.success(
            "No selected high-risk symptom was detected by this "
            "basic checker. If you feel unwell or symptoms develop, "
            "seek medical advice."
        )
