from ArrayStack import ArrayStack


def postfix_calc():
    expression = input("--> ")
    assignments = {}

    while expression != "done()":
        if "=" in expression:
            var_name_not_stripped, value_str_not_stripped = expression.split("=")
            var_name, value_str = var_name_not_stripped.strip(), value_str_not_stripped.strip()
            value_lst = value_str.split(" ")

            num_stack = ArrayStack()
            for i in range(len(value_lst)):
                if value_lst[i].isdigit():
                    num_stack.push(value_lst[i])
                elif value_lst[i].isalpha():
                    num_stack.push(assignments.get(value_lst[i]))
                else:
                    val1 = int(num_stack.pop())
                    val2 = int(num_stack.pop())
                    if value_lst[i] == "+":
                        total = val1 + val2
                    elif value_lst[i] == "-":
                        total = val2 - val1
                    elif value_lst[i] == "*":
                        total = val1 * val2
                    elif value_lst[i] == "/":
                        total = val2 / val1
                    num_stack.push(total)
            assignments[var_name] = total
            print(var_name)
            expression = input("--> ")

        else:
            expression_lst = expression.split(" ")
            num_stack = ArrayStack()

            for i in range(len(expression_lst)):
                if expression_lst[i].isdigit():
                    num_stack.push(int(expression_lst[i]))
                elif expression_lst[i].isalpha():
                    num_stack.push(assignments.get(expression_lst[i]))
                else:
                    val1 = int(num_stack.pop())
                    val2 = int(num_stack.pop())
                    if expression_lst[i] == "+":
                        total = val1 + val2
                    elif expression_lst[i] == "-":
                        total = val2 - val1
                    elif expression_lst[i] == "*":
                        total = val1 * val2
                    elif expression_lst[i] == "/":
                        total = val2 / val1
                    num_stack.push(total)

            print(num_stack.pop())
            expression = input("--> ")

    return


postfix_calc()
