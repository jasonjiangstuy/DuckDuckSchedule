import cv2
import os
# Idea: The camera is going to constantly send us image frames
# then we are going to continuously get hand and head locations data
# when button pressed send 5 facepics to api that are closest to expected pixels size
def getImageData(filename):
    # identify face rectangles
    # ONLY ONE FOR NOW
    faces = detectFaceLocations(filename,4)
    newname = filename.split('/')[-1]
    newname = newname.split('.')[0]
    
    # save to temp dir?? maybe we dont need to save
    img = cv2.imread(filename)
    for i, (x, y, w, h) in enumerate(faces):
        tempimg = img.copy()
        bufferw= w*1.5
        buffery= h*1.5

        tempimg = tempimg[int(x-bufferw):int(x+w+bufferw) , int(y-buffery):int(y+h+buffery)]
        newfilename = "temp_head_images/"+str(newname)+ "-" + str(i)+".jpeg"
        try:
            cv2.imwrite(newfilename, tempimg)
        except:
            pass
    
        # request api

        # remove temp headfile 
        # os.remove(newfilename)
    # get data back, log into db
    # os.remove(filename)
    
    return

# Returns faces = [(x,y,w,h),....]
def detectFaceLocations(filename, num_of_faces):
    # https://github.com/adarsh1021/facedetection
    # http://betafaceapi.com/
    # Load the cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read the input image
    img = cv2.imread(filename)

    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, num_of_faces)

    # # Draw rectangle around the faces
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # # Display the output
    # cv2.imshow('img', img)
    # cv2.waitKey()
    return faces
