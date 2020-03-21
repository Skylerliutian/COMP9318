## import modules here
import pandas as pd
import numpy as np
import helper

def read_data(filename):
    df = pd.read_csv(filename, sep='\t')
    return (df)
# ################### Question 1 ###################
def buc_single(prefix, data, column):
    length = column - 1
    result = []
    iter_time = 2 ** length
    for i in range(iter_time):
        copy = [i for i in data]
        for j in range(length):
            if i % (2 ** (length - j)) > (2 ** (length - j - 1) - 1):
                copy[j] = 'ALL'
        result.append(prefix + copy)
    return result


def buc_rec_general(df, result, prefix=[]):
    dims = df.shape[1]
    rows = df.shape[0]
    pre_cp = [i for i in prefix]
    if dims == 1:
        input_sum = sum(helper.project_data(df, 0))
        pre_cp.append(input_sum)
        result.append(pre_cp)
    elif rows == 1:
        s_tuple = list(df.iloc[0])
        tuples = buc_single(pre_cp, s_tuple, dims)
        # tuples 是[[],[]....]形式
        result += tuples
    else:
        dim0_vals = set(helper.project_data(df, 0).values)
        for dim0_v in dim0_vals:
            pre_cp.append(dim0_v)
            sub_data = helper.slice_data_dim0(df, dim0_v)
            buc_rec_general(sub_data, result, pre_cp)
            pre_cp = [i for i in prefix]
        pre_cp.append('ALL')
        sub_data = helper.remove_first_dim(df)
        buc_rec_general(sub_data, result, pre_cp)
    return result

def buc_rec_optimized(df):# do not change the heading of the function
    result = []
    column_name = df.columns.values
    result = buc_rec_general(df, result)
    final_result = pd.DataFrame(result, columns=column_name)
    return final_result

input_data = read_data('./asset/i_.txt')
output = buc_rec_optimized(input_data)
print(output)