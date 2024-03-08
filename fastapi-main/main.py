from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import base64
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# from . import emailTemplate

app = FastAPI()

class Msg(BaseModel):
    msg: str




# @app.post("/send-email/")
# async def send_email(Email: str, Name: str):
#     # sender_email = "onorah17@gmail.com"
#     # sender_password = "adty gdjr ouug gihs"
#     subject="Thank you! Your registration for the Tuwatunze event is confirmed."
#     # message="Dear "+ Name+" ,"" \n Welcome to Tuwatunze!. We are thrilled to have you join us for this exciting event\n Here are a few details to help you prepare:\nEvent Date: 13th April 2024 \nEvent Time: [Event Time]Event Address:Playstreet Lavington,Mugumo Road\nPlease feel free to reach out if you have any questions or need further information. We look forward to seeing you there!\nBest regards,\nEmily Githae\nTuwatunze Event organiser\n7000000000"
    
#     # sender_email = "norah@marathonxp.com"
#     # sender_password = "mdkg gylh upea caqa"
    
#     sender_email = "tuwatunze@gmail.com"
#     sender_password = "tbny zfqk jwjw uiqb"


#     # Create a message
#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = Email
#     msg['Subject'] = subject
#     # msg.attach(MIMEText(message, 'plain'))
#     print("Recepient log.....",Email)
#     # Add HTML content to the email
#     html_content = email_template.replace('[Participant\'s Name]', Name).replace('[Event Date]', 'April 14, 2024').replace('[Event Time]', '9:00 AM').replace('[Event Location]', 'Playstreet Lavington,Mugumo Road').replace('[Link to Event Page]', 'https://www.example.com/event')
#     msg.attach(MIMEText(html_content, 'html'))
#     try:
#         # Connect to Gmail's SMTP server
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()
#         server.login(sender_email, sender_password)

#         # Send the email
#         server.sendmail(sender_email, Email, msg.as_string())
#         server.quit()
#         return {"message": "Email sent successfully"}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))



@app.get("/")
async def root():
    return {"message": "Hello Woeld World. Welcome to FastAPI!"}


@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}


@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}


@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}
