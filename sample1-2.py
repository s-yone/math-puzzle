#1000 9999
##1 2 3 4
# + - X /
import re
calc = ["+","-","*","/",""]
def num_reverse(arr):
    result = []
    for i in reversed(arr):
        result.append(i)
    return result

meet_arr = []
for num in range(1000,10000):
    target = list(str(num))
    for one in calc:
        for two in calc:
            for three in calc:
                if one is not None and two is not None and three is not None:
                    formula = str(target[0]) + one + target[1] + two + target[2] + three + target[3]      
                    if not formula.find('/0') >= 1 and re.search(r'0[0-9]',formula) is None and len(formula) != 4:
                    #print(eval("1 %s 1"%one))
                    #number = eval("int(target[0])  int(target[2])")
                        number = eval(formula)
                        #number = eval("%d %s %d %s %d %s %d"%(int(target[0]),one,int(target[1]),two,int(target[2]),three,int(target[3])))
                        if number == int(''.join(num_reverse(target))):
                            print("true")
                            print(formula)
                            #print(formula)
                            meet_arr.append(number)
                    formura = ""
                    number=""

print(meet_arr)
