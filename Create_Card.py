import cv2
from datetime import datetime
print(datetime.now())

img = cv2.imread("poster.jpg")

# Put current DateTime on each frame
cv2.putText(img,str(datetime.now()),(30,30), cv2.FONT_HERSHEY_PLAIN, 1,(255,255,255))

text_to_show = "I love coding at WhiteHatJr."


cv2.putText(img,  
           text_to_show,
           (20, 220),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(0,0,255)
           )


cv2.imshow("output",img)
cv2.imwrite("Greetings.jpg",img)

cv2.waitKey(0)












# next_line = "Good Luck for great beginnings." 

# 
# cv2.putText(img,  
#            next_line,
#            (50, 320),  
#            fontFace=cv2.FONT_HERSHEY_DUPLEX,  
#            fontScale=1,  
#            color=(168,46,255))











