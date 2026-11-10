class Spaceship:
    def __init__(self, title: str, engine_power: float | int, max_speed: float | int):

        self.TITLE_SEPARATOR = ' + '
        self.SHIPS_COUNT_FOR_AVERAGE = 2

        is_valid_title = self.__is_valid_title(title)
        is_valid_number = self.__is_valid_number(engine_power, max_speed)

        if is_valid_title and is_valid_number:

            self.__title = title
            self.__engine_power = engine_power
            self.__max_speed = max_speed

        else:
            self.__title = 'Название отсутствует'
            self.__engine_power = -1
            self.__max_speed = -1

    def __lt__(self, other) -> bool:
        return self.get_engine_power() < other.get_engine_power()

    def __gt__(self, other) -> bool:
        return self.get_engine_power() > other.get_engine_power()

    def __add__(self, other) -> 'Spaceship':
        new_title = self.get_title() + self.TITLE_SEPARATOR + other.get_title()
        new_engine_power = self.get_engine_power() + other.get_engine_power()
        new_max_speed = (self.get_max_speed() + other.get_max_speed()) / self.SHIPS_COUNT_FOR_AVERAGE

        return Spaceship(new_title, new_engine_power, new_max_speed)

    def get_title(self) -> str:
        return self.__title

    def get_engine_power(self) -> float | int:
        return self.__engine_power

    def get_max_speed(self) -> float | int:
        return self.__max_speed

    def __is_valid_title(self, title) -> bool:
        if isinstance(title, str):
            if title.strip():
                return True

        return False

    def __is_valid_number(self, engine_power, max_speed) -> bool:
        if isinstance(engine_power, (float, int)) and isinstance(max_speed, (float, int)):
            if engine_power > 0 and max_speed > 0:
                return True

        return False
