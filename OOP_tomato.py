class Tomato:
    # Стадии созревания помидора

    states = {
        0: "sprouting",
        1: "vegetation",
        2: "blooming",
        3: "Mature Green Stage",
        4: "The Breaker Stage",
        5: "Turning Stage",
        6: "Pink Stage",
        7: "Light Red Stage",
        8: "Red and Final Stage"
    }

    harvesting_state = 4
    final_state = 8

    def __init__(self):
        self._state = 0

    # Переход к следующей стадии созревания
    def grow(self):
        if self._state <= self.final_state:
            self._state += 1
        self._print_state()

    # Проверка, созрел ли томат
    def is_ripe(self):
        if self._state >= self.harvesting_state:
            return True
        return False

    # Защищенные(protected) методы
    def _print_state(self):
        print(f'Tomato state is {Tomato.states[self._state]}')


class Gardener:

    # Выдаем садовнику растение для ухода
    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    # Ухаживаем за растением
    def work(self):
        print('Gardener is working...')
        self._plant.grow()


    # Собираем урожай
    def harvest(self):
        print('Gardener is harvesting...')
        if self._plant.is_ripe():
            print('Plant is ready to be harvested.')
        else:
            print('Too early! Your plant is green and not ripe.')



    # Статический метод
    # Выводит справку по садоводству
    @staticmethod
    def knowledge_base():
        print('''At what stage are tomatoes harvested?
Once the tomato reaches a stage when it's about ½ green and ½ pink (called the 'breaker stage'), 
the tomato can be harvested and ripened off the vine with no loss of flavor, quality or nutrition''')


Gardener.knowledge_base()
tomato = Tomato()
gardener = Gardener(name='Nadya', plant=tomato)
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()
gardener.work()
gardener.harvest()