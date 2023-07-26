# FastAPI Auth example

```bash
make run
```

It runs on `localhost:8086`

You can test with swagger by using `/docs`

or just run `make test`

it calls the following curl command:

```bash
curl --location --request GET 'localhost:8086/api/users/me' \
--header 'Authorization: Bearer hello'
```
