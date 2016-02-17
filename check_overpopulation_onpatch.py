
def check_overpopulation_onpatch(indiv_isdispersing, indiv_whichpatchid, indiv_habareapix, indiv_age,spatialresolution,homerangesize):
    """
    Describe!
    """    
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
        for LL in range(len(indiv_habareapix)):
            if indiv_whichpatchid[LL]==patchid and patchid>0L:
                numberOFpix = indiv_habareapix[LL]
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