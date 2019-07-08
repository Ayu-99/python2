import cv2

print(cv2.__version__)
img = cv2.imread("ibises.jpg", 1)  # 1 means Read as coloured image and 0 means B/W
print("======Image=======")
print(img)

print("===========Type Of Image========")
print(type(img))

print("=========Image Shape======")
print(img.shape)

print("========Image 0th Index=====")
print(img[0])

print("========Image Shape 0th Index=========")
print(img[0].shape)

print("=======Image length 0th Index==========")
print(len(img[0]))


