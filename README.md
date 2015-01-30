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

# Halo candidates for resimulation

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

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>X</th>
      <th>Y</th>
      <th>Z</th>
      <th>M200c</th>
      <th>Mvir</th>
      <th>Np</th>
      <th>Rvir</th>
      <th>neighbours[500]</th>
      <th>massive_neighbour_d[500]</th>
      <th>massive_neighbour_mass[500]</th>
      <th>neighbours[Rvir]</th>
      <th>massive_neighbour_d[Rvir]</th>
      <th>massive_neighbour_mass[Rvir]</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>184999</th>
      <td> 19.83838</td>
      <td> 29.40285</td>
      <td> 28.91830</td>
      <td> 6.647000e+09</td>
      <td> 7.878000e+09</td>
      <td>   135</td>
      <td>  40.303</td>
      <td>   1</td>
      <td> 0.294579</td>
      <td> 1.148900e+09</td>
      <td>  0</td>
      <td> 0.000000</td>
      <td> 0.000000e+00</td>
    </tr>
    <tr>
      <th>233107</th>
      <td> 31.17134</td>
      <td> 39.42450</td>
      <td> 38.69143</td>
      <td> 5.087800e+09</td>
      <td> 5.662000e+09</td>
      <td>    83</td>
      <td>  36.101</td>
      <td>   0</td>
      <td> 0.000000</td>
      <td> 0.000000e+00</td>
      <td>  0</td>
      <td> 0.000000</td>
      <td> 0.000000e+00</td>
    </tr>
    <tr>
      <th>117322</th>
      <td> 25.82530</td>
      <td>  5.46329</td>
      <td>  6.52503</td>
      <td> 3.348100e+10</td>
      <td> 3.726000e+10</td>
      <td>   489</td>
      <td>  67.649</td>
      <td>   1</td>
      <td> 0.393173</td>
      <td> 5.580200e+09</td>
      <td>  0</td>
      <td> 0.000000</td>
      <td> 0.000000e+00</td>
    </tr>
    <tr>
      <th>2848  </th>
      <td>  9.12347</td>
      <td>  8.89296</td>
      <td> 12.43929</td>
      <td> 3.520400e+10</td>
      <td> 3.939000e+10</td>
      <td>   577</td>
      <td>  68.916</td>
      <td>   3</td>
      <td> 0.338589</td>
      <td> 1.969500e+09</td>
      <td>  0</td>
      <td> 0.000000</td>
      <td> 0.000000e+00</td>
    </tr>
    <tr>
      <th>172676</th>
      <td> 30.23518</td>
      <td> 36.79990</td>
      <td> 21.45137</td>
      <td> 1.298200e+11</td>
      <td> 1.508000e+11</td>
      <td>  2163</td>
      <td> 107.798</td>
      <td>   6</td>
      <td> 0.420853</td>
      <td> 5.334000e+09</td>
      <td>  1</td>
      <td> 0.062736</td>
      <td> 1.477100e+09</td>
    </tr>
    <tr>
      <th>70678 </th>
      <td> 10.82039</td>
      <td> 26.39407</td>
      <td> 38.36138</td>
      <td> 2.399500e+11</td>
      <td> 2.590000e+11</td>
      <td>  3283</td>
      <td> 129.108</td>
      <td>   6</td>
      <td> 0.163449</td>
      <td> 4.103100e+09</td>
      <td>  1</td>
      <td> 0.107946</td>
      <td> 3.364500e+09</td>
    </tr>
    <tr>
      <th>32978 </th>
      <td>  9.62568</td>
      <td>  9.02892</td>
      <td> 34.73824</td>
      <td> 4.435400e+11</td>
      <td> 5.094000e+11</td>
      <td>  6720</td>
      <td> 161.768</td>
      <td>   7</td>
      <td> 0.499798</td>
      <td> 3.610700e+09</td>
      <td>  2</td>
      <td> 0.083095</td>
      <td> 1.805300e+09</td>
    </tr>
    <tr>
      <th>182073</th>
      <td> 31.20300</td>
      <td> 26.77412</td>
      <td> 23.41055</td>
      <td> 4.483800e+11</td>
      <td> 5.236000e+11</td>
      <td>  6599</td>
      <td> 163.257</td>
      <td>  11</td>
      <td> 0.080084</td>
      <td> 6.400800e+09</td>
      <td>  7</td>
      <td> 0.080084</td>
      <td> 6.400800e+09</td>
    </tr>
    <tr>
      <th>172029</th>
      <td> 34.15141</td>
      <td> 21.59876</td>
      <td> 20.78378</td>
      <td> 9.883400e+11</td>
      <td> 1.094000e+12</td>
      <td> 10942</td>
      <td> 208.677</td>
      <td>  19</td>
      <td> 0.105116</td>
      <td> 1.458200e+11</td>
      <td> 11</td>
      <td> 0.105116</td>
      <td> 1.458200e+11</td>
    </tr>
    <tr>
      <th>136214</th>
      <td> 30.22618</td>
      <td>  8.49520</td>
      <td> 25.78168</td>
      <td> 5.810800e+11</td>
      <td> 7.614000e+11</td>
      <td>  9466</td>
      <td> 184.952</td>
      <td>  19</td>
      <td> 0.400394</td>
      <td> 5.416000e+10</td>
      <td> 12</td>
      <td> 0.037607</td>
      <td> 3.815800e+10</td>
    </tr>
    <tr>
      <th>158699</th>
      <td> 42.90718</td>
      <td> 24.51457</td>
      <td>  6.15137</td>
      <td> 4.134200e+11</td>
      <td> 5.689000e+11</td>
      <td>  6813</td>
      <td> 167.835</td>
      <td>  22</td>
      <td> 0.130629</td>
      <td> 3.783000e+10</td>
      <td> 12</td>
      <td> 0.130629</td>
      <td> 3.783000e+10</td>
    </tr>
    <tr>
      <th>1227  </th>
      <td> 16.81753</td>
      <td>  5.79321</td>
      <td>  7.17660</td>
      <td> 9.413200e+11</td>
      <td> 1.060000e+12</td>
      <td> 13350</td>
      <td> 206.493</td>
      <td>  28</td>
      <td> 0.121082</td>
      <td> 2.404400e+10</td>
      <td> 11</td>
      <td> 0.121082</td>
      <td> 2.404400e+10</td>
    </tr>
    <tr>
      <th>171766</th>
      <td> 20.02799</td>
      <td> 23.20582</td>
      <td> 18.44313</td>
      <td> 1.414100e+12</td>
      <td> 1.667000e+12</td>
      <td> 20794</td>
      <td> 240.167</td>
      <td>  30</td>
      <td> 0.259627</td>
      <td> 1.189900e+10</td>
      <td> 10</td>
      <td> 0.214721</td>
      <td> 1.140700e+10</td>
    </tr>
    <tr>
      <th>171739</th>
      <td> 37.83602</td>
      <td> 27.06255</td>
      <td> 21.13517</td>
      <td> 1.574200e+12</td>
      <td> 1.781000e+12</td>
      <td> 19310</td>
      <td> 245.506</td>
      <td>  26</td>
      <td> 0.130843</td>
      <td> 1.898900e+11</td>
      <td> 10</td>
      <td> 0.130843</td>
      <td> 1.898900e+11</td>
    </tr>
    <tr>
      <th>158145</th>
      <td> 17.62967</td>
      <td> 29.36271</td>
      <td>  6.24698</td>
      <td> 1.806400e+12</td>
      <td> 2.107000e+12</td>
      <td> 24135</td>
      <td> 259.657</td>
      <td>  48</td>
      <td> 0.063067</td>
      <td> 6.220200e+10</td>
      <td> 18</td>
      <td> 0.063067</td>
      <td> 6.220200e+10</td>
    </tr>
    <tr>
      <th>60717 </th>
      <td>  7.20462</td>
      <td> 32.75721</td>
      <td> 35.18716</td>
      <td> 1.301200e+12</td>
      <td> 1.578000e+12</td>
      <td> 19666</td>
      <td> 235.797</td>
      <td>  50</td>
      <td> 0.377259</td>
      <td> 1.778300e+11</td>
      <td> 19</td>
      <td> 0.131970</td>
      <td> 2.232100e+10</td>
    </tr>
    <tr>
      <th>228540</th>
      <td> 35.64206</td>
      <td> 38.71817</td>
      <td> 29.77349</td>
      <td> 2.487800e+12</td>
      <td> 2.877000e+12</td>
      <td> 33301</td>
      <td> 288.066</td>
      <td>  39</td>
      <td> 0.193879</td>
      <td> 8.780500e+10</td>
      <td> 27</td>
      <td> 0.193879</td>
      <td> 8.780500e+10</td>
    </tr>
    <tr>
      <th>50660 </th>
      <td> 15.89451</td>
      <td> 40.37899</td>
      <td> 19.91348</td>
      <td> 3.430100e+12</td>
      <td> 3.976000e+12</td>
      <td> 47802</td>
      <td> 320.878</td>
      <td>  50</td>
      <td> 0.264443</td>
      <td> 5.760700e+10</td>
      <td> 31</td>
      <td> 0.264443</td>
      <td> 5.760700e+10</td>
    </tr>
    <tr>
      <th>157661</th>
      <td> 39.41720</td>
      <td> 36.42007</td>
      <td> 12.62284</td>
      <td> 3.010400e+12</td>
      <td> 3.277000e+12</td>
      <td> 49065</td>
      <td> 300.869</td>
      <td> 128</td>
      <td> 0.129710</td>
      <td> 1.348800e+13</td>
      <td> 74</td>
      <td> 0.129710</td>
      <td> 1.348800e+13</td>
    </tr>
    <tr>
      <th>228338</th>
      <td> 24.51139</td>
      <td> 40.22440</td>
      <td> 33.35339</td>
      <td> 3.989200e+12</td>
      <td> 4.934000e+12</td>
      <td> 54312</td>
      <td> 344.815</td>
      <td>  92</td>
      <td> 0.326186</td>
      <td> 1.003600e+11</td>
      <td> 68</td>
      <td> 0.326186</td>
      <td> 1.003600e+11</td>
    </tr>
  </tbody>
</table>

Maps of the selected halos are show below

![Halo candidates](halo_candidates.png "Halo candidates")











