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

## Notice

[`auth.models.HTTPBearer`] is a class that overrides `fastapi.security.http`.

`HTTPBearer` implemented in `fastapi.security.http` gives 403 response code when Bearer token is not received.

I need to give a 401 response code, so that was the reason I implemented `HTTPBearer` class.
