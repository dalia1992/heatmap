
import matplotlib.pyplot as plt
import numpy as np
from cv2 import resize

def add(image, heat_map, alpha=0.6, display=False, save=None, cmap='viridis', axis='off', 
        verbose=False, normalise=False, my_resize=False, colormap=False, dpi=4):

    height = image.shape[0]
    width = image.shape[1]

    # resize heat map
    if my_resize:
        heat_map_resized = resize(heat_map, (height, width))
    else:
        heat_map_resized=heat_map
    # normalize heat map
    max_value = np.max(heat_map_resized)
    min_value = np.min(heat_map_resized)
    if normalise:
        normalised_heat_map = (heat_map_resized - min_value) / (max_value - min_value)*255 
    else:
        normalised_heat_map= heat_map_resized
    # display
    fig=plt.figure(figsize=(height/dpi,width/dpi), dpi=dpi)
    plt.imshow(image)
    if colormap:
        plt.imshow(normalised_heat_map, alpha=alpha, cmap=cmap)
    else:
        plt.imshow(normalised_heat_map, alpha=alpha)
        
    plt.axis(axis)

    if display:
        plt.show()

    if save is not None:
        if verbose:
            print('save image: ' + save)
        plt.savefig(save, bbox_inches='tight', pad_inches=0)
