from fastapi import FastAPI
from ml import nlp
from pydantic import BaseModel
import starlette
from typing import List

app = FastAPI()

@app.get("/")
def read_main():
    return {
        "message": "Welcome to my First FastAPI api"}


class Article(BaseModel):
    content: str
    number: int
    comments: List[str] = []


@app.post("/article/")
def analyze_article1(articles: List[Article]):

    '''
    Analyze article(s) and return its entities
    using ✨ -- spaCy -- ✨

    Statistical models *will* have **errors**

    * Extract entities
    * Scream comments
    '''

    messages = []
    comments = []
    ents = []
    for article in articles:
        messages.append(article.content)

        for comment in article.comments:
            comments.append(comment.upper())

        doc = nlp(article.content)
        for ent in doc.ents:
            ents.append({"text": ent.text, "label": ent.label_})

    return {
        "messages": messages,
        "comments": comments,
        "ents": ents}


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
