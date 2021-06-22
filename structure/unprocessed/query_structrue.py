from pymatgen import Element, MPRester, Composition
import pymatgen.core as mg

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import os
import time

import itertools

os.getcwd()

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

start_time = time.time()
with MPRester() as m:
    data = m.query(criteria='*-*-I', properties=['pretty_formula', 'final_structure', 'icsd_ids', 'spacegroup'])
    df = pd.DataFrame(data=data)

    # 给dataframe传入布尔序列，传入新的dataframe中用于判断
    df_1 = df[df['spacegroup'].isin(['Pm-3m'])]

    print(df_1)
    # data.to_csv('query_result_O.csv')

