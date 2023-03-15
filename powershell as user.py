from os import system
user = input("User: ")
system("runas /user:int\\" + user + " powershell")
