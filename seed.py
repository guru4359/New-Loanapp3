from app import db
from models import Bank, User
from app import app

with app.app_context():
    db.create_all()

    # Create a default bank
    bank = Bank(name="Demo Cooperative Bank", address="Mumbai", logo="", theme_color="#003366")
    db.session.add(bank)
    db.session.commit()

    # Create a superadmin user
    admin = User(email="admin@demo.com", role="superadmin", bank_id=None)
    admin.set_password("admin123")
    db.session.add(admin)
    db.session.commit()

    print("Seeded SuperAdmin and Demo Bank.")