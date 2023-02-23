#Program that determines who's paying the bill.
import random
import sys

print("\t\t\t\t\tWelcome to Mukenya's App!!!\n"
      "\tThis will determine who's going to pay the bill. Choose 1/2.\n"
      "\t\t1. Yes\n"
      "\t\t2. No")
agree = int(input("Are you ready? "))
if agree == 1:
    print("Great let's start.....")
    names = input("Enter the names respectively(separate with a comma): ")
    folks = names.split(",")
    print(folks)
    #randomly generate the name of who's going to pay
    #since we don't know how many people are there we are going to fetch for the length of folks
    many = len(folks)
    pay = random.randint(0,many-1) #-1 is there because randint counts the index starting from 0.The many part will be empty thus substracting 1

    print(f"{folks[pay]} is going to pay for all of us. Thanks in advance")
    print("Hope you liked it. Come one come all.")

else:
    print("Okay. Bye bye!!")
    sys.exit()


