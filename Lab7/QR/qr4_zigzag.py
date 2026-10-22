def get_next_pos(row,collumn,size):
    newrow = None
    newcol = None
    if collumn%2 ==0:
        if collumn == 0:
            newrow = row-1
        else:
            newcol = collumn-1
    elif collumn%4==1:
        if row ==size-1:
            newcol = collumn-1
        else:
            newrow=row+1
            newcol=collumn+1
    elif collumn%4==3:
        if row ==0:
            newcol = collumn-1
        else:
            newrow = row-1
            newcol = collumn+1
    if newcol==None:
        newcol=collumn
    if newrow==None:
        newrow=row

    return(newrow,newcol)

def make_matrix(size):
    matrix = []
    for i in range(size):
        row = []
        for i in range(size):
            row.append(0)
        matrix.append(row)
    return matrix


def bit_list_to_raw_matrix(bit_list,qr_layout):

    size = qr_layout['side_length']
    raw_matrix = make_matrix(size)
    pos = (size-1,size-1)
    if len(bit_list)>size*size:
        return None
    illegal_pos_list = qr_layout['fixed_positions']['zeros'] + qr_layout['fixed_positions']['ones'] + qr_layout['meta_positions']['first'] + qr_layout['meta_positions']['second']
    for bit in bit_list:  
        while [pos[0],pos[1]] in illegal_pos_list:
            pos = get_next_pos(pos[0],pos[1],size)
        raw_matrix[pos[0]][pos[1]]=bit
        pos = get_next_pos(pos[0],pos[1],size)

    return raw_matrix

