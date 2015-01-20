# Index
- [Where to find Stuff](#markdown-header-where-to-find-stuff)
- [Simulation parameters](#markdown-header-simulation-parameters)

# Where to find stuff

## Simulations

### Base simulation directory
	/data4/lbignone/wmmw/out512

### Zoom simulation directory
	/data4/lbignone/wmmw/out512zoom


## Halos
### Rockstar
	simdir/halos/xx/hlist.txt

where "simdir" is the simulation directory mentioned above and xx is the snapshot number

### FOF
	simdir/group_"xxx"/

where "simdir" is the simulation directory mentioned above and xxx is the snapshot number

## Initial conditions
Initial conditions parameter files for MUSIC are located at

	/data4/lbignone/wmmw/512info/ics_512base.conf
    
for the base simulation and

	/data4/lbignone/wmmw/512info/ics_512zoom1.conf
    
for the zoom region

# Simulation Parameters

## Cosmological parameters

| Cosmological parameter | Value  |
| ---------------------- | ------ |
| Omega0	             | 0.3175 |
| OmegaLambda		     | 0.6825 |
| OmegaBaryon            |  0.049 |
| h                      | 0.6711 |
| sigma8                 | 0.8288 |
| ns                     | 0.9611 |
| Y                      |  0.248 |

## Softenings

|                      | [kcp] |
| -------------------- | ----- |
| SofteningHalo        |   1.5 |
| SofteningHaloMaxPhys |   1.0 |






