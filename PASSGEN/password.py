import random
upper_char=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
num=str(list(range(0,100)))
special_char=['@','#','!','$','%','^','&','*','(',')']
password= random.choice(upper_char)+random.choice(lower_char)+random.choice(num)+random.choice(special_char)+ random.choice(upper_char)+random.choice(lower_char)+random.choice(num)+random.choice(special_char)
print("YOUR PASSWORD IS: ",password)