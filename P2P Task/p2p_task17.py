import sqlite3

conn=sqlite3.connect('mydb.db')
c=conn.cursor()

c.execute("""CREATE TABLE bag(
emp_code int(5),
emp_name varchar(25),
basic_salary varchar(50)

)""")

c.execute("INSERT INTO bag VALUES(4790,'kohli',11500)")
all_employees = [
    (4791,'Rohit',12000),
    (4792,'Gill',13200),
    (4793,'Dhawan',23000),
    (4794,'Yuvi',27000),
]

c.executemany("INSERT INTO bag VALUES(?,?,?)",all_employees)

c.execute("SELECT emp_name FROM bag WHERE basic_salary<=12500")
print(c.fetchall())
        
conn.commit()
conn.close()