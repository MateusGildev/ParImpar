import random


cont = 0

print("=-"*20)
print("VAMOS JOGAR IMPAR OU PAR !!!")
print("=-"*20)

while True:
    valor = int(input("Digite um valor: "))
    computador = random.randint(0,10)
    total = computador+valor
    if valor < 0 or valor > 10:
        print("NÃO ACEITO NUMERO MENOR QUE ZERO E MAIOR QUE 10...")
        break
    jogada = " "
    while jogada  not in "PI":
        jogada = str(input("Par ou Ímpar? [P/I] ")).strip().upper() [0]
    print("-"*50)
    print("Vc jogou {} e o computador {}. Total de {}".format(valor,computador,total))
    print("-"*50)
    if jogada == "P":
        if total  % 2 == 0:
            print("VC VENCEU !!!")
            cont += 1
        else:
            print(("VC PERDEU..."))
            print("=-"*30)
            print("GAME OVER!!! Vc venceu {} vezes".format(cont))
            break
    if jogada == "I":
        if total % 2 == 1:
            print("VC VENCEU !!!")
            cont += 1
        else:
            print("VC PERDEU...")
            print("=-"*30)
            print("GAME OVER!!! Vc venceu {} vezes".format(cont))
            break

    
    