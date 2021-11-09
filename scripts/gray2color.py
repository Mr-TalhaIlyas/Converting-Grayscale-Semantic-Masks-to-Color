import numpy as np
from utils.gray2rgb import gray2rgb


class PalletNotDefined(Exception): 
     pass

class NotEnoughColors(Exception): 
     pass


available_pallets = ['ade20k', 'cityscape', 'lip', 'pannuke', 'pascal', 'vistas']

message = 'Select a Pallet to be used form the follwoing list or define a custom pallet \n LIST: {}'.format(available_pallets)

def gray2color(mask, use_pallet, custom_pallet=None):
    
    if custom_pallet is None:
        if use_pallet == 'ade20k':
            from utils.ade20k import pallet_ade20k as pallet
        elif use_pallet == 'cityscape':
            from utils.cityscape import pallet_cityscape as pallet
        elif use_pallet == 'lip':
            from utils.lip import pallet_lip as pallet
        elif use_pallet == 'lip':
            from utils.lip import pallet_lip as pallet
        elif use_pallet == 'pannuke':
            from utils.pannuke import pallet_pannuke as pallet
        elif use_pallet == 'pascal':
            from utils.pascal import pallet_pascal as pallet
        elif use_pallet == 'vistas':
            from utils.vistas import pallet_vistas as pallet
        else:
            raise PalletNotDefined(message)
    else:
        pallet = custom_pallet
    
    if len(np.unique(mask)) > len(pallet[0,:,0]):
        message2 = "Number of distinct colors in pallet must be greater than or equal to the\
                    number of unique classes present in Semantic-Mask. But the mask has {} colors\
                    and pallet has {} colors".format(len(np.unique(mask)), len(pallet[0,:,0]))
        raise NotEnoughColors(message2)
        
    rgb = gray2rgb(mask, pallet)
    rgb = (rgb * 255).astype(np.uint8)
    return rgb
    
