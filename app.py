import os
import openai
from flask import Flask, request, render_template

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.post("/translate")
def translate():
    front_end_res = request.get_json()
    language = front_end_res["language"]
    what_to_translate = front_end_res["data"]
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Translate this into {language}\n{what_to_translate}",
        temperature=0.4,
        max_tokens=120,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
    )
    return response.choices[0].text


if __name__ == '__main__':
    app.run()
