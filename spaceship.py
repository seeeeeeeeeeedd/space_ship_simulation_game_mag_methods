class Spaceship:
    def __init__(self, title: str, engine_power: float | int, max_speed: float | int):

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
