import os

def read_f_one(filename):
    a = []
    temp = ''
    f = open(filename, encoding='utf-8')

    for i in f:
        for j in i:
            if j != ' ':
                temp += j
            else:
                a.append(temp)
                temp = ''
    f.close()
    return(a)

def read_f_two(filename): 
    f = open(filename)
    m = []
    ma = []
    mm = []
    temp = ''

    for i in f:
        for j in i:
            if j != ' ':
                temp += j

            else:
                m.append(float(temp))
                temp = ''

            if j == '\n':
                if m == []:
                    mm.append(ma)
                    ma = []
                    continue
                ma.append(m)
                m = []

    f.close()
    return (mm)

def overall_satisfaction(expert_opinions):
    temp = []
    answer = []

    for i in range(len(expert_opinions[0])):
        temp.append(0)
    
    answer.append(temp)

    for j in expert_opinions:
        answer.append(j)
    
    for k in range(len(answer)):
        answer[k].append(0)
    
    for m in range(len(answer)):
        for u in range(len(answer[m])):
            if not(m == u):
                answer[m][u] = 1 / answer[u][m]
            else:
                answer[m][u] = 1
    return answer

def comparison_of_options(characteristics):
    temp_a = []
    temp_b = []
    answer = []

    for i in range(len(characteristics)):
        for k in range(len(characteristics[i])):    
            for j in range(len(characteristics[i])):
                temp_a.append((characteristics[i][k]) / (characteristics[i][j]))
            temp_b.append(temp_a)
            temp_a = []
        answer.append(temp_b)
        temp_b = []
    
    return answer

def alpha(comparison_of_options):
    temp = 0
    temp_a = []
    C = []

    for i in comparison_of_options:
        for j in i:
            for k in j:
                temp += k
            temp_a.append(temp / len(j))
            temp = 0
        C.append(temp_a)
        temp_a = []

    return C   

#Priority vectors for level 3
def pvl_3(alpha):
    temp_i = 0
    temp_a = []
    answer = []
    for i in range(len(alpha)):
        for k in range(len(alpha[i])):
            for j in range(len(alpha[i])):
                temp_i += alpha[i][j]
            temp_a.append(alpha[i][k] / temp_i)
            temp_i = 0
        answer.append(temp_a)
        temp_a = []

    return(answer)

def main():
    names = read_f_one(str(os.getcwd()) + "\\names.txt")
    inp = read_f_two(str(os.getcwd()) + "\\inp.txt")
    expert = read_f_two(str(os.getcwd()) + "\\expert.txt")

    inp = inp[0]
    expert = expert[0]

    print("\n-- Сравнительные характеристики оборудования --")
    for i in range(len(names)):
        print(names[i], end = '\t|')
        for j in inp[i]:
            print(j, end = '\t|')
        print()
    i = j = 0
    overall = overall_satisfaction(expert)
    print("\n\n-- Общее удовлетворение оборудованием --")
    
    for i in range(len(names)):
        print(names[i] + " \t(" + str(i+1) + ")", end = '\t| ')
        for j in overall[i]:
            print('{0:.2f}'.format(j), end = ' \t| ')
        print()
    i = j = 0

    comparison = comparison_of_options(inp)
    
    for i in range(len(comparison)):
        print("\n\n-- Сравнение вариантов с точки зрения " + str(names[i]) + " --")
        for j in range(len(comparison[i])):
            print( chr(97+int(j)), end = '\t')
            for k in range(len(comparison[i][j])):
                print('{0:.2f}'.format(comparison[i][j][k]), end = ' |\t ')
            print()
    i = j = 0

    al = alpha(comparison)
    a = []
    temp = 1
    print()

    for i in range(len(al)):
        for j in range(len(al[i])):
            temp *= al[i][j]
        a.append(pow(temp, (1 / 4)))
        print("α"+ str(i+1) +" = " + str(temp))
        temp = 1
    
    print("\nα  = " + str(sum(a)))
    i = j = 0

    print("-- Общее удовлетворение оборудованием --")
    for i in range(len(names)):
        print(names[i] + "\tx" + str(i+1) + " = " + str(  a[i] / sum(a) ))
    
    synthesis = pvl_3(al)
    synthesis = list(zip(*synthesis))

    print("\n-- Вектора приоритетов для уровня 3 --")
    for n in names:
        print("\t" + n, end=' ')

    for i in range(len(synthesis)):
        print("\n" + str(chr(65 + i)), end = ' | \t')
        for j in synthesis[i]:
            print('{0:.4f}'.format(j), end = '\t\t')
    i = j = 0

    answer = 0
    print("\n\n -- Глобальные приоритеты --",end = '')
    for i in range(len(synthesis)):
        print("\nK" + str(chr(65 + i)), end = ' = ')
        for j in range(len(synthesis[i])):
            print(" + " + str('{0:.2f}'.format(synthesis[i][j])) + " * " + str('{0:.2f}'.format(a[j] / sum(a))), end = '')
            answer += synthesis[i][j] * (a[j] / sum(a))
        print(" = " + str('{0:.4f}'.format(answer)), end = '')
        answer = 0
    i = j = 0
    input()

if __name__ == '__main__':
    main()