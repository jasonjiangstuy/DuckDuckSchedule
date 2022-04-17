import cv2
import os
import mediapipe as mp
import numpy as np
# Idea: The camera is going to constantly send us image frames
# then we are going to continuously get palm and head locations data
# when button pressed send 5 facepics to api that are closest to expected pixels size
def getImageData(filename):
    # identify face rectangles
    # ONLY ONE FOR NOW
    faces = detectFaceLocations(filename)
    newname = filename.split('/')[-1]
    newname = newname.split('.')[0]
    
    # save to temp dir?? maybe we dont need to save
    img = cv2.imread(filename)
    for i, (face_dict) in enumerate(faces):
        print(face_dict)
        tempimg = img.copy()
        tempimg = tempimg[int(face_dict['xmin']):int(face_dict['xmax']) , int(face_dict['ymin']):int(face_dict["ymax"])]
        newfilename = "temp_head_images/"+str(newname)+ "-" + str(i)+".jpeg"
        try:
            cv2.imwrite(newfilename, tempimg)
        except:
            pass
   
#    idetify locations of palms
    palm = detectPalmLocations(filename)
    i = 0
    # visualize palm
    # newfilename = "temp_palm_images/"+str(newname)+ "-" + str(i)+".jpeg"
    # cv2.imwrite(newfilename, palm)

        # remove temp headfile 
        # os.remove(newfilename)
    # get data back, log into db
    # os.remove(filename)
    
    return

# Returns faces = [(x,y,w,h),....]
def detectFaceLocations(filename):
    mp_face_detection = mp.solutions.face_detection
    mp_drawing = mp.solutions.drawing_utils
    with mp_face_detection.FaceDetection(
        model_selection=1, min_detection_confidence=0.5) as face_detection:
        image = cv2.imread(filename)
        # Convert the BGR image to RGB and process it with MediaPipe Face Detection.
        results = face_detection.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        annotated_image = image.copy()
        print(results.detections)
        print(type(results.detections))
        width = image.shape[0]
        height = image.shape[1]
        locations = []
        if results.detections:
            for detection in results.detections:
                bbox = detection.location_data.relative_bounding_box
                locations.append({
                    "xmin" : int(bbox.xmin * width*1.70),
                    "ymin" : int(bbox.ymin * height*.1),
                    "xmax" : int(bbox.width * width + bbox.xmin * width),
                    "ymax" : int(bbox.height * height*1.5 + bbox.ymin * height)
        })
        return locations

        #     print('Nose tip:')
        #     print(mp_face_detection.get_key_point(
        # detection, mp_face_detection.FaceKeyPoint.NOSE_TIP))
        # mp_drawing.draw_detection(annotated_image, detection)
        # cv2.imwrite('temp_head_images/annotated_image.png', annotated_image)    
        # cv2.imwrite('temp_head_images/annotated_image.png', image)    
def detectPalmLocations(filename):
    mpPalms = mp.solutions.hands
    palms = mpPalms.Hands(static_image_mode=False,
                        max_num_hands=2,
                        min_detection_confidence=0.5,
                        min_tracking_confidence=0.5)
    mpDraw = mp.solutions.drawing_utils
    img = cv2.imread(filename)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = palms.process(imgRGB)
    # print(results.multi_hand_landmarks)
    all_palm_coords = []
    if results.multi_hand_landmarks:
        for palmLms in results.multi_hand_landmarks:
            for id, lm in enumerate(palmLms.landmark):
                #print(id,lm)
                h, w, c = img.shape
                if (id == 4):
                    all_palm_coords.append((h, w))
                # cx, cy = int(lm.x *w), int(lm.y*h)
                #if id ==0:
                # cv2.circle(img, (cx,cy), 3, (255,0,255), cv2.FILLED)
            # mpDraw.draw_landmarks(img, palmLms, mpPalms.HAND_CONNECTIONS)
    # returns locations
    if len(all_palm_coords) != 0:
        print(all_palm_coords)
        return all_palm_coords
    # return img