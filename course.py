from tkinter import *
from PIL import Image, ImageTk  # Make sure to install Pillow using `pip install pillow`
from tkinter import ttk,messagebox
import sqlite3


class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1190x480+50+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # === Title ===
        title = Label(self.root, text="Management Course Details", font=("goudy old style", 20, "bold"), bg="#033054", fg="white")
        title.place(x=10, y=15, width=1180, height=35)

        # ===== Variables =====
        self.var_cid = StringVar()
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charge = StringVar()

        # ==== Widgets ====
        lbl_cid = Label(self.root, text="Course ID", font=("goudy old style", 15, "bold"), bg="white")
        lbl_cid.place(x=10, y=60)
        lbl_courseName = Label(self.root, text="CourseName", font=("goudy old style", 15, "bold"), bg="white")
        lbl_courseName.place(x=10, y=100)
        lbl_duration = Label(self.root, text="Duration", font=("goudy old style", 15, "bold"), bg="white")
        lbl_duration.place(x=10, y=140)
        lbl_charges = Label(self.root, text="Charges", font=("goudy old style", 15, "bold"), bg="white")
        lbl_charges.place(x=10, y=180)
        lbl_description = Label(self.root, text="Description", font=("goudy old style",15, "bold"), bg="white")
        lbl_description.place(x=10, y=220)

        # Text Entry Fields
        self.txt_cid = Entry(self.root, textvariable=self.var_cid, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_cid.place(x=150,y=60,width=200)

        self.txt_courseName = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_courseName.place(x=150, y=100, width=200)

        txt_duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, "bold"), bg="lightyellow")
        txt_duration.place(x=150, y=140, width=200)

        txt_charges = Entry(self.root, textvariable=self.var_charge, font=("goudy old style", 15, "bold"), bg="lightyellow")
        txt_charges.place(x=150, y=180, width=200)

        self.txt_description = Text(self.root, font=("goudy old style", 15, "bold"), bg="lightyellow")
        self.txt_description.place(x=150, y=220, width=500, height=130)

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

        lbl_search_courseName = Label(self.root, text="Course Name", font=("goudy old style", 15, "bold"), bg="white")
        lbl_search_courseName.place(x=720, y=60)
        txt_search_courseName = Entry(self.root, textvariable=self.search_var, font=("goudy old style", 15, "bold"), bg="lightyellow").place(x=870, y=60, width=180)
        btn_search =Button(self.root,text="search",font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.search).place(x=1060,y=59,width=120,height=26)

        # ========= Contant ============

        self.c_frame = Frame(self.root,bd=2,relief=RIDGE)
        self.c_frame.place(x=720,y=100,width=460,height=340)

        scrolly = Scrollbar(self.c_frame,orient=VERTICAL)
        scrollx = Scrollbar(self.c_frame,orient=HORIZONTAL)

        self.courseTable = ttk.Treeview(self.c_frame,columns=("cid","name","duration","charges","description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        scrollx.config(command=self.courseTable.xview)
        scrolly.config(command=self.courseTable.yview)

        self.courseTable.heading("cid",text="Course ID")
        self.courseTable.heading("name",text="Name")
        self.courseTable.heading("charges",text="Charges")
        self.courseTable.heading("duration",text="Duration")
        self.courseTable.heading("description",text="Description")
        self.courseTable["show"] = 'headings'

        self.courseTable.column("cid",width=100)
        self.courseTable.column("name",width=100)
        self.courseTable.column("charges",width=100)
        self.courseTable.column("duration",width=120)
        self.courseTable.column("description",width=150)
        self.courseTable.pack(fill=BOTH,expand=1)
        self.courseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()

    #===================================================

    def clear(self):
        self.show()
        self.var_cid.set("")
        self.var_course.set("")
        self.var_charge.set("")
        self.var_duration.set("")
        self.search_var.set("")
        self.txt_description.delete("1.0",END)
        self.txt_courseName.config(state=NORMAL)


    def delete(self):
        con = sqlite3.connect(database="rocky.db")
        cur = con.cursor()
        try:
            if self.var_cid.get() == "":
                messagebox.showerror("Error","Course Name Should be require.",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Please select course from the list.",parent=self.root)
                else:        
                    op = messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op == True:
                        cur.execute("delete from course where name=?",(self.var_course.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error du to {str(ex)}")



    def get_data(self,ev):
        self.txt_cid.config(state="readonly")
        self.txt_courseName.config(state="readonly")
        r = self.courseTable.focus()
        contant = self.courseTable.item(r)
        row = contant["values"]
        # print(row)
        self.var_cid.set(row[0])
        self.var_course.set(row[1])
        self.var_charge.set(row[2])
        self.var_duration.set(row[3])
        self.txt_description.delete("1.0",END)
        self.txt_description.insert(END,row[4])

    def add(self):
        con = sqlite3.connect(database="rocky.db")
        cur = con.cursor()
        try:
            if self.var_cid.get() == "" :
                messagebox.showerror("Error","Course ID Should be require.",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Course Name already present.",parent=self.root)
                else:
                    cur.execute("insert into course(cid,name,duration,charges,description) values (?,?,?,?,?)",(
                        self.var_cid.get(),
                        self.var_course.get(),
                        self.var_duration.get(),
                        self.var_charge.get(),
                        self.txt_description.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Added Successfully",parent=self.root)
                    self.show()
                # print(row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error du to {str(ex)}")
        
    def update(self):
        con = sqlite3.connect(database="rocky.db")
        cur = con.cursor()
        try:
            if self.var_cid.get() == "":
                messagebox.showerror("Error","Course Name Should be require.",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Select course from list.",parent=self.root)
                else:
                    cur.execute("update course set duration=?,charges=?,description=? where id=?",(
                        self.var_duration.get(),
                        self.var_charge.get(),
                        self.txt_description.get("1.0",END),
                        self.var_course.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course update Successfully",parent=self.root)
                    self.show()
                # print(row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error du to {str(ex)}")




    def show(self):
        con = sqlite3.connect(database="rocky.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            rows = cur.fetchall()
            self.courseTable.delete(*self.courseTable.get_children())
            for row in rows:
                self.courseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")      


    def search(self):
            con = sqlite3.connect(database="rocky.db")
            cur=con.cursor()
            try:
                cur.execute(f"select * from course WHERE name LIKE '%{self.search_var.get()}%'")
                rows = cur.fetchall()
                self.courseTable.delete(*self.courseTable.get_children())
                for row in rows:
                    self.courseTable.insert('',END,values=row)
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")

if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()
