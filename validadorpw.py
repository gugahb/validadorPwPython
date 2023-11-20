import re

def validar_senha(senha):
    # Critérios de validação
    comprimento_minimo = 8
    min_caracteres_especiais = 2
    min_numeros = 3
    min_maiusculas = 1

    # Contagem de caracteres especiais, números e letras maiúsculas
    count_caracteres_especiais = len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', senha))
    count_numeros = len(re.findall(r'\d', senha))
    count_maiusculas = len(re.findall(r'[A-Z]', senha))

    # Verifica se atende aos critérios
    if (
        len(senha) >= comprimento_minimo and
        count_caracteres_especiais >= min_caracteres_especiais and
        count_numeros >= min_numeros and
        count_maiusculas >= min_maiusculas
    ):
        return True
    else:
        return False

# Entrada de senha pelo usuário
senha_usuario = input("Digite sua senha: ")

# Verifica se a senha é válida
if validar_senha(senha_usuario):
    print("Senha forte!")
else:
    print("Senha Fraca. Por favor, siga as diretrizes de segurança, coloque caracteres especiais, números e letras maiúsculas")
