from flask_wtf import FlaskForm
from wtforms import SelectField ,StringField, SubmitField, TextAreaField, HiddenField
from wtforms.validators import DataRequired, ValidationError, Email


class ContactForm(FlaskForm):
    """Formulario de contacto"""
    name = StringField('Nombre', validators=[
        DataRequired('Ingresa tu Nombre')], 
        render_kw={"placeholder": "NOMBRE"})
    email = StringField('Email', validators=[
        DataRequired('Ingresa un Email'),
        Email('Email invalido')
        ],
        render_kw={"placeholder": "EMAIL"})
    phone = StringField('Telefono', validators=[
        DataRequired('Ingresa un Telefono')
        ],
        render_kw={"placeholder": "TELEFONO"})
    message = TextAreaField('Mensaje', validators=[
        DataRequired('Mensaje Vacio')
        ],
        render_kw={"placeholder": "MENSAJE", "id": "message_input"})
    subject = SelectField('Motivo', validators=[
        DataRequired('Selecciona Motivo')
        ],
        choices=[('SELECCIONA MOTIVO', 'SELECCIONA MOTIVO'),
            ('EMPEZAR PROYECTO', 'EMPEZAR PROYECTO'),
            ('FORMAR PARTE DEL EQUIPO', 'FORMAR PARTE DEL EQUIPO'),
            ('OTRO', 'OTRO'),
            ])
    submit = SubmitField('Enviar',
        render_kw={"id": "form_button"})
        
    
