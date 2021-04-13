[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![PyPI](https://img.shields.io/pypi/v/two) [![DOI](https://zenodo.org/badge/357129295.svg)](https://zenodo.org/badge/latestdoi/357129295)

# Grayscale to Color Semantic Mask Converotr

This `lib` converts the grayscale semantic masks obtained at the output a CNN and fills it with colors for example in case of 
`cityscape` dataset you have 30 channels at the output of CNN and after using `argmax` to create one channel semantic mask you
get the following output

![alt text](https://github.com/Mr-TalhaIlyas/Converting-Grayscale-Semantic-Masks-to-Color/blob/master/screens/gray.png)
which you can use for measuring `IOU`, `Dice` or other evaluation metrics. But it is a bit difficult for human visualization so this package 
converts the above output to following ouptut easy to visualize.
![alt text](https://github.com/Mr-TalhaIlyas/Converting-Grayscale-Semantic-Masks-to-Color/blob/master/screens/rgb.png)

## Dependencies

```
numpy
cv2
tensorflow
python >= 3.6
```

## Installation
[Pypi](https://pypi.org/project/gray2color/)
```
pip install gray2color
```

## Usage

```python
import cv2
from gray2color import gray2color

mask = cv2.imread('../gray.png', 0)
rgb = gray2color(mask, use_pallet='cityscape', custom_pallet=None)

```
## Available Pallets
Available Pallets are `ade20k`, `cityscape`, `lip`, `pannuke`, `pascal`, `vistas`

You can also define your custom color Pallets as follows

```python

# values are in order [R, G, B] ranging from [0, 255]

pallet_cityscape = np.array([[[128, 64, 128],
                            [244, 35, 232],
                            [70, 70, 70],
                            [102, 102, 156],
                            [190, 153, 153]]], np.uint8) / 255
```

## Returns

A `uint8` image with values ranging from [0, 255] you can save via

```python
import cv2

rgb = cv2.cvtColor(rgb, cv2.COLOR_BGR2RGB)  #   becaues cv2 will change color channels before writing
cv2.imwrite('../rgb.png', rgb)
```


## Raises Errors

```python

PalletNotDefined: if pallet is not specified

NotEnoughColors: if grayscale mask has more classes present than the colors in the pallet

```

