#Converting Face Image to pixels and writing to file
import cv2
import numpy as np
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
c= cv2.VideoCapture(1)
ramp_frames = 30

def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
	retval, im = c.read()
	return im

def dodgeV2(image, mask):
  return cv2.divide(image, 255-mask, scale=256)

while True:
	_,cap = c.read()
	gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 	for (x,y,w,h) in faces:
                roi_gray = gray[y-h/5:y+h+h/5, x-w/20:x+w+w/20]
                roi_color = cap[y-h/5:y+h+h/5, x-w/20:x+w+w/20]
		cv2.rectangle(cap,(x-w/20,y-h/5),(x+w+w/20,y+h+h/5),(255,0,0),2)
	cv2.imshow('hey',cap)
	k = cv2.waitKey(25)
	if k == ord('q'):
		print("Taking image...")
		cv2.imwrite("hello.jpg",roi_color)
		print("Image Saved!!")
		break;

im = cv2.imread('hello.jpg')
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray',gray)
inv = 255 - gray
#cv2.imshow('Inv',inv)
blur = cv2.GaussianBlur(inv, ksize=(21, 21),sigmaX=0, sigmaY=0)
#cv2.imshow('Blur',blur)
blend = dodgeV2(gray, blur)
cv2.imshow("pencil sketch", blend)
ret,th = cv2.threshold(blend,127,255,cv2.THRESH_BINARY)
ret1,th1 = cv2.threshold(blend,150,255,cv2.THRESH_BINARY)
cv2.imshow("Thresh", th)
cv2.imshow("Thresh1", th1)
'''
cv2.imwrite('blend.jpg',blend)
canny = cv2.Canny(th, 600, 700)
cv2.imshow('canny',canny)


im2,contours,hierarchy = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#print contours
cv2.imshow('contours',im2)
'''
xvalues = []
yvalues = []

for i in range(len(th)):
	for j in range(len(th[i])):
		if th[i][j]==0:
			xvalues.append(str(j))
			yvalues.append(str(i))

print len(th)
print len(th[0])


f = open('xf.txt','w')
f.write(' '.join(xvalues))
f.close()
f = open('yf.txt','w')
f.write(' '.join(yvalues))
f.close()

cv2.waitKey(0)
cv2.destroyAllWindows()

