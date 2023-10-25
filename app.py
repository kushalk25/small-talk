import os
import openai
import text_to_speech
import speech_to_text
import json
from flask import Flask, render_template, request, jsonify

# Create a Flask application
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

# openai setup
openai.api_key = os.getenv("OPENAI_API_KEY")

# Make global variable to store the conversatino history.
conversation = [{"role": "system", "content": "You are a helpful assistant"}]

# Define a route for the home page
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', conversation=conversation)

@app.route('/add_to_chat', methods=['POST'])
def add_to_chat():
    data = json.loads(request.data)

    input_type = data['input_type']
    user_input = ""

    if input_type == "speech":
        user_input = speech_to_text.record_audio()
    elif input_type == "text":
        user_input = data['user_input']

    conversation.append({"role": "user", "content": user_input})

    return jsonify(conversation)

@app.route('/chat', methods=['GET'])
def call_chat_gpt():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )
    result = response.choices[0].message.content
    conversation.append({"role": "assistant", "content": result})
    #text_to_speech.speak(chat_gpt_response)

    return jsonify(conversation)


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
