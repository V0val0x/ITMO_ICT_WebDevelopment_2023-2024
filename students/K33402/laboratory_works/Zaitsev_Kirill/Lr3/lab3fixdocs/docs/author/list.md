# Список всех авторов

Позволяет посмотреть список всех авторов

***URL*** : `/library/author`

***Method*** : `GET`

***Auth required*** : YES

***Permission required*** : None

## Success Responses

    HTTP 200 OK
    Allow: GET, POST, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    [
        {
            "id": 1,
            "full_name": "Зайцев К.Д."
        },
        {
            "id": 2,
            "full_name": "Круглов В.В.
        {
            "id": 3,
            "full_name": "Тургенев И.С."
        },
        {
            "id": 4,
            "full_name": "Фет А.А."
        }
    ]