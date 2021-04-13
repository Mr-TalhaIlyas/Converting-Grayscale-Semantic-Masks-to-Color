import numpy as np

# Even though the cityscape dataset provide the pixel wise labells of 30 classes but usually in most of the papers only 20 classes 
# are used for evaluation. So I added both of them

cityscape_class_full = ['unlabeled', 'ego_vehicle', 'rectification_border', 'out_of_roi', 'static', 'dynamic', 'ground', 'road',
                         'sidewalk', 'parking', 'rail track', 'building', 'wall', 'fence', 'guard rail', 'bridge',
                         'tunnel', 'pole', 'polegroup', 'traffic light', 'traffic sign', 'vegetation', 'terrain', 'sky',
                         'person', 'rider', 'car', 'truck', 'bus' ,'caravan', 'trailer', 'train', 'motorcycle', 'bicycle' ]

cityscape_class_names = ['road', 'sidewalk', 'building', 'wall', 'fence', 'pole',
                'traffic light', 'traffic sign',
                'vegetation', 'terrain', 'sky', 'person', 'rider', 'car',
                'truck', 'bus', 'train', 'motorcycle', 'bicycle']

# this will be usefull in case you wanna do Panoptic Segmentation
cityscape_THING_LIST = [11, 12, 13, 14, 15, 16, 17, 18]

pallet_cityscape =  np.array([[[ 0,  0,  0],
                                [ 0,  0,  0],
                                [ 0,  0,  0],
                                [ 0,  0,  0],
                                [ 0,  0,  0],
                                [111, 74,  0],
                                [ 81,  0, 81],
                                [128, 64,128],
                                [244, 35,232],
                                [250,170,160],
                                [230,150,1400],
                                [ 70, 70, 70],
                                [102,102,156],
                                [190,153,153],
                                [180,165,180],
                                [150,100,100],
                                [150,120, 90],
                                [153,153,153],
                                [153,153,153],
                                [250,170, 30],
                                [220,220,  0],
                                [107,142, 35],
                                [152,251,152],
                                [70,130,180],
                                [220, 20, 60],
                                [255,  0,  0],
                                [ 0,  0,142],
                                [ 0,  0, 70],
                                [ 0, 60,100],
                                [ 0,  0, 90],
                                [0,  0,110],
                                [ 0, 80,100],
                                [ 0,  0,230],
                                [119, 11, 32]]], np.uint8) / 255
pallet_cityscape_small = np.array([[[128, 64, 128],
                            [244, 35, 232],
                            [70, 70, 70],
                            [102, 102, 156],
                            [190, 153, 153],
                            [153, 153, 153],
                            [250, 170, 30],
                            [220, 220, 0],
                            [107, 142, 35],
                            [152, 251, 152],
                            [70, 130, 180],
                            [220, 20, 60],
                            [255, 0, 0],
                            [0, 0, 142],
                            [0, 0, 70],
                            [0, 60, 100],
                            [0, 80, 100],
                            [0, 0, 230],
                            [119, 11, 32]]], np.uint8) / 255



