ano_nascimento = int(input("Digite o ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))
idade_anos = ano_atual - ano_nascimento
idade_meses = idade_anos * 12
idade_dias = idade_anos * 365
print(f"A idade dessa pessoa é de {idade_anos} anos, {idade_meses} meses e {idade_dias} dias.")
