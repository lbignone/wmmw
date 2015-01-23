# Author: Lucas A. Bignone
# Contact: lbignone@iafe.uba.ar

# Selects halos following this criteria:
# Halos must be mass_frac_inside_rvir times more massive than all neighbours inside its virial radius
# Halos must not have a neighbour more massive than Max_mass_outside_rvir in a spehere of radius=distance

# Depending the criteria it can take a long time to complete (~1.5h).
# In console mode a progressbar is shown

from rockstar import rockstar_load

from astropy.utils.console import ProgressBar

import numpy as np

distance = 1 # search radius in Mpc/h
mass_frac_inside_rvir = 4 # Mass criteria (Mcen > mass_frac Mi)
Max_mass_outside_rvir = 1e13 

basedir = "/home/lbignone/simulations/wmmw/out512"
snap_number = 14

save_name = "candidates.txt"

halos_tot = rockstar_load(basedir, snap_number)

halos = halos_tot[(halos_tot.Mvir <= 1e13) & (halos_tot.Mvir >= 1e9)]


candidates = []

itersize = halos.M200b.size

with ProgressBar(itersize) as bar:

    for i in range(itersize):
        aproved = False
        x0 = halos.iloc[i].X
        y0 = halos.iloc[i].Y
        z0 = halos.iloc[i].Z
        id0 = halos.iloc[i].ID
        rvir0 = halos.iloc[i].Rvir
        
        Mcent = halos.iloc[i].Mvir
        
        cind = halos.index[i]
        
        d = np.sqrt((halos.X-x0)**2 + (halos.Y-y0)**2 + (halos.Z-z0)**2)
        ind_outside = d[(d<=distance) & (d.index != cind)].index
        ind_inside = d.loc[ind_outside][(d<=rvir0) & (d.index != cind)].index
        
        if (ind_outside.size == 0) and (ind_inside.size == 0):
            aproved = True
        else:
            Mmax_outside = halos.loc[ind_outside].Mvir.max()
            Mmax_inside = halos.loc[ind_inside].Mvir.max()
            
            if (Mmax_outside < Max_mass_outside_rvir) and (Mcent >= mass_frac_inside_rvir*Mmax_inside):
                aproved = True
                
        if aproved:
            candidates.append(id0)

        bar.update()

if save_name:
    with open(save_name, 'w') as f:
        print('#basedir = "/home/lbignone/simulations/wmmw/out512\"', file=f)
        print('#distance = {} # search radius in Mpc'.format(distance), file=f)
        print('#mass_frac = {} # Mass criteria (Mcen > mass_frac_ Mi)'.format(mass_frac_inside_rvir), file=f)
        print('#candidates ids', file=f)
        for id in candidates:
            print("{:.0f}".format(id), file=f)