from tkinter import *
from PIL import Image, ImageTk  # Make sure to install Pillow using `pip install pillow`
from tkinter import ttk,messagebox
import sqlite3


class StudentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1190x480+50+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # === Title ===
        title = Label(self.root, text="Manage Student Details", font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15, width=1180, height=35)

        # ===== Variables =====
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()

        # ==== column-1 ====
        lbl_roll = Label(self.root, text="Roll no", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=60)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=100)
        lbl_email = Label(self.root, text="Email", font=("goudy old style", 15, "bold"), bg="white").place(x=10, y=140)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style",15, "bold"), bg="white").place(x=10, y=180)


        lbl_state = Label(self.root, text="State", font=("goudy old style",15, "bold"), bg="white").place(x=10, y=220)
        # txt_state = Entry(self.root, textvariable=self.var_state, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=150, y=220, width=150)


        lbl_address = Label(self.root, text="Address", font=("goudy old style",15, "bold"), bg="white").place(x=10, y=270)

        #============= Entery fields - 1 ============ 
        self.txt_roll = Entry(self.root, textvariable=self.var_roll, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_roll.place(x=150, y=60, width=200)

        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 15, "bold"), bg="lightyellow")
        txt_name.place(x=150, y=100, width=200)
        
        txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 15, "bold"), bg="lightyellow")
        txt_email.place(x=150, y=140, width=200)

        self.txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender,values=("Select","Male","Femail","others"), font=("goudy old style", 15, "bold"),state="readonly",justify=CENTER)
        self.txt_gender.place(x=150, y=180, width=200)
        self.txt_gender.current(0)

        txt_state = ttk.Combobox(self.root, textvariable=self.var_state,values=["Select","Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"], font=("goudy old style", 15, "bold"),state="readonly",justify=CENTER)
        txt_state.place(x=150, y=220, width=150)
        txt_state.current(0)


        #============column-2========

        lbl_roll = Label(self.root, text="D.O.B", font=("goudy old style", 15, "bold"), bg="white").place(x=365, y=60)
        lbl_name = Label(self.root, text="Contact", font=("goudy old style", 15, "bold"), bg="white").place(x=365, y=100)
        lbl_email = Label(self.root, text="Addmission", font=("goudy old style", 15, "bold"), bg="white").place(x=365, y=140)
        lbl_gender = Label(self.root, text="Course", font=("goudy old style",15, "bold"), bg="white").place(x=365, y=180)
        lbl_city = Label(self.root, text="City", font=("goudy old style",15, "bold"), bg="white").place(x=310, y=220)
        txt_city = Entry(self.root, textvariable=self.var_city, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=370, y=220, width=120)
 

        lbl_pin = Label(self.root, text="Pin", font=("goudy old style",15, "bold"), bg="white").place(x=510, y=220)
        txt_pin = Entry(self.root, textvariable=self.var_pin, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=570, y=220, width=100)
        #============= Entery fields - 2 ============ 

        self.course_list = []
        # To function call
        self.fetch_course()

        txt_dob = Entry(self.root, textvariable=self.var_dob, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=480, y=60, width=200)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=480, y=100, width=200)
        txt_addmission = Entry(self.root, textvariable=self.var_a_date, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=480, y=140, width=200)

        self.txt_course = ttk.Combobox(self.root, textvariable=self.var_course,values=self.course_list, font=("goudy old style", 15, "bold"),state="readonly",justify=CENTER)
        self.txt_course.place(x=480, y=180, width=200)
        self.txt_course.set("Select")


        #===========Address===============


        self.txt_address = Text(self.root, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_address.place(x=150, y=270, width=500, height=100)

        #========== Buttons==================

        self.btn_add =Button(self.root,text="save",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.add)
        self.btn_add.place(x=150,y=400,width=110,height=40)
        self.btn_add =Button(self.root,text="Update",font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2",command=self.update)
        self.btn_add.place(x=270,y=400,width=110,height=40)
        self.btn_add =Button(self.root,text="Delete",font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2",command=self.delete)
        self.btn_add.place(x=390,y=400,width=110,height=40)
        self.btn_add =Button(self.root,text="Clear",font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2",command=self.clear)
        self.btn_add.place(x=510,y=400,width=110,height=40)

        #===== Search Panel =========
        self.search_var = StringVar()

        lbl_search_roll = Label(self.root, text="Roll No.", font=("goudy old style", 15, "bold"), bg="white").place(x=720, y=60)
        txt_search_roll = Entry(self.root, textvariable=self.search_var, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=870, y=60, width=180)
        btn_search =Button(self.root,text="search",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.search).place(x=1060,y=59,width=120,height=26)

        # ========= Contant ============

        self.c_frame = Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=720,y=100,width=460,height=340)

        scrolly = Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx = Scrollbar(self.c_frame,orient=HORIZONTAL)

        self.courseTable = ttk.Treeview(self.c_frame,columns=("roll","name","email","gender","dob","contact","addmission","course","state","city","pin","address"),xscrollcommand=scrollx.set,yscrollcommand=scrolly)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.courseTable.xview)
        scrolly.config(command=self.courseTable.yview)

        self.courseTable.heading("roll",text="Roll No")
        self.courseTable.heading("name",text="Name")
        self.courseTable.heading("email",text="Email")
        self.courseTable.heading("gender",text="Gender")
        self.courseTable.heading("dob",text="DOB")
        self.courseTable.heading("contact",text="Contact")
        self.courseTable.heading("addmission",text="Addmission")
        self.courseTable.heading("course",text="Course")
        self.courseTable.heading("state",text="State")
        self.courseTable.heading("city",text="City")
        self.courseTable.heading("pin",text="Pin")
        self.courseTable.heading("address",text="Address")
        self.courseTable["show"] = 'headings'

        self.courseTable.column("roll",width=100)
        self.courseTable.column("name",width=100)
        self.courseTable.column("email",width=100)
        self.courseTable.column("gender",width=100)
        self.courseTable.column("dob",width=100)
        self.courseTable.column("contact",width=100)
        self.courseTable.column("addmission",width=100)
        self.courseTable.column("course",width=100)
        self.courseTable.column("state",width=100)
        self.courseTable.column("city",width=100)
        self.courseTable.column("pin",width=100)
        self.courseTable.column("address",width=200)
        self.courseTable.pack(fill=BOTH,expand=1)
        self.courseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
       

    #===================================================

    def clear(self):
        self.show()
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_a_date.set(""),
        self.var_course.set("Select"),
        self.var_state.set("Select"),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.txt_address.delete("1.0",END),
        self.txt_roll.config(state=NORMAL),
        self.search_var.set("")


    def delete(self):
        con = sqlite3.connect(database="rocky.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error","Roll No. Should be require.",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Please select student from the list.",parent=self.root)
                else:        
                    op = messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op == True:
                        cur.execute("delete from student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error du to {str(ex)}")



    def get_data(self,ev):
        self.txt_roll.config(state='readonly')
        r = self.courseTable.focus()
        contant = self.courseTable.item(r)
        row = contant["values"]
        # print(row)
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_a_date.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.txt_address.delete("1.0",END),
        self.txt_address.insert(END,row[11])

        
    def add(self):
        con = sqlite3.connect(database="rocky.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error","Roll number Should be require.",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Roll number already present.",parent=self.root)
                else:
                    cur.execute("insert into student(roll,name,email,gender,dob,contact,addmission,course,state,city,pin,address) values (?,?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Details Added Successfully",parent=self.root)
                    self.show()
                # print(row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error du to {str(ex)}")
        
    def update(self):
        con = sqlite3.connect(database="rocky.db")
        cur = con.cursor()
        try:
            if self.var_roll.get() == "":
                messagebox.showerror("Error","Roll No. Should be require.",parent=self.root)
            else:
                cur.execute("select * from student where roll=?",(self.var_roll.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Select student from list.",parent=self.root)
                else:
                    cur.execute("UPDATE student SET name=? ,email=? ,gender=? ,dob=? ,contact=? ,addmission=? ,course=? ,state=? ,city=? ,pin=? ,address=?  where roll=?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                         self.var_roll.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","student update Successfully",parent=self.root)
                    self.show()
                # print(row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error du to {str(ex)}")


    def show(self):
        con = sqlite3.connect(database="rocky.db")
        cur=con.cursor()
        try:
            cur.execute("select * from student")
            rows = cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")


    def fetch_course(self):
        con = sqlite3.connect(database="rocky.db")
        cur=con.cursor()
        try:
            cur.execute("select name from course")
            rows = cur.fetchall()
            # v = []
            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])
            # print(v)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")      


    def search(self):
            con = sqlite3.connect(database="rocky.db")
            cur=con.cursor()
            try:
                cur.execute(f"select * from student WHERE roll=?",(self.search_var.get(),))
                row = cur.fetchone()
                if row!=None:
                    self.courseTable.delete(*self.courseTable.get_children())
                    self.courseTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found")
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = StudentClass(root)
    root.mainloop()
