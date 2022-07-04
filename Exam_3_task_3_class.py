# Тесты к задаче:
# 1. Вызовите справку по садоводству
# 2. Создайте объекты классов TomatoBush и Gardener
# 3. Используя объект класса Gardener, поухаживайте за кустом с помидорами
# 4. Попробуйте собрать урожай
# 5. Если томаты еще не дозрели, продолжайте ухаживать за ними
# 6. Соберите урожай

# Класс Tomato:
# 1. Создайте класс Tomato
# 2. Создайте статическое свойство states, которое будет содержать все стадии
# созревания помидора
# 3. Создайте метод __init__(), внутри которого будут определены два динамических
# protected свойства: 1) _index - передается параметром и 2) _state - принимает первое
# значение из словаря states
# 4. Создайте метод grow(), который будет переводить томат на следующую стадию
# созревания
# 5. Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг
# последней стадии созревания)

# Класс TomatoBush
# 1. Создайте класс TomatoBush
# 2. Определите метод __init__(), который будет принимать в качестве параметра
# количество томатов и на его основе будет создавать список объектов класса
# Tomato. Данный список будет храниться внутри динамического свойства tomatoes.
# 3. Создайте метод grow_all(), который будет переводить все объекты из списка
# томатов на следующий этап созревания
# 4. Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из
# списка стали спелыми
# 5. Создайте метод give_away_all(), который будет чистить список томатов после
# сбора урожая

# Класс Gardener
# 1. Создайте класс Gardener
# 2. Создайте метод __init__(), внутри которого будут определены два динамических
# свойства: 1) name - передается параметром, является публичным и 2) _plant -
# принимает объект класса Tomato, является protected
# 3. Создайте метод work(), который заставляет садовника работать, что позволяет
# растению становиться более зрелым
# 4. Создайте метод harvest(), который проверяет, все ли плоды созрели. Если все -
# садовник собирает урожай. Если нет - метод печатает предупреждение.
# 5. Создайте статический метод knowledge_base(), который выведет в консоль справку
# по садоводству.

class Tomato:

    states = {
        1: "Tomatoes in Mature Green Stage",
        2: "The Breaker Stage",
        3: "Turning Stage",
        4: "Pink Stage",
        5: "Light Red Stage",
        6: "Red and Final Stage"

    }

    def __init__(self, index):
        self._index = index
        self._state = state
        state = states[1]


    def grow(self, index):
        """переводит на следующую стадию созревания"""
        self.state += index
        print(Tomato.state)

    def is_ripe(self, state):
        """ будет проверять, что томат созрел (достиг последней стадии созревания)"""
        if state == states[6]:
            print("is ripe")

class TomatoBush(Tomato):

    def __init__(self, quantity):
        self.tomatoes = []
        if quantity:
            self.tomatoes.append(quantity)


    def grow_all(self, tomatoes):
        """будет переводить все объекты из списка томатов на следующий этап созревания"""
        super().__init__(self, state, index)
        self.state += index
        print(TomatoBush.state)

    def all_are_ripe(self, tomatoes):
        for tomato in tomatoes:
            if Tomato.state == states[6]:
                return True

    def give_away_all():
        """ будет чистить список томатов после сбора урожая"""
        for Tomato in TomatoBush:
            if is_ripe == True:
                tomatoes.remove(Tomato)

class Gardener(TomatoBush, Tomato):

    def __init__(self, name):
        self.name = name
        self._plant = plant
        plant = Tomato()

    def work():
        """ заставляет садовника работать, что позволяет растению становиться более зрелым"""
    pass

    def harvest():
        """ который проверяет, все ли плоды созрели. Если все - садовник собирает урожай. Если нет - метод печатает предупреждение"""
        if TomatoBush.is_ripe:
            return True
        else:
            print("Not all tomatoes are ripe")

    @staticmethod
    def knowledge_base():
        return (Tomato.states)

knowledge_base()
TomatoBush = TomatoBush()
Gardener = Gardener()
Gardener.grow_all()














