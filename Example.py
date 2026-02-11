import cv2

img = cv2.imread("test.jpg")

# draw rectangle (x1,y1,x2,y2)
cv2.rectangle(img, (50,50), (300,300), (0,255,0), 3)

cv2.imshow("Box", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
