nome = input("Qual seu nome? ")
idade = input("Qual sua idade? ")
idade = int(idade)

idade_minima = 18
idade_maxima = 40

if idade >= idade_minima and idade <= idade_maxima:
    print(nome,"você pode fazer o seu empréstimo!")
else:
    print("Sentimos muito,",nome,". Mas você não pode fazer empréstimo.")