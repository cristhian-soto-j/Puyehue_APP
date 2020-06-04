from app import db, mail
from flask import render_template, flash, redirect, url_for, request
from app.email.forms import ContactForm
from werkzeug.urls import url_parse
from app.email.send_email import contact_email
from app.main import bp 


@bp.route('/')


@bp.route('/index')
def index():
    return render_template('main/index.html')


@bp.route('/contacto', methods=['GET', 'POST'])
def contacto():
    form = ContactForm()
    if form.validate_on_submit():
        contact_email(form)
        return redirect('/index')
    return render_template('main/contacto.html', form=form)