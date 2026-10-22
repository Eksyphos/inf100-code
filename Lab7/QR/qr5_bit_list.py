from qr6_error_correction import generate_error_correction

def string_to_data(content_string):
    bit_list = ''
    for letter in str(content_string):
        asciinumber = ord(letter)
        binarynumber = f'{asciinumber:08b}'
        bit_list+=binarynumber
    return bit_list

def get_core_bit_list(content_string):
    modus = '0100'
    data = string_to_data(content_string)
    lengde = f'{len(content_string):08b}'
    terminator = '0000'
    bit_list = [int(x) for x in f'{modus}{lengde}{data}{terminator}']
    return bit_list

def pad_bit_list(core_bit_list,pad_to_bytes):
    count = 0
    padding1 = [1, 1, 1, 0, 1, 1, 0, 0]
    padding2 = [0, 0, 0, 1, 0, 0, 0, 1]
    while len(core_bit_list)<pad_to_bytes*8:
        if count%2:
            core_bit_list += padding2
        else:
            core_bit_list += padding1
        count+=1

def string_to_bit_list(content_string,qr_layout):
    bit_liste = get_core_bit_list(content_string)
    available_bits = int((352-len(bit_liste))/8)
    if available_bits>=qr_layout['error_correction_bytes']['H']:
        feilretting = 'H'
    elif available_bits>=qr_layout['error_correction_bytes']['Q']:
        feilretting = 'Q'
    elif available_bits>=qr_layout['error_correction_bytes']['M']:
        feilretting = 'M'
    elif available_bits>=qr_layout['error_correction_bytes']['L']:
        feilretting = 'L'
    else:
        return OverflowError

    padding_bytes = (available_bits/8)-qr_layout['error_correction_bytes'][feilretting]
    pad_bit_list(bit_liste,padding_bytes)
    ferdig_liste = generate_error_correction(bit_liste,feilretting)


    return(ferdig_liste,feilretting)