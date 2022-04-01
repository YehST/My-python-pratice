import cv2
import numpy as np

lena = cv2.imread("A_girl.jfif", 0)
cv2.imshow("lena", lena)
r, c = lena.shape
x = np.zeros((r, c, 8), dtype=np.uint8)
for i in range(8):
    x[:, :, i] = 2**i
r = np.zeros((r, c, 8), dtype=np.uint8)
for i in range(8):
    r[:, :, i] = cv2.bitwise_and(lena, x[:, :, i])
    mask = r[:, :, i] > 0
    r[mask] = 255
    cv2.imshow(str[i], r[:, :, i])
cv2.waitKey()
cv2.destroyAllWindows()
