import re
import math

class ConfigurationError(Exception):
    pass

def parse_configuration(text):
    lines = text.strip().splitlines()
    constants = {}

    for line in lines:
        line = line.strip()
        if line.startswith('значение'):
            name, value = parse_constant_declaration(line)
            constants[name] = value
        else:
            raise ConfigurationError(f"Unknown statement: {line}")

    # Обрабатываем значения констант для функций
    for name, value in constants.items():
        constants[name] = resolve_value(value, constants)

    return constants

def parse_constant_declaration(line):
    match = re.match(r'значение\s+(\w+)\s*->\s*(.+)', line)
    if not match:
        raise ConfigurationError(f"Invalid constant declaration: {line}")
    
    name = match.group(1)
    value = parse_value(match.group(2))
    return name, value

def parse_value(value):
    # Проверка на sqrt()
    sqrt_match = re.match(r'sqrt\((.+)\)', value)
    if sqrt_match:
        inner_value = parse_value(sqrt_match.group(1))
        return inner_value  # Возвращаем значение для обработки позже

    # Проверка на max()
    max_match = re.match(r'max\((.+)\)', value)
    if max_match:
        inner_values = parse_array(max_match.group(1))
        return inner_values  # Возвращаем массив для обработки позже

    if value.startswith('(') and value.endswith(')'):
        return parse_array(value[1:-1])
    elif re.match(r'^\d+(\.\d+)?$', value):
        return float(value)  # Преобразуем числа в float
    elif re.match(r'^[a-zA-Z_][\w]*$', value):
        return value  # Это имя константы
    else:
        raise ConfigurationError(f"Invalid value: {value}")

def parse_array(array_text):
    values = [parse_value(v.strip()) for v in array_text.split(',')]
    return values

def resolve_value(value, constants):
    # Если значение — это константа, получаем ее значение
    if isinstance(value, str) and value in constants:
        return resolve_value(constants[value], constants)

    # Если значение — число или массив, возвращаем его
    if isinstance(value, (float, list)):
        return value

    # Если значение — функция, вычисляем его
    if isinstance(value, list):
        if value[0] == 'sqrt':
            return math.sqrt(resolve_value(value[1], constants))
        elif value[0] == 'max':
            return max(resolve_value(v, constants) for v in value[1])
    
    return value  # Возвращаем значение по умолчанию
