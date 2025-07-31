# AI-Driven Loan Origination & KYC App for Cooperative Banks

This is a Flask-based multi-tenant loan application and KYC management system for small cooperative banks in India. It allows bank-specific configurations, multilingual support, file uploads, admin dashboards, and more.

## Features
- Bank-wise configuration (name, logo, colors)
- Role-based Admin + SuperAdmin system
- Loan types and KYC document management
- Loan application with KYC file uploads
- Email notifications (to be configured)
- Ready for deployment on Render (Starter Plan)

## Getting Started

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Initialize the database**
```bash
flask --app app.py init-db
python seed.py
```

3. **Run the app**
```bash
flask --app app.py run
```

Visit: `http://localhost:5000/admin/login`

Default SuperAdmin:
- Email: admin@demo.com
- Password: admin123

## Deployment Notes
- Replace SQLite with PostgreSQL for Render
- Add mail/SMS keys as needed