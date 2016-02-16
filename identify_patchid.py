def identify_patchid(indiv_xy_position, patchid_map):
    row=int(indiv_xy_position[0])
    col=int(indiv_xy_position[1])
    patchid=patchid_map[row][col]
    return patchid
