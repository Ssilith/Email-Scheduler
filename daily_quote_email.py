import os
import json
import smtplib
import http.client
import random
from email.message import EmailMessage

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
RECIPIENT_EMAILS = os.getenv("RECIPIENT_EMAILS").split(",")

def mask_email(email):
    email = email.strip()
    try:
        local, domain = email.split("@", 1)
    except ValueError:
        return "***"
    masked_local = local[:2] + "*" * max(len(local) - 2, 1)

    try:
        domain_name, ext = domain.rsplit(".", 1)
    except ValueError:
        return f"{masked_local}@***"
    masked_domain = domain_name[:1] + "*" * max(len(domain_name) - 1, 1)
    return f"{masked_local}@{masked_domain}.{ext}"

def fetch_random_quote():
    try:
        conn = http.client.HTTPSConnection("quotes15.p.rapidapi.com")
        
        headers = {
            'x-rapidapi-key': RAPIDAPI_KEY,
            'x-rapidapi-host': "quotes15.p.rapidapi.com"
        }
        
        language = random.choice(["pl", "en"])
        conn.request("GET", f"/quotes/random/?language_code={language}", headers=headers)
        res = conn.getresponse()
        data = res.read()
        
        if res.status == 200:
            quote_data = json.loads(data.decode("utf-8"))
            
            quote_text = quote_data.get('content', 'No quote available')
            
            originator = quote_data.get('originator', {})
            author_name = originator.get('name', 'Unknown')
            author_description = originator.get('description', '').strip()
            
            formatted_quote = f'"{quote_text}"\n\n- {author_name}'
            
            if author_description:
                formatted_quote += f"\n\nO autorze:\n{author_description}"
            
            return formatted_quote
        else:
            print(f"Could not fetch a quote. Status code: {res.status}")
            return None
            
    except Exception as e:
        print(f"Error fetching quote: {str(e)}")
        return None
    finally:
        conn.close()

def send_email(quote):
    try:
        for recipient in RECIPIENT_EMAILS:
            msg = EmailMessage()
            msg.set_content(f"Oto Twój cytat na dziś:\n\n{quote}")
            msg["Subject"] = "Cytat na dziś"
            msg["From"] = EMAIL_ADDRESS
            msg["To"] = recipient
            
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)
                print(f"Email sent successfully to {mask_email(recipient)}.")
                
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

def job():
    quote = fetch_random_quote()
    if quote:
        send_email(quote)
    else:
        print("No email sent due to failure in fetching quote.")

if __name__ == "__main__":
    job()
