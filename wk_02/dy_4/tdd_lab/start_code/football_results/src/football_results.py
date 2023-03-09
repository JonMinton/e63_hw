def get_result(final_score):
    if final_score["home_score"] > final_score["away_score"]:
        return "Home win"
    if final_score["home_score"] < final_score["away_score"]:
        return "Away win"
    if final_score["home_score"] == final_score["away_score"]:
        return "Draw"

def get_results(final_scores):
    return [get_result(x) for x in final_scores]
    # (You could try and use a list comprehension for this)