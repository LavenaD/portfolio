# Portfolio
A project for displaying my Curriculum Vitea. It allows the user to download my CV and send me a message using the contact form.
- **API**: FastAPI endpoint for sending me a message
- **UI**: To display my CV, see my linked in page and download my CV.

Template Name: iPortfolio
Template URL: https://bootstrapmade.com/iportfolio-bootstrap-portfolio-websites-template/
Author: BootstrapMade.com
License: https://bootstrapmade.com/license/

## Project Structure
```
Portfolio/ 
├──── api/ 
│─── ├── app.py                  # FastAPI application  

├──── app/
│       ├── app.py                  # Flask application
├────── ├──templates/
│           ├── index.html    
├────── ├──static/
│           ├──style.css  
└── README.md
```
## Installation

### Requirements
- Python 3.8+
- Tensorflow
- Kaggle hub
- FastAPI & Uvicorn

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/LavenaD/portfolio.git
cd portfolio
```
2. **Create virtual environment**
```bash
python -m venv iportfolio-env
iportfolio-env\Scripts\activate  # Windows
source iportfolio-env/bin/activate  # Linux/Mac
```
3. **Install dependencies**
```bash
cd "api" #your path here
pip install -r requirements.txt
cd "app" #your path here
pip install -r requirements.txt
```
#### FastAPI Server

1. **Start the API**
```bash
uvicorn app:app --reload
```

2. **Call the endpoint**
```bash
python app.py
```
## FastAPI Results
Sends a message with Name of the contact, Email and message from the contact to my gmail account.


## Deployment Links
- The Fast API is deployed at -(https://portfolio-1-8992.onrender.com)
- The Flask UI is deployed at -(https://portfolio-k82x.onrender.com/)

## API Endpoints
### POST `/send-email`
Sends the message

**Request:**
```json
{
  "name": "Your name",
  "email": "Your email",
  "message": "Here goes your message",
  "subject": "Subject for your email"
}
```

**Response:**
```json
{
            "success": True,
            "message": "Email sent successfully"
}
```

