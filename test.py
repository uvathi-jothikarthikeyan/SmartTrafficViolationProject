import cv2

img= cv2.imread("test.png")

cv2.rectangle(img,(50,50),(300,300),(0,255,0),3)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()