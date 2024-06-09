from dotenv import load_dotenv
import os
from fuzzywuzzy import fuzz
import json

from function.power_off import shutdown_computer
from function.open_browser import open_url_browser
from function.open_file import open_file_by_path
from function.check_weather import get_weather
from function.do_screenshot import screenshot
from function.change_volume import add_volume
from function.change_volume import reduce_volume
from function.work_with_window import control_window
from function.control_app import start_application
from function.connect_wifi import connect_to_wifi
from function.change_window import change_current_window
from function.work_with_text import control_text

load_dotenv("data/.env")


def read_json_file():
    with open(os.getenv("COMMANDS"), "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


commands = {
    **read_json_file()
}

commands_func = {
    "POWER_OFF": shutdown_computer,
    "OPEN_BROWSER": open_url_browser,
    "OPEN_FILES": open_file_by_path,
    "CHECK_WEATHER": get_weather,
    "DO_SCREENSHOT": screenshot,
    "ADD_SOUND": add_volume,
    "REDUCE_SOUND": reduce_volume,
    "CURRENT_WINDOW": control_window,
    "START_APP": start_application,
    "CONNECT_WI_FI": connect_to_wifi,
    "CHANGE_WINDOW": change_current_window,
    "WORK_TEXT": control_text,
}


def check_similar_word_in_text(word, text, threshold = 80):
    tokens = text.split()

    for token in tokens:
        similarity = fuzz.ratio(word, token)
        if similarity >= threshold:
            return True
    return False


def match_command(input_command, command_dict, threshold = 80):
    """
    Співставляє введену команду з найближчим ключем у command_dict.

    Аргументи:
        input_command: Введення користувача, яке потрібно співставити.
        command_dict: Словник, де ключами є бажані команди, а значеннями - словники синонімів з відповідними значеннями дій (можуть бути порожніми рядками).
        threshold: Мінімальний бал схожості для співставлення (за замовчуванням: 80).

    Повертає:
        Найближчий ключ зі словника command_dict або None, якщо жодне співставлення не перевищує поріг.
    """
    best_match = None
    highest_similarity = 0
    best_synonym = None

    for command, synonyms in command_dict.items():
        for synonym, action in synonyms.items():
            similarity = fuzz.ratio(input_command.lower(), synonym.lower())
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_match = command
                best_synonym = {synonym: action}

    if highest_similarity >= threshold:
        return best_match, best_synonym
    return None, None


def base(responce):
    name = os.getenv('NAME').lower()
    responce = responce.lower()
    threshold = int(os.getenv('THRESHOLD_NAME'))

    check = check_similar_word_in_text(
        name, responce, threshold
    )
    if check:
        sort_func(responce)


def sort_func(responce):
    threshold = int(os.getenv('THRESHOLD_COMMANDS'))
    matched_command, action_value = match_command(
        responce, commands, threshold)
    if matched_command:
        call_func(matched_command, action_value)


def call_func(matched_command, action_value):
    action = [value for value in action_value.values()][-1]
    if len(action) == 0:
        commands_func[matched_command]()
    else:
        commands_func[matched_command](action)
