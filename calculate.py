def calculate():
    grade_points = {
        'E': 4,
        'M': 3,
        'A': 2,
    }
    def get_point(standard):
        return grade_points.get(standard['grade'], 0)

    standards.sort(key=get_point, reverse=True)

    total_credits = 0
    rank_score = 0

    for standard in standards:
        if total_credits >= 80:
            break

        grade = standard['grade']
        credit = int(standard['credits'])
        
        if grade in grade_points:
            if total_credits + credit > 80:
                credit = 80 - total_credits

            rank_score += credit * grade_points[grade]
        total_credits += credit

    return (
        total_credits,
        rank_score
    )

standards = [
    {'grade': 'E', 'credits': '4'},
    {'grade': 'E', 'credits': '4'},
    {'grade': 'M', 'credits': '5'},
    {'grade': 'A', 'credits': '3'},
    {'grade': 'E', 'credits': '3'},
    {'grade': 'M', 'credits': '6'},
    {'grade': 'A', 'credits': '5'},
    {'grade': 'E', 'credits': '2'},
    {'grade': 'E', 'credits': '5'},
    {'grade': 'E', 'credits': '5'},
    {'grade': 'E', 'credits': '5'},
    {'grade': 'E', 'credits': '5'},
    {'grade': 'E', 'credits': '5'},
    {'grade': 'E', 'credits': '5'},
    {'grade': 'E', 'credits': '5'},
    {'grade': 'A', 'credits': '8'},
    {'grade': 'A', 'credits': '8'},

]
print(calculate())
