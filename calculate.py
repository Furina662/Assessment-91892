def calculate():
    total_credits = 0
    rank_score = 0
    for standard in standards:
        if total_credits >= 80:
            break
        grade = standard['grade']
        credit = int(standard['credits'])
        
        if grade == 'E':
            rank_score += credit * 4
        elif grade == 'M':
            rank_score += credit * 3
        elif grade == 'A':
            rank_score += credit * 2
        total_credits += credit

    return (
        total_credits,
        rank_score
    )

standards = [
    {'grade': 'E', 'credits': '10'},
    {'grade': 'E', 'credits': '10'},
    {'grade': 'E', 'credits': '10'},
    {'grade': 'E', 'credits': '10'},
    {'grade': 'E', 'credits': '10'},
    {'grade': 'E', 'credits': '10'},
    {'grade': 'E', 'credits': '10'},
    {'grade': 'M', 'credits': '10'},
]
print(calculate())
