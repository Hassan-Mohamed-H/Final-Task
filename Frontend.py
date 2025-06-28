
import customtkinter as ctk
from customtkinter import CTkImage
from tkinter import *
from PIL import Image, ImageTk
from Backend import (
    loginBack,Statestics, get_patients, get_patient_details, get_appointments_patient,
    get_prescriptions_patient, get_invoices_patient
)

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")




def show_frame(target):
    for f in [dashboard_frame, patients_frame, details_frame,statistics_frame]:
        f.pack_forget()
    target.pack(fill="both", expand=True)

def Clinic_Dashboard():
    title_label = ctk.CTkLabel(
        dashboard_frame,
        text="🩺 Clinic Dashboard",
        font=("Arial", 22, "bold"),
        text_color="#2C3E50"
    )
    title_label.pack(pady=(30, 25))

    def open_statistics(): 
        PatientsCount, appointmentsCount, invoicesTotal = Statestics()
        Statestics_Dashboard(PatientsCount, appointmentsCount, invoicesTotal)
        

    def manage_patients():
        Patients_Dashboard()
        show_frame(patients_frame)

    def add_patient():
        print("Adding New Patient...")

    def view_appointments():
        print("Viewing Appointments...")

    def view_prescriptions():
        print("Viewing Prescriptions...")

    def view_invoices():
        print("Viewing Invoices...")

    def logout():
        print("Logging out...")

    buttons = [
        ("📊 Statistics", open_statistics),
        ("👤 Manage Patients", manage_patients),
        ("➕ Add Patient", add_patient),
        ("📅 Appointments", view_appointments),
        ("📝 Prescriptions", view_prescriptions),
        ("🧾 Invoices", view_invoices),
        ("🔗 Logout", logout),
    ]

    for text, func in buttons:
        button = ctk.CTkButton(
            dashboard_frame,
            text=text,
            font=("Arial", 16, "bold"),
            width=600,
            height=50,
            corner_radius=10,
            fg_color="#2874A6",
            hover_color="#21618C",
            text_color="white",
            command=func
        )
        button.pack(pady=8)

def Statestics_Dashboard(PatientsCount, appointmentsCount, invoicesTotal):
    for widget in statistics_frame.winfo_children():
        widget.destroy()

    ctk.CTkLabel(statistics_frame, text="📊 Clinic Statistics", font=("Arial", 22, "bold")).pack(pady=(25, 20))

    ctk.CTkLabel(statistics_frame, text=f"👥 Total Patients: {PatientsCount}", font=("Arial", 16)).pack(pady=10)
    ctk.CTkLabel(statistics_frame, text=f"📅 Total Appointments: {appointmentsCount}", font=("Arial", 16)).pack(pady=10)
    ctk.CTkLabel(statistics_frame, text=f"💰 Total Invoice Amount: ${invoicesTotal}", font=("Arial", 16)).pack(pady=10)

    ctk.CTkButton(statistics_frame, text="⬅ Back", width=100, command=lambda: show_frame(dashboard_frame)).pack(pady=25)

    show_frame(statistics_frame)

def Patients_Dashboard():
    for widget in patients_frame.winfo_children():
        widget.destroy()

    frame = ctk.CTkFrame(patients_frame, width=840, height=580, fg_color="#EDEDED", corner_radius=20)
    frame.place(x=20, y=20)
    frame.pack_propagate(False)

    ctk.CTkLabel(frame, text="👤 Patients", font=("Arial", 22, "bold"), text_color="black").pack(pady=(25, 15))

    patients = get_patients()
    for idx, (pid, name, age) in enumerate(patients, start=1):
        row_frame = ctk.CTkFrame(frame, fg_color="#D7DBDD", corner_radius=10)
        row_frame.pack(padx=60, pady=5, fill="x")

        label = ctk.CTkLabel(row_frame, text=f"{idx}. {name} ({age} yrs)", font=("Arial", 14), anchor="w")
        label.pack(side="left", padx=15, pady=8, expand=True)

        btn = ctk.CTkButton(
            row_frame, text="Details", width=100, fg_color="#3498DB", hover_color="#2E86C1",
            command=lambda pid=pid: [show_details_Patients(pid), show_frame(details_frame)]
        )
        btn.pack(side="right", padx=15, pady=5)

    back_btn = ctk.CTkButton(frame, text="⬅ Back", width=100, font=("Arial", 14), command=lambda: show_frame(dashboard_frame))
    back_btn.pack(pady=25)

def show_details_Patients(patient_id):
    for widget in details_frame.winfo_children():
        widget.destroy()

    patient = get_patient_details(patient_id)
    appointments = get_appointments_patient(patient_id)
    prescriptions = get_prescriptions_patient(patient_id)
    invoices = get_invoices_patient(patient_id)

    scroll_frame = ctk.CTkScrollableFrame(details_frame, width=840, height=580, fg_color="#F2F3F4")
    scroll_frame.pack(padx=20, pady=20)

    name, gender, age, phone, address = patient
    ctk.CTkLabel(scroll_frame, text=f"👤 {name} ", font=("Arial", 18, "bold")).pack(pady=(10, 5))
    ctk.CTkLabel(scroll_frame, text=f"Gender: {gender} | Age {age} yrs | Phone: {phone}", font=("Arial", 14)).pack()
    ctk.CTkLabel(scroll_frame, text=f"Address: {address}", font=("Arial", 14)).pack(pady=(0, 15))

    ctk.CTkLabel(scroll_frame, text="🗕 Appointments", font=("Arial", 16, "bold")).pack(pady=(10, 5))
    if appointments:
        for date, time, notes in appointments:
            ctk.CTkLabel(scroll_frame, text=f"- {date} at {time} | Notes: {notes}", font=("Arial", 13)).pack(anchor="center", padx=10)
    else:
        ctk.CTkLabel(scroll_frame, text="No appointments.", font=("Arial", 13), text_color="gray").pack()

    ctk.CTkLabel(scroll_frame, text="📝 Prescriptions", font=("Arial", 16, "bold")).pack(pady=(15, 5))
    if prescriptions:
        for diagnosis, meds, date in prescriptions:
            ctk.CTkLabel(scroll_frame, text=f"- {date} | {diagnosis} → {meds}", font=("Arial", 13)).pack(anchor="center", padx=10)
    else:
        ctk.CTkLabel(scroll_frame, text="No prescriptions.", font=("Arial", 13), text_color="gray").pack()

    ctk.CTkLabel(scroll_frame, text="💵 Invoices", font=("Arial", 16, "bold")).pack(pady=(15, 5))
    if invoices:
        for amount, service, date in invoices:
            ctk.CTkLabel(scroll_frame, text=f"- {date} | {service} = ${amount}", font=("Arial", 13)).pack(anchor="center", padx=10)
    else:
        ctk.CTkLabel(scroll_frame, text="No invoices.", font=("Arial", 13), text_color="gray").pack()

    ctk.CTkButton(scroll_frame, text="⬅ Back", width=100, command=lambda: show_frame(patients_frame)).pack(pady=20)


def loginfront():
    win = Tk()
    win.geometry("1024x720+224+45")
    win.title("Login")
    win.resizable(False, False)

    bg_image = Image.open(r"E:\Python Track\final task\photos\login interface.png")
    bg_photo = ImageTk.PhotoImage(bg_image)
    lbl_bg = Label(win, image=bg_photo)
    lbl_bg.image = bg_photo
    lbl_bg.place(x=0, y=0)

    var_username = StringVar()
    var_password = StringVar()
    result = {"status": False}

    def login():
        username = var_username.get()
        password = var_password.get()
        data = loginBack(username, password)

        def after_success():
            result["status"] = True
            win.destroy()

        if data == "wrong_password":
               wrongpass = Label(win, text="Wrong Password", font=("Franklin Gothic Heavy", 14),
                          fg="#9c375f", background="#a1aaa9")
               wrongpass.place(x=518.9, y=460.09, width=166.78, height=24.27)

        elif data is None:
            wronguser = Label(win, text="Wrong username", font=("Franklin Gothic Heavy", 14),
                            fg="#9c375f", background="#a7b0af")
            wronguser.place(x=517.53, y=374.09, width=169.5, height=24.27)

        else:
            Login_done = Label(win, text="Login done !", relief="flat", font=("Franklin Gothic Heavy", 24),
                            fg="#f8e967", background="#9ca29d", activebackground="#f18f0f", bd=0)
            Login_done.place(x=367.43, y=547.42, width=263.9, height=52.26)
            win.after(3000, after_success)
        
        
    var_username = StringVar()
    var_password = StringVar()

    def focus_password(e):
        entry_password.focus_set()
        return "break"
    def focus_login(e):
        login()
        return "break"
    entry_username = Entry(win,font=("Franklin Gothic Heavy",20),fg="#c6d2c8",highlightthickness=3,
                highlightbackground="#576b53",highlightcolor="#576b53",relief="flat",bd=0,textvariable=var_username)
    entry_username.place(x=335.97,y=329.5,width=328.07,height=41.24)
    entry_username.bind("<Return>",focus_password)

    entry_password = Entry(win,font=("Franklin Gothic Heavy",20),fg="#c6d2c8",highlightthickness=2,
                highlightbackground="#576b53",highlightcolor="#576b53",relief="flat",bd=0,textvariable=var_password,show="*")
    entry_password.place(x=335.97,y=416.5,width=328.07,height=41.24)
    entry_password.bind("<Return>",focus_login)


    def bt_login_enter(e):
        bt_login.config(bg="#99ad61")
    def bt_login_leave(e):
        bt_login.config(bg="#97a670")    

    bt_login = Button(win,text="Login",font=("Franklin Gothic Heavy",20),fg="#bfd2c2",relief="flat",
                background="#97a670",activebackground="#657242",bd=0)
    bt_login.place(x=441.53,y=496.38,width=116.97,height=42.53)
    bt_login.config(command=login)
    bt_login.bind("<Enter>",bt_login_enter)
    bt_login.bind("<Leave>",bt_login_leave)
    win.mainloop()
    return result["status"]


if loginfront():
    app = ctk.CTk()
    app.title("Clinic Dashboard")
    app.geometry("880x620+400+100")
    app.configure(fg_color="#FFFFFF")
    app.resizable(False, False)

    dashboard_frame = ctk.CTkFrame(app, fg_color="white")
    patients_frame = ctk.CTkFrame(app, fg_color="white")
    details_frame = ctk.CTkFrame(app, fg_color="white")
    statistics_frame = ctk.CTkFrame(app, fg_color="white")

    Clinic_Dashboard()
    show_frame(dashboard_frame)

    app.mainloop()
