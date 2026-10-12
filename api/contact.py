from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class ContactForm(BaseModel):
    name: str
    email: str
    subject: str
    message: str

@app.post("/api/contact")
async def handle_contact(form_data: ContactForm):
    # In a production environment, you would add logic here to send an email via SendGrid, 
    # push the data to a Discord webhook, or insert it into a database like Supabase.
    
    print(f"New message from {form_data.name} ({form_data.email})")
    print(f"Subject: {form_data.subject}")
    
    return {"status": "success", "message": "Your message has been securely received."}
