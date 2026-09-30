import random

cardapio = {
    "Chocolate": 5.00,
    "Baunilha": 4.50,
    "Morango": 3.00,
    "Creme": 9.00,
}

brinde = ["Canudo", "Caneca", "Gelo", "Badge"]

def mostrar_cardapio():
    print("\n -- CARDÁPIO --")
    for sabor, preco in cardapio.items():
        print(f"{sabor} -> R${preco:.2f}")

def fazer_pedido():
    total = 0
    pedido = []

    while True:
        sabor = str(input("\nInforme o sabor (Digite 0 para sair): "))

        if sabor == "0":
            break

        elif sabor in cardapio:
            total += cardapio[sabor]
            pedido.append(sabor)
            print(f"\n{sabor} adicionado")

        else:
            print("\nEsse sabor não está no cardápio")

    return pedido, total


mostrar_cardapio()
pedido, total = fazer_pedido()

print(f"\nSeu pedido: {pedido}")
print(f"\nTotal: R${total:.2f}\n")

if total > 15:
    print(f"Você ganhou um brinde: {random.choice(brinde)}\n")