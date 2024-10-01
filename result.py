from tkinter import *
from PIL import Image, ImageTk  # Make sure to install Pillow using `pip install pillow`
from tkinter import ttk,messagebox
import sqlite3


class ResultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1190x480+50+170")
        self.root.config(bg="white")
        self.root.focus_force()

        # === Title ===
        title = Label(self.root, text="Add Student Result", font=("goudy old style", 20, "bold"), bg="orange", fg="#262626").place(x=5, y=15, width=1180, height=50)


        #==========Widgets===========

        #========= Variable ============

        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks_ob = StringVar()
        self.var_full_marks = StringVar()
        self.roll_list = []
        self.fetch_roll()


        lbl_select = Label(self.root,text="Select Student",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=100)
        lbl_name = Label(self.root,text="Name",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=160)
        lbl_course = Label(self.root,text="Course",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=220)
        lbl_marks_ob = Label(self.root,text="Marks Obtained",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=280)
        lbl_full_marks = Label(self.root,text="Full Marks",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=340)


        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_roll,values=self.roll_list, font=("goudy old style", 15, "bold"),state="readonly",justify=CENTER)
        self.txt_student.place(x=280, y=100, width=170)
        self.txt_student.set("Select")


        btn_search =Button(self.root,text="search",font=("goudy old style",20,"bold"),bg="#2196f3",fg="white",cursor="hand2",command=self.search).place(x=470,y=100,width=110,height=28)

        # =========== Entery =======
        self.name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, "bold"), bg="lightyellow",state='readonly').place(x=280, y=160, width=300)
        
        self.course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 20, "bold"), bg="lightyellow",state='readonly').place(x=280, y=220, width=300)
              
        self.marks = Entry(self.root, textvariable=self.var_marks_ob, font=("goudy old style", 20, "bold"), bg="lightyellow").place(x=280, y=280, width=300)
              
        self.full_marks = Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 20, "bold"), bg="lightyellow").place(x=280, y=340, width=300)


        # ======== Button ============
        btn_add = Button(self.root,text="Submit",font=("times new roman",15),bg="lightgreen",activebackground="lightblue",cursor="hand2",command=self.add).place(x=300,y=410,width=120,height=35)

        btn_clear = Button(self.root,text="Clear",font=("times new roman",15),bg="lightgray",activebackground="red",cursor="hand2",command=self.clear).place(x=430,y=410,width=120,height=35)

        #===== Image =========
        self.bg_img = Image.open("image/result.png")
        self.bg_img = self.bg_img.resize((500, 300), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)  # Corrected to use ImageTk.PhotoImage

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=630,y=100)

        #===============================================

    def fetch_roll(self):
        con = sqlite3.connect(database="rocky.db")
        cur=con.cursor()
        try:
            cur.execute("select roll from student")
            rows = cur.fetchall()
            # v = []
            if len(rows) > 0:
                for row in rows:
                    self.roll_list.append(row[0])
            # print(v)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")    


    def search(self):
            con = sqlite3.connect(database="rocky.db")
            cur=con.cursor()
            try:
                cur.execute(f"select name,course from student WHERE roll=?",(self.var_roll.get(),))
                row = cur.fetchone()
                if row!=None:
                   self.var_name.set(row[0])
                   self.var_course.set(row[1])
                else:
                    messagebox.showerror("Error","No record found")
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to {str(ex)}")


    def add(self):
        con = sqlite3.connect(database="rocky.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "" :
                messagebox.showerror("Error","Please first search student record.",parent=self.root)
            else:
                cur.execute("select * from result where name=? and course=?",(self.var_roll.get(), self.var_course.get()))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Result already present.",parent=self.root)
                else:
                    per=(int(self.var_marks_ob.get())*100)/int(self.var_full_marks.get())
                    cur.execute("insert into result(roll,name,course,marks_ob,ful_marks,per) values (?,?,?,?,?,?)",(
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_marks_ob.get(),
                        self.var_full_marks.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result Added Successfully",parent=self.root)
                # print(row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error du to {str(ex)}")

    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_marks_ob.set(""),
        self.var_full_marks.set(""),






if __name__ == "__main__":
    root = Tk()
    obj = ResultClass(root)
    root.mainloop()
