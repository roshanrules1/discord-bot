from math_calc import calc_string

calc = [i for i in input("enter arg:")]
sub_list = []
for i in range(len(calc)):
    if calc[i] == "(":
        for j in range(len(calc[i + 1 :])):
            if calc[j] != ")":
                sub_list.append(calc[j])
            else:
                break
        if "(" in sub_list:
            sub_list.remove("(")
        elif ")" in sub_list:
            sub_list.remove(")")
for i in range(len(calc)):
    for j in range(len(sub_list)):
        if sub_list[j] == calc[i]:
            calc.remove(calc[i])
        elif calc[i] == "(":
            calc.remove("(")
        elif calc[i] == ")":
            calc.remove(")")
print(sub_list, "\n", calc)
