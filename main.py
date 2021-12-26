# Implementation of the COCOMO estimation model for software development projects

modes = {
    '1': {'mode': 'Organic', 'a': 2.4, 'b': 1.05, 'c': 2.5, 'd': 0.38},
    '2': {'mode': 'Semi-Detached', 'a': 3, 'b': 1.12, 'c': 2.5, 'd': 0.35},
    '3': {'mode': 'Embedded', 'a': 3.6, 'b': 1.20, 'c': 2.5, 'd': 0.35}
}


def calculate_effort(kloc, mode):
    return modes[mode]['a'] * (kloc ** modes[mode]['b'])


def calculate_time(effort, mode):
    return modes[mode]['c'] * (effort ** modes[mode]['d'])


def calculate_num_developers(effort, time):
    return round(effort/time)


if __name__ == '__main__':
    while True:
        mode_selected = input("What is the mode of development (Type 1, 2 or 3)?\n"
                              "1. Organic\n2. Semi-Detached\n3. Embedded\n")
        if mode_selected in modes.keys():
            break
        else:
            print('Invalid input, please choose 1, 2 or 3')

    while True:
        try:
            loc = int(input('How many lines of code?\n'))
            break
        except ValueError:
            print('Please enter a valid integer.')

    effort_required = calculate_effort(loc/1000, mode_selected)
    time_required = calculate_time(effort_required, mode_selected)
    personnel = calculate_num_developers(effort_required, time_required)

    print(f"\nHere is your COCOMO calculation for {loc} lines of code "
          f"in {modes[mode_selected]['mode']} mode of development:")
    print(f"Effort: {round(effort_required, 2)}\nTime: {round(time_required, 2)}\nDevelopers: {personnel}")
