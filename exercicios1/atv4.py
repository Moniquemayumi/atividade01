dias = int(input("Digite o número de dias de aluguel: "))
quilometros = float(input("Digite o total de quilômetros rodados: "))
custo_diario = dias * 90
if quilometros > 100:
    quilometros_extras = quilometros - 100
    taxa_extra = quilometros_extras * 12
else:
    taxa_extra = 0
valor_total = custo_diario + taxa_extra
print(f"O valor total a ser pago é de R$ {valor_total:.2f}.")
