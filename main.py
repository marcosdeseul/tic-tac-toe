def get_list_by_N(n):
    return [None] * n * n

def print_map(n, play_list):
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

def check_all_same_markers_in_row(n, position, play_list, is_player_a):
    ## write unit test for the code below
    # if play_list[position - 1] != None:
    #     return 0
    play_list[position - 1] = is_player_a
    total = 0
    all_verticals = all(
        play_list[index] != None and play_list[index] == is_player_a
        for index in range(position % n - 1, n * n, n)
    )
    all_horizontals = all(
        play_list[index] != None and play_list[index] == is_player_a
        for index in range(n * (position // n), n * (position // n + 1))
    )
    print(list(range(n * (position // n), n * (position // n + 1))))
    if all_verticals:
        total += 1
    if all_horizontals:
        total += 1        
    return total

if __name__ == "__main__":
    print("hello")
