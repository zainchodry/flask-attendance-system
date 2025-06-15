from flask_sqlalchemy import SQLAlchemy
from datetime import date, datetime

db = SQLAlchemy()

class Employee(db.Model):
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    department = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"{self.name} - {self.department}"


class Attendance(db.Model):
    __tablename__ = "attendance"
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    date = db.Column(db.Date, default=date.today)
    status = db.Column(db.String(10))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    employee = db.relationship('Employee', backref='attendances')
