import multiprocessing
import time
def your_func():
    k = 0
    while k == 0:
        print(7777)

if __name__ == '__main__':
    p = multiprocessing.Process(target=your_func)
    p.start()
    # Ждём 300 секунд (5 минут)
    p.join(2)
    print(p.is_alive())
    # Если процесс живой,то убиваем его
    if p.is_alive():
        print('kdkdkdkdk')
        # Terminate
        p.terminate()