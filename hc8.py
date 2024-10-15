class Employee:
    def __init__(self, id, name, salary, department):
        self.id=id
        self.name=name
        self.salary=salary
        self.department=department
    def assign_department(self, change):
        self.department=change
    def print_details(self):
        print(self.id+" "+self.name+" "+str(self.salary)+" "+self.department)
    def calculate(self, salary, hw):
        o=hw-50
        if o>0: oa=o*(salary/50)
        self.salary=salary+oa
nv1=Employee("ADAM","E7876",50000,"ACCOUNTING")
nv2=Employee("JONES","E7499",45000,"RESEARCH")
nv3=Employee("MARTIN","E7900",50000,"SALES")
nv4=Employee("SMITH","E7698",55000,"OPERATIONS")
nv1.calculate(50000,100)  
nv1.print_details()