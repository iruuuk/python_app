cards = [['Астахов', 'Игорь', 'Александрович', 35, 'Муж', True, 'Москва', 'маркетолог'],
         ['Вавилова', 'Елена', 'Сергеевна', 40, True, True, 'Таганрог', 'бухгалтер'], 
         ['Карелин', 'Андрей', 'Васильевич', 25, 'Муж', False, 'Подольск', 'специалист'], 
         ['Воронова', 'Мария', 'Игоревна', 30, True, False, 'Москва', 'менеджер'], 
         ['Остроумовна', 'Карина', 'Владимировна', 44, True, True, 'Подольск', 'маркетолог'], 
         ['Борзов', 'Владимир', 'Андреевич', 40, 'Муж', False, 'Москва', 'начальник отдела']]
spec = ['маркетолог', 'бухгалтер', 'менеджер', 'специалист']
mid_manag = ['начальник отдела', 'главный бухгалтер']
top_manag = ['директор']
salary = [40000, 60000, 80000]
def adding_salary(cards, spec, mid_manag, top_manag, salary):
    for card in cards:
        if card[-1] in spec:
            card.append(float(salary[0]))
        elif card[-1] in mid_manag:
            card.append(float(salary[1]))
        elif card[-1] in top_manag:
            card.append(float(salary[2]))
    return cards
adding_salary(cards, spec, mid_manag, top_manag, salary)
print(adding_salary(cards, spec, mid_manag, top_manag, salary))

adding_sum = 5000
def dobavlenie(cards, adding_sum):
    for card in cards:
        if card[5] == True:
            card[-1] += adding_sum
    return cards
print(dobavlenie(cards, adding_sum))

procent = int(input('Введите процент отчислений: '))
def otchisleniya(cards, procent):
    for card in cards:
        card.append(card[-1]-(card[-1]*procent/100))
    return cards
print(otchisleniya(cards, procent))


def vyvod():
    for card in cards:
        print('ФИО сотрудника: ' + str(card[0:3]))
        print('Должность: ' + str(card[7]))
        print('Заработная плата за вычетом налоговых отчислений: ' + str(card[-1]))
    return card
vyvod()
