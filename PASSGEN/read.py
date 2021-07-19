import random
special_char=['@','#','!','$','%','^','&','*','(',')']
word_list=[]
with open ("words.txt",'r',encoding="cp437", errors='ignore') as file:
    data=file.readlines()
    # print(data)
    for line in data:
        words=line.split()
        # print(words)
        for item in words:
            if len(item)>5:
                word_list.append(item.capitalize())
word= random.choice(word_list)
spec=random.choice(special_char)
num=str(random.randint(10,99))
password=word+spec+num
print("Your readable password is {} ".format(password))