import cv2

image_people_path = ('smiling-portrait-three-male-friends-standing-against-blue-background_23-2148160233.jpg')

image_people = cv2.imread(image_people_path)

handle_people_face = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
handle_people_eyes = cv2.CascadeClassifier('haarcascade_eye.xml')

people_face_data = handle_people_face.detectMultiScale(image_people)
people_eyes_data = handle_people_eyes.detectMultiScale(image_people)

print(people_face_data, people_eyes_data)

for(x, y, w, h) in people_face_data:
    cv2.rectangle(image_people, (x, y), (x+w, y+h), (0, 255, 0), 3)

for(x, y, w, h) in people_eyes_data:
    cv2.rectangle(image_people, (x, y), (x+w, y+h), (0, 255, 0), 3)

cv2.imshow('People', image_people)
cv2.waitKey()