class Bank:
    __acc_name = []
    __acc_id = []
    __acc_bal = []
    __acc_intrest = []
    __intid=0
    def addacc(self):
        z = input("Enter the account name : ")
        self.__acc_name.append(z)
        z = int(input("Enter the id : "))
        self.__acc_id.append(z)
        print("Account Holder name : ", self.__acc_name[z-1])
        k = float(input(("Enter the amount to be added : ")))
        self.__acc_bal.append(k)
    def addoney(self):
        z = int(input("Enter the id : "))
        print("Account Holder name : ", self.__acc_name[z - 1])
        k1 = float(input(("Enter the amount to be added : ")))
        self.__acc_bal[z-1] += k1
        print("Money added Successfully")
        print("New Balance is : ", self.__acc_bal[z-1])
    def withdraw(self):
        z = int(input("Enter the id : "))
        print("Account Holder name : ", self.__acc_name[z - 1])
        k1 = float(input(("Enter the amount to be withdrawn : ")))
        self.__acc_bal[z - 1] -= k1
        print("Money withdrawn Successfully")
        print("New Balance is : ", self.__acc_bal[z - 1])
    def interest(self):
        z = int(input("Enter the id : "))
        print("Account Holder name : ", self.__acc_name[z - 1])
        bal = self.__acc_bal[z-1]
        si = (bal * 4 * 1) /100
        print("Interest is : ", si)
        print("Total Balance : ", bal+(si/12))
        self.__acc_intrest.append(si)
        self.__acc_bal[z - 1] += (si/12)
    def Transfer(self):
        z = int(input("Enter the id : "))
        print("Account Holder name : ", self.__acc_name[z - 1])
        print("Available Balance : ",self.__acc_bal[z-1])
        z1 = float(input("Enter the balance you want to transfer : "))
        try :
            if z1>self.__acc_bal[z-1]-100:
                print("Not Enough Funds")
            else:
                z2 = int(input("Enter the tansfer's id : "))
                print("Transfer'sAccount Holder name : ", self.__acc_name[z2 - 1])
                self.__acc_bal[z-1] -= z1
                self.__acc_bal[z2 - 1] += z1
                print("Transfer Successful")
        except:
            print("Server Down")
    def Show(self):
        z = int(input("Enter the id : "))
        print("Account Holder name : ", self.__acc_name[z - 1])
        print("Available Balance : ", self.__acc_bal[z - 1])
    def admin(self):
        print("Total Accounts : ", len(self.__acc_id))
        print("*ID*", "*Account Name*", "*Balance*")
        for i in range(len(self.__acc_id)):
            print(self.__acc_id[i], self.__acc_name[i], self.__acc_bal[i])




while(True):
    print("**************************************************************")
    print("1 . Add Account Holder")
    print("2 . Add Money ")
    print("3 . Remove Money")
    print("4 . See Interest")
    print("5 . Transfer Money")
    print("6 . Show Balance")
    z = int(input("Your Choice : "))
    print("**************************************************************")
    obj = Bank()
    if z == 1:
        obj.addacc()
        print("**************************************************************")
    elif z == 2:
        obj.addoney()
        print("**************************************************************")
    elif z == 3:
        obj.withdraw()
        print("**************************************************************")
    elif z == 4:
        obj.interest()
        print("**************************************************************")
    elif z == 5:
        obj.Transfer()
        print("**************************************************************")
    elif z == 6:
        obj.Show()
        print("**************************************************************")
    elif z == 7:
        obj.admin()




