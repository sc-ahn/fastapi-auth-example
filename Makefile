run:
	uvicorn main:app --host 0.0.0.0 --port 8086 --reload

test:
	curl --location --request GET 'localhost:8086/api/users/me' --header 'Authorization: Bearer hello'