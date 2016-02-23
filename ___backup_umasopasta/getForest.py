
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
