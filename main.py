import pandas
from turtle import Screen
from name_on_map import NameOnMap

screen = Screen()
name = NameOnMap()


# updating/ creating data frame for both learned and not learned states
def create_data_frame(state_list, have_learned):
    if not have_learned:
        unlearned_data_dict = {"Unlearned States": state_list}
        data_frame = pandas.DataFrame(unlearned_data_dict)
        data_frame.to_csv("Unlearned States.csv", index=False)
    else:
        learned_data_dict = {"Learned States": state_list}
        data_frame = pandas.DataFrame(learned_data_dict)
        data_frame.to_csv("Learned States.csv", index=False)


# updating the map on the base of state name and color (green=learned, red=unlearned)
def update_map(state_name, color):
    l_state = data[data["state"] == state_name]
    x_cor, y_cor = l_state["x"], l_state["y"]
    name.write_state_name_on_map(state_name, x_cor, y_cor, color)


# screen set up
screen.title("U.S. States Game")
screen.setup(725, 491)
screen.bgpic("blank_states_img.gif")

# reading data from 50_states.csv and converting it into list
data = pandas.read_csv("50_states.csv")
all_states = data['state'].to_list()

learned_states = []

# if there is some data already in learned states then update it on the map
screen.tracer(0)
try:
    with open("Learned States.csv") as file:
        learned_states = file.readlines()[1:]
    for i in range(len(learned_states)):
        learned_states[i] = learned_states[i].strip()
    for state in learned_states:
        update_map(state, "green")

except FileNotFoundError:
    pass
screen.update()

# This loop will take the input from user and update the learned states on map user can exit only if he/she type secret exit input
while len(learned_states) <= 50:
    user_input = screen.textinput(title=f"Guess the state {len(learned_states)}/{len(data)}",
                                  prompt="Enter the name of state?")
    if user_input in ["off", "cut", "of", "break", "terminate", "stop", "finish", "exit"] or user_input is None:
        break
    if user_input in learned_states:
        continue
    user_input = user_input.title()
    state = data[data["state"] == user_input]
    if not state.empty:
        learned_states.append(user_input)
        update_map(user_input, "green")

# creating not learned states list
not_learned_states = [state for state in all_states if state not in learned_states]
# creating/updating dataframes of both learned and not learned states
create_data_frame(not_learned_states, False)
create_data_frame(learned_states, True)

# updating map with states that is not learned yet
screen.tracer(0)
for state in not_learned_states:
    update_map(state, "red")
screen.update()

screen.exitonclick()
