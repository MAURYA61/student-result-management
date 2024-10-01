from tkinter import *
from PIL import Image, ImageTk  # Make sure to install Pillow using `pip install pillow`
from course import CourseClass
from student import StudentClass
from result import ResultClass
from report import ReportClass
from tkinter import messagebox
import sqlite3
import os

class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # === Title ===
        title = Label(self.root, text="Student Result Management System", font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)

        # ==== Menu ====
        m_frame = LabelFrame(self.root, text="Menu", font=("times new roman", 15), bg="white")
        m_frame.place(x=10, y=70, width=1250, height=80) 

        # == Buttons ==
        btn_course = Button(m_frame, text="Course", font=("goudy old style", 15, "bold"), bg="#033054", fg="white", cursor="hand2",command=self.add_course).place(x=20, y=5, width=200, height=40)

        btn_student = Button(m_frame, text="Student", font=("goudy old style", 15, "bold"), bg="#033054", fg="white", cursor="hand2",command=self.add_student).place(x=240, y=5, width=200, height=40)

        btn_result = Button(m_frame, text="Result", font=("goudy old style", 15, "bold"), bg="#033054", fg="white", cursor="hand2", command=self.add_result).place(x=460, y=5, width=200, height=40)

        btn_viewStudent = Button(m_frame, text="View Student Result", font=("goudy old style", 15, "bold"), bg="#033054", fg="white", cursor="hand2" ,command=self.view_result).place(x=680, y=5, width=200, height=40)

        btn_logout = Button(m_frame, text="Logout", font=("goudy old style", 15, "bold"), bg="#033054", fg="white", cursor="hand2",command=self.log_out).place(x=900, y=5, width=150, height=40)

        btn_exit = Button(m_frame, text="Exit", font=("goudy old style", 15, "bold"), bg="#033054", fg="white", cursor="hand2",command=self.exit).place(x=1080, y=5, width=150, height=40)

        # ==== Content Window ===
        self.bg_img = Image.open("image/bgImage.jpg")
        self.bg_img = self.bg_img.resize((920, 350), Image.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)  # Corrected to use ImageTk.PhotoImage

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=460, y=170, width=800, height=350)

        #===== Update--Details =====
        self.lbl_course = Label(self.root, text="total Courses\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#e43b06", fg="white")
        self.lbl_course.place(x= 457, y=530, width=250, height=100)

        self.lbl_student = Label(self.root, text="total Student\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#0676ad", fg="white")
        self.lbl_student.place(x=735, y=530, width=250, height=100)

        self.lbl_result = Label(self.root, text="total Result\n[ 0 ]", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#038074", fg="white")
        self.lbl_result.place(x=1010, y=530, width=250, height=100)

        # == Footer ==
        footer = Label(self.root, text="ROCKY - Student Result Management System\nContact us for any technical issue: 8809017568", font=("goudy old style", 12), bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

        #=== Functions Calling ===
        self.update_details()

    
    def update_details(self):
        con = sqlite3.connect(database="rocky.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
            # self.lbl_course.after(200,self.update_details)

            cur.execute("select * from student")
            cr = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n[{str(len(cr))}]")
            # self.lbl_student.after(200,self.update_details)

            cur.execute("select * from result")
            cr = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n[{str(len(cr))}]")
            # self.lbl_result.after(200,self.update_details)

            self.lbl_course.after(200,self.update_details)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")  


    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)


    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ResultClass(self.new_win)

    def view_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = ReportClass(self.new_win)

    def log_out(self):
        op = messagebox.askyesno("Confirm","Do you really want to logout ? ",parent=self.root)
        if op == True:
            self.root.destroy()
            os.system("python register.py")

    def exit(self):
        op = messagebox.askyesno("Confirm","Do you really want to exit.",parent=self.root)
        self.root.destroy()



if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
