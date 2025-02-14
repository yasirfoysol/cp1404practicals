# score_menu.py
# Menu-driven program to handle scores
def get_valid_score():
    """Get a valid score between 0 and 100."""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score. Must be between 0 and 100.")
        score = float(input("Enter score: "))
    return score

def print_stars(score):
    """Print as many stars as the score value."""
    print("*" * int(score))

def main():
    score = get_valid_score()
    while True:
        print("(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit")
        choice = input(">>> ").upper()
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_category(score)) # type: ignore
        elif choice == "S":
            print_stars(score)
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

main()
