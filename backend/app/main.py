# FastAPI entry
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.search.index import build_index
from app.search.query import search
from app.ranking.scorer import power_system_score
from app.personality.responses import search_reaction

app = FastAPI(title="Flux")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

index_data = build_index()

@app.get("/search")
def search_flux(q: str):
    results = search(q, index_data["vectorizer"], index_data["tfidf_matrix"], index_data["documents"])

    # Detect beginner vs advanced based on query complexity
    level = "advanced" if len(q.split()) > 3 else "beginner"

    enriched = []
    for r in results:
        enriched.append({
            "url": r["url"],
            "stats": power_system_score(r["score"])
        })

    return {
        "message": search_reaction(level),
        "results": enriched
    }
