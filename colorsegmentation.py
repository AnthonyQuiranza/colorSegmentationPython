import cv2
import numpy as np
def verImagen(image):
    cv2.namedWindow('Imagen', cv2.WINDOW_NORMAL)
    cv2.imshow('Imagen', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


## obteniendo color verde
green = np.uint8([[[0, 255, 0 ]]])
green_hsv = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print( green_hsv)

image = cv2.imread('./images/leave_lancha.jpg')
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
verImagen(hsv_img) ## 1
green_low = np.array([45 , 100, 50] )
green_high = np.array([75, 255, 255])
curr_mask = cv2.inRange(hsv_img, green_low, green_high)
hsv_img[curr_mask > 0] = ([75,255,200])
verImagen(hsv_img) ## 2
## Convertiendo hsv_img a escala de grises
## encontrando contorno
RGB_again = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2RGB)
gray = cv2.cvtColor(RGB_again, cv2.COLOR_RGB2GRAY)
verImagen(gray) ## 3
ret, threshold = cv2.threshold(gray, 90, 255, 0)
verImagen(threshold) ## 4
contours, hierarchy =  cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(image, contours, -1, (0, 0, 255), 3)
verImagen(image) ## 5