import argparse
import json
from parser import parse_configuration, ConfigurationError

def main():
    parser = argparse.ArgumentParser(description='Convert custom configuration language to JSON.')
    parser.add_argument('input_file', type=str, help='Path to the input configuration file')
    args = parser.parse_args()

    try:
        # Чтение файла с указанием кодировки
        with open(args.input_file, 'r', encoding='utf-8') as file:
            input_text = file.read()
        
        json_output = parse_configuration(input_text)
        print(json.dumps(json_output, indent=4))

    except ConfigurationError as e:
        print(f"Configuration error: {e}")
    except FileNotFoundError:
        print(f"File not found: {args.input_file}")


if __name__ == '__main__':
    main()
