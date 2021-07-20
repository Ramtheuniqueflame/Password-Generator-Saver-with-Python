import string
import random
import pickle
from types import ClassMethodDescriptorType 

info = {}

try:  #try and except is the method of error handling. If 'try' fails then 'except' executes.
    with open("pass-storage.p", "br") as readfile: #br_binary read
        info = pickle.load(readfile)
except:
    print('No data in pass storage file!')


s1 = string.ascii_uppercase 
s2 = string.ascii_lowercase
s3 = string.digits
s4 = string.punctuation
            
password_length = int(input(" Enter the length of Password:   "))

s = []

s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))

Password = "".join(random.sample(s, password_length))
print(Password)



answer = input("Would you like to consider this password ? ")
if 'yes' in answer:
    Account_name = input("Enter account name for which you would like to save this password: ")
    info[Account_name] = Password 
    with open('pass-storage.p' , "bw") as file: #bw_binaray write 
        pickle.dump(info, file, protocol=2)
        print("Your Password is Saved! ")
        print("If you want to extract this any old saved password, please  run get-pass.py file. Thank you! ")

else:
    print("Not an issue ")
