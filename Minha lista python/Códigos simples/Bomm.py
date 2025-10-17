from time import sleep
print('==' * 20)
print('\033[1mPrepareçe para a contagem regressiva\033[m')
print('==' * 20)
sleep(1)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('BOMMM')
print()
input('Pressione <enter> para continuar')
