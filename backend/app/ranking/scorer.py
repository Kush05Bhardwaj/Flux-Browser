# power system
def power_system_score(base_score):
    clarity = min(5, int(base_score * 50))
    depth = min(5, int(base_score * 40))

    return {
        "clarity": clarity,
        "depth": depth,
        "credibility": 4,
        "freshness": 3
    }