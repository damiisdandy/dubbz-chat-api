# Simple Chat API
This is the backend API for the Chat Application

## How to run
```
git clone https://github.com/damiisdandy/dubbz-chat-api dubbz-chat-api
cd dubbz-chat-api

# Creating and starting virtual environment
# you can use different ways of starting up virtual environment but I recommend pipenv
# https://pipenv.pypa.io/en/latest/
pipenv shell

# Installing packages
# you can use pipenv to install all packages in `Pipfile.lock` or you can use the `requirements.txt`
pipenv install # or pip install -r requirements.txt

# Starting application
python manage.py migrate
python manage.py runserver

# Running tests
python manage.py test
```

> Note: The delete functionality works with API keys, to get your API key, run a GET request to `http://localhost:8000/api/message/api-key/generate` this is done for testing purposes, you can use the api_key gotten as a token to perform delete functionality.
> The token is passed a Header `X-Api-Key`: <api_key> 