import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="Study with Mentor", page_icon="📖", layout="centered")

st.title("📖 स्टडी विद मेंटर (Study With Mentor)")
st.write("नमस्ते! आपका स्वागत है। यहाँ आपका AI मेंटर आपके हर सवाल का जवाब देने के लिए तैयार है।")

# अपनी Google Gemini API Key दर्ज करें
api_key = st.text_input("अपनी Google Gemini API Key दर्ज करें", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        if prompt := st.chat_input("अपने मेंटर से कुछ भी पूछें..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})

    except Exception as e:
        st.error(f"त्रुटि: {e}")
else:
    st.info("कृपया आगे बढ़ने के लिए अपनी API Key दर्ज करें।")
