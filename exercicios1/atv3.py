valor_total=float(input("Digite o valor total da compra: "))
if valor_total<=500:
    print("O valor total da compra não haverá imposto")
else:
    excedente= valor_total-500
    imposto= excedente*0.5
print(f"O imposto a ser pago é de R$ {imposto:.2f}.")
