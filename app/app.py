from flask import Flask, render_template, request, render_template_string
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/send-email", methods=["POST"])
def sendEmail():
    summary = None
    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        subject = request.form.get("subject")
        api_url = os.getenv("API_URL")
        try:
            print("subject:", subject)
            response = requests.post(f"{api_url}/send-email", json={"name": name, "email": email, "message": message, "subject": subject})
            print("FastAPI status:", response.status_code)
            print("FastAPI response:", response.text)

            if response.ok:
                data = response.json()
                print(data.get("success"))

                if data.get("success"):
                    print("Email sent successfully")
                    return {
                            "success": True,
                            "message": "Your message has been sent. Thank you!"
                            }
                
            
            return {
                "success": False,
                "message": "There was a problem sending your message."
                }, 500
        except Exception as error:

            print("Email error:", error)
    
            return {
                "success": False,
                "message": "There was a problem sending your message."
            }, 500


if __name__ == "__main__":
    app.run( host='0.0.0.0', debug=False)