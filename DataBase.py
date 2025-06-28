
import mysql.connector
from dotenv import load_dotenv
import os
import bcrypt

load_dotenv()

def connectDataBase():
    return mysql.connector.connect(
        host = os.getenv('HOST'),
        user = os.getenv('USER'),
        password = os.getenv('PASSWORD'),  
        database = os.getenv('DATABASE')
    )

conn = connectDataBase()
cur = conn.cursor()


# cur.execute("CREATE DATABASE clinic_db")


# cur.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY,username VARCHAR(50) NOT NULL,password VARCHAR(100) NOT NULL,email VARCHAR(100) NOT NULL)")

# cur.execute("CREATE TABLE patients (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(100),gender VARCHAR(10),age INT,phone VARCHAR(20),address TEXT)")

# cur.execute("CREATE TABLE appointments (id INT AUTO_INCREMENT PRIMARY KEY,patient_id INT,date DATE,time TIME,notes TEXT,FOREIGN KEY (patient_id) REFERENCES patients(id))")

# cur.execute("CREATE TABLE prescriptions (id INT AUTO_INCREMENT PRIMARY KEY,patient_id INT,diagnosis TEXT,medications TEXT,date DATE,FOREIGN KEY (patient_id) REFERENCES patients(id))")

# cur.execute("CREATE TABLE invoices (id INT AUTO_INCREMENT PRIMARY KEY,patient_id INT,amount DECIMAL(10,2),service_details TEXT,date DATE,FOREIGN KEY (patient_id) REFERENCES patients(id))")








# sql = "INSERT INTO invoices (patient_id, amount, service_details, date) VALUES (%s, %s, %s, %s)"
# data = [
#     (1, 300.00, 'Consultation + X-ray', '2025-06-21'),
#     (2, 150.00, 'Routine Checkup', '2025-06-22'),
#     (3, 400.00, 'Consultation + Prescription', '2025-06-23')
# ]
# cur.executemany(sql, data)
# conn.commit()




# cur.execute("INSERT INTO patients (name, gender, age, phone, address) VALUES ('Mohamed Salah', 'Male', 32, '01123456789', 'Cairo'),('Amina Hassan', 'Female', 28, '01098765432', 'Alexandria'),('Youssef Adel', 'Male', 45, '01234567890', 'Giza')")
# conn.commit()
# cur.execute("INSERT INTO appointments (patient_id, date, time, notes) VALUES (1, '2025-06-21', '10:00:00', 'Follow-up for knee pain'),(2, '2025-06-22', '12:30:00', 'Routine checkup'),(3, '2025-06-23', '15:45:00', 'Back pain consultation')")
# conn.commit()
# cur.execute("INSERT INTO prescriptions (patient_id, diagnosis, medications, date) VALUES (1, 'Knee inflammation', 'Ibuprofen 400mg twice daily', '2025-06-21'),(2, 'General fatigue', 'Vitamin B12 injection once a week', '2025-06-22'),(3, 'Back muscle strain', 'Paracetamol + Physiotherapy', '2025-06-23')")
# conn.commit()


# password = '12345678'
# t = password.encode('utf-8')
# u = bcrypt.gensalt()
# p = bcrypt.hashpw(t,u)

# sql = 'INSERT INTO users (username, password,email) VALUES (%s,%s,%s)'
# val = ('Hassan',p,'mno95pq7@gmail.com')
# cur.execute(sql,val)
# conn.commit()


