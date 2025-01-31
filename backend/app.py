from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace with your OpenAI API key (we'll handle this later)
openai.api_key = "your-openai-api-key"

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')

    # Call OpenAI API to generate content
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )

    content = response.choices[0].text.strip()
    return jsonify({'content': content})

if __name__ == '__main__':
    app.run(debug=True)
