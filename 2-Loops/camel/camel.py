def camel_to_snake(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char
    if snake_case and snake_case[0] == "_":
        snake_case = snake_case[1:]
    return snake_case


def main():
    camel_case = input("Please enter a variable name in camel case: ")
    if camel_case:
        snake_case = camel_to_snake(camel_case)
        print("Snake case:", snake_case)
    else:
        print("You didn't enter anything.")


main()
