from yn_check import yn_check
from input_return import input_return
from read_file import read_file
import os
import datetime

os.chdir(os.path.dirname(os.path.abspath(__file__)))
File_origin = "data/user/"


print("=======================================\n"
      "==            STARTING               ==\n"
      "==      User Management System       ==\n"
      "=======================================\n"
    )


while True:

    ##ここから help 機能
    command = input("Input Command : ")
    if command == "help":
        print("[HELP] \n"
            "new  ->  Make a New User File. \n"
            "add  ->  Add Notes to the already Existing User. \n"
            "end  ->  Exit the System. \n"
            )

    ##ここから add 機能
    elif command == "add":
        Add_Note_Check = 0


        def Add_Note_Check_Func():
            global Add_Note_Check
            
            if Add_Note_Check == "y" or Add_Note_Check == "Y":
                date_now = datetime.datetime.now()
                f.write(
                    "\n---------------------------------------------------\n" +
                    "Add Time     : " + str(date_now) + "\n\n" +
                    "Add Notes    : " + str(User_Note) + "\n" +
                    "---------------------------------------------------\n"
                    )

                print(
                    "Note Added to [ " + User_Name + " ]" +
                    "\n---------------------------------------------------\n" +
                    "Add Time     : " + str(date_now) + "\n\n" +
                    "Add Notes    : " + str(User_Note) + "\n" +
                    "---------------------------------------------------\n"
                    )
            elif Add_Note_Check == "n" or Add_Note_Check == "N":
                print("Note Abandoned. Try Again.")
                
            else:
                print("Unexpected ERROR Occured. Try Again. (Y/N)")
                Add_Note_Check = input()
                Add_Note_Check_Func()



        def Continue_Check():
            print("Do You Want to Add Another Notes?\n")
            Continue_Flag = input("(Y/N)")
            global Main_continue_flag
            if Continue_Flag == "y" or Continue_Flag == "Y":
                Main_continue_flag = 1
            elif Continue_Flag == "n" or Continue_Flag == "N":
                Main_continue_flag = 0
            else:
                print("Invalid Input. Try Again")
                Continue_Check()




        while True:
            Main_continue_flag = 0
            User_Name = input("Serch Name : ")
            File_path = File_origin + User_Name + ".txt"
            if not os.path.isfile(File_path):
                print("File Not Found. Try Again.")
                Main_continue_flag = 1
            elif os.path.isfile(File_path):
                with open(File_path, mode="a") as f:
                    print("File Found.")
                    print("Write Down New Note.")
                    User_Note = input("Add Note : ")
                    print("Are You Willing To Add This Note to [ " + User_Name + " ] ?")
                    Add_Note_Check = input("(Y/N)")
                    Add_Note_Check_Func()

            Continue_Check()
            
            if Main_continue_flag == 1:
                continue
            elif Main_continue_flag == 0:
                break
            else:
                print("Unknown ERROR OCCURED.")
                break
            
        print("----------------------------------------\n"
              "---------- Add New Note Function -------\n"
              "----------------- END ------------------\n"
             )

        ##ここまで add 機能

    elif command == "new":
        def All_Reset():
            global User_Name
            global User_Age
            global User_Address
            global User_Note
            global MF_continue_flag
            User_Name = ""
            User_Age = ""
            User_Address = ""
            User_Note = ""
            MF_continue_flag = 0

            print("-----------------------------------------")
            print("------------Start Adding User------------")
            print("-----------------------------------------")


        def input_Name():
            global User_Name
            User_Name = input("User Name : ")
            while User_Name == "":
                print("User name is empty. Try Again.")
                User_Name = input("User Name : ")    

        def input_Age():
            global User_Age
            User_Age = input("User Age : ")
            while User_Age == "":
                print("User Age is empty. Try Again.")
                User_Age = input("User Age : ")


        def input_Address():
            global User_Address
            User_Address = input("User Address : ")
            while User_Address == "":
                print("User Address is empty. Try Again.")
                User_Address = input("User Address : ")


        def input_Note():
            global User_Note
            User_Note = input("Note : ")
            if User_Note == "" :
                print("Note is Empty. Are You OK?(Y/N)\n")
                Note_YN = input()
                
                if Note_YN == "n" or Note_YN == "N":
                    input_Note()
                elif Note_YN == "y" or Note_YN == "Y":
                    pass
                else:
                    print("ERROR : Invalid Input. Try Again.\n")
                    input_Note()


        def RE_input():
            input_Name()
            input_Age()
            input_Address()
            input_Note()


        def Make_file():
            global Make_User_Data
            Make_User_Data = input("Are you sure to make this File?(Y/N)\n")
            if Make_User_Data == "n" or Make_User_Data == "N":
                global MF_continue_flag
                MF_continue_flag = 1
            elif Make_User_Data == "y" or Make_User_Data == "Y":
                pass
            else:
                print("ERROR : Invalid Input. Try Again.\n")
                Make_file()


        def Final_check():
            global Final_Ans
            Final_check_input = input()
            if Final_check_input == "y" or Final_check_input == "y":
                Final_Ans = "Yes"
            elif Final_check_input == "n" or Final_check_input == "N":
                Final_Ans = "No"
            else:
                print("ERROR : Invalid Input. Try Again.(Y/N)\n")
                Final_check()

        """
        --------------ここまで機能関数------------
        """

            
        while True:
            All_Reset()
            RE_input()
            print(os.getcwd())

            print("----------------------------------------")
            print("User Name    : "+str(User_Name))
            print("User Age     : "+str(User_Age))
            print("User Address : "+str(User_Address))
            print("User Notes   : "+str(User_Note))
            print("----------------------------------------")

            Make_file()

            global MF_continue_flag 
            if MF_continue_flag == 1: 
                continue

                
            File_path = File_origin + User_Name + ".txt"
                
            try:
                with open(File_path, mode = "x") as f:
                    date_now = datetime.datetime.now()
                    f.write(
                        "\n---------------------------------------------------\n" +
                        "Made Time    : " + str(date_now) + "\n\n" +
                        "User name    : " + str(User_Name) + "\n" +
                        "User Age     : " + str(User_Age) + "\n" +
                        "User Address : " + str(User_Address) + "\n" +
                        "User Notes   : " + str(User_Note) + "\n" +
                        "---------------------------------------------------\n"
                        )
                    
            except FileExistsError:
                with open(File_path, mode="a") as f:
                    date_now = datetime.datetime.now()
                    f.write(
                        "\n---------------------------------------------------\n" +
                        "Add Time     : " + str(date_now) + "\n\n" +
                        "User name    : " + str(User_Name) + "\n" +
                        "User Age     : " + str(User_Age) + "\n" +
                        "User Address : " + str(User_Address) + "\n" +
                        "User Notes   : " + str(User_Note) + "\n" +
                        "---------------------------------------------------\n"
                        )

            print("Finished Making User Successfuly.")
            print("Do You Want To Add Another User?(Y/N)")

            global Final_Ans
            Final_check()


            if Final_Ans == "Yes":
                continue
            elif Final_Ans == "No":
                break
            else:
                print("ERROR : UNEXPECTED ERROR OCCURED!!")
                break

        print("----------------------------------------\n"
              "--------- Make New User Function -------\n"
              "----------------- END ------------------\n"
             )

        ##ここまで new 機能
    elif command == "read":
        read_user = input("Input User Name : ")
        file_name = File_origin + read_user + ".txt"
        read_file(file_name)

        print("-----------------------------------------\n"
              "--------- Read User Data Function -------\n"
              "------------------ END ------------------\n"
            )



    elif command == "end":
        Cont_Flag = ""
        print("Do you want to exit?")
        while Cont_Flag == "ERROR" or Cont_Flag == "":
            get_input = input("Y/N : ")
            Cont_Flag = yn_check(get_input)

        if Cont_Flag == "yes":
            break

        elif Cont_Flag == "no":
            Cont_Flag = "ERROR"
            continue

    else:
        print("Invalid Input. Try Again.")
        continue


        



