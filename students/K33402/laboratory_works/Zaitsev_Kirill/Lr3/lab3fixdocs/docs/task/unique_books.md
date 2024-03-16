# За кем из читателей закреплены книги, количество экземпляров которых в библиотеке не превышает 2?

***URL*** : `/library/book/take_unique_books`

***Method*** : `GET`

***Auth required*** : YES

***Permission required*** : None

## Success Responses
    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    [
        {
            "book_copy": {
                "book": {
                    "name": "Белые ночи",
                    "publisher": "МИФ",
                    "category": [
                        {
                            "id": 4,
                            "category_name": "Фикшн"
                        },
                        {
                            "id": 5,
                            "category_name": "Повесть"
                        }
                    ],
                    "authors": [
                        {
                            "id": 1,
                            "full_name": "Достоевский Ф. М."
                        }
                    ]
                },
                "cipher": "35",
                "publishing_year": 2020
            },
            "reader": {
                "id": 1,
                "full_name": "Круглов В.В.",
                "passport": "1234123456",
                "birth_date": "2003-03-11",
                "phone_number": "+79939614888",
                "education": "н",
                "degree": false,
                "registration_date": "2024-01-06",
                "reading_ticket": 1223,
                "reading_room": 1
            },
            "take_date": "2024-01-06",
            "return_date": "2024-02-06"
        },
        {
            "book_copy": {
                "book": {
                    "name": "Мастер и Маргарита",
                    "publisher": "МИФ",
                    "category": [
                        {
                            "id": 3,
                            "category_name": "Роман"
                        }
                    ],
                    "authors": [
                        {
                            "id": 2,
                            "full_name": "Булгаков М.А."
                        }
                    ]
                },
                "cipher": "587",
                "publishing_year": 2017
            },
            "reader": {
                "id": 2,
                "full_name": "Зайцев К.Д.",
                "passport": "2441130",
                "birth_date": "2003-09-13",
                "phone_number": "+79819068181",
                "education": "н",
                "degree": false,
                "registration_date": "2024-01-06",
                "reading_ticket": 1124,
                "reading_room": 1
            },
            "take_date": "2024-01-04",
            "return_date": "2024-02-04"
        }
    ]