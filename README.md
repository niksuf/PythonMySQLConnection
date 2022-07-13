# Простые запросы к БД MySQL из Python

## Описание команд
Работа с базой данных MySQL осуществляется при помощи библиотеки ```pymysql```. Данные для подключения к базе данных ```host, user, password, db_name``` находятся в
отдельном файле ```config.py```.

Для создания таблицы используется команда:
```
CREATE TABLE `table_name`(...);
```
Для добавления записей в таблицу:
```
INSERT INTO `table_name` (...) VALUES (...);
```
Для обновления уже существующей записи:
```
UPDATE `table_name` SET ... WHERE ... ;
```
Для удаления записи:
```
DELETE FROM `table_name` WHERE ... ;
```
Удаление таблицы:
```
DROP TABLE `table_name`;
```
Вывод данных таблицы:
```
SELECT * FROM `table_name`;
```

## Инструкция по запуску
1. Скачать репозиторий к себе на компьютер при помощи команды:
```
git clone https://github.com/niksuf/PythonMySQLConnection
```
2. Прописать в фалйе ```config.py``` данные для подключения к базе данных.
3. Запустить приложение командой:
```
python main.py
```