import socket
from VerificadorIP import VerificadorIP

class VerificadorPortas:

    def __init__(self):
        self.portas_abertas = []
        self.ip_portas_abertas = []
        self.protocolos = [
            (80, "HTTP"),
            (443, "HTTPS"),
            (20, "FTP (dados)"),
            (21, "FTP (controle)"),
            (22, "SSH"),
            (23, "Telnet"),
            (25, "SMTP"),
            (110, "POP3"),
            (143, "IMAP"),
            (53, "DNS"),
            (67, "DHCP (servidor)"),
            (68, "DHCP (cliente)"),
            (69, "TFTP"),
            (123, "NTP"),
            (389, "LDAP"),
            (3389, "RDP"),
            (161, "SNMP (consulta)"),
            (162, "SNMP (traps)"),
            (22, "SFTP"),
            (22, "SCP"),
            (137, "SMB (início)"),
            (138, "SMB (transição)"),
            (139, "SMB (fim)"),
            (445, "SMB (netbios)"),
            (1433, "MSSQL"),
            (3306, "MySQL")
        ]

    def testar_conexao(self, ip, porta):
        try:
            # Cria um novo soquete para cada tentativa de conexão
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente_socket:
                cliente_socket.settimeout(1)  # Define um tempo limite para a conexão
                cliente_socket.connect((ip, porta))
                return True
        except (socket.timeout, ConnectionRefusedError):
            return False


    def iniciar_varredura_todas_portas(self, ip):
        for porta in range(1,65535):  # Todas as portas
            if self.testar_conexao(ip, porta):
                self.portas_abertas.append(porta)
        return self.portas_abertas

    def iniciar_varredura_intervalo_portas(self, ip, porta_inicial, porta_final):
        for porta in range(porta_inicial, porta_final + 1):  # Inclui a porta final
            if self.testar_conexao(ip, porta):
                self.portas_abertas.append(porta)
        return self.portas_abertas

    def iniciar_varredura_lista_portas(self, ip, portas):
        for porta in range(portas):  # Lista de portas
            if self.testar_conexao(ip, porta):
                self.portas_abertas.append(porta)
        return self.portas_abertas

    def iniciar_varredura_portas_famosas(self, ip):
        for protocolo in self.protocolos:  # Lista de portas
            if self.testar_conexao(ip, protocolo[0]):
                self.portas_abertas.append(protocolo)
        return self.portas_abertas

    # def iniciar_varredura_completa_de_todos_ips_e_portas_famosas_ativas(self,rede):
    #     verificador = VerificadorIP()
    #     ips_ativos = verificador.iniciar_varredura_na_rede(rede,1,254)
    #     for ip in ips_ativos:
    #         lista = self.iniciar_varredura_portas_famosas(ip)


