def main():
    d = {
        "Apple": 130,
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "Honeydew": 50,
        "Kiwi": 90,
        "Lemon": 15,
        "Lime": 20,
        "Orange": 80,
        "Peach": 60,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "Sweet Cherries": 100,
        "Tangerine": 50,
        "Watermelon": 80,
    }
    user = input("Input fruit for calories:")
    if user in d:
        print("Calories:", d[user])
    else:
        print("Invalid fruit")


main()
