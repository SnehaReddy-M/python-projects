import random

data = [
    {
        "name": "Instagram",
        "follower_count": 700,
        "description": "Social media platform",
        "country": "United States"
    },
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 650,
        "description": "Footballer",
        "country": "Portugal"
    },
    {
        "name": "Lionel Messi",
        "follower_count": 500,
        "description": "Footballer",
        "country": "Argentina"
    },
    {
        "name": "Virat Kohli",
        "follower_count": 270,
        "description": "Cricketer",
        "country": "India"
    },
    {
        "name": "Taylor Swift",
        "follower_count": 290,
        "description": "Singer",
        "country": "United States"
    },
    {
        "name": "Selena Gomez",
        "follower_count": 420,
        "description": "Singer and Actress",
        "country": "United States"
    }
]


def format_data(account):
    """Format account data into printable form."""
    name = account["name"]
    description = account["description"]
    country = account["country"]

    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Return True if guess is correct."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print("===== HIGHER LOWER GAME =====\n")

    score = 0
    game_should_continue = True

    account_b = random.choice(data)

    while game_should_continue:

        account_a = account_b
        account_b = random.choice(data)

        while account_a == account_b:
            account_b = random.choice(data)

        print(f"Compare A: {format_data(account_a)}")
        print("\nVS\n")
        print(f"Against B: {format_data(account_b)}")

        guess = input(
            "\nWho has more followers? Type 'A' or 'B': "
        ).lower()

        a_followers = account_a["follower_count"]
        b_followers = account_b["follower_count"]

        is_correct = check_answer(
            guess,
            a_followers,
            b_followers
        )

        if is_correct:
            score += 1
            print(f"\nCorrect! Current score: {score}\n")
        else:
            print(
                f"\nWrong! Final score: {score}"
            )
            print(
                f"A had {a_followers} million followers."
            )
            print(
                f"B had {b_followers} million followers."
            )
            game_should_continue = False


game()
