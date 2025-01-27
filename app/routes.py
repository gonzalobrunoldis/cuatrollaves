from flask import Blueprint, render_template, request, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/submit-contact', methods=['POST'])
def submit_contact():
    data = request.json
    # Here you would typically save the contact form data or send an email
    # For now, we'll just return a success message
    return jsonify({
        'status': 'success',
        'message': 'Gracias por contactarnos. Nos pondremos en contacto contigo pronto.'
    }) 