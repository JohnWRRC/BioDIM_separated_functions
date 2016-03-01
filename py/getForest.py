
def getForest(landscape_matrix):
    forest = []
    for row in range(len(landscape_matrix)):
        for col in range(len(landscape_matrix[0])):
            feature = landscape_matrix[row][col]
            if feature == 1: #HQ
                forest.append([row,col])
            if feature == 2: #MQ
                forest.append([row,col])                
    return forest

def getForest_habmat(landscape_matrix):
    '''
    This function is equal to getForest, but designed to user (real) maps that
    do not have quality on it. It is based on a binary map of habitat (1) and matrix (0)
    '''
    forest = []
    for row in range(len(landscape_matrix)):
        for col in range(len(landscape_matrix[0])):
            feature = landscape_matrix[row][col]
            if feature == 1: #HQ
                forest.append([row,col])
            #if feature == 2: #MQ
                #forest.append([row,col])                
    return forest
