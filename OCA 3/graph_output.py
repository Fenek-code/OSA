def make_square(array):
    temp = []
    answer = []
    maxlen = len(array)

    for i in array:
        if len(i) > maxlen:
            maxlen = len(i)
    
    counter = 0
    for i in array:
        for j in i:
            temp.append(j)
        while (len(temp) < maxlen):
            temp.append(0)
        answer.append(temp)
        temp = []

    while len(answer) < maxlen:

        for i in range(maxlen):
            temp.append(0)
        answer.append(temp)
        temp = []
    
    return answer

def result(point, lines, decryption):
    
    maxpoint = len(lines)
    for i in lines:
        if len(i) > maxpoint:
            maxpoint = len(i)

    n = 0
    m = 0
    k = 0
    h = 0
    past = decryption[k]-1
    for i in lines:
        temp = []

        for p in range(past):
            temp.append(0)
            n += 1

        if len(i) < maxpoint:
            for j in i:
                temp.append((j))

        lines[h] = temp
        if h >= past:
            past += decryption[k]-1
            k += 1
        h+=1

        

    if len(lines) < maxpoint:
        for i in range(maxpoint - len(lines)):
            temp = []
            for j in range(maxpoint):
                temp.append(0)
            lines.append(temp)


    max_x = 1000
    max_y = 1000
    pos = {}
    counter = 0
    n = 0
    for i in point:
        m = 0

        for j in i:
            part_x = (max_x / (len(i)+1))
            part_y = (max_y / (len(point)+1))
            pos[counter]= ((part_x * (m+1)), max_y - (part_y * (n+1)) )
            counter += 1
            m += 1

        n += 1

    import matplotlib.pyplot as plt
    import networkx as nx
    import numpy as np

    lines = make_square(lines)
    lines = np.matrix(lines)
    G = nx.from_numpy_matrix(lines, create_using=nx.DiGraph)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_nodes(G, pos, node_size=500, nodelist=range(len(pos)), node_color='g')

    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    nx.draw(G, pos)
    plt.show()

