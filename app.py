import os
import openai
from flask import Flask, render_template, request

# Create a Flask application
app = Flask(__name__)

# openai setup
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize an empty conversation list to store messages
conversation = []

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the user's input from the form
        user_input = request.form['user_input']

        chat_gpt_response = call_chat_gpt(user_input)

        # Add user's input and capitalized response to the conversation
        conversation.append({'user': user_input, 'bot': chat_gpt_response})

    return render_template('index.html', conversation=conversation)

def call_chat_gpt(input):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=input,
        temperature=0.6,
    )
    return response.choices[0].text


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
