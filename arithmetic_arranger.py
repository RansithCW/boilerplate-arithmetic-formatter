def arithmetic_arranger(problems, show_answers=False):
    
    prob_no = len(problems)
    # error if more than 5 problems at once
    if prob_no > 5:
        return "Error: Too many problems."
    
    # for each problem given, we will add the number1, number2, operator
    # and width to separate lists.
    # define the lists
    num1_list = []
    operator_list = []
    num2_list = []
    width_list = []
    answers = []
    # add items to lists
    for problem in problems:
        problem = problem.split()
        num1_list.append(problem[0])
        operator_list.append(problem[1])
        num2_list.append(problem[2])
        if problem[1] == '+':
            answers.append(int(problem[0]) + int(problem[2]))
        elif problem[1] == '-':
            answers.append(int(problem[0]) - int(problem[2]))
        try:
            width_list.append(len(str(max(int(problem[0]), int(problem[2])))))
        except ValueError:
            return "Error: Numbers must only contain digits."

    if not all([operator in '+-' for operator in operator_list]):
        return "Error: Operator must be '+' or '-'."
    
    arranged_problems = ''
    for i in range(prob_no):
        arranged_problems += f'  {num1_list[i] : >{width_list[i]}}    '
        
    arranged_problems += '\n'
    for i in range(prob_no):
        arranged_problems += f'{operator_list[i]} {num2_list[i] : >{width_list[i]}}    '
        
    arranged_problems += '\n'
    for i in range(prob_no):
        arranged_problems += '-'*(width_list[i] + 2) + ' '*4
        
    if show_answers:
        arranged_problems += '\n'
        for i in range(prob_no):
            arranged_problems += f' {answers[i] : >{width_list[i] + 1}}    '

    return arranged_problems
