from flask import Blueprint

bp = Blueprint('email', __name__,
    template_folder='templates')

from app.email import send_email