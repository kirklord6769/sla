print("Bem vindo a nossa boate")


resposta = int(input("Qual sua idade? "))
sla = 18

if resposta >=60 :
    print("Não era pra estar no asilo vovô?")
elif resposta >= 30:
    print("Se cuida coroa")
elif resposta >= 18:
    print("Pode entrar pae")
else:
    print("Vaza daqui pia de bosta")

print("Bem vindo a boate noite infinita deseja beber algo?")
rspta = input("")
if rspta == "sim":
    bebida = input("Qual bebida voce deseja? ")
    print(f"Aqui esta senhor {bebida} esta pronto")
else:
    print("Tudo bem tenha uma boa festa!")