import numpy as np


def perform_action(action: str, num1: int, num2: float):
    if action == "add":
        return num1 + num2
    elif action == "subtract":
        return num1 - num2
    elif action == "multiply":
        return num1 * num2
    elif action == "divide":
        return num1 / num2
    else:
        raise Exception("Invalid action")


def match_action_to_perform(input_variables: list, actions: list[str]):
    # input_variables = float(input_variables[-1])
    
    match input_variables:
        case [True, _, _, _]:
            print("The first element is True")
        case [False, str(word), int(num1), num2] if word in actions:
            print(f"Performing action: `{word}` on `{num1}` and `{num2}`")
            print(perform_action(word, num1, num2))
        case [False, str(word), int(num1), num2] if word not in actions:
            print(f"Invalid action: `{word}`, valid actions are {actions}")
        case _:
            print("Invalid input")


if __name__ == "__main__":
    actions = ["add", "subtract", "multiply", "divide"]

    print("Scenario 1: Skip due to first element == True")
    variables = [True, "add", 1, 5]
    match_action_to_perform(variables, actions)
    
    print("Scenario 2: Perform addition")
    variables = [False, "add", 1, 5]
    match_action_to_perform(variables, actions)
    
    print("Scenario 3: Perform division")
    variables = [False, "divide", 1, 5]
    match_action_to_perform(variables, actions)

    print("Scenario 4: Invalid Action")
    variables = [False, "not an action", 1, 5]
    match_action_to_perform(variables, actions)

    print("Scenario 5: Invalid Input")
    variables = []
    match_action_to_perform(variables, actions)

    print("Scenario 6: Potential Strict typing drawback")
    #using numpy's bool type should not match strict True/False in first elem
    variables = [np.bool_(True), "add", 1, 5]
    #returns invalid input
    match_action_to_perform(variables, actions)
