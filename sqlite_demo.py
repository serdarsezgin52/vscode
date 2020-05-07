import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

# c.execute("""CREATE TABLE employee (
#             first text,
#             last text,
#             pay integer
# )""")

emp_1 = Employee('Jhon', 'Doe', '80000')
emp_2 = Employee('Jane', 'Doe', '90000')

print(emp_1.first)
print(emp_1.last)
print(emp_1.pay)

# c.execute("INSERT INTO employee VALUES(?, ?, ?)",(emp_1.first, emp_1.last, emp_1.pay))

# conn.commit()

# c.execute("INSERT INTO employee VALUES(:first, :last, :pay)", {'first':emp_2.first, 'last':emp_2.last, 'pay':emp_2.pay})

# conn.commit()

c.execute("SELECT * FROM employee WHERE last =?", ('Schafer',))

print(c.fetchall())

c.execute("SELECT * FROM employee WHERE last = last",{'last': 'Doe'})

print(c.fetchall())
conn.commit()

conn.close()


    