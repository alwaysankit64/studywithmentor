import streamlit as st
import google.generativeai as genai

# पेज की सेटिंग - टाइटल और आइकन
st.set_page_config(page_title="Study With Mentor", page_icon="📚", layout="centered")

st.title("📚 स्टडी विद मेंटोर (Study With Mentor)")
st.write("नमस्ते! आपका स्वागत है। यहाँ आपका AI मेंटोर आपके हर सवाल का जवाब देने के लिए तैयार है।")

# सुरक्षा के लिए यूजर से Gemini API Key दर्ज करने की अनुमति
api_key = st.text_input("अपनी Google Gemini API Key दर्ज करें।", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # यहाँ 'gemini-pro' का उपयोग किया गया है जो API v1beta के साथ सही काम करता है
        model = genai.GenerativeModel('gemini-pro')
        
        # चैट का इतिहास सेव करने के लिए सेशन स्टेट
        if "messages" not in st.session_state:
            st.session_state.messages = []

        # पुराने मैसेज को स्क्रीन पर दिखाना
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # यूजर से इनपुट लेना
        if prompt := st.chat_input("अपने मेंटोर से कुछ भी पूछें..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # AI से जवाब जनरेट करना
            with st.chat_message("assistant"):
                response = model.generate_content(prompt)
                st.markdown(response.text)
                st.session_state.messages.append({"role": "assistant", "content": response.text})
                
    except Exception as e:
        st.error(f"त्रुटि: {e}")
else:
    st.warning("कृपया आगे बढ़ने के लिए अपनी API Key दर्ज करें।")
