# Сколько читателей имеют начальное образование, среднее, высшее, ученую степень?

***URL*** : `/library/reader/percentage`

***Method*** : `GET`

***Auth required*** : YES

***Permission required*** : None

## Success Responses

    HTTP 200 OK
    Allow: GET, HEAD, OPTIONS
    Content-Type: application/json
    Vary: Accept
    
    {
        "всего": 3,
        "начальное": 2,
        "среднее": 1,
        "высшее": 0
    }