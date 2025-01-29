from flask import Blueprint, render_template, request, jsonify
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/submit-contact', methods=['POST'])  
def submit_contact():
    sender_email = ""
    sender_password = ""
    smtp_server = ""
    smtp_port = 587
    try:
        if request.content_type != 'application/json':
            return jsonify({'status': 'error', 'message': 'Invalid Content-Type'}), 415
        
        data = request.get_json()
        if not data or 'name' not in data or 'email' not in data or 'message' not in data:
            return jsonify({'status': 'error', 'message': 'Missing data.'}), 400

        receiver_email = data['email']
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f"New Contact Form Submission: {data.get('name', 'No Name')}"
        
        body = f"Nombre: {data['name']}\nEmail: {data['email']}\nMensaje: {data['message']}"
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(msg)

        return jsonify({'status': 'success', 'message': 'Gracias por contactarnos. Nos pondremos en contacto contigo pronto.'})

    except smtplib.SMTPAuthenticationError:
        return jsonify({'status': 'error', 'message': 'Email authentication failed.'}), 401
    except smtplib.SMTPServerDisconnected:
        return jsonify({'status': 'error', 'message': 'Could not connect to the SMTP server.'}), 500
    except Exception as e:
        print(e)
        return jsonify({'status': 'error', 'message': 'Ocurrió un error al intentar enviar el correo electrónico.'}), 500
