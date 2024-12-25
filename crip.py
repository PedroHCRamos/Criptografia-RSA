import random

# Função para calcular o máximo divisor comum (MDC)
def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

# Função para calcular o inverso modular usando o algoritmo de Euclides estendido
def inverso_modular(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

# Função para verificar se um número é primo
def is_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Função para gerar um número primo
def gerar_numero_primo():
    while True:
        num = random.randint(100, 500)
        if is_primo(num):
            return num

# Função para gerar chaves RSA
def gerar_chaves():
    p = gerar_numero_primo()
    q = gerar_numero_primo()
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Escolha de 'e'
    e = 3
    while mdc(e, phi_n) != 1:
        e += 2

    d = inverso_modular(e, phi_n)
    return (e, n), (d, n)

# Função para criptografar
def criptografar(mensagem, chave_publica):
    e, n = chave_publica
    mensagem_numeros = [ord(char) for char in mensagem]
    mensagem_criptografada = [(char ** e) % n for char in mensagem_numeros]
    return mensagem_criptografada

# Função para descriptografar
def descriptografar(mensagem_criptografada, chave_privada):
    d, n = chave_privada
    mensagem_descriptografada = [(char ** d) % n for char in mensagem_criptografada]
    mensagem = ''.join(chr(char) for char in mensagem_descriptografada)
    return mensagem

# Função principal para interagir com o usuário
def main():
    # Gera as chaves ao iniciar
    chave_publica, chave_privada = gerar_chaves()
    print(f"Chave pública (e, n): {chave_publica}")
    print(f"Chave privada (d, n): {chave_privada}")

    while True:
        opcao = input("\nDeseja criptografar ou descriptografar uma mensagem? (c/d) ou sair (s): ").lower()

        if opcao == 'c':
            mensagem = input("Digite a mensagem a ser criptografada: ")
            mensagem_criptografada = criptografar(mensagem, chave_publica)
            print("Mensagem criptografada:", ','.join(map(str, mensagem_criptografada)))

        elif opcao == 'd':
            try:
                chave_privada_input = input("Digite a chave privada (d, n) no formato: d,n: ")
                d, n = map(int, chave_privada_input.split(','))
                mensagem_criptografada = input("Digite a mensagem criptografada (números separados por vírgula): ")
                mensagem_criptografada = list(map(int, mensagem_criptografada.split(',')))
                mensagem_descriptografada = descriptografar(mensagem_criptografada, (d, n))
                print("Mensagem descriptografada:", mensagem_descriptografada)
            except ValueError:
                print("Entrada inválida. Certifique-se de que a chave e a mensagem estão no formato correto.")

        elif opcao == 's':
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
