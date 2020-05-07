## import modules here
import numpy as np
def dot_product(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

################# Question 1 #################
def complete_link(data, cluster):
    n = data.shape[0]
    one_dim = []
    for i in range(n):
        for j in range(i + 1, n):
            one_dim.append(data[i][j])
    max_num = max(one_dim)
    flag = 0
    for i in range(n):
        for j in range(i + 1, n):
            if data[i][j] == max_num:
                c = [i, j]
                flag = 1
                break
        if flag:
            break
    clu = [cluster[c[0]], cluster[c[1]]]
    cluster.remove(clu[0])
    cluster.remove(clu[1])
    cluster.append(str(clu[0]) + ' ' + str(clu[1]))
    return c, cluster


def update_matrix(data, c):
    n = data.shape[0]
    new_data = []
    for i in range(n):
        if i not in c:
            temp = []
            for j in range(n):
                if j not in c:
                    temp.append(data[i][j])
            temp.append(min([data[i][c[0]], data[i][c[1]]]))
            new_data.append(temp)
    after_c = []
    for i in range(len(new_data)):
        after_c.append(new_data[i][-1])
    after_c.append(float(1))
    new_data.append(after_c)
    new_data = np.array(new_data)
    return new_data


def hc(data, k):# do not change the heading of the function
    result_dic = {}
    point_num = len(data)
    sim_matrix = []
    result = []
    cluster = [i for i in range(point_num)]
    for i in range(point_num):
        sim = []
        for j in range(point_num):
            sim.append(dot_product(data[i], data[j]))
        sim_matrix.append(sim)
    sim_matrix = np.array(sim_matrix)
    if k != 0:
        if k == 1:
            result = [0] * len(cluster)
            return result
        if 1 < k <= len(cluster):
            while len(cluster) != k:
                c, cluster = complete_link(sim_matrix, cluster)
                sim_matrix = update_matrix(sim_matrix, c)
        count = 0
        for i in cluster:
            if isinstance(i, str):
                split_list = i.split(' ')
                for j in split_list:
                    result_dic[int(j)] = count
                count += 1
        for i in cluster:
            if isinstance(i, int):
                result_dic[i] = count
                count += 1
        for i in sorted(result_dic):
            result.append(result_dic[i])
    return result


