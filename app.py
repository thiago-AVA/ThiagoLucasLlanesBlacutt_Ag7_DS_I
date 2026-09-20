# campanha de conscientização ambiental
print("Junte-se a nós na campanha de conscientização ambiental! 🌱")
imovel = input("informe nos do seu tipo de imovel (casa, apartamento, comercial): ")
gastos_de_agua = float(input("Informe o gasto de água em metros cúbicos: "))

if imovel == "comercial":
    print("Tarifa comercial aplicada – consulte o plano corporativo.")
elif imovel == "apartamento" or imovel == "casa" and gastos_de_agua < 10:
    print("Consumo econômico – excelente controle de água!")
else:
    print("Consumo elevado – considere medidas de economia de água e verifique vazamentos.")