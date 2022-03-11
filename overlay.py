import cv2
import numpy as np

# Loading our images 
background = cv2.imread('Assets/img1.jpg') # Background/Input image 
overlay_image = cv2.imread('Assets/overlay3.png') # Overlay image

overlay_image = cv2.resize(overlay_image, (1000,1000)) # Resize the overlay image to match the bg image dimensions
h, w = overlay_image.shape[:2]

# Create a new np array 
shapes = np.zeros_like(background, np.uint8)
# Put the overlay at the bottom-right corner
shapes[background.shape[0]-h:,background.shape[1]-w:] = overlay_image
# Change this into bool to use it as mask
mask = shapes.astype(bool)

# We'll create a loop to change the alpha value i.e transparancy of the overlay
for alpha in np.arange(0, 1.1, 0.1)[::-1]:
    bg_img = background.copy()
    bg_img[mask] = cv2.addWeighted(bg_img, 1 - alpha, shapes,alpha, 0)[mask]

    # print the alpha value on the image
    cv2.putText(bg_img,f'Alpha: {round(alpha,1)}',(50,200), cv2.FONT_HERSHEY_PLAIN,8,(200,200,200),7)

    bg_img = cv2.resize(bg_img,(630,630))
    cv2.imshow('Final Overlay',bg_img)
    cv2.waitKey(0)