import multiprocessing
import time
import random

semaforo = None

def init(s):
    global semaforo
    semaforo = s

def processo(num):
    global semaforo
    dist_perc: int = 0
    dist_total: int = 0
    
    print(f"A Pessoa {num} começou a andar pelo corredor {num}")
    while (dist_total < 200):
        dist_perc = random.randint(4, 6)
        dist_total += dist_perc
        if (dist_total > 200):
            dist_total = 200
        print(f"A pessoa {num} percorreu {dist_perc} m de um total de {dist_total}/200")
        time.sleep(1)
    print(f"A pessoa {num} chegou na porta")
    with semaforo:
        print(f"A pessoa {num} está cruzando pela porta")
        time.sleep(random.randint(1, 2))
    print(f"A pessoa {num} saiu da porta")

def main():
    arg: int = [0]*4
    i: int = 0
    sem = None
    
    for i in range(4):
        arg[i] = i + 1
    
    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(1)
        with multiprocessing.Pool(processes=4, initializer=init, initargs=(sem,)) as pool:
            pool.map(processo, arg)

if __name__ == '__main__':
    main()