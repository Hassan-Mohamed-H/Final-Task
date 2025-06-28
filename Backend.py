
from DataBase import connectDataBase
import customtkinter as ctk
import bcrypt


def loginBack(username, password_input):
    conn = connectDataBase()
    cur = conn.cursor()

    query = "SELECT * FROM Users WHERE username = %s"
    cur.execute(query, (username,))
    user = cur.fetchone()
    if user != None:
        passwordafterutf = password_input.encode('utf-8')
        passwordfromDB = user[2].encode('utf-8')
        check = bcrypt.checkpw(passwordafterutf,passwordfromDB)
        if check:
         return user
        else:
            return "wrong_password"
    
    else:
        return None


def Statestics():

    conn = connectDataBase()
    cur = conn.cursor()

    cur.execute("SELECT * FROM patients") 
    Patients = cur.fetchall()
    PatientsCount = len(Patients)
    
    cur.execute("SELECT * FROM appointments") 
    appointments = cur.fetchall()
    appointmentsCount = len(appointments)

    
    cur.execute("SELECT amount  FROM invoices") 
    invoices = cur.fetchall()
    
    invoicesTotal = 0
    for invoice in invoices:
        amount = invoice[0]
        if amount != None:
            invoicesTotal += amount

    return PatientsCount, appointmentsCount, invoicesTotal

def get_patients():
    conn = connectDataBase()
    cur = conn.cursor()
    cur.execute("SELECT id, name, age FROM patients ORDER BY id")
    patients = cur.fetchall()
    return patients

def get_patient_details(patient_id):
    conn = connectDataBase()
    cur = conn.cursor()
    order = "SELECT name, gender, age, phone, address FROM patients WHERE id = %s"
    val = (patient_id,)
    cur.execute(order,val)
    patient_details = cur.fetchone()
    return patient_details

def get_appointments_patient(patient_id):
    conn = connectDataBase()
    cur = conn.cursor()
    order = "SELECT date, time, notes FROM appointments WHERE patient_id = %s"
    val = (patient_id,)
    cur.execute(order,val)
    results = cur.fetchall()
    return results

def get_prescriptions_patient(patient_id):
    conn = connectDataBase()
    cur = conn.cursor()
    order = "SELECT diagnosis, medications, date FROM prescriptions WHERE patient_id = %s"
    val = (patient_id,)
    cur.execute(order,val)
    results = cur.fetchall()
    return results

def get_invoices_patient(patient_id):
    conn = connectDataBase()
    cur = conn.cursor()
    order ="SELECT amount, service_details, date FROM invoices WHERE patient_id = %s"
    val = (patient_id,)
    cur.execute(order,val)
    results = cur.fetchall()
    conn.close()
    return results
