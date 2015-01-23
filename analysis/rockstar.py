# Author: Lucas A. Bignone
# Contact: lbignone@iafe.uba.ar

""" Read Rockstar ASCII output"""

import pandas as pd
import numpy as np

columns = [
            "ID",
            "DescID",
            "Mvir",
            "Vmax",
            "Vrms",
            "Rvir",
            "Rs",
            "Np",
            "X",
            "Y",
            "Z",
            "VX",
            "VY",
            "VZ",
            "JX",
            "JY",
            "JZ",
            "Spin",
            "rs_klypin",
            "Mvir_all",
            "M200b",
            "M200c",
            "M500c",
            "M2500c",
            "Xoff",
            "Voff",
            "spin_bullock",
            "b_to_a",
            "c_to_a",
            "A[x]",
            "A[y]",
            "A[z]",
            "b_to_a(500c)",
            "PID"
        ]

def rockstar_load(basedir, snap_number):
    """ Load Rockstar ASCII output into a pandas DataFrame

    Args:
        basedir (str):  Base directory
        snap_number (int):  Snapshot number

    Returns:
        pandas DataFrame
    """

    fname = basedir + "/halos/{0}/hlist.txt".format(snap_number)

    data = np.genfromtxt(fname)

    df = pd.DataFrame(data, columns=columns, index=data[:,0])

    return df