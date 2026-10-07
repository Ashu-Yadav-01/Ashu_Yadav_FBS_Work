from hr import Hr
from dev import Dev
class EmpManage:
    empDat = {}
    def AddEmp(self):
        print("-------------------- Add Emp --------------------")
        empId = int(input("Enter the EmpID: "))
        if empId in self.empDat:
            print("Employee already Exists.....")
            return
        name = input("Enter the name of Emp: ")
        sal = float(input("Enter the Sal: "))
        print("1. HR")
        print("2. Developer")
        ch = int(input("Enter the Choice: "))
        if ch == 1:
            com = float(input("Enter the Comm: "))
    def displayEmp(self):
        print()
        #for emp in EmpManage.empData.values():
        #    print(emp)
    def searchEmp(self):
        print("Search Emp")
    def updateEmp(self):
        print("Update Emp")
    def deleteEmp(self):
        print("Delete Emp")