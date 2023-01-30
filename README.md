  ### В папку ***eda.ru***  
-  добавлен ноутбук **make_tbl_2.ipynb**.  
- добавлены файлы таблиц для data base:  
  
    - set_ingredients.csv  
    - recipes.csv  
    - units.csv  
    - ingredients.csv
 
 
 ### В папку ***eda.ru***  
-  добавлен ноутбук **grab_all_recipe_urls.ipynb**.  
9428 ссылок на рецепты сайта *eda.ru*  собраны в файле **all_url_df.csv**. 
-  добавлен ноутбук **scrap_recipes.ipynb** автоматического парсинга по ссылкам из **all_url_df.csv**.  
- в файле **recipe_df.csv** теперь 763 рецепта, в файле **ingr_df.csv** - 759 ингредиентов (результат парсинга 800 ссылок из 9428).  
### Добавлена папка ***eda.ru***.  
Структура *recipe_df.csv* и файлов *json* **ИЗМЕНИЛАСЬ!**  
Добавлены признаки:  
- cuisine
- meal_mode
- portions
- calories
- proteinContent
- fatContent
- carbohydrateContent   

Название признака *ingredients* изменено на *ingr_name*,  
название признака *quantity* изменено на *ingr_qwn*.  
Добавлены признаки *measure* и *quantity*. Пока они пустые, предполагается заносить в них единицу измерения и количество для каждого ингредиента, полученные из признака *ingr_qwn*.

### Ноутбуки:  
- **eda_ru-pars_2.ipynb** - парсинг сайта, формирует 3 файла:  

                - *recipe_df.csv* - датафрейм рецептов,  
                - *ingr_df.csv*  - датафрейм уникальных ингредиентов;  
                - *url_df_2.csv*  - датафрейм ссылок, по которым уже был произведен парсинг сайта
- **pd_json_convert.ipynb** - преобразование выбранных рецептов в JSON файл;  


### Файлы **json**:  
- **1_recipe.json** - JSON файл с одним рецептом,
- **5_recipes.json** - JSON файл с 5-ю рецептами,
- **16_recipes.json** - JSON файл с 16-ю рецептами.


### В папке ***sbornik-recipes.ru*** представлены ноутбуки парсинга сайта [sbornik-recipes.ru](http://sbornik-recipes.ru/)  и обработки его результатов, ноутбуки формирования базы данных PostgreSQL, а также файлы промежуточных результатов.

### Ноутбуки:  
- **parsing.ipynb** - парсинг сайта, формирует 2 файла:  

                - *recipe_df.csv* - датафрейм рецептов,  
                - *ingr_df.csv*  - датафрейм уникальных ингредиентов;  
                
- **pd_json_convert.ipynb** - преобразование выбранных рецептов в JSON файл;  
- **create_db&tables.ipynb** - формирование базы данных PostgreSQL;  
- **df_to_sql_db.ipynb** - экспорт датафреймов ***recipe_df.csv*** и ***ingr_df.csv*** в базу данных PostgreSQL.

### Файлы:  
- **1_recipe.json** - JSON файл с одним рецептом,
- **5_recipes.json** - JSON файл с 5-ю рецептами.

- **server.py** - альфа версия обработчика запросов. Получает JSON с названием блюда и отправляет JSON с рецептом.
                  надо подправить структуру входного JSON и брать данные из БД
                  UPD: Данные из файла берутся.
            
- **client.ipynb** - "отправитель" запросов. Посылает JSON с названием блюда и получает JSON с рецептом. Выводит его.

## web-application on flask:
- **app.py** - flask приложение. Создано и протестировано в PyCharm. Для запуска необходимо устновить flask в свое виртуальное окружение. После запуска приложения веб-страница приложения будет доступна по адресу: http://127.0.0.1:5000/
- **папка templates** - содержин шаблоны для корректного отображения страниц
![image](https://user-images.githubusercontent.com/57331385/212469926-74f31ca8-a579-443f-a9f7-e8d53a0c2bab.png)
![image](https://user-images.githubusercontent.com/57331385/212469940-496af632-9483-44e1-bc4d-733d27fc3b39.png)
