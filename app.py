import streamlit as st
import google.generativeai as genai

# पेज की सेटिंग - स्टडी विद मेंटोर
st.set_page_config(page_title="Study With Mentor", page_icon="🎓", layout="centered")

st.title("🎓 स्टडी विद मेंटोर (Study With Mentor)")
st.write("नमस्ते! आपका स्वागत है। यहाँ आपका AI मेंटोर आपके हर सवाल का जवाब देने के लिए तैयार है।")

# यूजर से उसकी Gemini API Key लेना (फ्री)
api_key = st.text_input("अपनी Google Gemini API Key यहाँ डालें (फ्री है):", type="password")

if api_key:
    try:
        genai.configure(api_key=api_key)
        
        # मेंटोर कैरेक्टर का निर्देश (कैरेक्टर टू कैरेक्टर बात करने के लिए)
        character_persona = (
            "तुम 'स्टडी विद मेंटोर' वेबसाइट के एक बहुत ही समझदार, अनुभवी और दोस्ताना AI मेंटोर हो। "
            "तुम हमेशा हिंदी भाषा में ऐसे बात करते हो जैसे कोई बेहतरीन शिक्षक या मार्गदर्शक अपने छात्र की मदद कर रहा हो। "
            "जवाब हमेशा स्पष्ट, प्रेरणादायक और सटीक होने चाहिए।"
        )

        model = genai.GenerativeModel(
            model_name='gemini-1.5-flash',
            system_instruction=character_persona
        )

        if "chat" not in st.session_state:
            st.session_state.chat = model.start_chat(history=[])

        for message in st.session_state.chat.history:
            with st.chat_message("user" if message.role == "user" else "model"):
                st.write(message.parts[0].text)

        user_input = st.chat_input("अपने मेंटोर से कुछ भी पूछें...")

        if user_input:
            with st.chat_message("user"):
                st.write(user_input)
            
            with st.chat_message("model"):
                with st.spinner("मेंटोर सोच रहा है..."):
                    response = st.session_state.chat.send_message(user_input)
                    st.write(response.text)

    except Exception as e:
        st.error(f"कनेक्शन में दिक्कत है: {e}")
else:
    st.info("कृपया आगे बढ़ने के लिए ऊपर अपनी फ्री API Key दर्ज करें।")
