import cv2
import numpy as np
resim = cv2.imread("kartal.jpg")  # resimin alınması okunmasısağlanır
cv2.imshow("Resim 1", resim)  # birinci paremetre baslık ikinci resim
cv2.waitKey(0)  # kapanmasını engeller
cv2.destroyAllWindows()  # butun her seyi kaptır sonda
