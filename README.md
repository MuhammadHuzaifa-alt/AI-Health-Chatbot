# AI-Health-Chatbot
Overview

AI Health Chatbot is a web-based healthcare assistant developed using Flask and the Groq API. The application provides general health-related guidance through a conversational chatbot interface while maintaining basic safety restrictions for sensitive medical queries.
The chatbot is designed to deliver simple and user-friendly health assistance without providing medical diagnoses or prescription
Features
=>AI-powered conversational health assistant
=>Real-time chatbot interaction
=>Responsive user interface
=>Safety filtering for sensitive queries
=>Flask backend integration
=>Groq API integration
=>Clean and modern UI design
Technologies Used
  Frontend
   =>HTML
   =>CSS
   =>JavaScript
Backend
   =>Python
   =>Flask
   =>AI Integration
   =>Groq API
   =>Llama 3.1 8B Instant Model
Project Structure
   health-chatbot/
│
├── app.py
├── config.py
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
Installation
1. Clone the Repository
   git clone <repository-url>
   cd health-chatbot
2. Create Virtual Environment
python -m venv venv

Activate the virtual environment:
Windows
venv\Scripts\activate
Linux / macOS
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
Requirements
Flask
groq
openai
Configuration
Update the API key inside config.py:
GROQ_API_KEY = "your_api_key"
For security purposes, it is recommended to use environment variables instead of storing API keys directly in the source code.
Example:
import os
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
Running the Application
Start the Flask server:
python app.py
The application will run at:
http://127.0.0.1:5000
Safety Features
The chatbot includes a basic safety filter to block potentially harmful medical-related queries such as:
Suicide-related content
Overdose instructions
Prescription requests
Medication dosage advice
Users are encouraged to consult healthcare professionals for serious medical concerns.
