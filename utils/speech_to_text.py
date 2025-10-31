import speech_recognition as sr

# to convert voices into text
def takecommand():
    while True: 
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("🎤 Listening...")
            r.pause_threshold = 2
            try:
                audio = r.listen(source, timeout=2, phrase_time_limit=5)
                print("🧠 Recognizing...")
                query = r.recognize_google(audio, language='hi-IN')
                print(f"\n👤 User said: {query}")
                return query

            except sr.WaitTimeoutError:
                print("⏳ Timeout: No speech detected.")
                return "none"
            except sr.UnknownValueError:
                print("❌ Could not understand audio.")
                return "none"
            except sr.RequestError:
                print("⚠️ API unavailable or network error.")
                return "none"
            except Exception as e:
                print(f"Error: {str(e)}")