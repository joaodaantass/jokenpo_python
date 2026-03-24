from time import sleep 
import random 
import emoji

pedra = emoji.emojize(":fist:", language="alias")
papel = emoji.emojize(":hand:", language="alias") 
tesoura = emoji.emojize(":v:", language="alias")
trofeu = emoji.emojize(":trophy:", language="alias")
feliz = emoji.emojize(":smile:", language="alias")
triste = emoji.emojize(":cry:", language="alias")
coracao = emoji.emojize(":broken_heart:", language="alias")
empate = emoji.emojize(":neutral_face:", language="alias")
erro = emoji.emojize(":x:", language="alias")  


print("-=-" * 30)
print(f"{'Jogo do Pedra-Papel-Tesoura':>50} {pedra} {papel} {tesoura}") 
print("-=-" * 30)
print() 

itens = ("PEDRA", "PAPEL", "TESOURA")

vitorias = {
    "PEDRA": "TESOURA",
    "PAPEL": "PEDRA",
    "TESOURA": "PAPEL"  
}

cpu = random.choice(itens) 
usuario = str(input("Digite a sua jogada: ").strip().upper()) 
print() 

if usuario not in itens: 
    print(f"Jogada inválida {erro}") 
    exit()   

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!") 
print() 

print(f"Você jogou {usuario}")
print() 

if usuario == cpu:
    print(f"EMPATE {empate} O computador também escolheu {cpu}")

elif vitorias[usuario] == cpu:
    print(f"Você GANHOU! {feliz}{trofeu} O computador escolheu {cpu}")

else:
    print(f"Você PERDEU {triste}{coracao} O computador escolheu {cpu}") 