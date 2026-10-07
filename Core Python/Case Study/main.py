from Empmanage import EmpManage
def logIn():
    em=EmpManage()
    uId=input("Enter the User Id= ")
    password=input("enter the Password= ")
    if uId=="admin" and password=="1234":
        while True:
            print("Plase Select 1 option from below: ")
            print("1.AddEmployee ")
            print("2.Dispaly All Employee  ")
            print("3.Search  Employee  ")
            print("4.Update  Employee  ")
            print("5.Delete Employee ")
            print("6.Exit ")
            choice=int(input("Enter the choice"))
            if choice==1:
                em.AddEmp()
            elif choice==2:
                em.displayEmp()
            elif choice==3:
                em.updateEmp()
            elif choice==4:
                em.searchEmp()
            elif choice==5:
                em.deleteEmp()
            elif choice==6:
                print("Thank you and visit agin...... ")
                break
            else:
                print("Invalid choice.... ")
            
    else:
        print("Invalid Id Or Password ")
logIn()