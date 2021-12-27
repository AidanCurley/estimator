# Implementation of the function point analysis estimation model for software development projects


function_points= {
    'User Input': {'L': 3, 'A': 4, 'H': 6, 'Num': 0, 'Total': 0},
    'User Output': {'L': 4, 'A': 5, 'H': 7, 'Num': 0, 'Total': 0},
    'User Inquiries': {'L': 3, 'A': 4, 'H': 6, 'Num': 0, 'Total': 0},
    'Logical Internal Files': {'L': 7, 'A': 10, 'H': 15, 'Num': 0, 'Total': 0},
    'External Interface Files': {'L': 5, 'A': 7, 'H': 10, 'Num': 0, 'Total': 0},
}

characteristics = {
    'Data Communications': {'question': 'How many communication facilities are there to aid in the transfer or '
                                        'exchange of information with the application or system?', 'Influence': 0},
    'Distributed Data Processing': {'question': 'How are distributed data and processing functions handled?',
                                    'Influence': 0},
    'Performance': {'question': 'Did the user require response time or throughput?', 'Influence': 0},
    'Heavily Used Configuration': {'question': 'How heavily used is the current hardware platform where the '
                                               'application will be executed?', 'Influence': 0},
    'Transaction Rate': {'question': 'How frequently are transactions executed daily, weekly, monthly, etc.?',
                         'Influence': 0},
    'On-Line Data Entry': {'question': 'What percentage of the information is entered online?', 'Influence': 0},
    'End-user Efficiency': {'question': 'Was the application designed for end-user efficiency?', 'Influence': 0},
    'Online Update': {'question': 'How many ILFs are updated by online transaction?', 'Influence': 0},
    'Complex Processing': {'question': 'Does the application have extensive logical or mathematical processing?',
                           'Influence': 0},
    'Re-usability': {'question': 'Was the application developed to meet one or many user’s needs?', 'Influence': 0},
    'Installation Ease': {'question': 'How difficult is conversion and installation?', 'Influence': 0},
    'Operational Ease': {'question': 'How effective and/or automated are start-up, back-up, and recovery procedures?',
                         'Influence': 0},
    'Multiple Site': {'question': 'Was the application specifically designed, developed, and supported to be '
                                  'installed at multiple sites for multiple organisations?', 'Influence': 0},
    'Facilitate Change': {'question': 'Was the application specifically designed, developed, and supported to '
                                      'facilitate change?', 'Influence': 0}
}


if __name__ == '__main__':
    for function_point in function_points.keys():
        while True:
            try:
                function_points[function_point]['Num'] = \
                    int(input(f"Please enter the number of {function_point} functions? : "))
                while True:
                    complexity = input(f"Please enter the complexity (L, A, H)? : ").upper()
                    if complexity in ['L', 'A', 'H']:
                        function_points[function_point]['Total'] = \
                            function_points[function_point]['Num'] * function_points[function_point][complexity]
                        break
                break
            except ValueError:
                print('ERROR: Not an integer!')

    unadjusted_fp_count = 0
    for value in function_points.values():
        unadjusted_fp_count += value['Total']
    print(f"\nUnadjusted Function Point Count = {unadjusted_fp_count}\n\n")

    for characteristic in characteristics.keys():
        while True:
            try:
                characteristics[characteristic]['Influence'] = int(input(f"{characteristics[characteristic]['question']} "))
                if -1 < characteristics[characteristic]['Influence'] < 6:
                    break
                else:
                    raise ValueError
            except ValueError:
                print(f'Please enter a value from 0 to 5')

    total_degree_of_influence = 0
    for value in characteristics.values():
        total_degree_of_influence += value['Influence']
    print(f"\nRESULTS\nTotal Degree of Influence = {total_degree_of_influence}")

    value_adjustment_factor = 0.65 + (total_degree_of_influence * 0.01)
    adjusted_fp_count = unadjusted_fp_count * value_adjustment_factor
    print(f"Adjusted Function Point Count = {adjusted_fp_count}\n")

