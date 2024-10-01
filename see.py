import sqlite3

def create_db():
    # Correct connection creation
    con = sqlite3.connect('rocky.db')  # Make sure to specify the correct database name
    cur = con.cursor()

    # Execute the SQL query to retrieve all data from the 'register' table
    cur.execute("SELECT * FROM register")

    # Fetch all rows from the query result
    rows = cur.fetchall()

    # Check if rows exist and print them
    if rows:
        for row in rows:
            print(row)
    else:
        print("Data not found")

    # Close the connection
    con.close()

# Call the function to create the database and fetch data
create_db()



def forgot_password_window(self):
        ForgotPassword(self.root)  # Call the forgot password class


class ForgotPassword:
    def __init__(self, root):
        self.root = Toplevel()
        self.root.title("Forgot Password")
        self.root.geometry("500x400+500+150")

        # Frame for Forgot Password
        title = Label(self.root, text="Forgot Password", font=("times new roman", 20, "bold"), bg="white", fg="green").pack(side=TOP, fill=X)

        # Email
        email = Label(self.root, text="Email", font=("times new roman", 15, "bold")).place(x=50, y=100)
        self.txt_email = Entry(self.root, font=("times new roman", 15), bg="lightgrey")
        self.txt_email.place(x=50, y=130, width=250)

        # Security Question
        question = Label(self.root, text="Security Question", font=("times new roman", 15, "bold")).place(x=50, y=170)
        self.cmb_quest = ttk.Combobox(self.root, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_quest["values"] = ("Select", "Your pet name", "Your birth place", "Your best friend name")
        self.cmb_quest.place(x=50, y=200, width=250)
        self.cmb_quest.current(0)

        # Answer
        answer = Label(self.root, text="Answer", font=("times new roman", 15, "bold")).place(x=50, y=240)
        self.txt_answer = Entry(self.root, font=("times new roman", 15), bg="lightgrey")
        self.txt_answer.place(x=50, y=270, width=250)

        # New Password
        new_password = Label(self.root, text="New Password", font=("times new roman", 15, "bold")).place(x=50, y=310)
        self.txt_new_password = Entry(self.root, font=("times new roman", 15), bg="lightgrey")
        self.txt_new_password.place(x=50, y=340, width=250)

        # Button Reset Password
        btn_reset_password = Button(self.root, text="Reset Password", font=("goudy old style", 15, "bold"), bg="#008000", fg="white", cursor="hand2", command=self.reset_password).place(x=50, y=380, width=200)

    def reset_password(self):
        # Connect to the database and verify the user by security question
        con = sqlite3.connect("rocky.db")
        cur = con.cursor()

        try:
            if self.txt_email.get() == "" or self.cmb_quest.get() == "Select" or self.txt_answer.get() == "" or self.txt_new_password.get() == "":
                messagebox.showerror("Error", "All Fields are Required", parent=self.root)
            else:
                cur.execute("SELECT * FROM register WHERE email=? AND question=? AND answer=?", (self.txt_email.get(), self.cmb_quest.get(), self.txt_answer.get()))
                row = cur.fetchone()

                if row == None:
                    messagebox.showerror("Error", "Invalid Security Answer", parent=self.root)
                else:
                    cur.execute("UPDATE register SET password=? WHERE email=?", (self.txt_new_password.get(), self.txt_email.get()))
                    con.commit()
                    messagebox.showinfo("Success", "Password has been reset", parent=self.root)
                    self.root.destroy()

        except Exception as es:
            messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)
        finally:
            con.close()