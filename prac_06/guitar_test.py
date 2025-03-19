from prac_06.guitar import Guitar

def main():
    # Create instances of Guitar
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)  # Expected age: 102 (in 2024)
    guitar2 = Guitar("Another Guitar", 2013, 500.00)    # Expected age: 11 (in 2024)

    # Test get_age() method
    print(f"{guitar1.name} get_age() - Expected 102. Got {guitar1.get_age(2024)}")
    print(f"{guitar2.name} get_age() - Expected 11. Got {guitar2.get_age(2024)}")

    # Test is_vintage() method
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.is_vintage()}")

if __name__ == "__main__":
    main()