from qr2_matrix_completion import set_fixed_fields,set_meta_fields

def should_flip(row,col,mask_no):
    masks = {
        '0':mask0,
        '1':mask1,
        '2':mask2,
        '3':mask3,
        '4':mask4,
        '5':mask5,
        '6':mask6,
        '7':mask7,
    }
    func =masks[str(mask_no)]
    return func(row,col)

def get_masked_matrix(matrix,mask_no):
    new_matrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]
    for irow,row in enumerate(matrix):
        for icol,col in enumerate(row):
            if should_flip(irow,icol,mask_no):
                new_matrix[irow][icol] = int(not col)
            else:
                new_matrix[irow][icol] = col

    return new_matrix

def get_refined_matrix(raw_matrix,error_correction_level,qr_layout):
    best_score = 999
    best_matrix = []
    
    for i in range(8):
        masked_matrix=get_masked_matrix(raw_matrix,str(i))
        
        set_meta_fields(masked_matrix,error_correction_level,i,qr_layout)
        set_fixed_fields(masked_matrix,qr_layout)

        score = score_matrix(masked_matrix)
        if score<best_score:
            best_matrix=masked_matrix
            best_score=score
    return best_matrix



def score_matrix(matrix):
    diff = 0
    for row in matrix:
        for col in row:
            if col ==1:
                diff +=1
            else:
                diff -=1
    return abs(diff)

############# MASKER ###############
def mask0(row,col):
    if (row + col) % 2 == 0:
        return True
def mask1(row,col):
    if row % 2 == 0:
        return True
def mask2(row,col):
    if col % 3 == 0:
        return True
def mask3(row,col):
    if (row + col) % 3 == 0:
        return True
def mask4(row,col):
    if (row//2 + col//3) % 2 == 0:
        return True
def mask5(row,col):
    if (row*col) % 2 + (row*col) % 3 == 0:
        return True
def mask6(row,col):
    if ((row*col) % 2 + (row*col) % 3) % 2 == 0:
        return True
def mask7(row,col):
    if ((row+col) % 2 + (row*col) % 3) % 2 == 0:
        return True 