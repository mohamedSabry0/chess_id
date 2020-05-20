import numpy as np
import cv2


def auto_canny(image, sigma=1):
    """
    Canny edge detection with automatic thresholds.
    """
    # compute the median of the single channel pixel intensities
    v = np.median(image)
 
    # apply automatic Canny edge detection using the computed median
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
 
    # return the edged image
    return edged


img = cv2.imread('./0.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = auto_canny(gray)
cv2.imwrite("canny.jpg", edges)
minLineLength=150
lines = cv2.HoughLinesP(image=edges,rho=1,theta=np.pi/180, threshold=170,lines=np.array([]), minLineLength=minLineLength,maxLineGap=300)
#lines = cv2.HoughLines(image=edges,rho=1,theta=np.pi/180, threshold=100)



a,b,c = lines.shape

print a

for i in range(a):
    print lines[i][0][0],lines[i][0][1]
    print lines[i][0][2],lines[i][0][3]
    cv2.circle(img, (lines[i][0][0],lines[i][0][1]), 3, (0,255,0),-1)
    cv2.circle(img, (lines[i][0][2],lines[i][0][3]), 3, (255,0,0),-1)
    cv2.imwrite('points.jpg', img)
    cv2.line(img, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 1)
    cv2.imwrite('houghlines5.jpg',img)
    

