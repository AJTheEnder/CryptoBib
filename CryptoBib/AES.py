from sage.all import *
import annuaireConversion as AC

'''
||==============================================||
||                 Constantes                   ||
||==============================================||
'''

S_BOX = [
    ['0x63', '0x7c', '0x77', '0x7b', '0xf2', '0x6b', '0x6f', '0xc5', '0x30', '0x01', '0x67', '0x2b', '0xfe', '0xd7', '0xab', '0x76'],
    ['0xca', '0x82', '0xc9', '0x7d', '0xfa', '0x59', '0x47', '0xf0', '0xad', '0xd4', '0xa2', '0xaf', '0x9c', '0xa4', '0x72', '0xc0'],
    ['0xb7', '0xfd', '0x93', '0x26', '0x36', '0x3f', '0xf7', '0xcc', '0x34', '0xa5', '0xe5', '0xf1', '0x71', '0xd8', '0x31', '0x15'],
    ['0x04', '0xc7', '0x23', '0xc3', '0x18', '0x96', '0x05', '0x9a', '0x07', '0x12', '0x80', '0xe2', '0xeb', '0x27', '0xb2', '0x75'],
    ['0x09', '0x83', '0x2c', '0x1a', '0x1b', '0x6e', '0x5a', '0xa0', '0x52', '0x3b', '0xd6', '0xb3', '0x29', '0xe3', '0x2f', '0x84'],
    ['0x53', '0xd1', '0x00', '0xed', '0x20', '0xfc', '0xb1', '0x5b', '0x6a', '0xcb', '0xbe', '0x39', '0x4a', '0x4c', '0x58', '0xcf'],
    ['0xd0', '0xef', '0xaa', '0xfb', '0x43', '0x4d', '0x33', '0x85', '0x45', '0xf9', '0x02', '0x7f', '0x50', '0x3c', '0x9f', '0xa8'],
    ['0x51', '0xa3', '0x40', '0x8f', '0x92', '0x9d', '0x38', '0xf5', '0xbc', '0xb6', '0xda', '0x21', '0x10', '0xff', '0xf3', '0xd2'],
    ['0xcd', '0x0c', '0x13', '0xec', '0x5f', '0x97', '0x44', '0x17', '0xc4', '0xa7', '0x7e', '0x3d', '0x64', '0x5d', '0x19', '0x73'],
    ['0x60', '0x81', '0x4f', '0xdc', '0x22', '0x2a', '0x90', '0x88', '0x46', '0xee', '0xb8', '0x14', '0xde', '0x5e', '0x0b', '0xdb'],
    ['0xe0', '0x32', '0x3a', '0x0a', '0x49', '0x06', '0x24', '0x5c', '0xc2', '0xd3', '0xac', '0x62', '0x91', '0x95', '0xe4', '0x79'],
    ['0xe7', '0xc8', '0x37', '0x6d', '0x8d', '0xd5', '0x4e', '0xa9', '0x6c', '0x56', '0xf4', '0xea', '0x65', '0x7a', '0xae', '0x08'],
    ['0xba', '0x78', '0x25', '0x2e', '0x1c', '0xa6', '0xb4', '0xc6', '0xe8', '0xdd', '0x74', '0x1f', '0x4b', '0xbd', '0x8b', '0x8a'],
    ['0x70', '0x3e', '0xb5', '0x66', '0x48', '0x03', '0xf6', '0x0e', '0x61', '0x35', '0x57', '0xb9', '0x86', '0xc1', '0x1d', '0x9e'],
    ['0xe1', '0xf8', '0x98', '0x11', '0x69', '0xd9', '0x8e', '0x94', '0x9b', '0x1e', '0x87', '0xe9', '0xce', '0x55', '0x28', '0xdf'],
    ['0x8c', '0xa1', '0x89', '0x0d', '0xbf', '0xe6', '0x42', '0x68', '0x41', '0x99', '0x2d', '0x0f', '0xb0', '0x54', '0xbb', '0x16']
]

TABLE_9 = [
    ['0x00', '0x09', '0x12', '0x1b', '0x24', '0x2d', '0x36', '0x3f', '0x48', '0x41', '0x5a', '0x53', '0x6c', '0x65', '0x7e', '0x77'],
    ['0x90', '0x99', '0x82', '0x8b', '0xb4', '0xbd', '0xa6', '0xaf', '0xd8', '0xd1', '0xca', '0xc3', '0xfc', '0xf5', '0xee', '0xe7'],
    ['0x3b', '0x32', '0x29', '0x20', '0x1f', '0x16', '0x0d', '0x04', '0x73', '0x7a', '0x61', '0x68', '0x57', '0x5e', '0x45', '0x4c'],
    ['0xab', '0xa2', '0xb9', '0xb0', '0x8f', '0x86', '0x9d', '0x94', '0xe3', '0xea', '0xf1', '0xf8', '0xc7', '0xce', '0xd5', '0xdc'],
    ['0x76', '0x7f', '0x64', '0x6d', '0x52', '0x5b', '0x40', '0x49', '0x3e', '0x37', '0x2c', '0x25', '0x1a', '0x13', '0x08', '0x01'],
    ['0xe6', '0xef', '0xf4', '0xfd', '0xc2', '0xcb', '0xd0', '0xd9', '0xae', '0xa7', '0xbc', '0xb5', '0x8a', '0x83', '0x98', '0x91'],
    ['0x4d', '0x44', '0x5f', '0x56', '0x69', '0x60', '0x7b', '0x72', '0x05', '0x0c', '0x17', '0x1e', '0x21', '0x28', '0x33', '0x3a'],
    ['0xdd', '0xd4', '0xcf', '0xc6', '0xf9', '0xf0', '0xeb', '0xe2', '0x95', '0x9c', '0x87', '0x8e', '0xb1', '0xb8', '0xa3', '0xaa'],	
    ['0xec', '0xe5', '0xfe', '0xf7', '0xc8', '0xc1', '0xda', '0xd3', '0xa4', '0xad', '0xb6', '0xbf', '0x80', '0x89', '0x92', '0x9b'],	
    ['0x7c', '0x75', '0x6e', '0x67', '0x58', '0x51', '0x4a', '0x43', '0x34', '0x3d', '0x26', '0x2f', '0x10', '0x19', '0x02', '0x0b'],
    ['0xd7', '0xde', '0xc5', '0xcc', '0xf3', '0xfa', '0xe1', '0xe8', '0x9f', '0x96', '0x8d', '0x84', '0xbb', '0xb2', '0xa9', '0xa0'],
    ['0x47', '0x4e', '0x55', '0x5c', '0x63', '0x6a', '0x71', '0x78', '0x0f', '0x06', '0x1d', '0x14', '0x2b', '0x22', '0x39', '0x30'],
    ['0x9a', '0x93', '0x88', '0x81', '0xbe', '0xb7', '0xac', '0xa5', '0xd2', '0xdb', '0xc0', '0xc9', '0xf6', '0xff', '0xe4', '0xed'],
    ['0x0a', '0x03', '0x18', '0x11', '0x2e', '0x27', '0x3c', '0x35', '0x42', '0x4b', '0x50', '0x59', '0x66', '0x6f', '0x74', '0x7d'],	
    ['0xa1', '0xa8', '0xb3', '0xba', '0x85', '0x8c', '0x97', '0x9e', '0xe9', '0xe0', '0xfb', '0xf2', '0xcd', '0xc4', '0xdf', '0xd6'],
    ['0x31', '0x38', '0x23', '0x2a', '0x15', '0x1c', '0x07', '0x0e', '0x79', '0x70', '0x6b', '0x62', '0x5d', '0x54', '0x4f', '0x46']
]

TABLE_11 = [
    ['0x00', '0x0b', '0x16', '0x1d', '0x2c', '0x27', '0x3a', '0x31', '0x58', '0x53', '0x4e', '0x45', '0x74', '0x7f', '0x62', '0x69'],
    ['0xb0', '0xbb', '0xa6', '0xad', '0x9c', '0x97', '0x8a', '0x81', '0xe8', '0xe3', '0xfe', '0xf5', '0xc4', '0xcf', '0xd2', '0xd9'],
    ['0x7b', '0x70', '0x6d', '0x66', '0x57', '0x5c', '0x41', '0x4a', '0x23', '0x28', '0x35', '0x3e', '0x0f', '0x04', '0x19', '0x12'],
    ['0xcb', '0xc0', '0xdd', '0xd6', '0xe7', '0xec', '0xf1', '0xfa', '0x93', '0x98', '0x85', '0x8e', '0xbf', '0xb4', '0xa9', '0xa2'],
    ['0xf6', '0xfd', '0xe0', '0xeb', '0xda', '0xd1', '0xcc', '0xc7', '0xae', '0xa5', '0xb8', '0xb3', '0x82', '0x89', '0x94', '0x9f'],
    ['0x46', '0x4d', '0x50', '0x5b', '0x6a', '0x61', '0x7c', '0x77', '0x1e', '0x15', '0x08', '0x03', '0x32', '0x39', '0x24', '0x2f'],
    ['0x8d', '0x86', '0x9b', '0x90', '0xa1', '0xaa', '0xb7', '0xbc', '0xd5', '0xde', '0xc3', '0xc8', '0xf9', '0xf2', '0xef', '0xe4'],
    ['0x3d', '0x36', '0x2b', '0x20', '0x11', '0x1a', '0x07', '0x0c', '0x65', '0x6e', '0x73', '0x78', '0x49', '0x42', '0x5f', '0x54'],
    ['0xf7', '0xfc', '0xe1', '0xea', '0xdb', '0xd0', '0xcd', '0xc6', '0xaf', '0xa4', '0xb9', '0xb2', '0x83', '0x88', '0x95', '0x9e'],
    ['0x47', '0x4c', '0x51', '0x5a', '0x6b', '0x60', '0x7d', '0x76', '0x1f', '0x14', '0x09', '0x02', '0x33', '0x38', '0x25', '0x2e'],
    ['0x8c', '0x87', '0x9a', '0x91', '0xa0', '0xab', '0xb6', '0xbd', '0xd4', '0xdf', '0xc2', '0xc9', '0xf8', '0xf3', '0xee', '0xe5'],
    ['0x3c', '0x37', '0x2a', '0x21', '0x10', '0x1b', '0x06', '0x0d', '0x64', '0x6f', '0x72', '0x79', '0x48', '0x43', '0x5e', '0x55'],
    ['0x01', '0x0a', '0x17', '0x1c', '0x2d', '0x26', '0x3b', '0x30', '0x59', '0x52', '0x4f', '0x44', '0x75', '0x7e', '0x63', '0x68'],
    ['0xb1', '0xba', '0xa7', '0xac', '0x9d', '0x96', '0x8b', '0x80', '0xe9', '0xe2', '0xff', '0xf4', '0xc5', '0xce', '0xd3', '0xd8'],
    ['0x7a', '0x71', '0x6c', '0x67', '0x56', '0x5d', '0x40', '0x4b', '0x22', '0x29', '0x34', '0x3f', '0x0e', '0x05', '0x18', '0x13'],
    ['0xca', '0xc1', '0xdc', '0xd7', '0xe6', '0xed', '0xf0', '0xfb', '0x92', '0x99', '0x84', '0x8f', '0xbe', '0xb5', '0xa8', '0xa3']
]

TABLE_13 = [
    ['0x00', '0x0d', '0x1a', '0x17', '0x34', '0x39', '0x2e', '0x23', '0x68', '0x65', '0x72', '0x7f', '0x5c', '0x51', '0x46', '0x4b'],
    ['0xd0', '0xdd', '0xca', '0xc7', '0xe4', '0xe9', '0xfe', '0xf3', '0xb8', '0xb5', '0xa2', '0xaf', '0x8c', '0x81', '0x96', '0x9b'],
    ['0xbb', '0xb6', '0xa1', '0xac', '0x8f', '0x82', '0x95', '0x98', '0xd3', '0xde', '0xc9', '0xc4', '0xe7', '0xea', '0xfd', '0xf0'],
    ['0x6b', '0x66', '0x71', '0x7c', '0x5f', '0x52', '0x45', '0x48', '0x03', '0x0e', '0x19', '0x14', '0x37', '0x3a', '0x2d', '0x20'],
    ['0x6d', '0x60', '0x77', '0x7a', '0x59', '0x54', '0x43', '0x4e', '0x05', '0x08', '0x1f', '0x12', '0x31', '0x3c', '0x2b', '0x26'],
    ['0xbd', '0xb0', '0xa7', '0xaa', '0x89', '0x84', '0x93', '0x9e', '0xd5', '0xd8', '0xcf', '0xc2', '0xe1', '0xec', '0xfb', '0xf6'],
    ['0xd6', '0xdb', '0xcc', '0xc1', '0xe2', '0xef', '0xf8', '0xf5', '0xbe', '0xb3', '0xa4', '0xa9', '0x8a', '0x87', '0x90', '0x9d'],
    ['0x06', '0x0b', '0x1c', '0x11', '0x32', '0x3f', '0x28', '0x25', '0x6e', '0x63', '0x74', '0x79', '0x5a', '0x57', '0x40', '0x4d'],
    ['0xda', '0xd7', '0xc0', '0xcd', '0xee', '0xe3', '0xf4', '0xf9', '0xb2', '0xbf', '0xa8', '0xa5', '0x86', '0x8b', '0x9c', '0x91'],
    ['0x0a', '0x07', '0x10', '0x1d', '0x3e', '0x33', '0x24', '0x29', '0x62', '0x6f', '0x78', '0x75', '0x56', '0x5b', '0x4c', '0x41'],
    ['0x61', '0x6c', '0x7b', '0x76', '0x55', '0x58', '0x4f', '0x42', '0x09', '0x04', '0x13', '0x1e', '0x3d', '0x30', '0x27', '0x2a'],
    ['0xb1', '0xbc', '0xab', '0xa6', '0x85', '0x88', '0x9f', '0x92', '0xd9', '0xd4', '0xc3', '0xce', '0xed', '0xe0', '0xf7', '0xfa'],
    ['0xb7', '0xba', '0xad', '0xa0', '0x83', '0x8e', '0x99', '0x94', '0xdf', '0xd2', '0xc5', '0xc8', '0xeb', '0xe6', '0xf1', '0xfc'],
    ['0x67', '0x6a', '0x7d', '0x70', '0x53', '0x5e', '0x49', '0x44', '0x0f', '0x02', '0x15', '0x18', '0x3b', '0x36', '0x21', '0x2c'],
    ['0x0c', '0x01', '0x16', '0x1b', '0x38', '0x35', '0x22', '0x2f', '0x64', '0x69', '0x7e', '0x73', '0x50', '0x5d', '0x4a', '0x47'],
    ['0xdc', '0xd1', '0xc6', '0xcb', '0xe8', '0xe5', '0xf2', '0xff', '0xb4', '0xb9', '0xae', '0xa3', '0x80', '0x8d', '0x9a', '0x97']
]

TABLE_14 = [
    ['0x00', '0x0e', '0x1c', '0x12', '0x38', '0x36', '0x24', '0x2a', '0x70', '0x7e', '0x6c', '0x62', '0x48', '0x46', '0x54', '0x5a'],
    ['0xe0', '0xee', '0xfc', '0xf2', '0xd8', '0xd6', '0xc4', '0xca', '0x90', '0x9e', '0x8c', '0x82', '0xa8', '0xa6', '0xb4', '0xba'],
    ['0xdb', '0xd5', '0xc7', '0xc9', '0xe3', '0xed', '0xff', '0xf1', '0xab', '0xa5', '0xb7', '0xb9', '0x93', '0x9d', '0x8f', '0x81'],
    ['0x3b', '0x35', '0x27', '0x29', '0x03', '0x0d', '0x1f', '0x11', '0x4b', '0x45', '0x57', '0x59', '0x73', '0x7d', '0x6f', '0x61'],
    ['0xad', '0xa3', '0xb1', '0xbf', '0x95', '0x9b', '0x89', '0x87', '0xdd', '0xd3', '0xc1', '0xcf', '0xe5', '0xeb', '0xf9', '0xf7'],
    ['0x4d', '0x43', '0x51', '0x5f', '0x75', '0x7b', '0x69', '0x67', '0x3d', '0x33', '0x21', '0x2f', '0x05', '0x0b', '0x19', '0x17'],
    ['0x76', '0x78', '0x6a', '0x64', '0x4e', '0x40', '0x52', '0x5c', '0x06', '0x08', '0x1a', '0x14', '0x3e', '0x30', '0x22', '0x2c'],
    ['0x96', '0x98', '0x8a', '0x84', '0xae', '0xa0', '0xb2', '0xbc', '0xe6', '0xe8', '0xfa', '0xf4', '0xde', '0xd0', '0xc2', '0xcc'],
    ['0x41', '0x4f', '0x5d', '0x53', '0x79', '0x77', '0x65', '0x6b', '0x31', '0x3f', '0x2d', '0x23', '0x09', '0x07', '0x15', '0x1b'],
    ['0xa1', '0xaf', '0xbd', '0xb3', '0x99', '0x97', '0x85', '0x8b', '0xd1', '0xdf', '0xcd', '0xc3', '0xe9', '0xe7', '0xf5', '0xfb'],
    ['0x9a', '0x94', '0x86', '0x88', '0xa2', '0xac', '0xbe', '0xb0', '0xea', '0xe4', '0xf6', '0xf8', '0xd2', '0xdc', '0xce', '0xc0'],
    ['0x7a', '0x74', '0x66', '0x68', '0x42', '0x4c', '0x5e', '0x50', '0x0a', '0x04', '0x16', '0x18', '0x32', '0x3c', '0x2e', '0x20'],
    ['0xec', '0xe2', '0xf0', '0xfe', '0xd4', '0xda', '0xc8', '0xc6', '0x9c', '0x92', '0x80', '0x8e', '0xa4', '0xaa', '0xb8', '0xb6'],
    ['0x0c', '0x02', '0x10', '0x1e', '0x34', '0x3a', '0x28', '0x26', '0x7c', '0x72', '0x60', '0x6e', '0x44', '0x4a', '0x58', '0x56'],
    ['0x37', '0x39', '0x2b', '0x25', '0x0f', '0x01', '0x13', '0x1d', '0x47', '0x49', '0x5b', '0x55', '0x7f', '0x71', '0x63', '0x6d'],
    ['0xd7', '0xd9', '0xcb', '0xc5', '0xef', '0xe1', '0xf3', '0xfd', '0xa7', '0xa9', '0xbb', '0xb5', '0x9f', '0x91', '0x83', '0x8d']
]

RIJNDAEL_MATRIX = sage.all.matrix([
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
])

RIJNDAEL_INVERSE_MATRIX = sage.all.matrix([
    [14, 11, 13, 9],
    [9, 14, 11, 13],
    [13, 9, 14, 11],
    [11, 13, 9, 14]
])

PX = [1, 0, 0, 0, 1, 1, 0, 1, 1]

RCON = [[0, 0, 0, 0, 0, 0, 0, 1], 
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 1, 1],
        [0, 0, 1, 1, 0, 1, 1, 0],
]

'''
||==============================================||
||           Fonctions de la clé AES            ||
||==============================================||
'''
class CleAES :
    '''
  <<===========Constructeur clé AES===========>>
    '''
    def __init__(self, cle) :
        #Conversion de la clé en code ASCII
        asciiCle = AC.conversionCharTo(cle, 'a')
        matriceCle = sage.all.matrix(4, 4)
        #Initialisation d'un index qui servira à suivre l'avancement dans la chaine
        indexStrCle = 0
        #Remplissage de la matrice avec les codes ascii récupérés
        for i in range(4) :
            for j in range(4) :
                matriceCle[i, j] = asciiCle[indexStrCle]
                indexStrCle += 1
        self.originalCle = matriceCle 
        self.subCleList = []
        self.currentKey = self.originalCle
        
    '''
  <<===========Fonction KeySchedule===========>>
    '''  
    def keySchedule(self) :
        for key in range(10) :
            #Création d'un sous-clé vide
            subKey = sage.all.matrix([[0, 0, 0, 0],
                                      [0, 0, 0, 0],
                                      [0, 0, 0, 0],
                                      [0, 0, 0, 0],])
            
            #Shuffle de la première colonne de la current key
            subKey[0, 0] = self.currentKey[1][3] 
            subKey[1, 0] = self.currentKey[2][3]
            subKey[2, 0] = self.currentKey[3][3]
            subKey[3, 0] = self.currentKey[1][3]  
            
            #Pour chaque élément de la 1ère colonne
            for i in range(4) :
                #Transformation d'un nombre en liste de 1 nombre (pour la conversion)
                preConversion = [subKey[i][0]]
                
                #Conversion de ce nombre en son équivalent hexadécimal
                hexByte = AC.conversionASCIITo(preConversion, 'h')
                
                if (len(hexByte[0]) != 2) :
                    hexByte[0] = '0' + hexByte[0]
                
                #Séparation des 2 composant du nombre hexadécimal en les convertissant en int
                indiceByte0 = int((hexByte[0][0]), 16)
                indiceByte1 = int((hexByte[0][1]), 16)
                
                #Remplacement de l'élément de la matrice par son équivalent dans la S_BOX
                subKey[i, 0] = int(S_BOX[indiceByte0][indiceByte1], 16)
                
                #Initialisation d'une liste qui servira au calcul de l'élément final
                #Notament pour l'opération XOR
                counterTab = [0, 0, 0, 0, 0, 0, 0, 0]           
                            # 7, 6, 5, 4, 3, 2, 1, 0      
                            #[ 2eme bin ][ 1er bin  ]
            
                #Conversion de l'élément i de la première colonne de la subKey en binaire
                binaryDataSubKey = format(subKey[i][0], 'b')               
                listBinarySubKey = []
                
                #Conversion de l'élément i de la première colonne de la currentKey en binaire
                binaryDataCurrentKey = format(self.currentKey[i][0], 'b')
                listBinaryCurrentKey = []
                
                #Remplissage de la liste de chiffre binaire jusqu'à une longueur de 8
                for b in range(len(binaryDataSubKey)) :
                    listBinarySubKey.append(binaryDataSubKey[b])
                while (len(listBinarySubKey) != 8) :
                    #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                    listBinarySubKey.insert(0, '0')
                    
                #Remplissage de la liste de chiffre binaire jusqu'à une longueur de 8
                for b in range(len(binaryDataCurrentKey)) :
                    listBinaryCurrentKey.append(binaryDataCurrentKey[b])
                while (len(listBinaryCurrentKey) != 8) :
                    #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                    listBinaryCurrentKey.insert(0, '0')
                    
                #Pour chaque chiffre binaire de la liste
                for b in range(8) :
                    #Opérations dans la counterList pour connaitre le binaire de fin
                    if (i == 0) :
                        counterTab[b] += RCON[key][b]
                    if (listBinaryCurrentKey[b] == '1') :
                        counterTab[b] += 1
                    if (listBinarySubKey[b] == '1') :
                        counterTab[b] += 1
                        
                #Quand un élément de la liste est impair mettre 1 sinon mettre 0
                for b in range(len(counterTab)) :
                    if (counterTab[b] % 2 == 1) :
                        counterTab[b] = 1
                    else :
                        counterTab[b] = 0
                        
                #Conversion du chiffre binaire final en int
                finalBinary = '0b'
                for b in range(len(counterTab)) :
                    counterTab[b] = str(counterTab[b])
                    finalBinary += counterTab[b]                        
                finalNumber = int(finalBinary, 2)
                #Remplacement de l'ancienne valeur par la nouvelle
                subKey[i, 0] = finalNumber
            
            for column in range(1, 4) :
                for j in range(4) :
                    #Conversion de l'élément j de la "column - 1" colonne de la subKey en binaire
                    binaryDataSubKey = format(subKey[j][column - 1], 'b')               
                    listBinarySubKey = []
                    
                    #Conversion de l'élément j de la "column" colonne de la currentKey en binaire
                    binaryDataCurrentKey = format(self.currentKey[j][column], 'b')
                    listBinaryCurrentKey = []
                    
                    #Remplissage de la liste de chiffre binaire jusqu'à une longueur de 8
                    for b in range(len(binaryDataSubKey)) :
                        listBinarySubKey.append(binaryDataSubKey[b])
                    while (len(listBinarySubKey) != 8) :
                        #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                        listBinarySubKey.insert(0, '0')

                    #Remplissage de la liste de chiffre binaire jusqu'à une longueur de 8
                    for b in range(len(binaryDataCurrentKey)) :
                        listBinaryCurrentKey.append(binaryDataCurrentKey[b])
                    while (len(listBinaryCurrentKey) != 8) :
                        #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                        listBinaryCurrentKey.insert(0, '0')
                        
                    #Calcul et conversion du chiffre binaire final en int
                    finalBinary = '0b'
                    for b in range(8) :
                        if (listBinarySubKey[b] != listBinaryCurrentKey[b]) :
                            finalBinary += '1'
                        else :
                            finalBinary += '0'
                    finalNumber = int(finalBinary, 2)
                    #Remplacement de l'ancienne valeur par la nouvelle
                    subKey[j, column] = finalNumber
                
            self.subCleList.append(subKey)
            self.currentKey = subKey
        self.currentKey = self.originalCle
        


'''
||==============================================||
||           Fonctions du message AES           ||
||==============================================||
'''            
class MessageAES :
    '''
  <<=========Constructeur message AES=========>>
    '''
    def __init__(self, message) :        
        self.messageHacher = []
        #Conversion du message en code ASCII
        asciiMessage = AC.conversionCharTo(message, 'a')
        #Initialisation d'un index qui servira à suivre l'avancement dans la chaine
        indexStrMessage = 0
        
        #Pour chaque blocks complet de 16 caractères que contient le message
        for parts in range(len(asciiMessage) // 16) :
            #On créé une matrice 4x4
            matricePartieMessage = sage.all.matrix(4, 4)
            
            #Remplissage de la matrice avec les codes ascii récupérés
            for i in range(4) :
                for j in range(4) :
                    matricePartieMessage[i, j] = asciiMessage[indexStrMessage]
                    indexStrMessage += 1
            
            self.messageHacher.append(matricePartieMessage)    
        
        #Si le message contient de un dernier block qui ne contient pas 16 caractères
        if(len(asciiMessage) % 16 != 0) :   
            #On créé une matrice 4x4
            matricePartieMessage = sage.all.matrix(4, 4)
            
            #Que l'on rempli des codes ascii ou de 32 (ascii code de l'espace)
            for i in range(4) :
                for j in range(4) :
                    
                    #Remplissage d'espaces
                    if(indexStrMessage >= len(asciiMessage)) :
                        matricePartieMessage[i, j] = 32
                    #Remplissage avec les codes ascii
                    else :
                        matricePartieMessage[i, j] = asciiMessage[indexStrMessage]
                    
                    indexStrMessage += 1
            
            self.messageHacher.append(matricePartieMessage)

    '''
  <<============Fonction SubBytes=============>>
    '''   
    def subBytes(self) :
        #Pour chaque matrice du message
        for messageParts in range(len(self.messageHacher)) :
            #Pour chaque élément de la matrice
            for i in range(4) :
                for j in range(4) :
                    #Transformation d'un nombre en liste de 1 nombre (pour la conversion)
                    preConversion = [self.messageHacher[messageParts][i, j]]
                    
                    #Conversion de ce nombre en son équivalent hexadécimal
                    hexByte = AC.conversionASCIITo(preConversion, 'h')
                    
                    if (len(hexByte[0]) != 2) :
                        hexByte[0] = '0' + hexByte[0]
                    
                    #Séparation des 2 composant du nombre hexadécimal en les convertissant en int
                    indiceByte0 = int((hexByte[0][0]), 16)
                    indiceByte1 = int((hexByte[0][1]), 16)
                    
                    #Remplacement de l'élément de la matrice par son équivalent dans la S_BOX
                    self.messageHacher[messageParts][i, j] = int(S_BOX[indiceByte0][indiceByte1], 16)
                
    '''
  <<===========Fonction ShiftRows=============>>
    ''' 
    def shiftRows(self) :
        #Pour chaque matrice dans le message
        for messageParts in range(len(self.messageHacher)) :
            #On garde en mémoire les anciennes valeurs de la ligne 1
            element10Tampon = self.messageHacher[messageParts][1, 0]
            element11Tampon = self.messageHacher[messageParts][1, 1]
            element12Tampon = self.messageHacher[messageParts][1, 2]
            element13Tampon = self.messageHacher[messageParts][1, 3]
            #On change la disposition des éléments de la ligne 1
            self.messageHacher[messageParts][1, 0] = element11Tampon
            self.messageHacher[messageParts][1, 1] = element12Tampon
            self.messageHacher[messageParts][1, 2] = element13Tampon
            self.messageHacher[messageParts][1, 3] = element10Tampon
            
            #On garde en mémoire les anciennes valeurs de la ligne 2
            element20Tampon = self.messageHacher[messageParts][2, 0]
            element21Tampon = self.messageHacher[messageParts][2, 1]
            element22Tampon = self.messageHacher[messageParts][2, 2]
            element23Tampon = self.messageHacher[messageParts][2, 3]
            #On change la disposition des éléments de la ligne 2
            self.messageHacher[messageParts][2, 0] = element22Tampon
            self.messageHacher[messageParts][2, 1] = element23Tampon
            self.messageHacher[messageParts][2, 2] = element20Tampon
            self.messageHacher[messageParts][2, 3] = element21Tampon
            
            #On garde en mémoire les anciennes valeurs de la ligne 3
            element30Tampon = self.messageHacher[messageParts][3, 0]
            element31Tampon = self.messageHacher[messageParts][3, 1]
            element32Tampon = self.messageHacher[messageParts][3, 2]
            element33Tampon = self.messageHacher[messageParts][3, 3]
            #On change la disposition des éléments de la ligne 3
            self.messageHacher[messageParts][3, 0] = element33Tampon
            self.messageHacher[messageParts][3, 1] = element30Tampon
            self.messageHacher[messageParts][3, 2] = element31Tampon
            self.messageHacher[messageParts][3, 3] = element32Tampon 
            
    '''
  <<===========Fonction MixColumn=============>>
    ''' 
    def mixColumn(self) :
        #Pour chaque matrice du message
        for index in range(len(self.messageHacher)) :
            messageParts = self.messageHacher[index]
            
            #Pour chaque ligne de la matrice de rijndael
            for i in range(4) :
                rijndaelRow = sage.all.matrix(RIJNDAEL_MATRIX.row(i))
                
                #Pour chaque colonne de la matrice courante
                for j in range(4) : 
                    messagePartsColumn = sage.all.matrix(messageParts.column(j))
                    
                    #Initialisation d'une liste qui servira au calcul de l'élément final
                    #Notament pour l'opération XOR
                    counterTab = [0, 0, 0, 0, 0, 0, 0, 0, 0]           
                                 #8, 7, 6, 5, 4, 3, 2, 1, 0      
                                 #X[ 2eme bin  ][ 1er bin  ]
                    
                    #Pour chaque élément d'une ligne et d'une colonne 
                    for m in range(4) :
                        #Conversion de l'élément m de la colonne courante en binaire
                        binaryData = format(messagePartsColumn[0][m], 'b')
                        listBinary = []
                        
                        #Remplissage de la liste de chiffre binaire jusqu'à une longueur de 8
                        for b in range(len(binaryData)) :
                            listBinary.append(binaryData[b])
                        while (len(listBinary) != 8) :
                            #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                            listBinary.insert(0, '0')

                        #Pour chaque chiffre binaire de la liste
                        for b in range(len(listBinary)) :
                            #Opérations dans la counterList pour connaitre le binaire de fin
                            if (rijndaelRow[0][m] == 1) :
                                if (listBinary[b] == '1') :   
                                    counterTab[b + 1] += 1
                            elif (rijndaelRow[0][m] == 2) :
                                if (listBinary[b] == '1') :   
                                    counterTab[b] += 1
                            elif (rijndaelRow[0][m] == 3) :
                                if (listBinary[b] == '1') :   
                                    counterTab[b + 1] += 1
                                    counterTab[b] += 1
                        
                        #Quand un élément de la liste est impair mettre 1 sinon mettre 0
                        for b in range(len(counterTab)) :
                            if (counterTab[b] % 2 == 1) :
                                counterTab[b] = 1
                            else :
                                counterTab[b] = 0
                                
                        #Si le 9ème bit est 1 alors XOR la counterList avec P(X)
                        if (counterTab[0] == 1) :
                            for b in range(len(counterTab)) :
                                if (counterTab[b] == PX[b]) :
                                    counterTab[b] = 0
                                else :
                                    counterTab[b] = 1
                    
                    #Conversion du chiffre binaire final en int
                    finalBinary = '0b'
                    for b in range(len(counterTab)) :
                        counterTab[b] = str(counterTab[b])
                        finalBinary += counterTab[b]                        
                    finalNumber = int(finalBinary, 2)
                    #Remplacement de l'ancienne valeur par la nouvelle
                    self.messageHacher[index][i, j] = finalNumber

    '''
  <<==========Fonction AddRoundKey============>>
    '''                         
    def addRoundKey(self, roundKey) :
        #Pour chaque matrice du message
        for messageParts in range(len(self.messageHacher)) :
            #Pour chaque élément de la matrice message courante et la cle courante 
            for i in range(4) :
                for j in range(4) :                   
                    #Conversion de l'élément courant de la matrice et la cle en binaire
                    binaryDataMessage = format(self.messageHacher[messageParts][i][j], 'b') 
                    binaryDataCle = format(roundKey[i][j], 'b')  
                    listBinaryMessage = []
                    listBinaryCle = []
                        
                    #Remplissage de la liste message de chiffre binaire jusqu'à une longueur de 8
                    for b in range(len(binaryDataMessage)) :
                        listBinaryMessage.append(binaryDataMessage[b])
                    while (len(listBinaryMessage) != 8) :
                        #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                        listBinaryMessage.insert(0, '0') 
                        
                    #Remplissage de la liste clé de chiffre binaire jusqu'à une longueur de 8
                    for b in range(len(binaryDataCle)) :
                        listBinaryCle.append(binaryDataCle[b])
                    while (len(listBinaryCle) != 8) :
                        #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                        listBinaryCle.insert(0, '0')
                        
                    resultat = []
                    #Pour chaque bit
                    for b in range(8) :
                        #Si le bit de la cle et du message sont différent alors le bit du résultat est 1
                        if (listBinaryMessage[b] != listBinaryCle[b]) :
                            resultat.append(1)
                        #sinon c'est 0
                        else :
                            resultat.append(0)
                    
                    #Conversion du chiffre binaire final en int
                    finalBinary = '0b'
                    for b in range(len(resultat)) :
                        resultat[b] = str(resultat[b])
                        finalBinary += resultat[b]                        
                    finalNumber = int(finalBinary, 2)
                    #Remplacement de l'ancienne valeur par la nouvelle
                    self.messageHacher[messageParts][i, j] = finalNumber
                    
    '''
  <<=========Fonction TurnIntoChar============>>
    '''
    def turnIntoChar(self) :
        codedMessage = ""
        #Pour chaque matrice du message
        for messageParts in range(len(self.messageHacher)) :
            #Pour chaque élément de la matrice
            for i in range(4) : 
                for j in range(4) :
                    codedMessage += chr(self.messageHacher[messageParts][i][j])
        print("Le message encrypté est : ")
        print(''.join([str(elem) for elem in codedMessage])) 
                    


'''
||==============================================||
||         Fonctions de décryptage AES          ||
||==============================================||
'''            
class DecryptMessageAES :
    '''
  <<=======Constructeur décrypteur AES========>>
    '''
    def __init__(self, encryptedMessage) : 
        self.messageHacherCypter = encryptedMessage
    
    '''
  <<========Fonction ReverseSubBytes==========>>
    '''   
    def reverseSubBytes(self) :
        #Pour chaque matrice du message
        for messageParts in range(len(self.messageHacherCypter)) :
            #Pour chaque élément de la matrice
            for i in range(4) :
                for j in range(4) :
                    #Conversion de l'élément en hexadécimal
                    hexByte = format(self.messageHacherCypter[messageParts][i][j], 'x')
                    
                    #Si c'est un hexa à un chiffre formatage en format 2 chiffre
                    if (len(hexByte) != 2) :
                        hexByte = '0' + hexByte
                        
                    #Formatage sous la forme 0x00 pour la recherche dans S_BOX
                    hexByte = '0x' + hexByte
                    
                    #Parcours de toute la S_BOX
                    for x in range(len(S_BOX)) :
                        for y in range(len(S_BOX[x])) :
                            #Si l'élément et l'élément x, y de la S_BOX sont les mêmes
                            if (S_BOX[x][y] == hexByte) :
                                #L'int 0xXY devient le nouvel élément i, j de la matrice
                                decryptInt = '0x' + format(x, 'x') + format(y, 'x')
                                self.messageHacherCypter[messageParts][i, j] = int(decryptInt, 16)
                                
    '''
  <<=======Fonction ReverseShiftRows==========>>
    '''
    def reverseShiftRows(self) :
        #Pour chaque matrice dans le message
        for messageParts in range(len(self.messageHacherCypter)) :
            #On garde en mémoire les anciennes valeurs de la ligne 1
            element10Tampon = self.messageHacherCypter[messageParts][1, 0]
            element11Tampon = self.messageHacherCypter[messageParts][1, 1]
            element12Tampon = self.messageHacherCypter[messageParts][1, 2]
            element13Tampon = self.messageHacherCypter[messageParts][1, 3]
            #On change la disposition des éléments de la ligne 1
            self.messageHacherCypter[messageParts][1, 0] = element13Tampon
            self.messageHacherCypter[messageParts][1, 1] = element10Tampon
            self.messageHacherCypter[messageParts][1, 2] = element11Tampon
            self.messageHacherCypter[messageParts][1, 3] = element12Tampon
            
            #On garde en mémoire les anciennes valeurs de la ligne 2
            element20Tampon = self.messageHacherCypter[messageParts][2, 0]
            element21Tampon = self.messageHacherCypter[messageParts][2, 1]
            element22Tampon = self.messageHacherCypter[messageParts][2, 2]
            element23Tampon = self.messageHacherCypter[messageParts][2, 3]
            #On change la disposition des éléments de la ligne 2
            self.messageHacherCypter[messageParts][2, 0] = element22Tampon
            self.messageHacherCypter[messageParts][2, 1] = element23Tampon
            self.messageHacherCypter[messageParts][2, 2] = element20Tampon
            self.messageHacherCypter[messageParts][2, 3] = element21Tampon
            
            #On garde en mémoire les anciennes valeurs de la ligne 3
            element30Tampon = self.messageHacherCypter[messageParts][3, 0]
            element31Tampon = self.messageHacherCypter[messageParts][3, 1]
            element32Tampon = self.messageHacherCypter[messageParts][3, 2]
            element33Tampon = self.messageHacherCypter[messageParts][3, 3]
            #On change la disposition des éléments de la ligne 3
            self.messageHacherCypter[messageParts][3, 0] = element31Tampon
            self.messageHacherCypter[messageParts][3, 1] = element32Tampon
            self.messageHacherCypter[messageParts][3, 2] = element33Tampon
            self.messageHacherCypter[messageParts][3, 3] = element30Tampon 
            
    '''
  <<=======Fonction Reverse MixColumn=========>>
    ''' 
    def reverseMixColumn(self) :
        todo = "A FAIRE"
        
    '''
  <<======Fonction Reverse AddRoundKey========>>
    ''' 
    def reverseAddRoundKey(self, roundKey) :
        #Pour chaque matrice du message
        for messageParts in range(len(self.messageHacherCypter)) :
            #Pour chaque élément de la matrice
            for i in range(4) :
                for j in range(4) :   
                    #Conversion de l'élément courant de la matrice et la cle en binaire
                    binaryDataMessage = format(self.messageHacherCypter[messageParts][i][j], 'b') 
                    binaryDataCle = format(roundKey[i][j], 'b')  
                    listBinaryMessage = []
                    listBinaryCle = []
                        
                    #Remplissage de la liste message de chiffre binaire jusqu'à une longueur de 8
                    for b in range(len(binaryDataMessage)) :
                        listBinaryMessage.append(binaryDataMessage[b])
                    while (len(listBinaryMessage) != 8) :
                        #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                        listBinaryMessage.insert(0, '0') 
                        
                    #Remplissage de la liste clé de chiffre binaire jusqu'à une longueur de 8
                    for b in range(len(binaryDataCle)) :
                        listBinaryCle.append(binaryDataCle[b])
                    while (len(listBinaryCle) != 8) :
                        #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                        listBinaryCle.insert(0, '0')
                        
                    resultat = []
                    #Pour chaque bit
                    for b in range(8) :
                        #Si le bit du message est égal à 1 alors le résultat est identique au bit de la clé
                        if (listBinaryMessage[b] == '0') :
                            if (listBinaryCle[b] == '1') :
                                resultat.append(1)
                            else :
                                resultat.append(0)
                        #sinon le résultat est différent du bit de la clé
                        else :
                            if (listBinaryCle[b] == '1') :
                                resultat.append(0)
                            else :
                                resultat.append(1)
                    
                    #Conversion du chiffre binaire final en int
                    finalBinary = '0b'
                    for b in range(len(resultat)) :
                        resultat[b] = str(resultat[b])
                        finalBinary += resultat[b]                        
                    finalNumber = int(finalBinary, 2)
                    #Remplacement de l'ancienne valeur par la nouvelle
                    self.messageHacherCypter[messageParts][i, j] = finalNumber
                           


'''
||==============================================||
||                 Zone de test                 ||
||==============================================||
'''
'''
mdp = "Cdfp56qpr8Z4G73c"
cle = CleAES(mdp)
print(cle.originalCle)

cle.keySchedule()
  
message = "Les chaussettes de l'archiduchesse sont-elle sèches, archisèches ?"
lastBlock = 1
if(len(message) % 16 != 0) :
    lastBlock = 1
else :
    lastBlock = 0
print("le message est d'une longueur de ", len(message), 
      " caractères, il possède ", len(message) // 16, 
      " blocks de 16 caractères et possède ", lastBlock, 
      " block incomplet de ", len(message) % 16, "caractères")

messageHacher = MessageAES(message)

messageHacher.subBytes()

messageHacher.shiftRows()

messageHacher.mixColumn()

messageHacher.addRoundKey(cle.currentKey)

messageHacher.turnIntoChar()
'''