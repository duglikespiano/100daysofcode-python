import turtle
import pandas

# def get_mouse_click_coordinate(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coordinate)

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = str(screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")).title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        states_name = turtle.Turtle()
        states_name.hideturtle()
        states_name.penup()
        state_data = data[data.state == answer_state]
        states_name.goto(state_data.x.iloc[0], state_data.y.iloc[0])
        states_name.write(state_data.state.item())
# turtle.write(answer_state)
