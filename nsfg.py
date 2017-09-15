import thinkstats2
import numpy as np
from collections import defaultdict

def ReadFemPreg(dct_file='2002FemPreg.dct', dat_file='2002FemPreg.dat.gz'):
    """
    This function read female pregnant information 
    :param dct_file: the format of the file documented in 2002FemPreg.dct
    :param dat_file: a gzip-compressed data file in plain text, with fixed width columns
    :return: a dataframe
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    CleanFemPreg(df)
    return df

def CleanFemPreg(df):
    """
    clean the preg data read from dat_file
    :param df: raw data read from dat_file
    :return: None
    """
    df['agepreg'] /= 100.0 # convert centiyear to year
    na_vals = [97, 98, 99] # 97 Not Ascertained, 98 Refused, 99 Don't Know
    df['birthwgt_lb'].replace(na_vals, np.nan, inplace=True)
    df['birthwgt_oz'].replace(na_vals, np.nan, inplace=True)
    df['totalwgt_lb'] = df['birthwgt_lb'] + df['birthwgt_oz'] / 16.0

def MakePregMap(df):
    """
    The function collects the pregnancy data for each respondent
    :param df: DataFrame with pregnancy data
    :return: a dictionary that maps from each case ID to a list of indices
    """
    # caseid is the integer ID of the respondent
    d = defaultdict(list)
    for index, caseid in df['caseid'].iteritems():
        d[caseid].append(index)
    return d

def PregOutcome(oc):
    """
    The function converts digit to readable pregnant outcome
    :param oc: the int or array of pregnant outcomes represented by digit
    :return: string or list of string of the outcomes
    """
    dict_outcome = {1:'LIVE BIRTH', 2:'INDUCED ABORTION', 3:'STILLBIRTH', 4:'MISCARRIAGE',
                       5:'ECTOPIC PREGNANCY', 6:'CURRENT PREGNANCY'}
    if type(oc) == int:
        return dict_outcome[oc]
    else:
        return [dict_outcome[i] for i in oc]

def ReadFemResp(dct_file='2002FemResp.dct', dat_file='2002FemResp.dat.gz'):
    """
    This function read female pregnant information 
    :param dct_file: the format of the file documented in 2002FemPreg.dct
    :param dat_file: a gzip-compressed data file in plain text, with fixed width columns
    :return: a dataframe
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    CleanFemResp(df)
    return df

def CleanFemResp(df):
    """Recodes variables from the respondent frame.

    df: DataFrame
    """
    pass