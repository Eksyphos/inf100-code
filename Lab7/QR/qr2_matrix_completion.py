def set_fixed_fields(matrix,qr_layout):
    for zeropos in qr_layout['fixed_positions']['zeros']:
        y,x = zeropos
        matrix[y][x] = 0
    for onepos in qr_layout['fixed_positions']['ones']:
        y,x = onepos
        matrix[y][x] = 1

def set_meta_fields(matrix,err_corr,mask_no,qr_layout):
    pattern = qr_layout['meta_patterns'][err_corr][mask_no]
    keys = ['first','second']
    for key in keys:
        for i,pos in enumerate(qr_layout['meta_positions'][key]):
            y,x = pos
            matrix[y][x] = pattern[i]

if __name__ == '__main__':
    from qr_dummies import sample_masked_matrix
    from qr1_draw import display
    from pathlib import Path
    import json

    # Retrieve sample of premasked matrix without meta/fixed fields
    # and getting the matching config for it.
    matrix, error_correction_level, mask_no = sample_masked_matrix()
    qr_layout = json.loads(Path('qrv2_layout.json').read_text(encoding='utf-8'))

    # Try the functions we have created here
    set_meta_fields(matrix, error_correction_level, mask_no, qr_layout)
    set_fixed_fields(matrix, qr_layout)

    # Draw the picture
    display(matrix)


