import turtle
import pandas
from text_generator import GenerateText

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
score = 0
correct_guess = []
guessing = True

data = pandas.read_csv("50_states.csv")
def report(correct_guesses):
    guessed_states_df = pandas.DataFrame(correct_guesses, columns=["state"])
    guessed_states_df.to_csv("guessed_states.csv")
    common_states = set(guessed_states_df['state']).intersection(data['state'])
    data_filtered = data[~data['state'].isin(common_states)]
    data_filtered.to_csv("states_to_study.csv")

count = 0
while guessing:

    answer_state = screen.textinput(title=f"{score}/50 Correct States", prompt="What's another state's name?")
    guess = str(answer_state.title())
    print(guess)
    count += 1
    if guess == "Exit":
        guessing = False
        report(correct_guess)
    #     check if guess is among the 50 states

    check_state = data[data["state"] == guess]
    if not check_state.empty:
        y_coordinate = check_state['y'].iloc[0]
        x_coordinate = check_state['x'].iloc[0]
        GenerateText(guess, x_coordinate, y_coordinate)
        correct_guess.append(guess)
        score += 1
        if count == 50:
            guessing = False
            report(correct_guess)

        print(correct_guess)


