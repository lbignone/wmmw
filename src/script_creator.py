
from os import makedirs


def create_gadget2(hid, level, box, SofteningHalo, SofteningBndry,
                   SofteningHaloMaxPhys, SofteningBndryMaxPhys,
                   baryons, folder=''):

    if baryons:
        outbaryons = "baryons"
    else:
        outbaryons = 'dark'

    with open("gadget2_template.par") as f:
        gadget_template_par = f.read()

    with open("gadget2_template.pbs") as f:
        gadget_template_pbs = f.read()

    output_par = gadget_template_par
    output_par = output_par.format(hid=hid,
                                   level=level,
                                   box=box,
                                   SofteningHalo=SofteningHalo,
                                   SofteningBndry=SofteningBndry,
                                   SofteningHaloMaxPhys=SofteningHaloMaxPhys,
                                   SofteningBndryMaxPhys=SofteningBndryMaxPhys,
                                   outbaryons=outbaryons)

    output_pbs = gadget_template_pbs
    output_pbs = output_pbs.format(hid=hid,
                                   level=level,
                                   box=box)

    output_fname = folder + "gadget2_R{hid}_level{level}_{box}"

    output_fname_par = output_fname + ".par"
    output_fname_pbs = output_fname + ".pbs"

    output_fname_par = output_fname_par.format(hid=hid,
                                               level=level,
                                               box=box)

    output_fname_pbs = output_fname_pbs.format(hid=hid,
                                               level=level,
                                               box=box)

    with open(output_fname_par, "w") as f:
        f.write(output_par)

    with open(output_fname_pbs, "w") as f:
        f.write(output_pbs)


def create_ics(hid, level, box, baryons, folder=''):
    with open("ics_template.par") as f:
        ics_template_par = f.read()

    with open("ics_template.pbs") as f:
        ics_template_pbs = f.read()

    if baryons:
        baryons_toggle = "yes"
        spread_toggle = "yes"
        outbaryons = "baryons"
    else:
        baryons_toggle = "no"
        spread_toggle = "no"
        outbaryons = 'dark'

    output_par = ics_template_par
    output_par = output_par.format(hid=hid,
                                   level=level,
                                   box=box,
                                   baryons_toggle=baryons_toggle,
                                   spread_toggle=spread_toggle,
                                   outbaryons=outbaryons)

    output_pbs = ics_template_pbs
    output_pbs = output_pbs.format(hid=hid,
                                   level=level,
                                   box=box,
                                   outbaryons=outbaryons)

    output_fname = folder + "ics_R{hid}_level{level}_{box}_{outbaryons}"

    output_fname_par = output_fname + ".par"
    output_fname_pbs = output_fname + ".pbs"

    output_fname_par = output_fname_par.format(hid=hid,
                                               level=level,
                                               box=box,
                                               outbaryons=outbaryons)

    output_fname_pbs = output_fname_pbs.format(hid=hid,
                                               level=level,
                                               box=box,
                                               outbaryons=outbaryons)

    with open(output_fname_par, "w") as f:
        f.write(output_par)

    with open(output_fname_pbs, "w") as f:
        f.write(output_pbs)


hids = [184999,
        233107,
        117322,
        2848,
        172676,
        70678,
        32978,
        182073,
        172029,
        136214,
        158699,
        1227,
        171766,
        171739,
        158145,
        60717,
        228540,
        50660,
        157661,
        228338,
        ]

levels = [10, 11, 12]

softenings = {
                10: {"halo":  0.74, "bndry": 1.5},
                11: {"halo":  0.8, "bndry": 90.0},
                12: {"halo":  0.5, "bndry": 90.0},
             }
softeningsMax = {
                10: {"halo":  0.49, "bndry": 1.0},
                11: {"halo":  0.8, "bndry": 90.0},
                12: {"halo":  0.5, "bndry": 90.0},
                }

baryons = [True, False]

box = "5RvirBox_Ellipsoid"

for hid in hids:
    for level in levels:
        for baryon in baryons:

            if baryon:
                outbaryons = "baryons"
            else:
                outbaryons = "dark"

            folder = "R{hid}/{level}_{box}_{outbaryons}/"
            folder = folder.format(hid=hid, level=level, box=box,
                                   outbaryons=outbaryons)
            SH = softenings[level]["halo"]
            SB = softenings[level]["bndry"]
            SMH = softeningsMax[level]["halo"]
            SMB = softeningsMax[level]["bndry"]

            try:
                makedirs(folder)
            except:
                pass

            create_gadget2(hid, level, box, SH, SB, SMH, SMB,
                           baryon, folder=folder)
            create_ics(hid, level, box, baryon, folder=folder)
