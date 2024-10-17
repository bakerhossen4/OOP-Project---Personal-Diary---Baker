from user import User
from diary import Diary
from datetime import datetime

tit_init = 0
con_init = 45

while True :
    print("--------------------------------------------")
    print("--- Welcome to Personal Diary System -------")
    print(" *********** 1. First add your name : *****")
    print("------------ 2. Add content to diary ------")
    print("------------ 3. View all contents ---------")
    print("------------ 4. Delete a content of list --")
    print( "----------- 5. Exit ----------------------")
    print("--------------------------------------------")
    test = int(input("Enter Input : "))
    if test == 1  :
        data = input("Enter your name : ")
        userob = User( data )
    elif test == 2 :
        title = tit_init
        tit_init = tit_init + 1
        content = con_init
        con_init = con_init + 1
        date = datetime.now()
        doj = Diary( title, content, date )
        userob.add_entry(doj)
    elif test == 3 :
        userob.show_entries()
    elif test == 4 :
        en = int(input("Enter Name : "))
        userob.delete_entry(en)