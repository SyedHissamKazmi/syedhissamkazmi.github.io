import os
from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class ContactForm(BaseModel):
    name: str
    email: str
    subject: str
    message: str

@app.post("/api/contact")
async def handle_contact(form_data: ContactForm):
    # This securely pulls your link from Vercel's settings
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    
    discord_payload = {
        "content": f"🚀 **New Message from Portfolio!**\n\n**Name:** {form_data.name}\n**Email:** {form_data.email}\n**Subject:** {form_data.subject}\n**Message:**\n```\n{form_data.message}\n```"
    }
    
    try:
        if webhook_url:
            requests.post(webhook_url, json=discord_payload)
    except Exception as e:
        print(f"Error: {e}")
        
    return {"status": "success"}
