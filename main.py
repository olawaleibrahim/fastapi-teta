from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_main():
    return {"message": "Welcome to my First FastAPI api"}

print(app)

@app.get("/article/{article_id}")
def analyze_article(article_id: int, q: str = None):
    return {
        "article id": article_id,
        "previous id": article_id -1,
        "q": q
        }