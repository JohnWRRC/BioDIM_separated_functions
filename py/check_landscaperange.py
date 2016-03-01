
def check_landscaperange(list_of_xy, Form1_landscape_matrix):
    
    list_of_xy_modified=[]
    for i in range(len(list_of_xy)):
        list_of_xy_modified.append(list_of_xy[i])
    
    changed_quadrant=[]
    for indiv in range(len(list_of_xy)):
        #let row be ok
        ns=0
        ew=0
        
        if list_of_xy_modified[indiv][0]<0:
            list_of_xy_modified[indiv][0]=list_of_xy_modified[indiv][0]+len(Form1_landscape_matrix)
            ns=+1 #gone to North
        if list_of_xy_modified[indiv][0]>len(Form1_landscape_matrix):
            list_of_xy_modified[indiv][0]=list_of_xy_modified[indiv][0]-len(Form1_landscape_matrix)
            ns=-1 #gone to South
        #let col be ok  
        if list_of_xy_modified[indiv][1]>len(Form1_landscape_matrix):
            list_of_xy_modified[indiv][1]=list_of_xy_modified[indiv][1]-len(Form1_landscape_matrix)
            ew=+1 #gone to East        
        if list_of_xy_modified[indiv][1]<0:
            list_of_xy_modified[indiv][1]=list_of_xy_modified[indiv][1]+len(Form1_landscape_matrix)
            ew=-1 #gone to West
        changed_quadrant.append([ns,ew])
    return list_of_xy_modified, changed_quadrant