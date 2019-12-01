# Сравни зарплату

В данном проекте подгружаются уровни заработных плат с HeadHunter.ru и SuperJob.ru по городу Москве.

## Как установить

Для начала Вам нужно создать файл .env, в котором должны быть прописаны значения:
```Python3
auth_token_hh=Bearer Ваш Токен в HeadHunter
user-agent_hh=Ссылка вашего приложения в HeadHunter
X-Api-App-Id=Ваш токен в SuperJob
```
и сохранить его в корневой папке.

Выбранные наиболее популярные языки программирования:

* JavaScript
* Java
* Python
* Ruby
* PHP
* C++
* C#
* C
* Go
* Shell
* Objective-C
* Scala
* Swift
* TypeScript

### Пример запуска

`python salary.py`

### Цель проекта

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:
Если данные введены правильно, при выполнении файла salary.py появится таблица с уровнем заработной платы, что означает успешную авторизацию в hh.ru, superjob.ru.

`pip install -r requirements.txt`


Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
