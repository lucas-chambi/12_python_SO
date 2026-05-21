import multiprocessing
import time
import random

semaforo = None

def init(s):
    global semaforo
    semaforo = s

def corrida(equipe):
    global semaforo
    c1: str = ''
    c2: str = ''
    volta: int = 1
    tempo: int = 0

    if (random.randint(1, 2) == 1):
        c1 = 'carro 1'
        c2 = 'carro 2'
    else:
        c1 = 'carro 2'
        c2 = 'carro 1'

    print(f"O {c1} da equipe {equipe} está pronto para entrar na corrida")
    print(f"O {c2} da equipe {equipe} está pronto para entrar na corrida")
    with semaforo:
        print(f"O {c1} da equipe {equipe} entrou na corrida")
        while (volta <= 3):
            tempo = random.randint(3, 5)
            time.sleep(tempo)
            print(f"O {c1} da equipe {equipe} fez em {tempo}s a {volta}a de 3 voltas")
            volta += 1
        print(f"O {c1} da equipe {equipe} terminou suas voltas e saiu da corrida")
    volta = 1
    with semaforo:
        print(f"O {c2} da equipe {equipe} entrou na corrida")
        while (volta <= 3):
            tempo = random.randint(2, 5)
            time.sleep(tempo)
            print(f"O {c2} da equipe {equipe} fez em {tempo}s a {volta}a de 3 voltas")
            volta += 1
        print(f"O {c2} da equipe {equipe} terminou suas voltas e saiu da corrida")

def main():
    args: str = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    sem = None

    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(5)
        with multiprocessing.Pool(processes=7, initializer=init, initargs=(sem,)) as pool:
            pool.map(corrida, args)

if __name__ == '__main__':
    main()