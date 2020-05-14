"""
Задание 16. Банковские счета
Некоторый банк хочет внедрить систему управления счетами клиентов, поддерживающую следующие операции:
Пополнение счета клиента.
Снятие денег со счета.
Запрос остатка средств на счете.
Перевод денег между счетами клиентов.
Начисление процентов всем клиентам.
Вам необходимо реализовать такую систему. Клиенты банка идентифицируются именами (уникальная строка, не содержащая
пробелов). Первоначально у банка нет ни одного клиента. Как только для клиента проводится операция пополнения,
снятия или перевода денег, ему заводится счет с нулевым балансом. Все дальнейшие операции проводятся только с этим
счетом. Сумма на счету может быть как положительной, так и отрицательной, при этом всегда является целым числом. """


def deposit(arg):
    name, money = arg
    bank[name] = bank.setdefault(name, 0) + int(money)


def withdraw(arg):
    name, money = arg
    bank[name] = bank.setdefault(name, 0) - int(money)


def balance(arg):
    name = arg[0]
    if name in bank:
        print(bank[name])
    else:
        print('ERROR')


def transfer(arg):
    name_1, name_2, money = arg
    withdraw((name_1, money))
    deposit((name_2, money))


def income(arg):
    percent = int(arg[0])
    for name, balanse in bank.items():
        if balanse > 0:
            bank[name] = bank.get(name) + balanse * percent // 100


bank = {}
bank_fun = {
    'DEPOSIT': deposit, 'WITHDRAW': withdraw,
    'BALANCE': balance, 'TRANSFER': transfer,
    'INCOME': income
}
with open("input16.txt") as f:
    content = f.readlines()
for line in content:
    data = list(line.split())
    fun_name = data[0]
    arg = data[1:]
    bank_fun[fun_name](arg)
