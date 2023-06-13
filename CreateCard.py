import cv2
img=cv2.imread("solar-system.jpg")
text_2_show="sun"
cv2.putText(img,text_2_show,(20,300),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Mercury",(115,250),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Venus",(190,250),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Earth",(280,280),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Mars",(380,250),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Jupiter",(520,290),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Saturn",(760,290),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Uranus",(950,290),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.putText(img,"Neptune",(1100,290),fontFace=cv2.FONT_HERSHEY_COMPLEX,fontScale=0.5,color=(255,255,255))
cv2.imshow("Output",img)
cv2.waitKey(0)