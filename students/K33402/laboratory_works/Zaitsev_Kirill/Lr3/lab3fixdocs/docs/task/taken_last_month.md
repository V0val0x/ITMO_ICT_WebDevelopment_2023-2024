# Кто из читателей взял книгу более месяца тому назад?

***URL*** : `/library/book-taken/take_last_month`

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
            "id": 4,
            "take_date": "2024-01-06",
            "return_date": "2024-02-06",
            "book_copy": 1,
            "reader": 1
        },
        {
            "id": 6,
            "take_date": "2024-01-04",
            "return_date": "2024-02-04",
            "book_copy": 6,
            "reader": 2
        }
    ]   