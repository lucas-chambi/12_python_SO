import multiprocessing
import random
import time

placar: int = 0

def init(pl):
    global placar
    placar = pl

def corrida(sapo, salto_m):
    global placar
    posicao: int = 0
    salto: int = 0
    sapo_num: str = ''

    sapo_num = (f'sapo {sapo}')
    while (posicao < 30):
        salto = random.randint(0, salto_m)
        posicao += salto
        if salto > 0:
            print(f"O {sapo_num} saltou {salto} cm, distância percorrida: posição: {posicao} cm/30 cm")
        else:
            print(f"O {sapo_num} tropeçou e não conseguiu avançar... :(, distância percorrida: posição: {posicao} cm/30 cm")
        time.sleep(0.2)
    print(f"O {sapo_num} terminou a corrida em {placar.value + 1}o lugar!")
    placar.value += 1

def main():
    args = [(0, 0)]*5
    salto_max = random.randint(1, 5)
    sapos: int = 0
    i: int = 0
    posicao_do_sapo: int = 0

    posicao_do_sapo = multiprocessing.Value('i', 0)

    for i in range(5):
        sapos = i + 1
        args[i] = (sapos, salto_max)
    print(f"Salto máximo possível nesta rodada: {salto_max}\nTodos os sapos irâo começar no 'já!'")
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1....')
    time.sleep(1)
    print("JJJJAAAAAAAAAAAAAA!!!!!!!")

    with multiprocessing.Pool(processes=5, initializer=init, initargs=(posicao_do_sapo,)) as pool:
        pool.starmap(corrida, args)

if __name__ == '__main__':
    main()