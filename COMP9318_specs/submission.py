import scipy
import numpy as np
import pickle
import time


def k_means_star(vector, centroids, max_iter, k=256):
    for _ in range(max_iter):
        x = []
        for v in vector:
            l1_dis = abs(centroids - v).sum(axis=1)
            x.append(l1_dis)
        C = np.array(x).argmin(axis=1)
        for i in range(k):
            cluster = vector[np.where(C == i)]
            if cluster.size != 0:
                centroids[i] = np.median(cluster, 0)
    return centroids


def last_k_m(vector, centroids):
    x = []
    for v in vector:
        l1_dis = abs(centroids - v).sum(axis=1)
        x.append(l1_dis)
    C = np.array(x).argmin(axis=1)
    return C


def pq(data, P, init_centroids, max_iter):
    N = data.shape[0]
    M = data.shape[1]
    data = data.reshape(N, P, int(M/P)).transpose(1,0,2)
    codebooks = []
    codes = []
    for i in range(P):
        codebooks.append(k_means_star(data[i], init_centroids[i], max_iter))
        codes.append(last_k_m(data[i], codebooks[-1]))
    codebooks = np.array(codebooks)
    codes = np.array(codes).transpose().astype(np.uint8)
    return codebooks, codes


def add_to_pq(matrix, l):
    e = [matrix[i][l[i]] for i in range(len(l))]
    return np.array(e).sum(axis=0)[-1]


def query(queries, codebooks, codes, T):
    P = codebooks.shape[0]
    result = []
    for q in range(queries.shape[0]):
        res = []
        dis_matrix = []
        query = queries[q].reshape(P, -1)
        for i in range(P):
            dis = list(abs(codebooks[i] - query[i]).sum(axis=1))
            dis_matrix.append(dis)
        all_dis = []
        for points in codes:
            sum = 0
            for i, n in enumerate(points):
                sum += dis_matrix[i][n]
            all_dis.append(sum)
        all_dis = np.array(all_dis)
        ordered = all_dis.argsort()
        for i in ordered:
            if len(res) < T:
                res.append(i)
            else:
                if (codes[i] == codes[res[-1]]).all():
                    res.append(i)
                else:
                    break
        result.append(set(res))
    return result

# def convert_codes(codes):
#     dic_codes = {}
#     for index, code in enumerate(codes):
#         if tuple(code) in dic_codes:
#             dic_codes[tuple(code)].append(index)
#         else:
#             dic_codes[tuple(code)] = [index]
#     return dic_codes
#
#
# def query(queries, codebooks, codes, T):
#     good_centroids = list(set([i[0] for i in codes] + [i[1] for i in codes]))
#     P = codebooks.shape[0]
#     result = []
#     dic_codes = convert_codes(codes)
#     for q in range(queries.shape[0]):
#         res = set()
#         query = queries[q].reshape(P, -1)
#         dis_matrix = []
#         for i in range(P):
#             dis = list(abs(codebooks[i] - query[i]).sum(axis=1))
#             dis_matrix.append(dis)
#         gd_cen_matrix = []
#         for item in dis_matrix:
#             temp = []
#             for index, dis in enumerate(item):
#                 if index in good_centroids:
#                     temp.append([index, dis])
#             temp.sort(key=lambda x: x[1])
#             gd_cen_matrix.append(temp)
#         traversed = set()
#         first = [0] * len(gd_cen_matrix)
#         pqueue = []
#         e = [gd_cen_matrix[i][first[i]] for i in range(len(first))]
#         first.append(np.array(e).sum(axis=0)[-1])
#         pqueue.append(first)
#
#         while len(res) < T:
#
#             pop_e = pqueue.pop()[:-1]
#             temp = [gd_cen_matrix[i][pop_e[i]][0] for i in range(len(pop_e))]
#             if tuple(temp) in dic_codes:
#                 for i in dic_codes[tuple(temp)]:
#                     res.add(i)
#             traversed.add(tuple(pop_e))
#             # start = time.time()
#             for i in range(len(pop_e)):
#                 new_p = [j for j in pop_e]
#                 new_p[i] += 1
#                 all_zero_flag = 1
#                 all_traversed = 1
#
#                 for j in range(len(new_p)):
#                     if i != j:
#                         if new_p[j] != 0:
#                             all_zero_flag = 0
#                         x = [n for n in new_p]
#                         x[j] -= 1
#                         if tuple(x) not in traversed:
#                             all_traversed = 0
#
#                 if all_zero_flag or all_traversed:
#                     pqueue.append(new_p + [add_to_pq(gd_cen_matrix, new_p)])
#             # end = time.time()
#             # print(end - start)
#             pqueue.sort(key=lambda x: x[-1], reverse=True)
#         result.append(res)
#     return result
#

# with open('./example/Query_File_1', 'rb') as f:
#     queries = pickle.load(f, encoding='bytes')
# with open('./example/Codes_1', 'rb') as f:
#     codes = pickle.load(f, encoding='bytes')
# with open('./example/Codebooks_1', 'rb') as f:
#     codebooks = pickle.load(f, encoding='bytes')
# with open('./example/Candidates_1', 'rb') as f:
#     c = pickle.load(f, encoding='bytes')
# start = time.time()
# # queries = queries[:1]
# candidates = query(queries, codebooks, codes, T=10)
# end = time.time()
# time_cost_2 = end - start
#
# print("part 2: ", time_cost_2)
# print(c)
# print(candidates)

# with open('./toy_example/Data_File', 'rb') as f:
#     Data_File = pickle.load(f, encoding='bytes')
# with open('./toy_example/Centroids_File', 'rb') as f:
#     Centroids_File = pickle.load(f, encoding='bytes')
# data = Data_File
# centroids = Centroids_File
# start = time.time()
# codebooks, codes = pq(data, P=2, init_centroids=centroids, max_iter=20)
#
# end = time.time()
# time_cost_1 = end - start
# print("part1: ", time_cost_1)
#
#
# with open('./toy_example/Query_File', 'rb') as f:
#     queries = pickle.load(f, encoding='bytes')
#
#
# start = time.time()
#
# candidates = query(queries, codebooks, codes, T=10)
# end = time.time()
# time_cost_2 = end - start
#
# print("part 2: ", time_cost_2)
#
# print(candidates)
# # print(codes, codebook)








