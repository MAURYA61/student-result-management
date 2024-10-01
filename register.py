from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3
import os


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.setup_background()
        self.create_register_frame()

    def setup_background(self):
        # Background Image
        self.bg = ImageTk.PhotoImage(file="logingfiles/reimage/back.jpg")
        Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        # Left Image
        img = Image.open("logingfiles/reimage/singup.jpg").resize((400, 500), Image.LANCZOS)
        self.left = ImageTk.PhotoImage(img)
        Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

    def create_register_frame(self):
        # Register Frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="REGISTER HERE", font=("times new roman", 20, "bold"), bg="white", fg="green")
        title.place(x=50, y=30)

        # Creating input fields
        self.create_input_fields(frame1)

        # Register Button
        self.btn_register = Button(frame1, text="Register Now", font=("goudy old style", 15, "bold"), bg="#008000", fg="white", cursor="hand2", command=self.register_data)
        self.btn_register.place(x=50, y=420, width=200)

        Button(frame1, text="Sign In", font=("goudy old style", 15, "bold"), bg="#008000", fg="#fff", cursor="hand2", command=self.open_login).place(x=260, y=420, width=210)

    def create_input_fields(self, frame):
        # Row 1
        self.txt_fname = self.create_label_entry(frame, "First Name", 50, 100, 250)
        self.txt_lname = self.create_label_entry(frame, "Last Name", 370, 100, 250)

        # Row 2
        self.txt_contact = self.create_label_entry(frame, "Contact No.", 50, 170, 250)
        self.txt_email = self.create_label_entry(frame, "Email", 370, 170, 250)

        # Row 3
        self.cmb_quest = self.create_security_question(frame, 50, 240)
        self.txt_answer = self.create_label_entry(frame, "Answer", 370, 240, 250)

        # Row 4
        self.txt_password = self.create_label_entry(frame, "Password", 50, 310, 250, show="*")
        self.txt_cpassword = self.create_label_entry(frame, "Confirm Password", 370, 310, 250, show="*")

        # Terms Checkbox
        self.var_chk = IntVar()
        Checkbutton(frame, text="I Agree with terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", font=("times new roman", 13)).place(x=50, y=380)

    def create_label_entry(self, frame, label_text, x, y, width, show=None):
        Label(frame, text=label_text, font=("times new roman", 15, "bold"), bg="white", fg="grey").place(x=x, y=y)
        entry = Entry(frame, font=("times new roman", 15), bg="lightgrey", show=show)
        entry.place(x=x, y=y + 30, width=width)
        return entry

    def create_security_question(self, frame, x, y):
        Label(frame, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="grey").place(x=x, y=y)
        cmb = ttk.Combobox(frame, font=("times new roman", 13), state='readonly', justify=CENTER)
        cmb["values"] = ("Select", "Your pet name", "Your birth place", "Your best friend name")
        cmb.place(x=x, y=y + 30, width=250)
        cmb.current(0)
        return cmb

    def register_data(self):
        if self.validate_registration_fields():
            try:
                # Database connection
                con = sqlite3.connect(database="rocky.db")
                cur = con.cursor()
                # Inserting data into the database
                cur.execute("INSERT INTO register(f_name, l_name, contact, email, question, answer, password) VALUES(?, ?, ?, ?, ?, ?, ?)",
                            (
                                self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_contact.get(),
                                self.txt_email.get(),
                                self.cmb_quest.get(),
                                self.txt_answer.get(),
                                self.txt_password.get()
                            ))

                con.commit()
                messagebox.showinfo("Success", "Registration Successful", parent=self.root)
                self.clear_fields()

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
            finally:
                con.close()

    def validate_registration_fields(self):
        if (self.txt_fname.get() == "" or self.txt_contact.get() == "" or self.txt_email.get() == "" or
                self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or
                self.txt_password.get() == "" or self.txt_cpassword.get() == ""):
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
            return False
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please Agree with our Terms & Conditions", parent=self.root)
            return False
        elif self.txt_password.get() != self.txt_cpassword.get():
            messagebox.showerror("Error", "Password & Confirm password should be the same", parent=self.root)
            return False
        return True

    def clear_fields(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.var_chk.set(0)

    def open_login(self):
        self.root.destroy()
        root = Tk()
        Login(root)
        root.mainloop()


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        self.setup_background()
        self.create_login_frame()

    def setup_background(self):
        # Background Image
        self.bg = ImageTk.PhotoImage(file="logingfiles/reimage/back.jpg")
        Label(self.root, image=self.bg).place(x=250, y=0, relwidth=1, relheight=1)

        # Left Image
        img = Image.open("logingfiles/reimage/singup.jpg").resize((400, 500), Image.LANCZOS)
        self.left = ImageTk.PhotoImage(img)
        Label(self.root, image=self.left).place(x=80, y=100, width=400, height=500)

    def create_login_frame(self):
        # Login Frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=500)

        title = Label(frame1, text="LOGIN HERE", font=("times new roman", 20, "bold"), bg="white", fg="green")
        title.place(x=50, y=30)

        # Email and Password Input
        self.txt_email = self.create_label_entry(frame1, "Email", 50, 100, 250)
        self.txt_password = self.create_label_entry(frame1, "Password", 50, 170, 250, show="*")

        # Forget password button
        Button(frame1, text="Forgot Password?", font=("times new roman", 13), bg="white", fg="blue", bd=0, command=self.forgot_password_window).place(x=50, y=250)

        # Login and Register buttons
        Button(frame1, text="Login", font=("goudy old style", 15, "bold"), bg="#008000", fg="white", cursor="hand2", command=self.login_data).place(x=50, y=300, width=200)
        Button(frame1, text="Register Now", font=("goudy old style", 15, "bold"), bg="#008000", fg="white", cursor="hand2", command=self.register).place(x=300, y=300, width=200)

    def create_label_entry(self, frame, label_text, x, y, width, show=None):
        Label(frame, text=label_text, font=("times new roman", 15, "bold"), bg="white", fg="grey").place(x=x, y=y)
        entry = Entry(frame, font=("times new roman", 15), bg="lightgrey", show=show)
        entry.place(x=x, y=y + 30, width=width)
        return entry

    def login_data(self):
        if self.validate_login_fields():
            try:
                # Database connection
                con = sqlite3.connect("rocky.db")
                cur = con.cursor()
                cur.execute("SELECT * FROM register WHERE email=? AND password=?", (self.txt_email.get(), self.txt_password.get()))
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Invalid Email or Password", parent=self.root)
                else:
                    messagebox.showinfo("Success", "Welcome", parent=self.root)
                    self.root.destroy()
                    os.system("python dasboard.py")


            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
            finally:
                con.close()

    def validate_login_fields(self):
        if self.txt_email.get() == "" or self.txt_password.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
            return False
        return True

    def forgot_password_window(self):
        self.forgot_window = Toplevel(self.root)
        self.forgot_window.title("Forgot Password")


        self.forgot_window.geometry("400x300")
        self.forgot_window.config(bg="white")

        Label(self.forgot_window, text="We Are wrok on that", font=("times new roman", 15), bg="white").pack(pady=10)
        # email_entry = Entry(self.forgot_window, font=("times new roman", 15))
        # email_entry.pack(pady=10)

        # Button(self.forgot_window, text="Submit", command=lambda: self.verify_email(email_entry.get())).pack(pady=20)

    def verify_email(self, email):
        con = sqlite3.connect("rocky.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM register WHERE email=?", (email,))
        row = cur.fetchone()
        
        if row:
            messagebox.showinfo("Success", "Email found! You can reset your password.", parent=self.forgot_window)
            # Here you can add more logic to reset the password
        else:
            messagebox.showerror("Error", "Email not found!", parent=self.forgot_window)

        con.close()


    def register(self):
        self.root.destroy()
        root = Tk()
        Register(root)
        root.mainloop()


if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
