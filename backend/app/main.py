# FastAPI entry
from fastapi import FastAPI
from app.search.index import build_index
from app.search.query import search
from app.ranking.scorer import power_system_score
from app.personality.responses import search_reaction

app = FastAPI(title="Flux")

vectorizer, matrix, docs = build_index()

@app.get("/search")
def search_flux(q: str):
    results = search(q, vectorizer, matrix, docs)

    enriched = []
    for r in results:
        enriched.append({
            "url": r["url"],
            "stats": power_system_score(r["score"])
        })

    return {
        "message": search_reaction("beginner"),
        "results": enriched
    }
