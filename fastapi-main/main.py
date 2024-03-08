from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import base64
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from . import emailTemplate

app = FastAPI()

class Msg(BaseModel):
    msg: str


#  Email template


with open(r'C:\Users\HP\OneDrive\Documents\projects\HRMS\venv\banner.jpg', 'rb') as image_file:
    encoded_image = base64.b64encode(image_file.read()).decode('utf-8')
    
email_template = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Email Template</title>
<style>
    body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        margin: 0;
        padding: 0;
        background-color: #f4f4f4;
    }

    .container {
        max-width: 600px;
        margin: 20px auto;
        padding: 20px;
        background-color: #fff;
        border-radius: 5px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    }

    h1 {
        color: #333;
        text-align: center;
    }

    p {
        color: #555;
        margin-bottom: 20px;
    }

    .btn {
        display: inline-block;
        padding: 10px 20px;
        background-color: #007bff;
        color: #fff;
        text-decoration: none;
        border-radius: 3px;
    }

    .btn:hover {
        background-color: #0056b3;
    }

    .banner {
        width: 100%;
        max-height: 200px;
        object-fit: cover;
        border-radius: 5px;
    }

    @media only screen and (max-width: 600px) {
        .container {
            padding: 10px;
        }

        h1 {
            font-size: 24px;
        }

        p {
            font-size: 14px;
        }

        .btn {
            padding: 8px 16px;
        }

        .banner {
            max-height: 150px;
        }
    }
</style>
</head>
<body>
    <div class="container">
    
     
        
        <p>Dear [Participant's Name],</p>
        <p>We hope this message finds you well. </p>
        <p>Marathon XP, a service design firm, (https://www.marathonxp.com/)  is thrilled to announce our partnership with Tuwatunze, a learning support center for children with learning disabilities, in an impactful Corporate Social Responsibility (CSR) project.</p>
        <p>Our initiative is designed to bridge the gap between parental expectations and children's education, while concurrently raising awareness about special education for children grappling with learning disabilities. </p>
        <p>In pursuit of these objectives, Marathon XP is hosting an open day with a workshop experience on <b>13th April 2024 at Playstreet Lavington, Mugumo road from 9am to 2pm</b>. The event will include a panel discussion featuring experts in the field of learning disabilities in children and educators</p>
        <p>We can’t wait to meet you! </p>
        <p>See you soon! </p>

    </div>
</body>
</html>

"""
@app.post("/send-email/")
async def send_email(Email: str, Name: str):
    # sender_email = "onorah17@gmail.com"
    # sender_password = "adty gdjr ouug gihs"
    subject="Thank you! Your registration for the Tuwatunze event is confirmed."
    # message="Dear "+ Name+" ,"" \n Welcome to Tuwatunze!. We are thrilled to have you join us for this exciting event\n Here are a few details to help you prepare:\nEvent Date: 13th April 2024 \nEvent Time: [Event Time]Event Address:Playstreet Lavington,Mugumo Road\nPlease feel free to reach out if you have any questions or need further information. We look forward to seeing you there!\nBest regards,\nEmily Githae\nTuwatunze Event organiser\n7000000000"
    
    # sender_email = "norah@marathonxp.com"
    # sender_password = "mdkg gylh upea caqa"
    
    sender_email = "tuwatunze@gmail.com"
    sender_password = "tbny zfqk jwjw uiqb"


    # Create a message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = Email
    msg['Subject'] = subject
    # msg.attach(MIMEText(message, 'plain'))
    print("Recepient log.....",Email)
    # Add HTML content to the email
    html_content = email_template.replace('[Participant\'s Name]', Name).replace('[Event Date]', 'April 14, 2024').replace('[Event Time]', '9:00 AM').replace('[Event Location]', 'Playstreet Lavington,Mugumo Road').replace('[Link to Event Page]', 'https://www.example.com/event')
    msg.attach(MIMEText(html_content, 'html'))
    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, Email, msg.as_string())
        server.quit()
        return {"message": "Email sent successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}
