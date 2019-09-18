import os
BankAccounts = {}

def errorMessage():
     print("\n\t----------------------------------------") 
     print("\t|(((( Please just enter numbers!!! ))))|")
     print("\t----------------------------------------")

def buyBuy():
    print("\n\n\n\n\t**********************************************")
    print("\t*** Thank you for your using our services! ***")
    print("\t**********************************************\n\n\n\n\n")
    

def EnterAccountNum():   
    while True:
        try:      
            Account = int(input("\n\n\tEnter new account number> "))
            if Account not in BankAccounts:              
               BankAccounts[Account] = 0
               print("\n\n\t((((((Account created))))))")
               return
            else:
                print("\n\n\t-->Account already exist<--")    
        except:
            errorMessage()

def AdmAnAccount(menuAdm1):  
    while True:
        try:              
            print("\n\t1. Withdraw money>")
            print("\t2. Insert money>")
            print("\t3. Show balance>")
            print("\t4. Exit ")
            menuAdm2 = int(input("\n\tSelect menu options> "))                           
            if menuAdm2 == 1:  
                os.system('cls')
                menuWithdraw = int(input("\n\n\tEnter amount to withdraw> "))
                if menuWithdraw < BankAccounts[menuAdm1]:
                    BankAccounts[menuAdm1] -= menuWithdraw
                    print("\t-------")
                else:
                     print(f"\n\tThe amount is too high your balance is only --> {BankAccounts[menuAdm1]}" )                  
            elif menuAdm2 == 2:
                 os.system('cls')
                 menuInsert = int(input("\n\n\tEnter amount to insert> "))
                 BankAccounts[menuAdm1] += menuInsert
                 print("\t+++++++") 
            elif menuAdm2 == 3:
                os.system('cls')
                print(f"\n\n\tYour balance in current account number {menuAdm1} is {BankAccounts[menuAdm1]}" ) 
                print("\t---------------------------------------------------",)
            elif menuAdm2 == 4:
                os.system('cls')
                break               
            
        except:
            errorMessage()  
            
while True:
    try:
        print("\n\n\t**********MAIN MENU*********")
        print("\t* 1. Create an account     *")
        print("\t* 2. Administer an account *")
        print("\t* 3. Exit                  *")
        print("\t****************************")
        menuMain = int(input("\tSelect menu options> ")) 
        os.system('cls')
        if menuMain == 1:
            EnterAccountNum()            
        elif menuMain == 2:
             menuAdm1 = int(input("\n\n\tEnter existing account number> "))
             if menuAdm1 in BankAccounts:              
                AdmAnAccount(menuAdm1)
             else:
                print("\n\tAccount does not exist!")
        elif menuMain == 3:
            buyBuy()
            break
                             
    except:
        errorMessage()
       



