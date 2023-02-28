# https://www.youtube.com/watch?v=IY0nZLEg6MA&list=PL-Jc9J83PIiEyUGT3S8zPdTMYojwZPLUM&index=16
# not working
def main():
    #  taking the exp as a string as it will conatin brackets and operators, not just numbers. 
    exp = input() 
    operands = list()
    operators = list()

    for i in range(0, len(exp)):
        if exp[i] == "(":
            # push
            operators.append(exp[i])
        elif exp[i].isdigit():
            # push
            operands.append(exp[i])
        elif exp[i] ==")":
            # pop until found "("
            while exp[i] !="(":
                # pop
                op = operators[-1]
                operators = operators[0:-1]
                v1 = operands[-1]
                operands = operands[0:-1]
                v2 = operands[-1]

                val = process(v1, v2, op)
                operands.append(val)
            # pop thhe remaining "("
            operators = operators[0:-1]

            # when will the loop be exited, either len of operators over 
        elif exp[i] =="+" or "-" or "*" or "/":
            if len(operators)>0:
                while(precendence_of_operators(exp[i])<=precendence_of_operators(operators[-1]) or exp[i]!="("):
                    op = operators[-1]
                    operators=operators[0:-1]

                    v1 = operands[-1]
                    operands = operands[0:-1]
                    v2 = operands[-1]

                    val = process(v1, v2, op)
                    operands.append(val)

            operators.append(exp[i])
        else:
            return
        while len(operators)>0:
            # pop
            op = operators[-1]
            operators = operators[0:-1]
            v1 = operands[-1]
            operands = operands[0:-1]
            v2 = operands[-1]

            val = process(v1, v2, op)
            operands.append(val)
    
    final = operands[-1]
    print(final)


def precendence_of_operators(op):
    if op=="+" or op =="-":
        return 1
    elif op =="*" or op== "/":
        return 2
    else:
        return 
def process(v1, v2, op):
    if op=="+":
        return v2+v1
    elif op =="-":
        return v2-v1
    elif op=="*":
        return v2*v1
    elif op =="/":
        return v2/v1
    else:
        return

main()
