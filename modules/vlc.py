# data set tables for CAVLC
# Based on the document of ITU-T Recommendation H.264 05/2003 edition

import numpy as np

def get_nC_table_index(nC):
    """
    Get nC table index according to nC
    Args:
        nC: the nC value
    returns:
        the table index of coeff_token
    """
    table = 0
    if nC>=0 and nC<2:
        table = 0
    elif nC>=2 and nC<4:
        table = 1
    elif nC>=4 and nC<8:
        table = 2
    elif nC>=8:
        table = 3
    elif nC==-1:
        table = 4

    return table

#table 9-5
# Assignment of codeNum to values of coded_block_pattern for macroblock prediction modes
coded_block_pattern = np.array([
[47, 0],   # codeNum = 0
[31, 16],   # codeNum = 1
[15, 1],
[0, 2],
[23, 4],
[27, 8],     # codeNum = 5
[29, 32],
[30, 3],
[7, 5],
[11, 10],
[13, 12], # codeNum = 10
[14, 15],
[39, 47],
[43, 7],
[45, 11],
[46, 13], # codeNum = 15
[16, 14],
[3, 6],
[5, 9],
[10, 31],
[12, 35], # codeNum = 20
[19, 37],
[21, 42],
[26, 44],
[28, 33],
[35, 34], # codeNum = 25
[37, 36],
[42, 40],
[44, 39],
[1, 43],
[2, 45], # codeNum = 30
[4, 46],
[8, 17],
[17, 18],
[18, 20],
[20, 24], # codeNum = 35
[24, 19],
[6, 21],
[9, 26],
[22, 28],
[25, 23], # codeNum = 40
[32, 27],
[33, 29],
[34, 30],
[36, 22],
[40, 25], # codeNum = 45
[38, 38],
[41, 41]
])

#table 9-5
# 4x16x4 matrix of table of coeff_taken
# [nC][TotalCoeff][TrailingOnes]
# nC varies from 0 ~ 3 according to Table 9-5 on page 159
# table0: 0 <= nC < 2
# table1: 2 <= nC < 4
# table2: 4 <= nC < 8
# table3: 8 <= nC
# Notice: '0b' is the prefix for NaluStreamer.py
coeff_token = np.array([
                        #talbe0
                        [['1', '-', '-', '-'], # row = 0
                         ['000101', '01', '-', '-'],
                         ['00000111', '000100', '001', '-'],
                         ['000000111', '00000110', '0000101', '00011'],
                         # row = 4
                         ['0000000111', '000000110', '00000101', '000011'],
                         ['00000000111', '0000000110', '000000101', '0000100'],
                         ['0000000001111', '00000000110', '0000000101', '00000100'],
                         ['0000000001011', '0000000001110', '00000000101', '000000100'],
                         # row = 8
                         ['0000000001000', '0000000001010', '0000000001101', '0000000100'],
                         ['00000000001111', '00000000001110', '0000000001001', '00000000100'],
                         ['00000000001011', '00000000001010', '00000000001101', '0000000001100'],
                         ['000000000001111', '000000000001110', '00000000001001', '00000000001100'],
                         # row = 12
                         ['000000000001011', '000000000001010', '000000000001101', '00000000001000'],
                         ['0000000000001111', '000000000000001', '000000000001001', '000000000001100'],
                         ['0000000000001011', '0000000000001110', '0000000000001101', '000000000001000'],
                         ['0000000000000111', '0000000000001010', '0000000000001001', '0000000000001100'],
                         # row = 16
                         ['0000000000000100', '0000000000000110', '0000000000000101', '0000000000001000'],
                        ],

                        #talbe1
                       [['11', '-', '-', '-'], # row = 0
                         ['001011', '10', '-', '-'],
                         ['000111', '00111', '011', '-'],
                         ['0000111', '001010', '001001', '0101'],
                         # row = 4
                         ['00000111', '000110', '000101', '0100'],
                         ['00000100', '0000110', '0000101', '00110'],
                         ['000000111', '00000110', '00000101', '001000'],
                         ['00000001111', '000000110', '000000101', '000100'],
                         # row = 8
                         ['00000001011', '00000001110', '00000001101', '0000100'],
                         ['000000001111', '00000001010', '00000001001', '000000100'],
                         ['000000001011', '000000001110', '000000001101', '00000001100'],
                         ['000000001000', '000000001010', '000000001001', '00000001000'],
                         # row = 12
                         ['0000000001111', '0000000001110', '0000000001101', '000000001100'],
                         ['0000000001011', '0000000001010', '0000000001001', '0000000001100'],
                         ['0000000000111', '00000000001011', '0000000000110', '0000000001000'],
                         ['00000000001001', '00000000001000', '00000000001010', '0000000000001'],
                         # row = 16
                         ['00000000000111', '00000000000110', '00000000000101', '00000000000100'],
                        ],
                         
                        #talbe2
                       [['1111', '-', '-', '-'], # row = 0
                         ['001111', '1110', '-', '-'],
                         ['001011', '01111', '1101', '-'],
                         ['001000', '01100', '01110', '1100'],
                         # row = 4
                         ['0001111', '01010', '01011', '1011'],
                         ['0001011', '01000', '01001', '1010'],
                         ['0001001', '001110', '001101', '1001'],
                         ['0001000', '001010', '001001', '1000'],
                         # row = 8
                         ['00001111', '0001110', '0001101', '01101'],
                         ['00001011', '00001110', '0001010', '001100'],
                         ['000001111', '00001010', '00001101', '0001100'],
                         ['000001011', '000001110', '00001001', '00001100'],
                         # row = 12
                         ['000001000', '000001010', '000001101', '00001000'],
                         ['0000001101', '000000111', '000001001', '000001100'],
                         ['0000001001', '0000001100', '0000001011', '0000001010'],
                         ['0000000101', '0000001000', '0000000111', '0000000110'],
                         # row = 16
                         ['0000000001', '0000000100', '0000000011', '0000000010'],
                        ],

                        #talbe3
                       [['000011', '-', '-', '-'], # row = 0
                         ['000000', '000001', '-', '-'],
                         ['000100', '000101', '000110', '-'],
                         ['001000', '001001', '001010', '001011'],
                         # row = 4
                         ['001100', '001101', '001110', '001111'],
                         ['010000', '010001', '010010', '010011'],
                         ['010100', '010101', '010110', '010111'],
                         ['011000', '011001', '011010', '011011'],
                         # row = 8
                         ['011100', '011101', '011110', '011111'],
                         ['100000', '100001', '100010', '100011'],
                         ['100100', '100101', '100110', '100111'],
                         ['101000', '101001', '101010', '101011'],
                         # row = 12
                         ['101100', '101101', '101110', '101111'],
                         ['110000', '110001', '110010', '110011'],
                         ['110100', '110101', '110110', '110111'],
                         ['111000', '111001', '111010', '111011'],
                         # row = 16
                         ['111100', '111101', '111110', '111111'],
                        ],

                        #talbe4
                       [['01', '-', '-', '-'], # row = 0
                         ['000111', '1', '-', '-'],
                         ['000100', '000110', '001', '-'],
                         ['000011', '0000011', '0000010', '000101'],
                         # row = 4
                         ['000010', '00000011', '00000010', '0000000'],
                         ['-', '-', '-', '-'],
                         ['-', '-', '-', '-'],
                         ['-', '-', '-', '-'],
                         # row = 8
                         ['-', '-', '-', '-'],
                         ['-', '-', '-', '-'],
                         ['-', '-', '-', '-'],
                         ['-', '-', '-', '-'],
                         # row = 12
                         ['-', '-', '-', '-'],
                         ['-', '-', '-', '-'],
                         ['-', '-', '-', '-'],
                         ['-', '-', '-', '-'],
                         # row = 16
                         ['-', '-', '-', '-'],
                        ],

                        ])

#table 9-6
level_prefix = np.array(['1',
                         '01',
                         '001',
                         '0001',
                         '00001',   #4
                         '000001',
                         '0000001',
                         '00000001',
                         '000000001', #8
                         '0000000001',
                         '00000000001',
                         '000000000001',
                         '0000000000001', #12
                         '00000000000001', 
                         '000000000000001',
                         '0000000000000001'])

#table 9-7 & 9-8
# [total_zeros][total_coeff]
total_zeros = np.array([['-', '1', '111', '0101', '00011', '0101', '000001', '000001', '000001', '000001', '00001', '0000', '0000', '000', '00', '0'],
                        ['-', '011', '110', '111', '111', '0100', '00001', '00001', '0001', '000000', '00000', '0001', '0001', '001', '01', '1'],
                        ['-', '010', '101', '110', '0101', '0011', '111', '101', '00001', '0001', '001', '001', '01', '1', '1', '-'],
                        ['-', '0011', '100', '101', '0100', '111', '110', '100', '011', '11', '11', '010', '1', '01', '-', '-'],
                        # row 4
                        ['-', '0010', '011', '0100', '110', '110', '101', '011', '11', '10', '10', '1', '001', '-', '-', '-'],
                        ['-', '00011', '0101', '0011', '101', '101', '100', '11', '10', '001', '01', '011', '-', '-', '-', '-'],
                        ['-', '00010', '0100', '100', '100', '100', '011', '010', '010', '01', '0001', '-', '-', '-', '-', '-'],
                        ['-', '000011', '0011', '011', '0011', '011', '010', '0001', '001', '00001', '-', '-', '-', '-', '-', '-'],
                        # row 8
                        ['-', '000010', '0010', '0010', '011', '0010', '0001', '001', '000000', '-', '-', '-', '-', '-', '-', '-'],
                        ['-', '0000011', '00011', '00011', '0010', '00001', '001', '000000', '-', '-', '-', '-', '-', '-', '-', '-'],
                        ['-', '0000010', '00010', '00010', '00010', '0001', '000000', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                        ['-', '00000011', '000011', '000001', '00001', '00000', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                        # row 12
                        ['-', '00000010', '000010', '00001', '00000', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                        ['-', '000000011', '000001', '000000', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                        ['-', '000000010', '000000', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],
                        ['-', '000000001', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
                        ])

#table 9-9
# [total_zeros][total_coeff]
total_zeros_2x2 = np.array([['-', '1', '1', '1'],
                            ['-', '01', '01', '0'],
                            ['-', '001', '00', '-'],
                            ['-', '000', '-', '-'],
                            ])

#table 9-10
# [run_before][zerosLeft]
run_before = np.array([['-', '1', '1', '11', '11', '11', '11', '111'],
                       ['-', '0', '01', '10', '10', '10', '000', '110'],
                       ['-', '-', '00', '01', '01', '011', '001', '101'],
                       ['-', '-', '-', '00', '001', '010', '011', '100'],
                       # row 4
                       ['-', '-', '-', '-', '000', '001', '010', '011'],
                       ['-', '-', '-', '-', '-', '000', '101', '010'],
                       ['-', '-', '-', '-', '-', '-', '100', '001'],
                       ['-', '-', '-', '-', '-', '-', '-', '0001'],
                       # row 8
                       ['-', '-', '-', '-', '-', '-', '-', '00001'],
                       ['-', '-', '-', '-', '-', '-', '-', '000001'],
                       ['-', '-', '-', '-', '-', '-', '-', '0000001'],
                       ['-', '-', '-', '-', '-', '-', '-', '00000001'],
                       # row 12
                       ['-', '-', '-', '-', '-', '-', '-', '000000001'],
                       ['-', '-', '-', '-', '-', '-', '-', '0000000001'],
                       ['-', '-', '-', '-', '-', '-', '-', '00000000001']
                       ])

if __name__ == "__main__":
    print(coeff_token.shape)
    print(coeff_token)
    print(coeff_token[0][0][0])
    print(coeff_token[0][2][1])
    print(coeff_token[0][8][1])
    print(type(coeff_token[0][0][0]))

    print(level_prefix[2])
    print(total_zeros[9][6])

    print(total_zeros[0])
    print(total_zeros[0][0])

    result = np.where(coeff_token[0] == '00000000100')
    print('Tuple of arrays returned : ', result[0], result[1])
    print(coeff_token[0][9][3])

    country = np.array([['USA', 'Japan', 'UK', '', 'India', '-'],
                        ['USA2', 'Japan2', 'UK2', '233', 'India2', 'China2']]) 
    temp = np.where(country == 'Japan2')
    print('Country finding result: ', temp)
    print(country[temp])