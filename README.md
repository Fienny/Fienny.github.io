# API для мобильного приложения Перевал.Online

Приложение предназначено для туристов, которые хотят добавить перевал в базу данных.
В данном проекте реализован API для создания, сохранения, просмотра и редактирования базы данных.
[Ссылка на Перевал.Online](https://pereval.online/)

---

##### Реализованные методы:
* _Post_ для сохранение нового объекта "Pereval_added", "User", "Coordinates", "Activities", "Pereval_areas", "Pereval_images" в БД
  *   Пример структуры объекта Pereval_added: 
    ```    
        "id": 1,
        "beautyTitle": "пер.",
        "title": "CCCCCC",
        "other_titles": "Ноа",
        "connect": "DDDDD",
        "winter_lvl": "1А",
        "summer_lvl": "2А",
        "autumn_lvl": "3А",
        "spring_lvl": "4Ф",
        "user_added": "http://127.0.0.1:8000/users/1/",
        "coord_id": "http://127.0.0.1:8000/coordinates/1/",
        "status": "new"  
    ```
* _Get pereval_added/id/_ - возвращает JSON объект типа Pereval_added
* _ PATCH pereval_added/id _ - изменяет поля Pereval_added. Возвращает JSON объект:
  ```
  {
      "state": 1,
      "message": "Successfully updated pereval!"
  }
  ```
  1 — если успешно удалось отредактировать запись в базе данных.
  0 — в противном случае.
* _GET /submitData/?user__email=email_ - список данных обо всех объектах, которые пользователь с почтой <email> отправил на сервер.


##### Использованная База Данных:
* _PostgreSQL_

---
