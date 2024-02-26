from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def read_main(name: str, message: str):
    return {"message": f"Hello {name}! {message}"}
