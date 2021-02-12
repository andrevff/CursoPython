import random
import playsound
color = {
    'clean': '\033[m',
    'b_blue': '\033[44m',
    'l_blue': '\033[34m',
    'l_green': '\033[32m',
    'l_red': '\033[31m'
}

result = random.randint(1, 3)
print('{} J O K E N P Ô {}'.format(color['b_blue'], color['clean']).center(40))
print('-'*34)
print("""{}1 - Pedra
2 - Papel
3 - Tesoura{}""".format(color['l_blue'], color['clean']))
print('-'*34)
op = int(input('Digite o número pressione ENTER: '))
print('-'*34)
if result == op and result == 1:
    print('MÁQUINA: PEDRA       VOCÊ: PEDRA')
    print('{} EMPATE {}'.format(color['l_blue'], color['clean']).center(40))
    playsound.playsound('empate.wav')
elif result == op and result == 2:
    print('MÁQUINA: PAPEL       VOCÊ: PAPEL')
    print('{} EMPATE {}'.format(color['l_blue'], color['clean']).center(40))
    playsound.playsound('empate.wav')
elif result == op and result == 3:
    print('MÁQUINA: TESOURA       VOCÊ: TESOURA')
    print('{} EMPATE {}'.format(color['l_blue'], color['clean']).center(40))
    playsound.playsound('empate.wav')
elif result == 1 and op == 2:
    print('MÁQUINA: PEDRA       VOCÊ: PAPEL')
    print('{} VOCÊ VENCEU! {}'.format(color['l_green'], color['clean']).center(40))
    playsound.playsound('victory.mp3')
elif result == 1 and op == 3:
    print('MÁQUINA: PEDRA       VOCÊ: TESOURA')
    print('{} VOCÊ PERDEU! {}'.format(color['l_red'], color['clean']).center(40))
    playsound.playsound('lose.wav')
elif result == 2 and op == 1:
    print('MÁQUINA: PAPEL       VOCÊ: PEDRA')
    print('{} VOCÊ PERDEU! {}'.format(color['l_red'], color['clean']).center(40))
    playsound.playsound('lose.wav')
elif result == 2 and op == 3:
    print('MÁQUINA: PAPEL       VOCÊ: TESOURA')
    print('{} VOCÊ VENCEU! {}'.format(color['l_green'], color['clean']).center(40))
    playsound.playsound('victory.mp3')
elif result == 3 and op == 1:
    print('MÁQUINA: TESOURA       VOCÊ: PEDRA')
    print('{} VOCÊ VENCEU! {}'.format(color['l_green'], color['clean']).center(40))
    playsound.playsound('victory.mp3')
elif result == 3 and op == 2:
    print('MÁQUINA: TESOURA       VOCÊ: PAPEL')
    print('{} VOCÊ PERDEU! {}'.format(color['l_red'], color['clean']).center(40))
    playsound.playsound('lose.wav')
