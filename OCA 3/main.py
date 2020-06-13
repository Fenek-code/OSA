decryption = []
def read_f_one(filename):
    a = []
    temp = ''
    f = open(filename)

    for i in f:
        for j in i:
            if j != ' ':
                temp += j
            else:
                a.append(float(temp))
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
                    decryption.append(len(ma))
                    ma = []
                    continue
                ma.append(m)
                m = []

    f.close()
    return (mm)

def read_f_two_G(filename): 
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
                    ma = list(zip(*ma))
                    mm.append(ma)
                    decryption.append(len(ma))
                    ma = []
                    continue
                ma.append(m)
                m = []

    f.close()
    return (mm)

def write_f_two(mas, filename):
    f = open(filename, 'w')
    answer = ''
    for i in mas:
        for j in i:
            answer += '{0:.2f}'.format(j) + " "
        answer += '\n'
    f.write(answer)
    f.close()
            
def processing(a_p, b_p):
    c_p = []

    for i in b_p:
        temp = 0
        counter = 0

        while (counter < len(i)):
            temp += i[counter] * a_p[counter]

            print('{0:.2f}'.format(i[counter]) + " * " + '{0:.2f}'.format(a_p[counter]) + " + ", end = '' )
            counter += 1

        c_p.append(temp)
        print(" = " + '{0:.2f}'.format(temp))

    summ = sum(c_p)
    print("Σ = " + '{0:.2f}'.format(summ))
    counter = 0
    while (counter < len(c_p)):
        c_p[counter] = c_p[counter] / summ
        counter += 1

    return c_p            

def max_elem(arr):
    s = 0
    for i in range(len(arr)):
        if arr[i] > s:
            s = arr[i]
            maximum = i
    return maximum

def wr_ar(a, foreword):
    counter = 0
    for i in a:
        if foreword:
            print(chr(97+int(counter)), end = '')
            counter += 1
        print (" " + str(i) + "; ")



def main():

    forgraf = []
    a = read_f_one("C:\\Users\\litvi\\OneDrive\\University\\2nd course\\Semester II\\OCA\\OCA 3\\a.txt")
    b = read_f_two("C:\\Users\\litvi\\OneDrive\\University\\2nd course\\Semester II\\OCA\\OCA 3\\net.txt")
    c = read_f_two_G("C:\\Users\\litvi\\OneDrive\\University\\2nd course\\Semester II\\OCA\\OCA 3\\net.txt")
    
    array = []
    array.append(a)
    counter = 0

    for i in range(len(c)):
        for j in c[i]:
            forgraf.append(j)
        


    while(counter < len(b)):
        a = processing(array[counter], b[counter]) 
        array.append( a )
        counter += 1
    
    wr_ar(array, True)
    influence = max_elem(array[counter])
    print("Максимальное влияние имеет " + chr(97+int(len(array)-1)) + str(influence+1) + " со значением " + '{0:.2f}'.format(array[counter][influence]))
    write_f_two(array, "odds.txt")
    
    print("---доп---\nХотите увидить граф? (Y/N)")
    outp = input()
    if (outp.lower() == "y" ):
        import graph_output
        graph_output.result(array, forgraf, decryption)

if __name__ == "__main__":
    main()
    