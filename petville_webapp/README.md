## Petville

curl example commands for our API:
* to get your token = [curl -X POST http://127.0.0.1:8000/api/v1/token_auth/ -d "username=[YOURUSERNAME]&password=[YOURPASSWORD]"]
* to access information using your token = [curl http://127.0.0.1:8000/api/v1/users/ -H 'Authorization: Token [TOKENHERE]']
