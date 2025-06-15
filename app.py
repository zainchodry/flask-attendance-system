from flask import Flask, request, render_template, url_for, redirect, flash
from models import db, Employee, Attendance
from datetime import date, datetime, time as dtime
from flask_migrate import Migrate
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///attendance.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = os.urandom(24)

db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()



@app.route('/')
def home():
    return render_template('home.html')



@app.route('/employees')
def view_employees():
    employees = Employee.query.all()
    return render_template('view_employees.html', employees=employees)



@app.route('/add-employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        department = request.form['department']

        if not name or not department:
            flash("All fields are required.", "danger")
        else:
            new_emp = Employee(name=name, department=department)
            db.session.add(new_emp)
            db.session.commit()
            flash("Employee added successfully!", "success")
            return redirect(url_for('view_employees'))

    return render_template('add_employee.html')



@app.route('/mark-attendance', methods=['GET', 'POST'])
def mark_attendance():
    employees = Employee.query.all()
    today = date.today()

    
    if today.weekday() >= 5:  
        flash("Saturday and Sunday are off. Cannot mark attendance.", "warning")
        return redirect(url_for('home'))

    if request.method == 'POST':
        now = datetime.now()
        current_time = now.time()
        late_threshold = dtime(10, 0)  

        for emp in employees:
            
            status = request.form.get(f'status_{emp.id}')
            if status:
                
                existing = Attendance.query.filter_by(employee_id=emp.id, date=today).first()
                if existing:
                    continue  

        
                attendance_time = now.time()

            
                if status == 'Present':
                    if attendance_time > late_threshold:
                        final_status = 'Late'
                    else:
                        final_status = 'In Time'
                else:
                    final_status = status 

                attendance = Attendance(
                    employee_id=emp.id,
                    date=today,
                    status=final_status,
                    timestamp=now
                )
                db.session.add(attendance)

        db.session.commit()
        flash("Attendance recorded successfully!", "success")
        return redirect(url_for('home'))

    return render_template('mark_attendance.html', employees=employees)




@app.route('/search')
def search_attendance():
    search_date = request.args.get('date')
    status = request.args.get('status')
    
    query = Attendance.query

    if search_date:
        try:
            search_date = datetime.strptime(search_date, '%Y-%m-%d').date()
            query = query.filter(Attendance.date == search_date)
        except ValueError:
            flash("Invalid date format.", "danger")

    if status:
        query = query.filter(Attendance.status == status)

    records = query.order_by(Attendance.date.desc()).all()
    return render_template('search_attendance.html', records=records)



@app.route('/report')
def attendance_report():
    all_attendance = Attendance.query.order_by(Attendance.date.desc()).all()
    return render_template('attendance_report.html', attendance=all_attendance)



@app.route('/delete-employee/<int:id>')
def delete_employee(id):
    try:
        employees = Employee.query.get(id)
        if employees:
            db.session.delete(employees)
            db.session.commit()
            return redirect(url_for('home'))
    except Exception as e:
        print("Employee ith this id is not Found", e)
        return redirect(url_for('home'))
    

@app.route('/delete-employee/')
def delete():
    employees = Employee.query.all()
    return render_template("delete.html", employees = employees)

if __name__ == "__main__":
    app.run(debug=True)
