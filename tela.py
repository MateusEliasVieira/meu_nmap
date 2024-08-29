# tela.py
from VerificadorIP import VerificadorIP
from VerificadorPortas import VerificadorPortas

entrada = -1

def menu():
    print('======================= MENU =======================')
    print('1 - Verificar todos ips ativos na rede')
    print('2 - Verificar se um ip está ativo')
    print('3 - Verificar intervalo de portas em um dispositivo')
    print('4 - Verificar lista de portas em um dispositivo')
    print('5 - Verificar todas as portas em um dispositivo')
    print('6 - Verificar portas famosas em um dispositivo')
    print('0 - Sair')
    entrada = int(input('Opção: '))
    return entrada

def opcao_1():
    rede = input('Rede: ')
    ip_inicial = int(input('IP inicial: '))
    ip_final = int(input('IP final: '))
    varredura = VerificadorIP()
    ips_ativos = varredura.iniciar_varredura_na_rede(rede, ip_inicial, ip_final)
    for ip in ips_ativos:
        print(f'{ip} ativo.')

def opcao_2():
    ip = input('IP: ')
    varredura = VerificadorIP()
    ips_ativo = varredura.iniciar_varredura_no_dispositivo(ip)
    if ips_ativo:
        print(f'{ip} ativo.')

def opcao_3():
    ip = input('IP: ')
    porta_inicial = int(input('Porta inicial: '))
    porta_final = int(input('Porta final: '))
    print(f"\nVarredura de portas iniciada para o dispositivo com IP {ip}...")
    varredura = VerificadorPortas()
    portas_abertas = varredura.iniciar_varredura_intervalo_portas(ip, porta_inicial, porta_final)
    if len(portas_abertas) == 0:
        print('Nenhuma porta aberta encontrada para o intervalo de portas especificado.')
    else:
        for porta in portas_abertas:
            print(f'O IP {ip} está com a porta {porta} aberta.')

def opcao_4():
    ip = input('IP: ')
    portas = input('Portas: ').split(",")
    print(f"\nVarredura de portas iniciada para o dispositivo com IP {ip}...")
    varredura = VerificadorPortas()
    portas_abertas = varredura.iniciar_varredura_lista_portas(ip, portas)
    if len(portas_abertas) == 0:
        print('Nenhuma porta aberta encontrada para a lista de portas especificado.')
    else:
        for porta in portas_abertas:
            print(f'O IP {ip} está com a porta {porta} aberta.')

def opcao_5():
    ip = input('IP: ')
    print(f"\nVarredura de portas iniciada para o dispositivo com IP {ip}...")
    varredura = VerificadorPortas()
    portas_abertas = varredura.iniciar_varredura_todas_portas(ip)
    if len(portas_abertas) == 0:
        print('Nenhuma porta aberta encontrada.')
    else:
        for porta in portas_abertas:
            print(f'O IP {ip} está com a porta {porta} aberta.')

def opcao_6():
    ip = input('IP: ')
    print(f"\nVarredura de portas famosas iniciada para o dispositivo com IP {ip}...")
    varredura = VerificadorPortas()
    portas_abertas_famosas = varredura.iniciar_varredura_portas_famosas(ip)
    if len(portas_abertas_famosas) == 0:
        print('Nenhuma porta famosa aberta encontrada.')
    else:
        for porta in portas_abertas_famosas:
            print(f'O IP {ip} está com a porta {porta[0]} ({porta[1]}) aberta.')

while entrada != 0:
    opcao = menu()
    if opcao == 1:
        opcao_1()
    elif opcao == 2:
        opcao_2()
    elif opcao == 3:
        opcao_3()
    elif opcao == 4:
        opcao_4()
    elif opcao == 5:
        opcao_5()
    elif opcao == 6:
        opcao_6()

