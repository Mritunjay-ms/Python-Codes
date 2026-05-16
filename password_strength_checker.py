import re
def password_checker():
    password=input('enter a password:')
    check="password strength is too weak"
    if(len(password)==0):
        print('Please Enter a Password!.....')
        return
    def checker1():
        nonlocal check
        if(re.search(r'[A-Z]',password) and re.search(r'[a-z]',password)):
            check="password strength is weak"
            return True
        return False
    def checker2():
        nonlocal check
        digit=re.compile(r'\d')
        matches=digit.findall(password)
        if(len(matches)!=0 and weak):
            check="password strength is moderate"
            return True
        return False
    def checker3():
        nonlocal check
        special=re.compile(r'[^A-Za-z0-9]')
        matches=special.findall(password)
        if(len(matches)!=0 and weak and moderate):
            check="password strength is strong"
            return True
        return False
    weak=checker1()
    moderate=checker2()
    strong=checker3()
    checker1()
    checker2()
    checker3()
    return check
print(password_checker())