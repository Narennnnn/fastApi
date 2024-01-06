# FastAPI Demo

This is a simple FastAPI application that provides endpoints for generating random numbers.

## Steps to follow:

   ```bash
   git clone https://github.com/your-username/fastapi-random-number-generator.git
   ```
   ```bash
   pip install -r requirements.txt
   ````
   ```bash
   uvicorn main:app --reload
   ```
###### The application will be running at http://127.0.0.1:8000. You can access the Swagger documentation at http://127.0.0.1:8000/docs to explore and test the available 

```bash
http://127.0.0.1:8000/random/{limit}
```

###### Replace {limit} with an integer value e.g. 999
```bash
  {
  "number": <random_number>,
  "limit": 999
}
