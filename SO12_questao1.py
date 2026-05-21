import multiprocessing
import time

semaforo = None

def init(s):
    global semaforo
    semaforo = s

def processo(carro, direcao):
    global semaforo

    print(f"O carro {carro} chegou no semáforo.")
    time.sleep(0.1)
    with semaforo:
        print (f"O carro {carro} está passando pelo semáforo.")
        time.sleep(3)
    print(f"O carro {carro} passou pelo semáforo e continuou dirigindo para o {direcao}")


def main():
    arg: str = [('1', 'norte'), ('2', 'sul'), ('3', 'leste'), ('4', 'oeste')]
    sem = None

    with multiprocessing.Manager() as manager:
        sem = manager.Semaphore(1)
        with multiprocessing.Pool(processes=4, initializer=init, initargs=(sem,)) as pool:
            pool.starmap(processo, arg)

if __name__ == '__main__':
    main()