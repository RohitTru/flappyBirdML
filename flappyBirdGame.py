import pygame
import neat
import neat
import os
import random

# Initialize pygame window Dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800

# Import game assets images into list
assets = ['base.png','bg.png','bird1.png','bird2.png','bird3.png','pipe.png']

# Load in the assets function
BIRD_IMG = []
def importAssets(assets):
    for i in assets:
        asset = os.path.join("imgs",str(i))
        loadedAsset = pygame.image.load(asset)
        sizedAsset = pygame.transform.scale2x(loadedAsset)
        if int(sizedAsset.get_width()) > 600:
            BASE_IMG = sizedAsset
            print("retrieved base")
            print(type(BASE_IMG))
        if 500 < int(sizedAsset.get_width()) < 600:
            BG_IMG = sizedAsset
            print("retrieved BG")
        if int(sizedAsset.get_width()) < 100:
            BIRD_IMG.append(sizedAsset) 
            print("retrieved Bird")
        if 100 < int(sizedAsset.get_width()) < 105:
            PIPE_IMG = sizedAsset
            print("retrieved pipe")
    return BASE_IMG, BG_IMG, BIRD_IMG, PIPE_IMG
            




def main():
    importAssets(assets)

    


if __name__ == "__main__":
    main()