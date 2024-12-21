from threading import Thread
from time import sleep

class Knight(Thread):
    def __init__(self, name:str, power:int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        count_power = 100
        number_days = 0

        for i in range(count_power):
            if count_power > 0:
                count_power -= self.power 
                number_days += 1
                sleep(1)
                print(f'{self.name} сражается {number_days} день(дня)..., осталось {count_power} воинов.')
                if count_power <= 0:
                    print(f'{self.name} одержал победу спустя {number_days} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')