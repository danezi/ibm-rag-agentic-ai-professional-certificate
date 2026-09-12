from flask import Flask, request, jsonify, render_template
from model import llama_response, granite_response, mistral_response
import time

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    user_message = data.get('message')
    model = data.get('model')

    if not user_message or not model:
        return jsonify({"error": "Missing message or model selection"}), 400

    system_prompt = (
        "You are an AI assistant helping with customer inquiries. "
        "You must always return ALL five fields: summary, sentiment, response, "
        "category, and action. Never omit any field, especially 'response'.\n\n"
        "Example of a correctly formatted output for the message "
        "'My package never arrived':\n"
        '{"summary": "The user\'s package was never delivered.", '
        '"sentiment": 10, '
        '"response": "I\'m sorry to hear your package didn\'t arrive. '
        'We will look into this right away and keep you updated.", '
        '"category": "shipping", '
        '"action": "Check the tracking status and contact the carrier to '
        'locate the missing package."}'
    )

    start_time = time.time()

    try:
        if model == 'llama':
            result = llama_response(system_prompt, user_message)
        elif model == 'granite':
            result = granite_response(system_prompt, user_message)
        elif model == 'mistral':
            result = mistral_response(system_prompt, user_message)
        else:
            return jsonify({"error": "Invalid model selection"}), 400

        result['duration'] = time.time() - start_time
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
