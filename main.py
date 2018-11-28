def get_list_by_N(n):
    return [None] * n * n

def create_map_by_N(n, play_list):
    n_format = n * n // 10 + 1
    flexible_format = "{}".format(n_format)
    flexible_format_template = " {:" + flexible_format + "d} "
    flexible_format_template_str = " {:>" + flexible_format + "s} "
    separator = "\n" + "-".join(["-" * (n_format + 2)] * n) + "\n"
    result = ""
    for row in range(0, n):
        for col in range(0, n):
            index = col + row * n
            target = play_list[index]
            if play_list[index] == None:
                result += flexible_format_template.format(index + 1)
            else:
                result += flexible_format_template_str.format("o" if target else "x")
            if col < n-1:
                result += "|"
        if row < n-1:
            result += separator
    return result

def count_max_n_markers_in_rows(valid_indexes, play_list, is_player_a):
    result = 0
    for index in valid_indexes:
        if play_list[index] == is_player_a:
            result += 1
        else:
            result = 0
        if result >= 3:
            break
    return result

def get_n_vertical_marker_from_position(n, is_player_a, play_list, position_to_index):
    possible_indexes = [
        index for index
        in range(position_to_index - 2 * n, position_to_index + 2 * n + 1, n)
        if index >= 0 and index < n * n
    ]
    return count_max_n_markers_in_rows(possible_indexes, play_list, is_player_a)



def get_n_horizontal_marker_from_position(n, is_player_a, play_list, position_to_index):
    left_end_margin = 2 if position_to_index % n > 2 else position_to_index % n
    right_end_margin = 2 if n - position_to_index % n > 2 else n - position_to_index % n
    possible_indexes = [
        index for index
        in range(position_to_index - left_end_margin, position_to_index + right_end_margin + 1, 1)
        if index >= 0 and index < n * n
    ]
    return count_max_n_markers_in_rows(possible_indexes, play_list, is_player_a)

def get_n_left_up_diagonal_marker_from_position(n, is_player_a, play_list, position_to_index):
    possible_indexes = [
        index for index
        in range(position_to_index - 2 * (n+1), position_to_index + 2 * (n+1) + 1, n + 1)
        if index >= 0 and index < n * n
    ]
    return count_max_n_markers_in_rows(possible_indexes, play_list, is_player_a)

def get_n_right_up_diagonal_marker_from_position(n, is_player_a, play_list, position_to_index):
    possible_indexes = [
        index for index
        in range(position_to_index - 2 * (n-1), position_to_index + 2 * (n-1) + 1, n - 1)
        if index >= 2 and index < n * n - 2
    ]
    return count_max_n_markers_in_rows(possible_indexes, play_list, is_player_a)

def check_all_same_markers_in_row(n, position, play_list, is_player_a):

    alreadyOccupied = play_list[position - 1] != None
    if alreadyOccupied:
        return 0

    position_to_index = position - 1
    play_list[position_to_index] = is_player_a
    total = 0

    # vericals
    n_verticals = get_n_vertical_marker_from_position(
        n,
        is_player_a,
        play_list,
        position_to_index
    )
    if n_verticals >= 3:
        total += 1

    # horizontals
    n_horizontals = get_n_horizontal_marker_from_position(
        n,
        is_player_a,
        play_list,
        position_to_index
    )
    if n_horizontals >= 3:
        total += 1

    # right-up diagonals
    n_right_up_diagonals = get_n_right_up_diagonal_marker_from_position(
        n,
        is_player_a,
        play_list,
        position_to_index
    )
    if n_right_up_diagonals >= 3:
        total += 1

    # left-up diagonals
    n_left_up_diagonals = get_n_left_up_diagonal_marker_from_position(
        n,
        is_player_a,
        play_list,
        position_to_index
    )
    if n_left_up_diagonals >= 3:
        total += 1
    return total

if __name__ == "__main__":
    playerA = input("type Player A name: ")
    playerB = input("type Player B name: ")
    n = int(input("type map size: "))
    play_list = get_list_by_N(n)

    inGame = True
    print(create_map_by_N(n, play_list))
    while inGame:
        position = int(input(playerA + ", choose a box to place an 'o' into: \n>> "))
        canWinA = check_all_same_markers_in_row(n, position, play_list, True) > 0

        print(create_map_by_N(n, play_list))
        if canWinA:
            print("Congratulations {}! You have won.".format(playerA))
            break

        position = int(input(playerB + ", choose a box to place an 'x' into: \n>> "))
        canWinB = check_all_same_markers_in_row(n, position, play_list, False) > 0

        print(create_map_by_N(n, play_list))
        if canWinB:
            print("Congratulations {}! You have won.".format(playerB))
            break
