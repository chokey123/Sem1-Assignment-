#Wong Yi Xing
#TP068170

import os

filename1 = 'med.txt'
filename2 = 'customer.txt'
filename3 = 'order.txt'

#save data function
def save_med(l):
    #if already had the file, continue write the file.
    try:
        med_txt = open(filename1,"a")
    #if don't, create the file and write it.
    except:
        med_txt = open(filename1,"w")
    #write the message into the file.
    for item in l:
        med_txt.write(str(item)+'\n')
    med_txt.close()

def save_customer(l):
    # if already had the file, continue write the file.
    try:
        customer_txt = open(filename2,"a")
    # if don't, create the file.
    except:
        customer_txt = open(filename2,"w")
    # write the message into the file.
    for item in l:
        customer_txt.write(str(item)+'\n')
    customer_txt.close()

def save_order(l):
    # if already had the file, continue write the file.
    try:
        order_txt = open(filename3,"a")
    # if don't, create the file.
    except:
        order_txt = open(filename3,"w")
    # write the message into the file.
    for item in l:
        order_txt.write(str(item)+'\n')
    order_txt.close()



#function everyone can use

#view medicine list
def view():
        #if file exits then open it
        if os.path.exists(filename1):
            with open(filename1,'r') as file: #read files
                medicine = file.readlines()
                for l in medicine:
                    lst0 = l.replace("]", "").replace("[","").replace("'","") #remove extra elements in the str
                    lst = lst0.split(",") #make it become a list
                    print(
                        "no."+ lst[0],"\n"
                        "name: " + lst[1], "\n"
                        "expired date: " + lst[2], "\n"
                        "price: " + lst[3], "\n"
                        "specification: " + lst[4])
        else:
            print("don't have any uploaded medicine.")

        view_exit = input("enter any key whenever you want to stop viewing.\n")
        if view_exit =="":
            pass
        else:
            pass



#admin function

#let admin login
def admin_login():
    while True: #make a loop for admin to input username and password
        admin_username=input("please enter your username: ")
        admin_password=input("please enter your password: ")
        if admin_username and admin_password == "admin": #directly assign username and password for admin
            print("you have successfully logged in.")
            admin()
            break #stop the loop if successfully logged in
        else:
            admin_login_exit=input("Wrong Password.\n"
                                   "Enter y to continue login\n"
                                   "Enter ay key else to exit.")
            try:
                #continue loop if user wants to try again.
                if admin_login_exit == "y":
                    continue
                else:
                    break
            except:
                #let user input again if any error occurs
                print("ERROR!!")
                continue

#upload medicine
def upload():
    while True:
        try:
            med_lis = [] #create variable as list
            med_no = input("please input the medicine no.: ")
            name = input("please input the medicine name: ")
            exp_date = input("please input the expired date: ")
            specification = input("please input the specification: ")
            price = int(input("please input the price(RM) (type in number): "))
            med = [med_no, name, exp_date, price, specification] #insert those input variable into the list
            med_lis.append(med) #insert med into med_lis
            save_med(med_lis) #save it as txt files
            print("upload completed.")
        except ValueError:
            print("please input the price in number")
            continue
        #ask user if he wants to continue uploading
        upload_exit = input("do you wish to continue? \n"
                                "enter y to continue.\n"
                                "enter any key else to exit.\n")

        if upload_exit == "y":
            continue
        else:
            break

#modify medicine
def modify():
    #let users view medicine before modifying
    print("please view the medicine list first. \n")
    view()
    while True:
        #read the file if the file exists
        if os.path.exists(filename1):
            with open(filename1, 'r') as file:
                medicine_old = file.readlines()
        else:
            print("don't have any uploaded medicine.")
            break
        med_name = input("please enter the name of medicine you want to modify: ")
        with open(filename1, 'w') as wfile:
            lst = []
            found = False #mark a variable as False
            for l in medicine_old:
                lst = l.replace("]", "").replace("[","").replace("'","") #remove extra elements in str
                lst = lst.split(",") #make it become a list
                if lst[1].strip() == med_name:
                    lst[0] = input("med no: ")
                    lst[1] = input("medicine name: ")
                    lst[2] = input("expired date: ")
                    lst[3] = input("price(RM): ")
                    lst[4] = input("specification: ")
                    wfile.write(str(lst))
                    found = True #mark found as True if found medicine to modify
                else:
                    wfile.write(l) #write same thing back if isn't the medicine to modify
            if found: #if found is True
                pass
            else: #if found is False
                print("can't find the medicine")
        modify_exit = input("enter y to continue modify.\n"
                        "enter any key else to exit.\n")
        if modify_exit == 'y':
            continue
        else:
            break

#delete medicine
def delete():
    print("please view the medicine list.")
    view()
    while True:
        med_name = input("please enter the name of medicine you want to delete: ")
        #print(med_name1)
        if os.path.exists(filename1):
            with open(filename1,'r') as file: #read files if files exists
                medicine_old=file.readlines()
        else:
            medicine_old = []
        ifdel=False
        if medicine_old: #if medicine_old exists
            with open(filename1,'w') as wfile: #write file
                lst = []
                for l in medicine_old:
                    lst = l.replace("]", "").replace("[","").replace("'","")
                    lst = lst.split(",")
                    #write everything again except deleted medicine
                    if lst[1].strip() != med_name:
                        wfile.write(l)
                    else:
                        #if the medicine has found, let ifdel be True
                        ifdel = True
                if ifdel: #if ifdel is True
                    print("the medicine informaiton has been deleted")
                else: #if ifdel is false
                    print("didn't find the medicine")
        delete_exit = input("enter y if you wish to continue.\n"
                            "enter any key else to exit.\n")
        if delete_exit =="y":
            continue
        else:
            break

#search specific mediicne
def search_medicine():
    while True:
        if os.path.exists(filename1): #read the file if file exists
            med_name = str(input("please input the medicine name you want to search: "))

            with open(filename1,'r') as file:
                medicine = file.readlines()
                found = False #mark found variable as False
                for l in medicine:
                    lst0 = l.replace("]","").replace("[","").replace("'","") #remove extra elements in str
                    lst = lst0.split(",") # make it become a list
                    if med_name == lst[1].strip(): #display if found the medicine
                        print(
                          "no."+lst[0],"\n"
                          "name: "+lst[1],"\n"
                          "expired date: "+lst[2],"\n"
                          "specification: "+lst[3],"\n"
                          "price(RM): "+lst[4])
                        found =True #mark found as True if found the medicine
                    else:
                        pass
                if found: #if found is true
                    pass
                else: # if found is false
                    print("can't find the medicine.")
        search_medicine_exit = input("enter y if you want to continue. \n enter any key else if you want to exit.\n")
        if search_medicine_exit =="y":
            continue
        else:
            break

#search specific customer's order
def search_order():
    while True:
        name = input("please enter the name of customer you want to search: ")
        if os.path.exists(filename3):
            with open(filename3, 'r') as file: #read the files if exists
                medicine = file.readlines()
                success = False
                for l in medicine:
                    lst0 = l.replace("]", "").replace("[","").replace("'","")
                    lst = lst0.split(",")
                    if name == lst[0].strip():
                        print("\n"
                        "customer name: " + lst[0],"\n"
                        "medicine name: " + lst[1], "\n"
                        "amount of medicine: " + lst[2], "\n"
                        "amount paid(RM): " + lst[3], "\n"
                        )
                        success = True
                    else:
                        pass
                if success: #if the success is True
                    pass
                else: #if sucess is false
                    print("didn't find the order.")
        search_order_exit = input("press y if you wish to continue.\n Press any key else if you want to exit.\n")
        if search_order_exit == 'y':
            continue
        else:
            break

#view all of the order
def view_order():
    if os.path.exists(filename3):
        with open(filename3, 'r') as file: #read files if exists
            order = file.readlines()
            for l in order:
                lst0 = l.replace("]","").replace("[","").replace("'","")
                lst = lst0.split(",")
                print(
                        "customer name: " + lst[0], "\n"
                        "medicine name: " + lst[1], "\n"
                        "amount of medicine: " + lst[2], "\n"
                        "amount paid(RM): " + lst[3], "\n"
                        "Payment Method: " + lst[4], "\n"
                       )
    else:
        print("don't have any order currently.")
    view_exit = input("enter any key whenever you want to stop viewing.\n")
    if view_exit =="":
        pass
    else:
        pass




#registered customer function

#place order and payment
def order(name):
    while True:
        med_lis = []
        order_lis = []
        print("please view the available medicine.")
        view()
        med_choice = int(input("please enter the medicine no. you wish to purchase: "))
        success = False
        if os.path.exists(filename1):
            with open(filename1,'r') as file:
                med_lis=file.readlines()
                for l in med_lis:
                    lst = l.replace("]", "").replace("[","").replace("'","")
                    lst = lst.split(",")
                    if int(lst[0].strip()) != med_choice:
                        pass
                    else:
                        try:
                            payment = ""
                            amount = int(input("how many do you want to buy?"))
                            pay_method = int(input("which payment method? \n 1.Credit card\n 2.Touch N Go Ewallet.\n please input number(1/2): "))
                            if pay_method == 1:
                                payment = "Credit Card"
                                pin_code = input("please input your Card pin code.")
                            elif pay_method == 2:
                                payment = "Touch N Go Ewallet"
                                pin_code = input("please input your Touch N Go Ewallet pin code.")
                            else:
                                print("please input 1 or 2 only.")
                            order = [name, lst[1], amount, (int(lst[3])*amount),payment]
                            order_lis.append(order)
                            save_order(order_lis)
                            print("payment successful")
                            print("saved your order.")
                            success = True
                        except ValueError:
                            print("please input amount and payment method in numbers.")
                            continue
                if success:
                    pass
                else:
                    print("can't find the medicine. PLease try again.")
                    continue
        order_exit = input("enter y if you want to continue order.\n"
                           "enter any key else if you want to exit.\n")
        if order_exit == 'y':
            continue
        else:
            break

#let customer view all his order
def view_own_order(name):
    while True:
        if os.path.exists(filename3):
            with open(filename3, 'r') as file:
                order = file.readlines()
                found = False
                for l in order:
                    lst = l.replace("[", "").replace("]","").replace("'","")
                    lst = lst.split(",")
                    if name == lst[0].strip():
                        found = True
                        print("\n"
                        "customer name: " + lst[0], "\n"
                        "medicine name: " + lst[1], "\n"
                        "amount of medicine: " + lst[2], "\n"
                        "amount paid(RM): " +lst[3], "\n"
                        "Payment Method: " +lst[4], "\n"
                    )
                    else:
                        pass
                if found:
                    pass
                else:
                    print("you haven't order anything yet.\n")
        view_own_order_exit = input("enter any key if you want to exit.\n")
        if view_own_order_exit == "":
            break
        else:
            break

#let customer view his perfonal informaiton
def view_personal_info(name):
    while True:
        if os.path.exists(filename2):
            with open(filename2,'r') as file:
                customer = file.readlines()
                found = False
                for l in customer:
                    lst0 = l.replace("[","").replace("]","").replace("'","")
                    lst = lst0.split(",")
                    if name == lst[0].strip():
                        print("\n----------------------------------\n")
                        print("username: "+lst[0])
                        print("home address: "+lst[1])
                        print("email id: "+lst[2])
                        print("phone number: "+lst[3])
                        print("gender: "+lst[4])
                        print("birthday: "+lst[5])
                        print("\n----------------------------------\n")
                        found = True
                    else:
                        pass
                if found:
                    pass
                else:
                    print("can't find your information")
        view_personal_info_exit = input("enter any key whenever you want to exit.\n")
        if view_personal_info_exit == '':
            break
        else:
            break







#new customer function
def registration():
    customer_lst=[]
    while True:
            #input information
            username = input("please enter your username: ")
            address = input("please enter your home address: ")
            email_id = input("please enter your email id: ")
            contact_number = input("please enter your phone number: ")
            gender = input("please enter your gender.(male/female): ")
            birthday = input("please enter your birthday.")
            password = input("please enter your password: ")
            con_password = input("please confirm your password: ")
            if password != con_password:
                print("please confirm your password again.")
                continue
            else:
                break

    #store the value into customer_info
    customer_info = [username,address,email_id,contact_number,gender,birthday,password]
    customer_lst.append(customer_info) #append into customer_lst
    save_customer(customer_lst) #save the info
    print("registration complete. ")



#menu

#option for admin
def admin():
      print("-----------------------------------")
      while True:
          try:
                menu_admin = int(input("do you want to \n"
                             "1.upload medicine detail\n"
                             "2.view uploaded medicine\n"
                             "3.update/modify medicine information\n"
                             "4.delete medicine information\n"
                             "5.search medicine\n"
                             "6.view orders of customers\n"
                             "7.search order of specific customer\n"
                             "8.exit\n"
                             "------------------------\n"
                             "pls enter here: "))
                if menu_admin ==1:
                    upload()
                elif menu_admin ==2:
                    view()
                elif menu_admin==3:
                    modify()
                elif menu_admin==4:
                    delete()
                elif menu_admin ==5:
                    search_medicine()
                elif menu_admin ==6:
                    view_order()
                elif menu_admin ==7:
                    search_order()
                elif menu_admin ==8:
                    break
          except ValueError:
              print("ERROR!! please type in number.")
              continue

#option for new customer
def new_customer():
    while True:
        try:
            menu_new_customer = int(input("do you want to\n"
                                    "1.view medicine detail\n"
                                    "2.registration\n"
                                    "3.exit\n"
                                    "---------------------\n"
                                    "please enter here: "))
            if menu_new_customer == 1:
                view()
            elif menu_new_customer == 2:
                registration()
                break
            elif menu_new_customer ==3:
                break
        except ValueError:
            print("ERROR!!! please type in number.")
            continue

#option for registered customer
def registered_customer(l):
    print("\n\n***************************"
        "WELCOME!!",l,
          "*****************************\n")
    while True:
        try:
            menu_registered_customer = int(input("do you want to\n"
                                           "1.view medicine detail\n"
                                           "2.place order and payment\n"
                                           "3.view your own order\n"
                                           "4.view personal information\n"
                                           "5.exit\n"
                                           "--------------------\n"
                                           "please enter here (type in number): "))

            if menu_registered_customer == 1:
                view()
            elif menu_registered_customer ==2:
                order(customer_username)
            elif menu_registered_customer == 3:
                view_own_order(customer_username)
            elif menu_registered_customer == 4:
                view_personal_info(customer_username)
            elif menu_registered_customer ==5:
                break
            else:
                print("ERROR!!!")
                continue
        except ValueError:
            print("ERROR!! please retry (type in numbers)")


#main program
while True:
        print("-----------------------------")
        try:
            menu1 = int(input("Are you : \n"
      "\t1.Admin\n"
      "\t2.New Customer\n"
      "\t3.Registered Customer\n"
      "\t4.I wish to exit.\n"
      "------------------------------\n"
      "please enter here: "))
            print("------------------------------")

            if menu1 == 1:
                admin_login()
            elif menu1 ==2:
                new_customer()
            elif menu1 ==3:
                    while True:
                        if os.path.exists(filename2):
                            #input detalis
                            customer_username = str(input("please enter your username: "))
                            password = str(input("please enter your password: "))
                            success = False
                            with open(filename2, 'r') as file:
                                customer = file.readlines()
                                for l in customer:
                                    #remove extra element in l
                                    lst0 = l.replace("[", "").replace("]", "").replace("'", "")
                                    lst = lst0.split(",")
                                    # if the customer_username and password is matched
                                    if customer_username == lst[0] and password == lst[-1].strip():
                                        print("login successful.")
                                        registered_customer(customer_username)
                                        success = True
                                        break
                                    else:
                                        pass
                                if success:
                                    break
                                else:
                                    print("\nWrong username or password.\n")
                        #ask if user want to leave
                        login_exit = input(
                            "enter y to login again.\n"
                            "enter any other key to exit.\n")
                        if login_exit == 'y':
                            continue
                        else:
                            break

            elif menu1 ==4:
                break
        except ValueError:
            print("ERROR!!! please enter a number")




