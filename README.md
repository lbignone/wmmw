# Base simulation 

## Location

Cluster Geryon2 Centro de Astro-Ingeniería

    /fast_scratch1/regonzar/lgzoom/out512

## Parameters

- N = 512^3

Further details in:

    parameters-usedvalues

## Cosmological parameters

Planck Collaboration results [[ArXiv]](http://arxiv.org/abs/1303.5062)

| Cosmological parameter |  Value  |
|------------------------|---------|
| $\Omega_m$             |   0.307 |
| $\Omega_\Lambda$       |   0.693 |
| $\Omega_b$             | 0.04825 |
| $h$                    |   0.677 |
| $\sigma_8$             |  0.8288 |
| $n_s$                  |  0.9611 |
| $Y$                    |   0.248 |

## Halos

Rockstar halos including substructures in:

    /fast_scratch1/regonzar/lgzoom/out512/halos/xx/hlist.txt

where xx is the snapshot number

## Initial conditions

    /fast_scratch1/regonzar/lgzoom/ics_gadget_512base.dat

More information in 

    /fast_scratch1/regonzar/lgzoom/512info

- lgzoom.param:  Gadget-2 parameters for base simulation
- ics_512base.conf: MUSIC config file for base simulation
- ics_512zoom1.conf: MUSIC config file for a zoom simulation **don't change random seeds and run in a single node with up to 40 threads**


## TODO

- Identify galaxies with FOF
- Calcular halo mass function
- Calculate number of neighbours within 500 kpc/h and store their mass
- Build sample consisting of semi isolated galaxies where the main component mass is > 0.3 times the mass of its companion