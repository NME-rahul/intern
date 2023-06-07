import openai
from flask import Flask, render_template, request

openai.api_key = "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"
model = "gpt-3.5-turbo"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/helpdesk', methods=['POST'])
def ChatGPT():
    prompt = request.form['prompt']
    try:
        response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5
        )
        answer = response.choices[0].text.split('\n')[0]
        return render_template('result.html', prompt=prompt, generated_text=answer)

    except Exception as error:
        return render_template('result.html', prompt=prompt, generated_text=error)
	
    
if __name__ == "__main__":
    app.run(debug=True)



