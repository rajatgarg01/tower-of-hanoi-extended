import sys
def tower_hanoi(disk): 
    def TowerOfHanoiWithDirection(n, start_move="blue", direction="clockwise", input_state=None, final_state=None):
        if direction == "clockwise":
            s_pole = 'A'  # Source pole for clockwise
            d_pole = 'B'  # Destination pole for clockwise
            i_pole = 'C'  # Intermediate pole for clockwise
        else:  # direction == "counterclockwise"
            s_pole = 'A'  # Source pole for counterclockwise
            d_pole = 'C'  # Destination pole for counterclockwise
            i_pole = 'B'  # Intermediate pole for counterclockwise
        poles = [s_pole, d_pole, i_pole] if direction == "clockwise" else [s_pole, i_pole, d_pole]

        def move_disk(disk, from_pole, to_pole):
            pass

        def next_pole(current_pole):
            current_idx = poles.index(current_pole)
            return poles[(current_idx + 1) % 3] if direction == "clockwise" else poles[(current_idx - 1) % 3]

        def red_move(state):
            for from_pole, to_pole in [(s_pole, d_pole), (s_pole, i_pole), (d_pole, i_pole), (d_pole, s_pole), (i_pole, s_pole), (i_pole, d_pole)]:
                if state[from_pole] and (not state[to_pole] or state[from_pole][0] < state[to_pole][0]) and state[from_pole][0] != 1:
                    disk = state[from_pole].pop(0)
                    state[to_pole].insert(0, disk)
                    move_disk(disk, from_pole, to_pole)
                    return state
            return state

        def blue_move(smallest_at, state):
            next_pos = next_pole(smallest_at)
            if 1 in state[smallest_at]:
                disk = state[smallest_at].pop(0)
                state[next_pos].insert(0, disk)
                move_disk(1, smallest_at, next_pos)
            return next_pos, state

        if input_state is not None:
            state = {key: value[:] for key, value in input_state.items()}
        else:
            state = {s_pole: list(range(1, n + 1)), d_pole: [], i_pole: []}

        smallest_at = s_pole
        is_blue_turn = start_move == "blue"
        total_moves = (1 << n) - 1
        step_counter = 0

        for move in range(1, total_moves + 2):
            if is_blue_turn:
                smallest_at, state = blue_move(smallest_at, state)
            else:
                state = red_move(state)
            is_blue_turn = not is_blue_turn
            step_counter += 1

            if final_state is not None and state == final_state:
                return "Goal is reached", step_counter

        return "impossible", step_counter

    for start_color in ["blue", "red"]:
        for direction in ["clockwise", "counterclockwise"]:
            keys = ['A', 'B', 'C']
            initial_state = {key: values for key, values in zip(keys, disk[0])}
            final_state = {key: values for key, values in zip(keys, disk[1])}
            
            # Ensure keys are properly initialized
            for key in keys:
                if key not in initial_state:
                    initial_state[key] = []
                if key not in final_state:
                    final_state[key] = []

            n = sum(len(peg) for peg in initial_state.values())
            result, step_counter = TowerOfHanoiWithDirection(n, start_color, direction, initial_state, final_state)
            if result == "Goal is reached":
                return f"{start_color} move and {direction} direction: Total steps: {step_counter}, goal is reached"
    return "impossible"


num_case = int(sys.stdin.readline())
for _ in range(num_case):
    disk = [0, 0]
    disk[0] = [[int(t) for t in s.split()] for s in sys.stdin.readline().split(',')]
    disk[1] = [[int(t) for t in s.split()] for s in sys.stdin.readline().split(',')]
    print(tower_hanoi(disk))
