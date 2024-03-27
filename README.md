### Hexlet tests and linter status:
[![Actions Status](https://github.com/YuliaPie/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/YuliaPie/python-project-50/actions)

[![Actions Status](https://github.com/YuliaPie/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/YuliaPie/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/4142ce737f9a364bcd4e/maintainability)](https://codeclimate.com/github/YuliaPie/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/4142ce737f9a364bcd4e/test_coverage)](https://codeclimate.com/github/YuliaPie/python-project-50/test_coverage)

Описание

Вычислитель отличий - программа принимающая путь к двум файлам и выводящая отличия между ними.
Принимает файлы с расширениями json, yaml, yml. Поддерживается обработка вложенных словарей.
Есть возможность задать формат вывода.

Установка и запуск:

- Склонируйте репозиторий локально.
- В командной строке из корневой директории выполните следующие команды:
  * poetry build
  * poetry publish --dry-run (возможно придется ввести имя пользователя и пароль)
  * python3 -m pip install --user dist/*.whl

- Программу можно запускать из командной строки следующими командами: 

  * gendiff -h - Вывод справки
  * gendiff filepath1.json filepath2.json - Запуск с представлением  результатов по умолчанию (деревом) 
  * gendiff --format plain filepath1.json filepath2.json -  Запуск с плоским представлением  результатов
  * gendiff --format json filepath1.json filepath2.json -  Запуск  с представлением  результатов в формате json 

Далее приведены asciinema для иллюстрации запуска программы:


[![asciicast](https://asciinema.org/a/fEQLIDjXuhZ3EQLmC6ju77mIM.svg)](https://asciinema.org/a/fEQLIDjXuhZ3EQLmC6ju77mIM)

[![asciicast](https://asciinema.org/a/cq5deWE2oYrMUFw8h4djjpVaO.svg)](https://asciinema.org/a/cq5deWE2oYrMUFw8h4djjpVaO)

[![asciicast](https://asciinema.org/a/87ACK4hZGj1a4ODZJ4okUM6wB.svg)](https://asciinema.org/a/87ACK4hZGj1a4ODZJ4okUM6wB)

[![asciicast](https://asciinema.org/a/8f7ixlzf3bF39BFu1gLOezGyQ.svg)](https://asciinema.org/a/8f7ixlzf3bF39BFu1gLOezGyQ)

[![asciicast](https://asciinema.org/a/D7DeVYhkPoGPp7jpld2ymsieu.svg)](https://asciinema.org/a/D7DeVYhkPoGPp7jpld2ymsieu)