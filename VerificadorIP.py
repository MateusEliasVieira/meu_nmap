import subprocess
import platform

class VerificadorIP:

    def __init__(self):
        self.resposta = ''
        self.comando = ''
        self.ips_ativos = []
        self.sistema = platform.system().lower()

    def ping(self, ip):
        try:
            if self.sistema == 'windows':
                comando = ['ping', '-n', '4', ip]
                resposta = f'Resposta de {ip}:'
            else:
                comando = ['ping', '-c', '4', ip]
                resposta = f'Resposta de {ip}:'

            output = subprocess.check_output(comando, stderr=subprocess.STDOUT, universal_newlines=True)
            return resposta in output
        except subprocess.CalledProcessError:
            return False

    def iniciar_varredura_na_rede(self, rede, ip_inicial = 1, ip_final = 65535):
        for i in range(ip_inicial, ip_final):  # Assume uma sub-rede /24
            ip = f"{rede}.{i}"
            if self.ping(ip):
                self.ips_ativos.append(ip)
        return self.ips_ativos

    def iniciar_varredura_no_dispositivo(self, ip):
        if self.ping(ip):
            return True
        else:
            return False


