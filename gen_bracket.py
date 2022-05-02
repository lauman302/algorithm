def gen_bracket(control, open_bracket, close_bracket, prefix):
    if open_bracket == 0 and close_bracket == 0:
        print(prefix)
    else:
        if open_bracket > 0:
            gen_bracket(
                control + 1, open_bracket - 1, close_bracket, prefix + '('
            )
        if (control > 0 and close_bracket > 0):
            gen_bracket(
                control - 1, open_bracket, close_bracket - 1, prefix + ')'
            )


if __name__ == '__main__':
    length = int(input())
    control = 0
    open_bracket = length
    close_bracket = length
    gen_bracket(control, open_bracket, close_bracket, '')
