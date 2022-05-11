import json
choose=input("enter you want login or signup (signup choose (1)login choose (2)):")
l=[]
d={}
if choose=="1":
    username=input("please enter your full name : ")
    pas1=input("please enter your password: ")
    upper=0
    lower=0
    digit=0
    special=0
    for i in pas1:
        if i>='a' and i<='z':
            upper+=1
        
        if i>='1' and i<='9':
            digit+=1
        
        if i>='A' and i<='Z':
            lower+=1
        
        if i=='@'or i=='$' or i=='_' or i=='#':
            special+=1 
    if upper>=1 and lower>=1 and digit>=1 and special>=1:
        print("your password is valid ")
        pas2=input("please confirm your password : ")
        if pas1==pas2:
            print("your password is succefully confirm")
            
            birth_date=input("enter Your Date Of Birth:")
            Gender=input("enter your Gender: ")
            hobbies=input("Enter Your hobby:")
            
            d["birth date"]=birth_date
            d["Gender"]=Gender
            d["Hobbies"]=hobbies
            d["Username"]=username
            d["Password"]=pas1
            
            
            myfile=open("userdetails.json","w")
            json.dump(d,myfile,indent=4)
            myfile.close()
            
        else:
            print("your password is not confirmed, sorry try again")        
    else:
        print("your password is not valid please try again")
elif choose=="2":
    user_name=input("enter your username:")
    login_pas=input("enter your Log in Password: ")
    with open("userdetails.json","r") as x:
        login_info=json.load(x)

        if login_info["Username"]==user_name and login_info["Password"]==login_pas:
            
            print("usrname = ",login_info["Username"])
            print("password = ",login_info["Password"])
               
            print("birth date = ",login_info["birth date"])
            print("Gender = ",login_info["Gender"])
            print("Hobbies = ",login_info["Hobbies"])
        else:
            print(" sorry! Password and username are Invalid please first login your profile information")
else:
    print("please choose only 1 or 2 ")
