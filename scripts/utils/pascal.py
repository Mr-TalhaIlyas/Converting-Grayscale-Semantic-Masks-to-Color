import numpy as np

voc_class_names = ['background', 'aeroplane', 'bicycle', 'bird',
                'boat',
                'bottle', 'bus', 'car', 'cat', 'chair', 'cow',
                'diningtable',
                'dog', 'horse', 'motorbike', 'person',
                'pottedplant',
                'sheep', 'sofa', 'train', 'tv/monitor']

pallet_voc = np.array([[[0, 0, 0], 
                        [0, 0, 128], 
                        [0, 128, 0], 
                        [0, 128, 128],
                        [128, 0, 0], 
                        [128, 0, 128], 
                        [128, 128, 0],
                        [128, 128, 128],
                        [0, 0, 64], 
                        [0, 0, 192], 
                        [0, 128, 64],
                        [0, 128, 192],
                        [128, 0, 64], 
                        [128, 0, 192], 
                        [128, 128, 64],
                        [128, 128, 192], 
                        [0, 64, 0], 
                        [0, 64, 128],
                        [0, 192, 0],
                        [0, 192, 128], 
                        [128, 64, 0]]],np.uint8) / 255
