import cv2 as cv
import numpy

img=cv.imread('village.png')
img2=cv.imread('turgut.png')

img=cv.resize(img,(600,600))
img2=cv.resize(img2,(600,600))#both the image must have same size

#lets try split method
b,g,r=cv2.split(img)#so this split the image in BGR channels
#lets try merge method
img=cv2.merge((b,g,r))#so this method again merge the BGR channel to one image
#we had already used resize method lets try it again

#lets us see how we can select a ROI and copy that part to other place
hut=img[208:405,16:201]#selecting the coordinate of the object which we want to copy to other place
img[341:538,392:577]=hut#defining the coordinate of that part where we want to copy the object
#so this method copy an object
#now lets try how to add two image
dst=cv.add(img,img2)#so this is the way you can add two images
#now lets try add weights
weighted=cv.addWeighted(img,.4,img2,.6,0)#so by this way we can add image of our desired weight
cv.imshow("ROI",weighted)

cv.waitKey(0)
cv.destroyAllWindows()
