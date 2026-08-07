import random
import string

pass_len = 8
charVal = string.ascii_letters + string.digits + string.punctuation

# password = ""
# for i in range(pass_len):
#     password += random.choice(charVal)

# print("your random password is : " , password)

#list comprehension method:
password = "".join([random.choice(charVal)for i in range(pass_len)])
print(password)