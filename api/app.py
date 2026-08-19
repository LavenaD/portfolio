import os


from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse

from dotenv import load_dotenv
import resend
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
        "http://127.0.0.1:5000",
        "http://localhost:5000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
resend.api_key = os.getenv("RESEND_API_KEY")

print("API key loaded:", bool(resend.api_key))

class EmailRequest(BaseModel):
    name: str
    email: str
    message: str
    subject: str


@app.post("/send-email")
async def send_email(request: EmailRequest):

    try:
        print("Name:", request.name)
        print("Email:", request.email)
        print("Subject:", request.subject)
        print("Message:", request.message)
        params = {
            "from": "onboarding@resend.dev",

            # This can still be your Gmail address
            "to": "lavena.dmello@gmail.com",

            "subject": request.subject,

            "reply_to": request.email,

            "html": f"""
                <h2>New Website Enquiry</h2>

                <p><strong>Name:</strong> {request.name}</p>

                <p><strong>Email:</strong> {request.email}</p>

                <p><strong>Message:</strong></p>

                <p>{request.message}</p>
            """
        }

        email_response = resend.Emails.send(params)

        return {
            "success": True,
            "message": "Email sent successfully"
        }

    except Exception as error:

        print("Email error:", error)

        return JSONResponse(
            status_code=500,
            content={
                "success": False,
                "message": "Unable to send email"
            }
        )