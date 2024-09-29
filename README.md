# Конфигурационный парсер

парсинг учебного конфигурационного языка и преобразования его в формат JSON.

* **Функциональность**:
  * Обработка простых констант и массивов.
  * Поддержка математических операций: сложение, вычитание, умножение, деление, а также функции `sqrt()` и `max()`.
  * Возможность вычисления значений констант на основе других констант.

* **Как это работает???**:
  * Входные данные принимаются из текстового файла, путь к которому задается в командной строке.
  * Парсер анализирует каждую строку и извлекает константы, массивы и математические выражения.
  * Вычисляет значения, если они зависят от других констант или выражений.
  * Результат выводится в формате JSON.

* **Примеры использования**:
  * Запуск парсера: `python main.py <путь_к_файлу>`
  * Примеры входных файлов:
    * `значение a -> 10`
    * `значение arr -> (1, 2, 3)`
    * `значение sqrt_a -> sqrt(a)`

* **Тестирование**: Проект включает тесты для проверки корректности работы парсера с различными сценариями.

* **Ошибки**: Парсер генерирует сообщения об ошибках для некорректных конструкций, таких как неизвестные операторы или неправильный синтаксис.
