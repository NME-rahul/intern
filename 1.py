import openai
from flask import Flask, render_template, request

openai.api_key = "your_api_key"
model = "gpt-3.5-turbo"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def ChatGPT():
    prompt = request.form['prompt']
    try:
        response = openai.Completion.create(
        model=model,
        prompt=str(prompt),
        max_tokens=1000,
        n=1,
        stop='\n',
        temperature=0.5
        )
        answer = response.choices[0].text.split('\n')[0]
        return render_template('index.html', prompt=prompt, result=answer)

    except Exception as error:
        return render_template('index.html', prompt=prompt, result=error)
	
    
if __name__ == "__main__":
    app.run(port=4533, debug=True)
