from datetime import datetime
from app import db
# from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5
from flask_user import UserMixin, UserManager


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='0')

    # User information
    name_first = db.Column(db.String(16))
    name_second = db.Column(db.String(16))
    surename_first = db.Column(db.String(16))
    surename_second = db.Column(db.String(16))
    health = db.Column(db.String(32))
    salary = db.Column(db.Integer)
    phone = db.Column(db.Integer, unique=True)
    rut = db.Column(db.String(16), unique=True)

    # User authentication
    email = db.Column(db.String(32), nullable=False, server_default='0', unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    #password_hash = db.Column(db.String(128))
    password = db.Column(db.String(255), nullable=False, server_default='')
    active = db.Column(db.Boolean(), nullable=False, server_default='0') ##

    # Relationship
    roles = db.relationship('Role', secondary='user_roles', backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<User {}{}>'.format(self.name_first.capitalize(), self.surename_first.capitalized())

    # def set_password(self, password):
    #     self.password_hash = generate_password_hash(password)

    # def check_password(self, password):
    #     return check_password_hash(self.password_hash, password)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False, server_default=u'', unique=True) # for @roles_accepted()
    label = db.Column(db.Unicode(255), server_default=u'') # for display


class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE')) 


class UserInvitation(db.Model):
    __tablename__ = 'user_invitations'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=False)
    # save the user of the invitee
    invited_by_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    invited_by_user = db.relationship('User', uselist=False)
    # token used for registration page to identify user registering
    token = db.Column(db.String(100), nullable=False, server_default='')


# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))


