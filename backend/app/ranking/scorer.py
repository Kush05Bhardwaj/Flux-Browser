# power system
def power_system_score(base_score):
    return {
        "clarity": min(5, round(base_score * 10)),
        "depth": min(5, round(base_score * 8)),
        "credibility": 4,
        "freshness": 3
    }