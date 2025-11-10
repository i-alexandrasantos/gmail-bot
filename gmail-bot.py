
import pyautogui
print(pyautogui.position())
import time

#print("Iniciando teste...")
#time.sleep(2)
#print("Teste concluído.")

#Bot para criar vários e-mails e inserir um modelo específico antes do disparo.
#Vezes que irá se repetir
repeticoes = 10

pyautogui.PAUSE = 0.3

time.sleep(5)
#start

for i in range(repeticoes):
    print(f"Iniciando a sequência  #{i+1}")

    #
    pyautogui.click(x=97,y=225)
    #mais opcoes
    pyautogui.click(x=1204,y=831)
    #modelos
    pyautogui.click(x=1034,y=740)
    #clique no modelo
    time.sleep(2)
    pyautogui.click(x=720,y=548)
    #

    print(f"Fim da sequência  #{i+1}")

    time.sleep(1)