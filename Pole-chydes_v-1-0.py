import random

# БАЗА ДАННЫХ СЛОВ (Вшита прямо в скрипт - All in One)
WORDS_POOL = [
    "АКВАРЕЛЬ", "АЛМАЗ", "АПЕЛЬСИН", "АРБУЗ", "БАНАН", "БАРАБАН", "БЕГЕМОТ", "БИЛЕТ",
    "БЛОКНОТ", "БОРЩ", "БУТЫЛКА", "ВАРЕНЬЕ", "ВЕЛОСИПЕД", "ВЕРТОЛЕТ", "ВЕТЕР", "ВИНОГРАД",
    "ВОДОПАД", "ВУЛКАН", "ГИТАРА", "ГОРОД", "ГРИБ", "ДЕРЕВО", "ДИНОЗАВР", "ДОЖДЬ",
    "ДОРОГА", "ДРАКОН", "ЕЖИК", "ЖИРАФ", "ЖУРНАЛ", "ЗАБОР", "ЗАМОК", "ЗВЕЗДА",
    "ЗЕБРА", "ЗОНТИК", "ИГРА", "ИГРУШКА", "КАКТУС", "КАЛЕНДАРЬ", "КАРАНДАШ", "КАРТИНА",
    "КИРПИЧ", "КИТ", "КЛЮЧ", "КНИГА", "КОМПЬЮТЕР", "КОРАБЛЬ", "КОРОНА", "КОСМОС",
    "КОТ", "КРАСКА", "КРОВАТЬ", "КРОКОДИЛ", "ЛАМПА", "ЛИМОН", "ЛИСА", "ЛОДКА",
    "ЛОШАДЬ", "ЛЯГУШКА", "МАГАЗИН", "МАШИНА", "МЕДВЕДЬ", "МОЛОКО", "МОНИТОР", "МОРОЖЕНОЕ",
    "МОСТ", "МЯЧ", "ОБЛАКО", "ОГУРЕЦ", "ОКНО", "ОСТРОВ", "ОЧКИ", "ПАЛЬМА",
    "ПАУК", "ПЕНАЛ", "ПЕРЦАТКА", "ПИНГВИН", "ПИРОГ", "ПИЦЦА", "ПЛАНЕТА", "ПОЕЗД",
    "ПОДУШКА", "ПОМИДОР", "ПОПУГАЙ", "РАДУГА", "РАКЕТА", "РЮКЗАК", "САМОЛЕТ", "СВЕЧА",
    "СЛОН", "СОЛНЦЕ", "СТАКАН", "СТУЛ", "ТЕЛЕФОН", "ТЕТРАДЬ", "ТИГР", "ТОРТ",
    "УЛИТКА", "УТЮГ", "ФОНАРЬ", "ФОТОГРАФИЯ", "ХЛЕБ", "ЦВЕТОК", "ЧАЙНИК", "ЧАСЫ",
    "ЧЕМОДАН", "ЧЕРЕПАХА", "ШАПКА", "ШОКОЛАД", "ЩЕТКА", "ЭКРАН", "ЮБКА", "ЯБЛОКО"
]

# ANSI КОДЫ ДЛЯ ЦВЕТА (Встроены в Python, работают без скачивания библиотек)
CLR_RESET = "\033[0m"
CLR_RED = "\033[31m"
CLR_GREEN = "\033[32m"
CLR_YELLOW = "\033[33m"
CLR_BLUE = "\033[34m"
CLR_PURPLE = "\033[35m"
CLR_CYAN = "\033[36m"
STYLE_BOLD = "\033[1m"

def play_round():
    answer = random.choice(WORDS_POOL)
    question = f"Загадано секретное слово из русского языка, в нём {len(answer)} букв."
    
    display_word = ["⭐"] * len(answer)
    guessed_letters = set()
    score = 0
    
    wrong_attempts = 0
    max_attempts = 5

    print(f"\n{CLR_CYAN}{STYLE_BOLD}========================================")
    print("=== ДОБРО ПОЖАЛОВАТЬ НА ПОЛЕ ЧУДЕС! ===")
    print(f"========================================{CLR_RESET}")
    print(f"Вопрос: {CLR_YELLOW}{question}{CLR_RESET}")
    print(f"Слово на табло: {CLR_BLUE}{' '.join(display_word)}{CLR_RESET}")
    print(f"ℹ️ Чтобы выйти из игры, напишите: {CLR_RED}{STYLE_BOLD}СТОП{CLR_RESET}")
    print("--------------------------------------------------")

    while "⭐" in display_word and wrong_attempts < max_attempts:
        sectors = [100, 200, 300, 400, 500, "ПРИЗ", "БАНКРОТ"]
        wheel_result = random.choice(sectors)
        
        print(f"\n--- Вращайте барабан! ---")
        
        if wheel_result == "БАНКРОТ":
            print(f"На барабане сектор: {CLR_RED}{STYLE_BOLD}{wheel_result}{CLR_RESET}")
            print(f"{CLR_RED}💥 Вы обанкротились! Все ваши очки сгорают.{CLR_RESET}")
            score = 0
            print(f"Ваш текущий счет: {CLR_YELLOW}{score}{CLR_RESET} очков.")
            print("--------------------------------------------------")
            continue
        elif wheel_result == "ПРИЗ":
            print(f"На барабане сектор: {CLR_PURPLE}{STYLE_BOLD}{wheel_result}{CLR_RESET}")
            print(f"{CLR_PURPLE}🎁 Сектор ПРИЗ! Вам начисляется 500 очков.{CLR_RESET}")
            wheel_result = 500
        else:
            print(f"На барабане сектор: {CLR_GREEN}{wheel_result}{CLR_RESET}")
            
        print(f"Очки за ход: {CLR_GREEN}{wheel_result}{CLR_RESET} | Ваш счет: {CLR_YELLOW}{score}{CLR_RESET} очков")
        
        err_color = CLR_RED if wrong_attempts >= 3 else CLR_RESET
        print(f"Ошибки: {err_color}{wrong_attempts} из {max_attempts}{CLR_RESET}")
        
        choice = input("Введите БУКВУ или напишите 'СЛОВО' (угадать целиком): ").strip().upper()

        if choice == "СТОП":
            print(f"\n{CLR_RED}{STYLE_BOLD}🛑 ИГРА ПРЕРВАНА ПОЛЬЗОВАТЕЛЕМ{CLR_RESET}")
            print(f"Загаданное слово было: {CLR_YELLOW}{answer}{CLR_RESET}")
            print(f"Ваш итоговый баланс очков: {CLR_GREEN}{score}{CLR_RESET}")
            print("--------------------------------------------------")
            return False

        if choice == "СЛОВО":
            user_word = input("Введите слово: ").strip().upper()
            if user_word == "СТОП":
                print(f"\n{CLR_RED}{STYLE_BOLD}🛑 ИГРА ПРЕРВАНА ПОЛЬЗОВАТЕЛЕМ{CLR_RESET}")
                print(f"Загаданное слово было: {CLR_YELLOW}{answer}{CLR_RESET}")
                print(f"Ваш итоговый баланс очков: {CLR_GREEN}{score}{CLR_RESET}")
                print("--------------------------------------------------")
                return False
            
            if user_word == answer:
                display_word = list(answer)
                if isinstance(wheel_result, int):
                    score += wheel_result * 2
                break
            else:
                wrong_attempts += 1
                print(f"{CLR_RED}❌ Неверно! Это не то слово. (Ошибка {wrong_attempts}/{max_attempts}){CLR_RESET}")
                print("--------------------------------------------------")
                continue

        if len(choice) != 1 or not choice.isalpha():
            print(f"{CLR_RED}⚠️ Ошибка: нужно ввести только одну букву.{CLR_RESET}")
            print("--------------------------------------------------")
            continue

        if choice in guessed_letters:
            print(f"{CLR_YELLOW}📝 Вы уже называли эту букву.{CLR_RESET}")
            print("--------------------------------------------------")
            continue

        guessed_letters.add(choice)

        check_choice = 'Е' if choice == 'Ё' else choice
        letter_found = False
        
        for index, letter in enumerate(answer):
            target_letter = 'Е' if letter == 'Ё' else letter
            if target_letter == check_choice:
                display_word[index] = letter
                letter_found = True

        if letter_found:
            print(f"{CLR_GREEN}✅ Да! Есть такая буква!{CLR_RESET}")
            if isinstance(wheel_result, int):
                score += wheel_result
        else:
            wrong_attempts += 1
            print(f"{CLR_RED}❌ Нет такой буквы. (Ошибка {wrong_attempts}/{max_attempts}){CLR_RESET}")

        print(f"Слово сейчас: {CLR_BLUE}{' '.join(display_word)}{CLR_RESET}")
        print("--------------------------------------------------")

    if wrong_attempts >= max_attempts:
        print(f"\n{CLR_RED}{STYLE_BOLD}💀 ИГРА ОКОНЧЕНА! Вы израсходовали все попытки.{CLR_RESET}")
        print(f"Загаданное слово было: {CLR_YELLOW}{answer}{CLR_RESET}")
        print(f"Ваш итоговый баланс очков: {CLR_GREEN}{score}{CLR_RESET}")
    else:
        print(f"\n{CLR_GREEN}{STYLE_BOLD}🎉 ПОЗДРАВЛЯЕМ! Слово успешно разгадано!{CLR_RESET}")
        print(f"Правильный ответ: {CLR_YELLOW}{answer}{CLR_RESET}")
        print(f"Вы заработали: {CLR_GREEN}{score}{CLR_RESET} очков!")
    
    print("--------------------------------------------------")
    return True

def main():
    while True:
        keep_playing = play_round()
        
        if not keep_playing:
            break
            
        action = input(f"\nЧтобы сыграть еще раз, напишите {CLR_GREEN}{STYLE_BOLD}ЗАНОВО{CLR_RESET} (или что угодно для выхода): ").strip().upper()
        if action != "ЗАНОВО":
            print(f"{CLR_CYAN}Спасибо за игру! До встречи.{CLR_RESET}")
            break

if __name__ == "__main__":
    main()
