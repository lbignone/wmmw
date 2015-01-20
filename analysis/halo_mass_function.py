# Plot simulation halo mass function and compare it with theorical results usgin HMFcalc
# ( http://hmf.icrar.org/ )
#
#
#

from pygadget import Fof

import numpy as np

from matplotlib.pyplot import *


def mass_function(mass, volume, n_bins):
    """ Calculate halo mass function

    Parameters:
        mass:   mass array in M_Sun / h
        volume: simulation volume in Mpc / h
        n_bins: numer of bins

    return mass, dn/dlogM
    """
    bins = np.logspace(np.log10(mass.min()), np.log10(mass.max()), n_bins)

    hist_result = np.histogram(fof.groupmass, bins=bins)

    m = []
    dlogm = []
    for i in range(1, hist_result[1].size):
        m.append((hist_result[1][i] + hist_result[1][i-1])/2)
        dlogm.append(np.log10(hist_result[1][i]) - np.log10(hist_result[1][i-1]))

    dlogm = np.array(dlogm)
    V = box_length**3
    dndlogm = hist_result[0]/(dlogm*V)

    return m, dndlogm

# FOF halos
basedir = '/home/lbignone/Simulations/wmmw/out512'

snapnum = 14

fof = Fof(basedir, snapnum)

dm_mass = 8.20612e+07 # dark matter mass in M_Sun/h
box_length = 50.0 # box length in Mpc/h
V = box_length**3
n = 100 # number of bins

fof.groupmass = fof.grouplen * dm_mass

m, dndlogm = mass_function(fof.groupmass, volume=V, n_bins=n)

plot(m, dndlogm, label="FOF ($512^3$)", linestyle="solid")


# Rockstar halos

rock_mass = np.genfromtxt(basedir+"/halos/14/hlist.txt", usecols=[21,])
rock_mass = rock_mass[rock_mass>0]

m, dndlogm = mass_function(rock_mass, volume=V, n_bins=n)

plot(m, dndlogm, label=r"Rockstar ($512^3$)", linestyle="dashed")

# Plot Theorical curve

fname = "hmfcalc/mVector_PLANCK-SMT .txt" # HMFCalc output

m, dndlogm = np.genfromtxt(fname, usecols=[0, 7], unpack=True)

plot(m, dndlogm, label="HMF-calc", linestyle="dotted")


xlabel(r"Mass ($M_\odot h^{-1}$)")
ylabel(r"Mass function $(\frac{dn}{dlogM})$ $h^3 Mpc^{-3}$")
xlim(1e10, 1e14)
xscale("log")
yscale("log")
legend(loc=0)
grid()

show()