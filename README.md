# Question_Generator
Generate question(s) base on users request.

Question Generator

A simple web application that generates questions based on a given subject and topic using API.


Features

1.	Generate questions based on subject and topic
1.	User-friendly interface
2.	FastAPI backend
3.	Dynamic HTML rendering
4.	Handles API errors gracefully


Tech Stack

Backend: FastAPI (Python)
Frontend: HTML, CSS
API: question generation (Gemini / external API)



Project Structure



Question_Generator

│

├── main.py

└── static/

     ├── index.html

     └── style.css





 Installation & Setup

 1. Clone the repository


git clone https://github.com/Marfo-Thomas01/Question_Generator.git


3. Install dependencies
  pip install fastapi uvicorn requests



4.Run the Application


uvicorn main:app --reload



Open your browser and go to:

http://127.0.0.1:8000 the port might not be the same. the default browser will open the application.




Known Issues

1.	Free APIs may have usage limits
2.	Some APIs may return inconsistent formats
3.	Requires internet connection for AI generation



Future Improvements

1.	Add AJAX (no page reload)
2.	Add loading spinner
3.	Improve UI design
4.	Save generated questions
5.	Export questions as PDF


Author

Thomas Marfo



