from utils.utils import get_llm,get_prompt,str_parse
from flask import Flask,render_template,Response
from utils.text_to_speech import speak_hindi
from utils.speech_to_text import takecommand
import time

app=Flask(__name__)

#llm
llm=get_llm()
#prompt
prompt=get_prompt()

# renders the main user interface
@app.route("/")
def main():
    return render_template("index.html")

# Stream route: Continuously listens to Hindi voice input, gets Gemini replies, speaks them, and streams real-time updates to the UI with SSE Transport.
@app.route('/stream')
def stream():
    def generate():

        # Maintains and store the chat history
        chat_history = []

        while True:
            try:
                yield "data: 🎤 Listening...\n\n"

                # taking the voice input and converting into text
                voice_input = takecommand().lower()
                
                # if the voice_input is empty
                if not voice_input or voice_input == "none":
                    yield "data: ❌ No input detected. Listening again...\n\n"
                    continue

                yield f"data: 👤 User said: {voice_input}\n\n"

                # exit condition
                if "एग्जिट" in voice_input:
                    yield "data: 🎤 Assistant: धन्यवाद! आपका दिन शुभ हो।\n\n"
                    speak_hindi("धन्यवाद! आपका दिन शुभ हो।")
                    break

                chat_history.append({'user': voice_input})
                
                # using chain to reply the given input using llm in hindi
                chain = prompt | llm | str_parse
                ai_reply = chain.invoke({'user_query': voice_input, 'chat_history': chat_history})
                chat_history.append({'bot': ai_reply})
                yield f"data: 🤖 Response: {ai_reply}\n\n"

                # playing the AI response
                yield "data: Speaking response in Hindi...\n\n"
                speak_hindi(ai_reply)

                # continue loop — listen again
                time.sleep(1)

            except Exception as e:
                yield f"data: ⚠️ Error: {str(e)}\n\n"
                speak_hindi("माफ कीजिए, कुछ समस्या आ गई है। कृपया दोबारा कोशिश करें।")

    return Response(generate(), mimetype='text/event-stream')

if __name__ == "__main__":
    app.run(debug=True)
