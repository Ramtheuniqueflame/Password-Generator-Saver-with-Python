import pickle


m_password = input(" Enter Master Password: ")


if m_password == "Master":
    account_name = input("Enter Account name: ")
    with open("pass-storage.p", "br") as readfile: 
        info = pickle.load(readfile)

    if account_name in info: 
        
        print(" Your password is: ", info[account_name])
    else:
        print('No account exists!!!')

else:
    print(" Master Password is wrong!")

