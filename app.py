from flask import Flask, render_template, request

# Create a Flask application
app = Flask(__name__)

# Initialize an empty conversation list to store messages
conversation = []

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the user's input from the form
        user_input = request.form['user_input']

        # Capitalize the user's input
        capitalized_text = user_input.upper()

        # Add user's input and capitalized response to the conversation
        conversation.append({'user': user_input, 'bot': capitalized_text})

    return render_template('index.html', conversation=conversation)

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
