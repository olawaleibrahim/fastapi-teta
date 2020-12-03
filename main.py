from fastapi import FastAPI
from ml import nlp

app = FastAPI()

@app.get("/")
def read_main():
    return {"message": "Welcome to my First FastAPI api"}

print(app)


@app.post("/article/")
def analyze_article1(body: dict):
    return body


@app.get("/article/{article_id}")
def analyze_article(article_id: int, q: str = None):
    count = 0

    if q:
        doc = nlp(q)
        count = len(doc.ents)
    else:
        pass
    return {
        "article id": article_id,
        "previous id": article_id -1,
        "q": q,
        "count": count
        }
