
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Bank(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(200))
    logo = db.Column(db.String(200))
    theme_color = db.Column(db.String(50))
    users = db.relationship("User", backref="bank", lazy=True)
    loan_types = db.relationship("LoanType", backref="bank", lazy=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20))  # 'admin' or 'superadmin'
    bank_id = db.Column(db.Integer, db.ForeignKey('bank.id'), nullable=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class LoanType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bank_id = db.Column(db.Integer, db.ForeignKey('bank.id'), nullable=False)
    name = db.Column(db.String(100))
    term_months = db.Column(db.Integer)
    min_amount = db.Column(db.Float)
    max_amount = db.Column(db.Float)
    interest_rate = db.Column(db.Float)
    kyc_requirements = db.relationship("KycRequirement", backref="loan_type", lazy=True)

class KycRequirement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    loan_type_id = db.Column(db.Integer, db.ForeignKey('loan_type.id'), nullable=False)
    document_name = db.Column(db.String(100))
    required = db.Column(db.Boolean, default=True)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bank_id = db.Column(db.Integer, db.ForeignKey('bank.id'))
    loan_type_id = db.Column(db.Integer, db.ForeignKey('loan_type.id'))
    applicant_name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    account_number = db.Column(db.String(30), nullable=True)
    amount_requested = db.Column(db.Float)
    kyc_documents = db.relationship("KycDocumentUpload", backref="application", lazy=True)

class KycDocumentUpload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application_id = db.Column(db.Integer, db.ForeignKey('application.id'), nullable=False)
    document_name = db.Column(db.String(100))
    file_path = db.Column(db.String(200))
