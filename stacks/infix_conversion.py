# https://www.youtube.com/watch?v=Nfui0rgbQe8&list=PL-Jc9J83PIiEyUGT3S8zPdTMYojwZPLUM&index=17

def main():

    exp = input()
    prefix = list()
    postfix = list()
    operators = list()

    for i in range(0, len(exp)):
            if exp[i] == "(":
                # push
                operators.append(exp[i])
            elif exp[i].isdigit():
                # push
                prefix.append(exp[i])
                postfix.append(exp[i])
            elif exp[i] ==")":
                # pop until found "("
                while exp[i] !="(":
                    # pop
                    op = operators[-1]
                    operators = operators[0:-1]
                    
                    v1 = prefix[-1]
                    prefix = prefix[0:-1]
                    v2 = prefix[-1]
                    prefix.append(op+v2+v1)

                    v1_post = postfix[-1]
                    postfix = postfix[0:-1]
                    v2_post = postfix[-1]

                    postfix.append(op+v2_post+v1_post)
                # pop thhe remaining "("
                operators = operators[0:-1]

                # when will the loop be exited, either len of operators over 
            elif exp[i] =="+" or "-" or "*" or "/":
                if len(operators)>0:
                    while(precendence_of_operators(exp[i])<=precendence_of_operators(operators[-1]) or exp[i]!="("):
                        op = operators[-1]
                        operators=operators[0:-1]

                        v1 = prefix[-1]
                        prefix = prefix[0:-1]
                        v2 = prefix[-1]
                        prefix.append(op+v2+v1)

                        v1_post = postfix[-1]
                        postfix = postfix[0:-1]
                        v2_post = postfix[-1]

                        prefix.append(op+v2_post+v1_post)

                operators.append(exp[i])
            else:
                return
            while len(operators)>0:
                # pop
                v1 = prefix[-1]
                prefix = prefix[0:-1]
                v2 = prefix[-1]
                prefix.append(op+v2+v1)

                v1_post = postfix[-1]
                postfix = postfix[0:-1]
                v2_post = postfix[-1]

                postfix.append(op+v2_post+v1_post)
              
            print("prefix", prefix[-1])
            print("postfix", postfix[-1])

def precendence_of_operators(op):
    if op=="+" or op =="-":
        return 1
    elif op =="*" or op== "/":
        return 2
    else:
        return 

main()