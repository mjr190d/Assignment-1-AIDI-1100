from fastapi import FastAPI # Imp FastAPI class from fastapi package

app = FastAPI()

# GET method because this only reads two inputs and calculates a result.
# Nothing is created, saved, or changed on the server.
@app.get("/add")
def add(a: int, b: int):
    # The ": int" type hints tell FastAPI to convert a and b from text to integers.
    # Without them, a and b would arrive as strings and "2" + "3" would give "23".
    return {"sum": a + b}