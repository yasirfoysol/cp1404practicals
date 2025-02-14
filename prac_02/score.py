# score.py
# Program to categorize a score
def determine_score_category(score):
    """Determine the category of a score."""
    if 0 <= score < 50:
        return "Bad"
    elif 50 <= score < 90:
        return "Passable"
    elif 90 <= score <= 100:
        return "Excellent"
    else:
        return "Invalid score"


def main():
    import random
    score = float(input("Enter score: "))
    print(determine_score_category(score))

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score} - {determine_score_category(random_score)}")


main()
