import cv2
import face_recognition
img =cv2.imread("Elon_Musk.jpg")
rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
Img_encodin = face_recognition.face_encodings(rgb_img)[0]


img2 =cv2.imread("images/Elon_Musk.jpg")
rgb_img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
Img_encodin2 = face_recognition.face_encodings(rgb_img2)[0]

result = face_recognition.compare_faces([Img_encodin],Img_encodin2)
print("Result: " ,result)

cv2.imshow("Img",img)
cv2.imshow("Img2",img2)
cv2.waitKey(0)