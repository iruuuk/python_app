user = ['Dmitriy', 'Angelina', 'Ekaterina', 'Vasiliy']
arm = [1, 2, 3, 4]
password = ['3nfhr44n', 'hcgd65g', '456hfhhfh', '345bvhfh']

free_arm = []

def delete_user(name, user_list, arm_list, password_list):
    for i in range(len(user_list)):
        if user_list[i] == name:
            del user_list[i]
            del password_list[i]
            arm_del = arm_list.pop(i)
            free_arm.append(arm_del)
            break
        
def add_user(username, user_password):
    user.append(username)
    password.append(user_password)
    max_ = sorted(arm)[-1]
    if not free_arm:
        arm.append(max_+1)
    else:
        arm.append(free_arm.pop(0))
        
def login(name, arm_num):
    for i in range(len(user)):
        if user[i] == name:
            if arm[i] == arm_num:
                return('Добро пожаловать')
            else:
                return('Логин или пароль неверны')
    return('Такого пользователя нет')
 
def login_3_tries():
    try_num = 0
    while try_num < 3:
        login_result = login(input('Введите имя: '), int(input('Введите номер АРМ: ')))
        if login_result != 'Добро пожаловать' and try_num < 2:
            print(login_result)
            print('У вас осталось ', 2-try_num, 'попытки')
            try_num += 1
        elif login_result != 'Добро пожаловать' and try_num == 2:
            print(login_result)
            print('Учетная запись заблокирована')
            try_num += 1
        else:
            if login_result == 'Добро пожаловать':
                print(login_result)
                try_num = 3
login_3_tries()
           
            
delete_user('Ekaterina', user, arm, password)
add_user('Saveliy', '4937394kfs')
add_user('Vitaliy', '374934hfd')
print(login('Dmitriy', 1))
login('Vitaliy', 2)
#print(login(input('Введите имя: '), int(input('Введите номер АРМ: '))))


        

print(user)
print(arm)
print(password)
print(free_arm)
