# Index
- [Base Simulation](#markdown-header-base-simulation)
- [Zoom Simulation](#markdown-header-zoom-simulation)
- [Codes](#markdown-header-codes)
- [Simulation parameters](#markdown-header-simulation-parameters)
- [Halo candidates to resimulate](#markdown-header-halo-candidates-to-resimulate)

# Base Simulation

## Base simulation directory
	/data4/lbignone/lgzoom/out512
	
## Initial conditions
Initial conditions parameter files for MUSIC are located at

	/data4/lbignone/lgzoom/512info/ics_512base.conf

## Rockstar halos
	simdir/halos/xx/hlist.txt

where "simdir" is the simulation directory mentioned above and xx is the snapshot number

## FOF halos
	simdir/group_"xxx"/

where "simdir" is the simulation directory mentioned above and xxx is the snapshot number

# Zoom simulations

Zoom simulations are located in
	
	/data4/wmmw/<halo_id>/<zoom level>/
	
If `<halo_id>` starst with a letter "R" the halo id corresponds to a Rockstar halo id, otherwhise is a FOF halo id

The folling information is available in each halo/zoom directory:

- `ics_512_<halo_id>_level<zoom_level>.dat`	MUSIC itial conditions
- `ics_512_<halo_id>_level<zoom_level>.conf`	MUSIC initial condition parameter file
- `ics_512_<halo_id>_level<zoom_level>.conf_log.txt`	MUSIC log file
- `gadget2_<halo_id>_level<zoom_level>.par`	GADGET2 parameter file
- `output_list.txt`	List of times for snapshot outputs
- GADGET2 output files: snapshots, cpu, energy, timings, etc... (only if already computed)

# Codes

Source codes for GADGET, MUSIC and ROCKSTAR can be found in `/data4/lbignone/wmmw/codes` together with some example scripts for compilation in Geryon2
	
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

# Halo candidates to resimulate

A first halo catalogue was compiled from Rockstar halos in the base simulation that satisfy the following criteria:

1. Halo mass in the range [5e9 - 5e12] MSun/h
2. Halo mass is at least 4 time the mass of the most massive neighbour inside the halo virial radius
3. There is no neighouring halo more massive than 1e13 Msun/h in a 1 Mpc/h radius

The halo ids that form this catalogue can be found in 
	
	/data4/lbignone/wmmw/candidates.txt

This initial sample was then distributed in `5` logarithmic mass bins. Each
mass bin was further sorted into bins representing differents ranges of number
of neighbours found inside the virial radius of each halo. The number of
neighbours ranges that where used where:

- N <= 10
- 10 < N <= 20
- 20 < N <= 50
- 50 < N <= 100	

A random sample of 20 halos was constructed as to represent the different categories
of mass and number of neighbours described above. The final list can be found in

	/data4/lbignone/wmmw/selected_halos.txt
	
The file follows the same format as Rockstar ASCII output with the adition of some columns:

- `mass_bin` The correspondig mass bin for the halo [0-4]
- `neighbours[500]` The number of neighbours inside a 500 kpc/h radius
- `neighbours[Rvir]` The number of neighbours inside the virial radius
- `neighbours_bin` The correspondig number of neighbours bin for the halo [0-3]
- `massive_neighbour_d[500]` Distance to the most massive neighbour inside a 500 kpc/h radius. In Mpc/h
- `massive_neighbour_mass[500]` Mass of the most massive neighbour inside a 500 kpc/h radius. In MSun/h
- `massive_neighbour_d[Rvir]` Distance to the most massive neighbour inside the virial radius. In Mpc/h
- `massive_neighbour_mass[Rvir]` Mass of the most massive neighbour inside the virial radius. In MSun/h

For reference an abreviated table is shown bellow


Maps of the selected halos are show below













