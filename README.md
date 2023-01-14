### В папке ***sbornik-recipes.ru*** представлены ноутбуки парсинга сайта [sbornik-recipes.ru](http://sbornik-recipes.ru/)  и обработки его результатов, ноутбуки формирования базы данных PostgreSQL, а также файлы промежуточных результатов.

## Ноутбуки:  
- **parsing.ipynb** - парсинг сайта, формирует 2 файла:  

                - *recipe_df.csv* - датафрейм рецептов,  
                - *ingr_df.csv*  - датафрейм уникальных ингредиентов;  
                
- **pd_json_convert.ipynb** - преобразование выбранных рецептов в JSON файл;  
- **create_db&tables.ipynb** - формирование базы данных PostgreSQL;  
- **df_to_sql_db.ipynb** - экспорт датафреймов ***recipe_df.csv*** и ***ingr_df.csv*** в базу данных PostgreSQL.

## Файлы:  
- **1_recipe.json** - JSON файл с одним рецептом,
- **5_recipes.json** - JSON файл с 5-ю рецептами.

- **server.py** - альфа версия обработчика запросов. Получает JSON с названием блюда и отправляет JSON с рецептом.
                  надо подправить структуру JSON и брать данные из наших файлов (или БД)
            
- **client.ipynb** - "отправитель" запросов. Посылает JSON с названием блюда и получает JSON с рецептом. Выводит его.

## web-application on flask:
- **app.py** - flask приложение. Создано и протестировано в PyCharm. Для запуска необходимо устновить flask в свое виртуальное окружение. После запуска приложения веб-страница приложения будет доступна по адресу: http://127.0.0.1:5000/
- **папка templates** - содержин шаблоны для корректного отображения страниц
