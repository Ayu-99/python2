import cv2
img = cv2.imread("ibises.jpg", 1)  # recieves image as nd array
print(img)
cv2.imshow("Title", img)  # converts array into image


cv2.waitKey(0)  # wait till users press a key

# Quit after 3 sec
#cv2.waitKey(3000)

cv2.destroyAllWindows()

#see assignment