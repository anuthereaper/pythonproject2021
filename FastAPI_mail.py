# https://github.com/sabuhish/fastapi-mail
# https://sabuhish.github.io/fastapi-mail/example/
from fastapi import FastAPI, BackgroundTasks, UploadFile, File, Form
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from pydantic import BaseModel, EmailStr
from typing import List

class EmailSchema(BaseModel):
    email: List[EmailStr]

conf = ConnectionConfig(
    MAIL_USERNAME = "xxxxxxxxxxxxxxx@gmail.com",
    MAIL_PASSWORD = "xxxxxxxxxxxxxxx",    # use app password if using google
    MAIL_FROM = "xxxxxxxxxxxx@gmail.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)

app = FastAPI()

html = """
<p>Thanks for using Fastapi-mail</p> 
"""
@app.post("/email")
async def simple_send(email: EmailSchema) -> JSONResponse:

    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=email.dict().get("email"),  # List of recipients, as many as you can pass from API client
        body=html,
        subtype="html"
        )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})  

# POST message with below body
#{
#    "email": [
#        "Anupam.Chand@shell.com"
#    ]
#}