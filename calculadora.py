print("Início do Programa")


base = float(input("\nQual o valor da base deste triângulo?\n"))
lado2_tri = float(input("\nE qual é o valor de um dos lados do triângulos sem ser a base?\n"))
lado3_tri = float(input("\nE qual é o valor do outro lado do triângulos sem ser a base?\n"))
altura_tri = float(input("\nQual a altura do triângulo?"))

peri_tri = base + lado2_tri + lado3_tri
area_tri = (base * altura_tri)/2

print(f'O triângulo em questão tem um perímetro igual a '{peri_tri}, com uma área de {area_tri}.)