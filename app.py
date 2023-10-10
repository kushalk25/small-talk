import os
import openai
import text_to_speech
import speech_to_text
from flask import Flask, render_template, request

# Create a Flask application
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# openai setup
openai.api_key = os.getenv("OPENAI_API_KEY")

# Make global variable to store the conversatino history.
conversation = [{"role": "system", "content": "You are a helpful assistant"}]

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        input_type = request.form['input_type']
        user_input = ""

        if input_type == "speech":
            user_input = speech_to_text.record_audio()
        elif input_type == "text":
            user_input = request.form['user_input']

        conversation.append({"role": "user", "content": user_input})
        # get the chatgpt response and add that too
        chat_gpt_response = call_chat_gpt(user_input)
        conversation.append({"role": "assistant", "content": chat_gpt_response})
        text_to_speech.speak(chat_gpt_response)

    return render_template('index.html', conversation=conversation)

def call_chat_gpt(input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    return response.choices[0].message.content


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
