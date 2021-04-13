import numpy as np

# orgininal order as in dataset
# pannuke_classes = ['Neoplastic', 'Inflammatory', 'Connective', 'Dead ', 'Epithelial', 'Background']

# this one is after I rearranged the oreder for my needs
pannuke_classes = ['Background', 'Inflammatory', 'Connective', 'Dead ', 'Epithelial', 'Neoplastic ']

pallet_pannuke = pallet_mine = np.array([[[  0,  0,  0],# BG
                                        [0  ,255,  0],# Inflammatory
                                        [  0,  0, 255],# Connective
                                        [255,255,  0],#Dead
                                        [255,165,  0],#Epithelial
                                        [255,  0,  0] #Neoplast
                                        ]], np.uint8)/255
