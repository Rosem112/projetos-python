from time import sleep

print('\033[2;31m=\033[m'*37)
print('\033[2;37mContagem regressiva para o ANO NOVO!\033[m')
print('\033[2;31m=\033[m'*37)

sleep(2)
for num in range(5, 0, -1):
    print('{: ^37}'.format(num))
    sleep(1)

print('\033[2;31m=\033[m'*37)
print('{: ^47}'.format(' \033[2;37mBUUM!  BUUM!  POOW!\033[m '))
print('{: ^47}'.format(' \033[2;33mFELIZ ANO NOVO!\033[m '))
print('\033[2;31m=\033[m'*37)
