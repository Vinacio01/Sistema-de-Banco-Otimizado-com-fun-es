def menu():
    return input("""
========== MENU DO SISTEMA ==========
[s] Sacar
[d] Depósito
[e] Extrato
[q] Sair
=====================================
Escolha uma opção: """)

def depositar(saldo, extrato):
    valor = float(input('Digite seu depósito: '))
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print('Depósito realizado com sucesso!')
    else:
        print('Operação falhou. Valor inválido.')
    return saldo, extrato

def sacar(saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    valor = float(input('Qual o valor do saque: '))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print('Saldo insuficiente.')
    elif excedeu_limite:
        print('O limite de saque é de R$ 500,00.')
    elif excedeu_saques:
        print('Limite diário de saques atingido.')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque: R$ {valor:.2f}\n'
        numero_saques += 1
        print('Saque realizado com sucesso!')
    else:
        print('Valor inválido para saque.')

    return saldo, extrato, numero_saques

def mostrar_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    print(extrato if extrato else "Não foram realizadas movimentações.")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("==============================\n")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = menu()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(
                saldo, extrato, limite, numero_saques, LIMITE_SAQUES
            )
        elif opcao == "e":
            mostrar_extrato(saldo, extrato)
        elif opcao == "q":
            print('Você saiu do sistema.')
            break
        else:
            print('Operação inválida. Tente novamente.')

if __name__ == "__main__":
    main()
