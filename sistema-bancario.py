MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
LIMITE = 1000
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(MENU)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("⚠️ Operação falhou! Valor de depósito inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor <= 0:
            print("⚠️ Operação falhou! Valor de saque inválido.")
        elif valor > saldo:
            print("⚠️ Operação falhou! Saldo insuficiente.")
        elif valor > LIMITE:
            print(f"⚠️ Operação falhou! Limite de R$ {LIMITE:.2f} excedido.")
        elif numero_saques >= LIMITE_SAQUES:
            print(f"⚠️ Operação falhou! Limite diário de {LIMITE_SAQUES} saques atingido.")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print(extrato if extrato else "Não foram realizadas movimentações.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=============================")

    elif opcao == "q":
        print("✅ Operação finalizada. Obrigado por usar o banco!")
        break

    else:
        print("❌ Opção inválida! Tente novamente.")
