import sqlite3

def create_db():
    con = sqlite3.connect(database="rocky.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT , name text , duration text, charges text , description text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT , name text,email text,gender text,dob text,contact text,addmission text,course text,state text,city text,pin text,address text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT , roll text, name text, course text ,marks_ob text , ful_marks text, per text)")
    con.commit()


    con = sqlite3.connect("rocky.db")
    cur = con.cursor()
     # Create table if not exists
    cur.execute("""CREATE TABLE IF NOT EXISTS register (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        f_name TEXT,
                        l_name TEXT,
                        contact TEXT,
                        email TEXT,
                        question TEXT,
                        answer TEXT,
                        password TEXT
                    )
                """)
    con.commit()
 

    # cur.execute("DROP TABLE IF EXISTS register")
    print("ho gya")

    
    con.close()
    
create_db()