codigo_regiao = int(input("Digite o código da região (1 a 5): 1- norte, 2- sul, 3- sudeste, 4- nordeste, 5- centro-oeste"))
valor_original = float(input("Digite o valor original da compra: "))
desconto = 0
if codigo_regiao == 1:
    desconto = 0.05   
elif codigo_regiao == 2:
    desconto = 0.15 
elif codigo_regiao == 3:
    desconto = 0.07  
elif codigo_regiao == 4:
    desconto = 0.12  
elif codigo_regiao == 5:
    desconto = 0.20  
else:
    print("Código de região inválido.")
    exit()
valor_desconto = valor_original * desconto
print(f"O valor do desconto concedido é: R$ {valor_desconto:.2f}")
