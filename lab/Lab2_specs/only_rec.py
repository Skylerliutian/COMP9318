import pandas as pd
import numpy as np
import helper


def read_data(filename):
    df = pd.read_csv(filename, sep='\t')
    return (df)


def buc(df, result, prefix=[]):
    dims = df.shape[1]
    pre_cp = [i for i in prefix]
    if dims == 1:
        pre_cp.append(sum(helper.project_data(df, 0)))
        result.append(pre_cp)
    else:
        dim0_vals = set(helper.project_data(df, 0).values)
        for i in dim0_vals:
            pre_cp.append(i)
            rest_data = helper.slice_data_dim0(df, i)
            buc(rest_data, result, pre_cp)
            pre_cp = [i for i in prefix]
        pre_cp.append('ALL')
        rest_data = helper.remove_first_dim(df)
        buc(rest_data, result, pre_cp)
    return result

input_data = read_data('./asset/i_.txt')
result = buc(input_data, [])
col_name = input_data.columns.values
output = pd.DataFrame(result, columns=col_name)
print(output)