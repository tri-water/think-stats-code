import math

def CohenEffectSize(group1, group2):
    """
    This function calculates Cohen's d to describe the size of an effect
    :param group1: pandas dataframe
    :param group2: pandas dataframe
    :return: a float
    """
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1*var1 + n2*var2)/(n1 + n2)
    d = diff/math.sqrt(pooled_var)
    return d

def Mode(hist_data):
    """
    This function find the mode from hist_data
    :hist_data: a Hist
    :return: the key appearing most frequently
    """
    dict = hist_data.GetDict()
    return max(hist_data, key=dict.get)

   

