def generate_knight_rules(n):
    for i in range(0, n):
        for j in range(0, n):
            if (i-2) >= 0:
                if (j-2) >= 0:
                    print_rule(n, i, j, i-1, j-2)
                    print_rule(n, i, j, i-2, j-1)
                elif (j-1) >= 0:
                    print_rule(n, i, j, i-2, j-1)

                if (j+2) < n:
                    print_rule(n, i, j, i-2, j+1)
                    print_rule(n, i, j, i-1, j+2)
                elif (j+1) < n:
                    print_rule(n, i, j, i-2, j+1)
            elif (i-1) >= 0:
                if (j-2) >= 0:
                    print_rule(n, i, j, i-1, j-2)
                if (j+2) < n:
                    print_rule(n, i, j, i-1, j+2)

            if (i+2) < n:
                if (j - 2) >= 0:
                    print_rule(n, i, j, i + 1, j - 2)
                    print_rule(n, i, j, i + 2, j - 1)
                elif (j - 1) >= 0:
                    print_rule(n, i, j, i + 2, j - 1)

                if (j+2) < n:
                    print_rule(n, i, j, i+2, j+1)
                    print_rule(n, i, j, i+1, j+2)
                elif (j+1) < n:
                    print_rule(n, i, j, i+2, j+1)
            elif (i+1) < n:
                if (j-2) >= 0:
                    print_rule(n, i, j, i+1, j-2)
                if (j+2) < n:
                    print_rule(n, i, j, i+1, j+2)


def generate_bishop_rules(n):
    for i in range(0, n):
        for j in range(0, n):
            [m, k] = [i-1, j-1]
            while m >= 0 and k >= 0:
                print_rule(n, i, j, m, k)
                m -= 1
                k -= 1

            [m, k] = [i + 1, j + 1]
            while m < n and k < n:
                print_rule(n, i, j, m, k)
                m += 1
                k += 1

            [m, k] = [i + 1, j - 1]
            while m < n and k >= 0:
                print_rule(n, i, j, m, k)
                m += 1
                k -= 1

            [m, k] = [i - 1, j + 1]
            while m >= 0 and k < n:
                print_rule(n, i, j, m, k)
                m -= 1
                k += 1


rules_counter = 0


def print_rule(n, i_curr, j_curr, i_next, j_next):
    global rules_counter
    rules_counter += 1
    print(str(i_curr*n + j_curr + 1) + ' -> ' + str(i_next*n + j_next + 1))


def run_program():
    n = int(input('Enter chess board size: '))
    figure = input('Generate rules for Knight (k) or Bishop (b): ')

    if figure == 'k':
        print('Production rules for Knight: ')
        generate_knight_rules(n)
    elif figure == 'b':
        print('Production rules for Bishop: ')
        generate_bishop_rules(n)
    else:
        print('Incorrect input. Please enter (k) or (b)')

    print('Total rules quantity: ' + str(rules_counter))


run_program()
