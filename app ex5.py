import streamlit as st

menu = {
    101: ("Cachorro Quente", 8.50),
    102: ("Bauru Simples", 4.50),
    104: ("Hambúrguer", 5.50),
    105: ("Cheeseburger", 6.60),
    106: ("Refrigerante", 6.00)
}

st.title("Cardápio")
st.write("""
| Código | Lanche           | Valor  |
|--------|------------------|--------|
| 101    | Cachorro Quente  | 8,50   |
| 102    | Bauru Simples    | 4,50   |
| 104    | Hambúrguer       | 5,50   |
| 105    | Cheeseburger     | 6,60   |
| 106    | Refrigerante     | 6,00   |
""")


codigo = st.number_input("Digite o código do lanche:", min_value=101, max_value=106, step=1)
quantidade = st.number_input("Digite a quantidade desejada:", min_value=1, step=1)


if codigo in menu:
    nome, preco = menu[codigo]
    total = quantidade * preco
    st.success(f"Você pediu {quantidade} x {nome}. O valor total é R$ {total:.2f}.")
else:
    st.error("Código do lanche inválido. Por favor, insira um código válido.")

