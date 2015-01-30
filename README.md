# Index
- [Where to find Stuff](#markdown-header-where-to-find-stuff)
	1. [Base Simulation](#markdown-header-base-simulation)
	2. [Zoom Simulation](#markdown-header-zoom-simulation)
- [Simulation parameters](#markdown-header-simulation-parameters)

# Where to find stuff

## Base Simulation

### Base simulation directory
	/data4/lbignone/lgzoom/out512
	
### Initial conditions
Initial conditions parameter files for MUSIC are located at

	/data4/lbignone/lgzoom/512info/ics_512base.conf

### Rockstar halos
	simdir/halos/xx/hlist.txt

where "simdir" is the simulation directory mentioned above and xx is the snapshot number

### FOF halos
	simdir/group_"xxx"/

where "simdir" is the simulation directory mentioned above and xxx is the snapshot number


### Initial conditions
Initial conditions parameter files for MUSIC are located at

	/data4/lbignone/lgzoom/512info/ics_512base.conf

## Zoom simulations

Zoom simulations are located in
	
	/data4/wmmw/<halo_id>/<zoom level>/
	
If `<halo_id>` starst with a letter "R" the halo id corresponds to a Rockstar halo id, otherwhise is a FOF halo id

The folling information is available in each halo/zoom directory:

- `ics_512_<halo_id>_level<zoom_level>.dat`	MUSIC itial conditions
- `ics_512_<halo_id>_level<zoom_level>.conf`	MUSIC initial condition parameter file
- `ics_512_<halo_id>_level<zoom_level>.conf_log.txt`	MUSIC log file
- `gadget2_<halo_id>_level<zoom_level>.par`	GADGET2 parameter file
- `output_list.txt`	List of times for snapshot outputs
- GADGET2 output files: snapshots, cpu, energy, timings, etc... (only if already run)
	

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

## Softenings for base simulation

|                      | [kcp] |
| -------------------- | ----- |
| SofteningHalo        |   1.5 |
| SofteningHaloMaxPhys |   1.0 |







