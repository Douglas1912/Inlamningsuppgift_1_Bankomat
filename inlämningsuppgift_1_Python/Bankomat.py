import os
BankAccounts = {}
def errorMessage():
     print("\n\t----------------------------------------") 
     print("\t|(((( Please just enter numbers!!! ))))|")
     print("\t----------------------------------------")
def byeBye():
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
def LoginMenu(loginToAccount):  
    while True:
        try:              
            print("\n\t1. Withdraw money>")
            print("\t2. Insert money>")
            print("\t3. Show balance>")
            print("\t4. Exit ")
            selectInLoginMenu = int(input("\n\tSelect menu options> "))                           
            if selectInLoginMenu == 1:  
                os.system('cls')
                menuWithdraw = int(input("\n\n\tEnter amount to withdraw> "))
                if menuWithdraw <= BankAccounts[loginToAccount] and menuWithdraw > 0:
                    BankAccounts[loginToAccount] -= menuWithdraw
                    print("\t-------")
                else:
                     print(f"\n\tInvalid amount your balance is only --> {BankAccounts[loginToAccount]} €" )                  
            elif selectInLoginMenu == 2:
                 os.system('cls')
                 menuInsert = int(input("\n\n\tEnter amount to insert> "))
                 if menuInsert < 0:
                    print(f"\n\tTo low cant accept amount below zero! " )  
                 else:                      
                     BankAccounts[loginToAccount] += menuInsert
                     print("\t+++++++") 
            elif selectInLoginMenu == 3:
                 os.system('cls')
                 print(f"\n\n\tYour balance in current account number {loginToAccount} is {BankAccounts[loginToAccount]} €" ) 
                 print("\t---------------------------------------------------",)
            elif selectInLoginMenu == 4:
                 os.system('cls')
                 break                          
        except:
            errorMessage()              
while True:
    try:
        print("\n\n\t**********MAIN MENU*********")
        print("\t* 1. Create an account     *")
        print("\t* 2. Login to account      *")
        print("\t* 3. Exit                  *")
        print("\t****************************")
        selectInMainMenu = int(input("\tSelect menu options> ")) 
        os.system('cls')
        if selectInMainMenu == 1:
            EnterAccountNum()            
        elif selectInMainMenu == 2:
             loginToAccount = int(input("\n\n\tEnter existing account number> "))
             if loginToAccount in BankAccounts:              
                LoginMenu(loginToAccount)
             else:
                print("\n\tAccount does not exist!")
        elif selectInMainMenu == 3:
            byeBye()
            break                            
    except:
        errorMessage()
       



