
def check_overpopulation_onpatch(indiv_isdispersing, indiv_whichpatchid, indiv_habarea, indiv_age, spatialresolution, homerangesize, userbase = False):
    """
    This function checks, in each patch, how many individuals there are; this number is compared with
    the maximum number of individuals the patch supports, based on their minimum homerange; if there the number
    of individuals is greater than the carrying capacity, some of them are chosen to disperse.
    Input: 
    - indiv_isdispersing: list indentifying which animal is dispersing (1) or not dispersing (0)
    - indiv_whichpatchid: list indentifying the patch id of the patch each animal is in (=0 when dispersing)
    - indiv_habarea: list identifying the area of the patch the animal is in (=0 when dispersing)
    - indiv_age: not used, but may be useful!!!
    - spatialresolution: spatial resolution/grain (pixel size) of the maps
    - homerangesize: minimum size of an agent homerange, in hectares
    - userbase: False = simulated database maps are used
                True = user (real) maps are used
    Output:
    - isdispersing_aux: new list indentifying which animal is dispersing (1) or not dispersing (0)
    """    
    
    #### what happens with id = 0 (when animals are dispersing, outside patches??)
    
    isdispersing_aux=[]    
    for i in range(len(indiv_isdispersing)):
        isdispersing_aux.append(indiv_isdispersing[i])
        
    patchidSET={}
    for i in indiv_whichpatchid:
        try: patchidSET[i] += 1
        except KeyError: patchidSET[i] = 1
    
    keys = patchidSET.keys()
    keys.sort()
    
    patchid_overpopLIST=[]
    for k in keys:
        patchid=k
        numind=patchidSET[k]
        for LL in range(len(indiv_habarea)):
            if indiv_whichpatchid[LL]==patchid and patchid>0L:
                if userbase:
                    areaha = indiv_habarea[LL] # if userbase, habitat area is already in hectares
                else:
                    numberOFpix = indiv_habarea[LL] ############ isso esta certo?? o res ja nao eh em hectares?
                    areaEACHpix = spatialresolution*spatialresolution
                    areaha = numberOFpix*areaEACHpix/10000
                
                numHR = int(areaha/homerangesize)+1
                if numHR<numind:
                    overpop = numind-numHR
                    patchid_overpopLIST.append([patchid, overpop])
                else:
                    overpop = 0
                    
    needdisperseLIST=[]
    for m in range(len(patchid_overpopLIST)):
        patchid=patchid_overpopLIST[m][0]
        overpop=patchid_overpopLIST[m][1]

        #check how many isdispersing on the patch
        dispersing=0
        for n in range(len(indiv_whichpatchid)):
            ###if indiv_whichpatchid[n]==patchid and indiv_isdispersing[n]==1:
            if indiv_whichpatchid[n]==patchid and isdispersing_aux[n]==1:
                dispersing+=1
        needdisperse=overpop-dispersing
        if needdisperse>0:
            needdisperseLIST.append([patchid, overpop, dispersing, needdisperse])
    
    # here we may include age - cubs are more prone to disperse!
    for o in range(len(needdisperseLIST)):
        patchid=needdisperseLIST[o][0]
        overpop=needdisperseLIST[o][1]
        dispersing=needdisperseLIST[o][2]
        needdisperse=needdisperseLIST[o][3]
        
        newdisperser=0        
        for p in range(len(indiv_whichpatchid)):
            if indiv_whichpatchid[p]==patchid:
                #if indiv_isdispersing[p]==0:
                if isdispersing_aux[p]==0:
                    if needdisperse>newdisperser:
                        isdispersing_aux[p]=1
                        newdisperser+=1

    #return indiv_isdispersing
    return isdispersing_aux