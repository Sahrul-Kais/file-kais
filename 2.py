import re

def usernameCheck(username):
    if(re.match("^(?=.*?[(@)]).[(a-z)]{2,12}$",username)):
        return True
    else:
        return False

def passwordCheck(password):
    if(re.match("^[(0-9)]{6}$",password)):
        return True 
    else:
        return False

print(usernameCheck("@sahru"))
print(passwordCheck("212223"))