import random

def get_safetyness_mortality(tab_in, spatialresolution, species_profile, distPix=0):
    '''
    This function gets the mortality of safetyness of an individual, given a table of mortality/safetyness
    probability and the distance an animal is from habitat edges (towards inside or outside pathces)
    Mortality/safetyness also depends on species ecological profile
    Input:
    - tab_in: table of mortality or safetyness
    - spatialresolution: spatial resolution of the map (or grain, the size of the pixels)
    - species_profile: ecological profile of the species
    - distPix: distance the animal is from habitat edges, in pixels (not in meters)
    Output:
    - tab_in[][]: Mortality/safetyness value, given a position and a species profile (it is an element of the table)
    '''
    
    distMeters=float(distPix)*float(spatialresolution)
    
    if distMeters>0:
        distMeters=float(distPix+1)*float(spatialresolution)
    
    for line in range(len(tab_in)):
        line_dist=tab_in[line][0]
        if float(distMeters) < float(line_dist):
            if line==0:
                if species_profile=="Core dependent":
                    return tab_in[line][1]
                elif species_profile=="Frag. dependent":
                    return tab_in[line][2]
                elif species_profile=="Habitat dependent":
                    return tab_in[line][3]
                elif species_profile=="Moderately generalist":
                    return tab_in[line][4]
                elif species_profile=="Highly generalist":
                    return tab_in[line][5]
                else:
                    return 0
                    
            else:
                if species_profile=="Core dependent":
                    return tab_in[line-1][1]
                elif species_profile=="Frag. dependent":
                    return tab_in[line-1][2]
                elif species_profile=="Habitat dependent":
                    return tab_in[line-1][3]
                elif species_profile=="Moderately generalist":
                    return tab_in[line-1][4]
                elif species_profile=="Highly generalist":
                    return tab_in[line-1][5]
    return 0


def kill_individual_new(tab_mortality, spatialres, sp_profile, distfromedgePix):
    '''
    This function calculates the mortality rate, for a given species profile and position in the landscape,
    and randomly defines if an individual will keep alive or die, given this mortality rate.
    Input:
    - tab_mortality: mortality table (a matrix)
    - spatialres: spatial resolution of the landscape map (or grain, the size of the pixels)
    - sp_profile: ecological profile of the species
    - distfromedgePix: minimum distance from the animal's position to habitat edges, in pixels
    Output:
    - continuealive: a variable stating whether the animal is still alive (1) or not (0)
    '''
    
    prob_die=get_safetyness_mortality(tab_in=tab_mortality, spatialresolution=spatialres, species_profile=sp_profile, distPix=distfromedgePix)
    
    prob_dieMAX=0.2 ## ???
    prob_dieMAX_target=0.001 ### ???
    prob_die_corrected=prob_die/prob_dieMAX*prob_dieMAX_target

    if prob_die_corrected>random.uniform(0,1):
        continuealive=0
    else:
        continuealive=1

    return continuealive