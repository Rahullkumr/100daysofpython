import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('USA states game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('./50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    ans_state = (turtle.textinput(title=f'{len(guessed_states)}/50 States Correct',
                                  prompt="What's another state's name? ")).title()

    if ans_state == 'Exit':
        # states_you_missed.csv
        missed_states_dict = {
            "Missed States": [state for state in all_states if state not in guessed_states]
        }
        df = pd.DataFrame(missed_states_dict)
        df.to_csv('./states_you_missed.csv', mode='w')
        break

    if ans_state in all_states:
        guessed_states.append(ans_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data['state'] == ans_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(ans_state)

