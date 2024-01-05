def arithmetic_arranger(problems, show_answers=False):

    prob_no = len(problems)
    # error if more than 5 problems at once
    if prob_no > 5:
        return "Error: Too many problems."
    
    # For each problem given, we will add the number1, number2, operator
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
        if len(problem[0]) > 4 or len(problem[2]) > 4:
          return 'Error: Numbers cannot be more than four digits.'
        num1_list.append(problem[0])
        operator_list.append(problem[1])
        num2_list.append(problem[2])
        # width is the length of the longer number, which is essentially the larger number. Just using max() on the two integers gives the number with max starting digit, but we want the larger number, so max() of int() of each is taken 
        try:
            width_list.append(len(str(max(int(problem[0]), int(problem[2])))))
        except ValueError:
            return "Error: Numbers must only contain digits."
        if problem[1] == '+':
            answers.append(int(problem[0]) + int(problem[2]))
        elif problem[1] == '-':
            answers.append(int(problem[0]) - int(problem[2]))
    
    if not all([operator in '+-' for operator in operator_list]):
        return "Error: Operator must be '+' or '-'."
    
    arranged_problems = ''
  
    for i in range(prob_no):
        arranged_problems += f'  {num1_list[i] : >{width_list[i]}}'
        if i < prob_no - 1:
            arranged_problems += ' '*4
    arranged_problems += '\n'
  
    for i in range(prob_no):
        arranged_problems += f'{operator_list[i]} {num2_list[i] : >{width_list[i]}}'
        if i < prob_no - 1:
            arranged_problems += ' '*4
    arranged_problems += '\n'
  
    for i in range(prob_no):
        arranged_problems += '-'*(width_list[i] + 2) 
        if i < prob_no - 1:
            arranged_problems += ' '*4
    
    if show_answers:
        arranged_problems += '\n'
        for i in range(prob_no):
            arranged_problems += f' {answers[i] : >{width_list[i] + 1}}'
            if i < prob_no - 1:
                arranged_problems += ' '*4
    
    return arranged_problems
    
