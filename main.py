# my solution
# import turtle
# import pandas
#
# screen = turtle.Screen()
# screen.title("U.S States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
# # how to define coordinates by clicking on screen
# # def get_mouse_click_coor(x, y):
# #     print(x, y)
# # turtle.onscreenclick(get_mouse_click_coor)
# correct_guess = 0
# game = True
# data = pandas.read_csv("50_states.csv")
# answer_list =[]
#
# def write_state(correct_answer, x, y):
#     new_state = turtle.Turtle()
#     new_state.penup()
#     new_state.hideturtle()
#     new_state.goto(x, y)
#     new_state.write(arg=f"{correct_answer}", align="center", font=("Courier", 10, "normal"))
#
# while game:
#     answer_state = screen.textinput(title=f"{correct_guess}/50 States Correct", prompt="What's another state's name?")
#     answer_state = answer_state.title()
#     search_answer = data[data.state == answer_state]
#     if search_answer.empty:
#         pass
#     else:
#         correct_answer = search_answer.state
#         correct_answer = correct_answer.item()
#         x = int(search_answer.x)
#         y = int(search_answer.y)
#         write_state(correct_answer, x, y)
#         if correct_answer not in answer_list:
#             correct_guess += 1
#             answer_list.append(correct_answer)
#
# turtle.mainloop()

# key
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        # not in key/prevent counting already guessed
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # or answer_state
        t.write(state_data.state.item())

screen.exitonclick()