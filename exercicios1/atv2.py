segundos= float(input("Digite o tempo em segundos:" ))
horas= segundos//3600
segundos= segundos%3600
minutos= segundos//60
segundos= segundos%60
print("O tempo é de %d horas, %d minutos e %d segundos" %(horas, minutos, segundos))
