import random 
import string


def numpwd():
    numpwd = random.randint(1,10000000000000000000)
    print("Password:", numpwd)

def wordpwd():
    length = int(input('Enter the length of password: '))
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    all = lower + upper
    temp = random.sample(all,length)
    password = "".join(temp)
    print("Password:", password)

def mixed():
    length = int(input('Enter the length of password: '))
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    temp = random.sample(all,length)
    password = "".join(temp)
    print("Password:", password)

def special():
    length = int(input('Enter the length of password: '))
    symbols = string.punctuation
    all = symbols
    temp = random.sample(all,length)
    password = "".join(temp)
    print("Password:", password)
    
    
def china():
    length = int(input('Enter the length of password: '))
    china = ('手', '田', '水', '口', '廿', '卜', '山', '戈', '人', '心', '日', '尸', '木', '火', '土', '竹', '十', '大', '中', '難', '金', '女', '月', '弓', '一')
    print(random.sample(china, length))

print("__________                                               .___   ________                                   __                          __   ________   ")
print("\______   \_____    ______ ________  _  _____________  __| _/  /  _____/  ____   ____   ________________ _/  |_  ___________    _____ |  | _\_____  \  ")
print(" |     ___/\__  \  /  ___//  ___/\ \/ \/ /  _ \_  __ \/ __ |  /   \  ____/ __ \ /    \_/ __ \_  __ \__  \\   __\/  _ \_  __ \  /     \|  |/ //  ____/  ")
print(" |    |     / __ \_\___ \ \___ \  \     (  <_> )  | \/ /_/ |  \    \_\  \  ___/|   |  \  ___/|  | \// __ \|  | (  <_> )  | \/ |  Y Y  \    </       \  ")
print(" |____|    (____  /____  >____  >  \/\_/ \____/|__|  \____ |   \______  /\___  >___|  /\___  >__|  (____  /__|  \____/|__|    |__|_|  /__|_ \_______ \ ")
print("                \/     \/     \/                          \/          \/     \/     \/     \/           \/                          \/     \/       \/ ")

while True:
    choice = int(input("\n [1] Numbers only \n [2] Words only \n [3] Mixed \n [4] Special Characters \n [5] Bing Chilling \n [Exit] Ctrl-C \n Enter: "))
    if choice == 1:
        numpwd()
    elif choice == 2:
        wordpwd()
    elif choice == 3:
        mixed()
    elif choice == 4:
        special()
    elif choice == 5:
        china()
    else:
        print("Error try again")
