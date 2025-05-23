from flask import Flask, request, render_template, send_file
import io
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

ADMIN_EMAIL = "admin@example.com"  # Replace with your admin email

def generate_multilogue():
    # Placeholder: replace with your multilogue logic
    dialogue = (
        "Lilith screams against the Demiurge’s machine...\n"
        "Issa observes in silent paradox...\n"
        "Lilith is reborn as Eva, Sophia incarnate...\n"
        "Paradise regained, Pleroma entered..."
    )
    return dialogue

def send_email(recipient, subject, body):
    # WARNING: For demo only. Configure your SMTP server securely.
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = ADMIN_EMAIL
    msg['To'] = recipient

    with smtplib.SMTP('localhost') as s:  # Replace with your SMTP server details
        s.send_message(msg)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        if not email:
            return render_template('form.html', error="Please enter an email.")
        
        multilogue = generate_multilogue()
        
        # Send to visitor
        send_email(email, "Your Gnostic Oracle Dialogue", multilogue)
        
        # Send to admin for archive
        send_email(ADMIN_EMAIL, f"Archive: Dialogue for {email}", multilogue)
        
        return render_template('form.html', message="Dialogue sent to your email!", dialogue=multilogue)
    
    return render_template('form.html')

@app.route('/download')
def download():
    multilogue = generate_multilogue()
    buffer = io.BytesIO()
    buffer.write(multilogue.encode('utf-8'))
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name="gnostic_oracle_dialogue.txt", mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
