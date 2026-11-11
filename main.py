from spaceship import Spaceship

DECIMAL_SEPARATOR_SYMBOL = '.'
EMPTY_REPLACEMENT = ''
MAX_REPLACEMENTS_COUNT = 1

EMPTY_LIST_MESSAGE = 'В списке недостаточно кораблей. Требуется минимум два'

MIN_SPACESHIPS_COUNT = 2

UNKNOWN_COMMAND_MESSAGE = 'Неизвестная команда. Попробуйте снова'

commands = {
    '1': 'Создать корабль',
    '2': 'Посмотреть все корабли',
    '3': 'Сравнить мощность двух кораблей',
    '4': 'Объединить два корабля',
    '5': 'Выйти'
}

(CREATE_SPACESHIP_COMMAND, SHOW_ALL_SPACESHIPS_COMMAND, COMPARE_SPACESHIPS_COMMAND, COMBINE_TWO_SPACESHIPS_COMMAND,
 EXIT_COMMAND) = commands.keys()

spaceships = []


def print_commands():
    for number, command in commands.items():
        print(f'{number}: {command}')


def get_spaceship_data():
    is_title_valid = False

    while not is_title_valid:
        title = input('Введите название корабля: ').strip()

        if title:
            is_title_valid = True
        else:
            print('Название не может быть пустым. Попробуйте снова.')

    is_engine_power_valid = False

    while not is_engine_power_valid:
        engine_power_input = input('Укажите мощность двигателя: ').strip()

        if engine_power_input.replace(DECIMAL_SEPARATOR_SYMBOL, EMPTY_REPLACEMENT, MAX_REPLACEMENTS_COUNT).isdigit():
            engine_power = float(engine_power_input)
            is_engine_power_valid = True
        else:
            print('Мощность должна быть числом. Попробуйте снова.')

    is_max_speed_valid = False

    while not is_max_speed_valid:
        max_speed_input = input('Укажите максимальную скорость: ').strip()

        if max_speed_input.replace(DECIMAL_SEPARATOR_SYMBOL, EMPTY_REPLACEMENT, MAX_REPLACEMENTS_COUNT).isdigit():
            max_speed = float(max_speed_input)
            is_max_speed_valid = True
        else:
            print('Скорость должна быть числом. Попробуйте снова')

    return title, engine_power, max_speed


def find_spaceship_by_title(title: str):
    for spaceship in spaceships:
        if spaceship.get_title().lower() == title.lower():
            return spaceship

    return None


def compare_spaceships(first_spaceship, second_spaceship):
    if first_spaceship > second_spaceship:
        print(f'Мощность первого корабля ({first_spaceship.get_engine_power()}) больше, '
              f'чем второго ({second_spaceship.get_engine_power()})')
    elif first_spaceship < second_spaceship:
        print(f'Мощность второго корабля ({second_spaceship.get_engine_power()}) больше, '
              f'чем первого ({first_spaceship.get_engine_power()})')
    else:
        print('Мощности равны')


def get_two_spaceships():
    first_user_spaceship_title = input('Укажите название первого корабля: ').strip()
    second_user_spaceship_title = input('Укажите название второго корабля: ').strip()

    first_spaceship = find_spaceship_by_title(first_user_spaceship_title)
    second_spaceship = find_spaceship_by_title(second_user_spaceship_title)

    return first_spaceship, second_spaceship


is_program_running = True

while is_program_running:
    print_commands()
    user_command_number = input('Выберете действие и укажите его номер: ').strip()

    if user_command_number in commands:
        if user_command_number == CREATE_SPACESHIP_COMMAND:
            title, engine_power, max_speed = get_spaceship_data()
            user_spaceship = Spaceship(title, engine_power, max_speed)
            spaceships.append(user_spaceship)
        elif user_command_number == SHOW_ALL_SPACESHIPS_COMMAND:
            if spaceships:
                for spaceship in spaceships:
                    print(spaceship)
            else:
                print('Список пуст')
        elif user_command_number == COMPARE_SPACESHIPS_COMMAND:
            spaceships_count = len(spaceships)

            if spaceships_count >= MIN_SPACESHIPS_COUNT:
                first_spaceship, second_spaceship = get_two_spaceships()

                if first_spaceship is not None and second_spaceship is not None:
                    compare_spaceships(first_spaceship, second_spaceship)
                else:
                    print('Один из кораблей не найден')
            else:
                print(EMPTY_LIST_MESSAGE)
        elif user_command_number == COMBINE_TWO_SPACESHIPS_COMMAND:
            spaceships_count = len(spaceships)

            if spaceships_count >= MIN_SPACESHIPS_COUNT:
                first_spaceship, second_spaceship = get_two_spaceships()

                if first_spaceship is not None and second_spaceship is not None:
                    user_spaceship = first_spaceship + second_spaceship
                    spaceships.append(user_spaceship)
                    print(user_spaceship)
                else:
                    print('Один из кораблей не найден')
            else:
                print(EMPTY_LIST_MESSAGE)
        elif user_command_number == EXIT_COMMAND:
            print('Выход из программы')
            is_program_running = False
        else:
            print(UNKNOWN_COMMAND_MESSAGE)
    else:
        print(UNKNOWN_COMMAND_MESSAGE)
