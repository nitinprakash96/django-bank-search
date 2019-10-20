
# Django bank search app

## Features

- API to fetch  bank detail, given branch IFSC code
- API to fetch all details of branches using bank name and it's city. Limit and offset on these APIs
- Authentication using JWT with validity = 5 days.


## Setup

- Create a `python3` virtualenv and clone the project.
  ```sh
    virtualenv fyle
    source fyle/bin/activate
    cd fyle/
    git clone https://github.com/nitinprakash96/django-bank-search.git
    cd django-bank-search # Navigate to the project directory
  ```

- Install required deps.

  ```sh
    pip install -r requirements.txt
  ```

- Update database config in `fyle/settings.py`
  ```python
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
    }
  }
  ```

- Run the server

  ```sh
    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver
  ```


##  APIs

- Register: `POST accounts/register/`.
  - Sample CURL:

    ```sh
    curl -X POST "http://127.0.0.1:8000/accounts/register/" -H "accept: application/json" -H "Content-Type: application/json" -H "X-CSRFToken: VhOpX6dw3YfUBIRj4cy0VtRUoN6ey7Rmc0Gv1kRarACxAoHjpCo4sK6hhS0LHJv5" -d "{ \"username\": \"John\", \"first_name\": \"string\", \"last_name\": \"string\", \"email\": \"john@doe.com\", \"password\": \"secret\", \"password_confirm\": \"secret\"}" | json_pp
    ```

- Now that registration is successfull, you can obtain a `JWT token` using `POST /api-token-auth/`. Validity of the token is 5 days.
  - Sample CURL for getting `JWT token`:

    ```sh
    curl -X POST "http://127.0.0.1:8000/api-token-auth/" -H "accept: application/json" -H "Content-Type: application/json" -H "X-CSRFToken: VhOpX6dw3YfUBIRj4cy0VtRUoN6ey7Rmc0Gv1kRarACxAoHjpCo4sK6hhS0LHJv5" -d "{ \"username\": \"admin\", \"password\": \"newsecret\"}" | json_pp
    ```


   - You can also refresh the token(while the token is still active). Sample CURL for refreshing `JWT token`:

    ```sh
    curl -X POST "http://127.0.0.1:8000/api-token-refresh/" -H "accept: application/json" -H "Content-Type: application/json" -H "X-CSRFToken: Dld0ldW5jenSsA8zVGg8DlRGQHUphHSKU456prAJHQKvrgYzg66caC63JMOWqjwt" -d "{ \"token\": \"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTY0NTY4NjU1LCJlbWFpbCI6ImFudWJoYXZ1amphd2FsQGdtYWlsLmNvbSJ9.GMbLTZYicKyyTvXAipdFRz-xhcQ65fZBdKoW_j9h1Xs\"}" | json_pp
    ```

- ### Using Bank API's

  - `GET /bank/<ifsc>/`
    - `GET` request to fetch a bank details, given branch IFSC code.
    - `JWT token` should be included in the headers as `Authorization:"<jwt_token>"`

    - Sample CURL:

      ```sh
      curl -X GET "http://127.0.0.1:8000/bank/ABHY0065036/" -H "accept: application/json" -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTY1MDAxNjg5LCJlbWFpbCI6ImFudWJoYXZ1amphd2FsQGdtYWlsLmNvbSJ9.PB9ES8ZNLm9K7qzgupwCY3m5kVW7fFUdyLrIXun4cDf" -H "X-CSRFToken: SwW2YIBihC639fHu82K0v5eX34EVb1t59fO82WfWFetG8VxutsA42mtkW9yskD7O" | json_pp
      ```

  - `GET /bank?bank_name=<bank-name>&city=<city-name>&limit=<limit>&offset=<offset>`

    - `GET` request to fetch all details of branches, given bank name and a city.
    - This should also include `JWT token` in the headers.
    - Sample CURL:

      ```sh
      curl -X GET "http://127.0.0.1:8000/bank?bank_name=SOUTH+INDIAN+BANK&city=KERELA&limit=10&offset=20" -H "accept: application/json" -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTY1MDAzOTg5LCJlbWFpbCI6ImFudWJoYXZ1amphd2FsQGdtYWlsLmNvbSJ9.hRsOMvVn3wkOLChBuzmaaGOne1n4RE1zKQO0bH7mdrU" -H "X-CSRFToken: 9l8CxhHc5agdYSWB3bmt5ZjCk77kNI5nq40IBvlQtMDQXyMBoBcxCgyZdc1RWkJ6" | json_pp
      ```
