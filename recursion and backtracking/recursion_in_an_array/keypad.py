# Errors out
codes = [".;:","abc","def" ,"ghi", "jkl", "mno", "pqrs", "tu","vwx","yz"]

def keypad(numbers):
    if len(numbers) ==0:
        bres = list()
        bres.append("")
        return bres
#    573  -- faiith 73 will bring reesults
    char = numbers[0] #5
    ros = numbers[1:] #73

#     Faith
    rres = keypad(ros)

    mres = list()
    for i in range(0, len(codes[int(char)])):
        code = char[i]
        for rstr in rres:
            mres.append(code+rstr)

    return mres


def main():

    numbers = input()
    result = keypad(numbers)
    print(result)

main()
