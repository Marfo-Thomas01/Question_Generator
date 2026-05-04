import json
import requests
import html
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


STARTOCODE_QUESTION_GENERATOR = "https://startocode-ai-api-v1.fly.dev/ask"


def build_page(results_html=""):
    with open("static/index.html", encoding="utf-8") as file:
        html_content = file.read()

    html_content = html_content.replace("<!-- RESULTS -->", results_html)
    return html_content


@app.get("/")
def home():
    return HTMLResponse(build_page())


@app.post("/generate")
def generate(
    subject: str = Form(...),
    topic: str = Form(...),
    num_questions: int = Form(...),
    
    
):

    instructions = (
        f"Generate exactly {num_questions} questions about the topic "
        f'"{topic}" in the subject "{subject}". '
        f"Return ONLY a JSON array of strings, no other text. "
        f'Example: ["Question 1?", "Question 2?"]'
    )


    # for the api calling
    try:
        # because of the new api im using 

        response = requests.post(
            STARTOCODE_QUESTION_GENERATOR,
            json={"question": instructions},
            timeout=30
        )
    


      

        data = response.json()
        print("RAW API RESPONSE:", data)

        answers = data.get("answer", "[]")
        # for debugging
        print("RAW ANSWERS:", answers)
        print("FULL API RESPONSE:", data)

   

    except Exception as e:
        print("API ERROR:", e)
        answers = ""

    # parsing when the api has reached its credit limt
    if "credit" in answers.lower():
        questions = [" API limit reached. Try again later or change API."]
    else:
        try:
            questions = json.loads(answers)
            if not isinstance(questions, list):
                raise ValueError()
        except:
            questions = [
                q.strip("-•1234567890. ").strip()
                for q in answers.split("\n")
                if q.strip()
            ]

    # for the html
    questions_html = ""
    for question in questions:
        questions_html += f"<li>{html.escape(question)}</li>"

    results_html = f"""
    <div class="results">
        <h2>{html.escape(subject)} - {html.escape(topic)}</h2>
        <ol>{questions_html}</ol>
    </div>
    """

    return HTMLResponse(build_page(results_html))