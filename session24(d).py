import cv2
img = cv2.imread("ibises.jpg", 1)  # recieves image as nd array
#cv2.imshow("Title", img)

print(img)
shape = img.shape
resizedImg = cv2.resize(img, (400, 400))
cv2.imshow("Title", img)

cv2.imwrite("MyIbises.jpg", resizedImg)

cv2.waitKey(0)
cv2.destroyAllWindows()


