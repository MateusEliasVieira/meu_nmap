# sixcore.py
import os
from colorama import init, Fore
from VerificadorIP import VerificadorIP
from VerificadorPortas import VerificadorPortas
from pyfiglet import Figlet

entrada = -1

# Inicializa colorama
init()


def exibir_banner():
    # Criar uma instância do Figlet
    figlet = Figlet(font='slant')  # Você pode mudar a fonte conforme desejado
    # Texto do banner
    texto = "SIXCORE"
    # Gerar e exibir o banner
    banner = figlet.renderText(texto)
    print(banner)

def main():
    exibir_banner()

if __name__ == "__main__":
    main()

def imprimir_com_cor(texto, cor):
    print(f"{cor}{texto}{Fore.RESET}")

def limpar_tela_windows():
    os.system('cls')

def menu():
    limpar_tela_windows()
    print('\n1 - Verificar todos ips ativos na rede')
    print('2 - Verificar se um ip está ativo')
    print('3 - Verificar intervalo de portas em um dispositivo')
    print('4 - Verificar lista de portas em um dispositivo')
    print('5 - Verificar todas as portas em um dispositivo')
    print('6 - Verificar portas famosas em um dispositivo')
    print('0 - Sair')
    entrada = int(input('>> '))
    if entrada > 6 or entrada < 0:
        imprimir_com_cor('Opção inválida!',Fore.RED)
    else:
        return entrada

def opcao_1():
    rede = input('Rede: ')
    if len(rede.split('.')) == 3:
        ip_inicial = int(input('IP inicial: '))
        ip_final = int(input('IP final: '))
        varredura = VerificadorIP()
        ips_ativos = varredura.iniciar_varredura_na_rede(rede, ip_inicial, ip_final)
        for ip in ips_ativos:
            imprimir_com_cor(f'{ip} ativo.',Fore.GREEN)
    else:
        imprimir_com_cor("Formato de IP inválido!",Fore.RED)

def opcao_2():
    ip = input('IP: ')
    if len(ip.split('.')) == 4:
        varredura = VerificadorIP()
        ips_ativo = varredura.iniciar_varredura_no_dispositivo(ip)
        if ips_ativo:
            imprimir_com_cor(f'{ip} ativo.',Fore.GREEN)
    else:
        imprimir_com_cor("Formato de IP inválido!",Fore.RED)

def opcao_3():
    ip = input('IP: ')
    if len(ip.split('.')) == 4:
        porta_inicial = int(input('Porta inicial: '))
        porta_final = int(input('Porta final: '))
        if porta_final > porta_inicial:
            print(f"\nVarredura de portas iniciada para o dispositivo com IP {ip}...")
            varredura = VerificadorPortas()
            portas_abertas = varredura.iniciar_varredura_intervalo_portas(ip, porta_inicial, porta_final)
            if len(portas_abertas) == 0:
                print('Nenhuma porta aberta encontrada para o intervalo de portas especificado.')
            else:
                imprimir_com_cor("============= Relatório =============", Fore.RED)
                for porta in portas_abertas:
                    imprimir_com_cor(f'{ip}:{porta}', Fore.GREEN)
                imprimir_com_cor("=====================================", Fore.RED)

        else:
            print("A porta inicial deve ser menor que a porta final!")

    else:
        imprimir_com_cor("Formato de IP inválido!",Fore.RED)

def opcao_4():
    ip = input('IP: ')
    if len(ip.split('.')) == 4:
        portas = input('Portas: ').split(",")
        print(f"\nVarredura de portas iniciada para o dispositivo com IP {ip}...")
        varredura = VerificadorPortas()
        portas_abertas = varredura.iniciar_varredura_lista_portas(ip, portas)
        if len(portas_abertas) == 0:
            print('Nenhuma porta aberta encontrada para a lista de portas especificado.')
        else:
            imprimir_com_cor("============= Relatório =============",Fore.RED)
            for porta in portas_abertas:
                imprimir_com_cor(f'{ip}:{porta}',Fore.GREEN)
            imprimir_com_cor("=====================================", Fore.RED)

    else:
        imprimir_com_cor("Formato de IP inválido!",Fore.RED)

def opcao_5():
    ip = input('IP: ')
    if len(ip.split('.')) == 4:
        print(f"\nVarredura de portas iniciada para o dispositivo com IP {ip}...")
        varredura = VerificadorPortas()
        portas_abertas = varredura.iniciar_varredura_todas_portas(ip)
        if len(portas_abertas) == 0:
            print('Nenhuma porta aberta encontrada.')
        else:
            imprimir_com_cor("============= Relatório =============",Fore.RED)
            for porta in portas_abertas:
                imprimir_com_cor(f'{ip}:{porta}',Fore.GREEN)
            imprimir_com_cor("=====================================", Fore.RED)

    else:
        imprimir_com_cor("Formato de IP inválido!",Fore.RED)

def opcao_6():
    ip = input('IP: ')
    if len(ip.split('.')) == 4:
        print(f"\nVarredura de portas famosas iniciada para o dispositivo com IP {ip}...")
        varredura = VerificadorPortas()
        portas_abertas_famosas = varredura.iniciar_varredura_portas_famosas(ip)
        if len(portas_abertas_famosas) == 0:
            print('Nenhuma porta famosa aberta encontrada.')
        else:
            imprimir_com_cor("============= Relatório =============",Fore.RED)
            for porta in portas_abertas_famosas:
                imprimir_com_cor(f'{ip}:{porta}',Fore.GREEN)
                imprimir_com_cor(f'{ip}:{porta[0]} Serviço:{porta[1]}',Fore.GREEN)
            imprimir_com_cor("=====================================", Fore.RED)

    else:
        imprimir_com_cor("Formato de IP inválido!",Fore.RED)

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

