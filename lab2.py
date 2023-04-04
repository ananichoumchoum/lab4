#lab2.py
#Anne Smith
#ITSC203
#from the program testlogin.out crack password
 

import pexpect
import re
import random
import string

child = pexpect.spawn('./testlogin.out')
child.expect(': ')
child.sendline('Ok ')
child.expect(': ')
child.expect(': ')
child.expect(': ')
child.sendline('Ok ')
print(f'BEFORE: {child.before}\nAFTER: {child.after}\nBUFFER: {child.buffer}')
child.expect(': ')
crazystr = child.before[211:-11]
print(crazystr)
results = re.findall('[\w{3}@ :]+', crazystr.decode())
print(results)
name = results[2:-1:3] 
name.append(results[-1])
print(name)
email = re.findall ('[\w :]+', str(name))
print(email)
almostthere = email[0:-1:3] 
print(almostthere)
username = []
for names in almostthere:
    hello = names.rsplit(' ', 1)
    username.append( hello[-1])
    print(username)
N = 8
repeat = 9999
result = []
timer = 0
for x in range(repeat):
    if timer <= 4:
        child.expect(': ')
        var = child.before.decode()
        words = var.split()
        term = "choice"   
        if term in str(words):
            print("\n\n\nYou found a match\n\n\n")
            result.append(username[timer])
            result.append(password)
            print(result)
            child.sendline('c')
            timer += 1
            print("new username: ",username[timer],"timer is now at:", x, " at index[",timer,"]")
            child.expect(': ')
            
        child.sendline(username[timer])
        child.expect(': ')  
        password = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=N))  
        child.sendline(password) 
        child.expect(': ')
        child.expect(': ') 
    elif timer >= 5:
        timer = 0
        print("second loop in")
print(result)
