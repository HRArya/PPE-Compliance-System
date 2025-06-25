from ultralytics import YOLO
import cv2
import math


# from playsound import playsound

import pygame


# Initialize pygame mixer
pygame.mixer.init()

# Load the sound file
warning_sound = pygame.mixer.Sound('severe-warning-alarm-98704.mp3')  # Replace with your sound file path



# def is_in_not_safe_area(person_box, not_safe_area):
#     x1, y1, x2, y2 = person_box
#     nsafe_x1, nsafe_y1, nsafe_x2, nsafe_y2 = not_safe_area
    
#     # Check if the person's box is within the safe area
#     return (x1 >= nsafe_x1 and y1 >= nsafe_y1 and x2 <= nsafe_x2 and y2 <= nsafe_y2)


def is_in_not_safe_area(person_box, not_safe_area):
    x1, y1, x2, y2 = person_box
    nsafe_x1, nsafe_y1, nsafe_x2, nsafe_y2 = not_safe_area
    
    # Check if any corner of the person's box is within the not safe area
    return not (
        x2 < nsafe_x1 or  # Right edge of person box is left of left edge of not safe area
        x1 > nsafe_x2 or  # Left edge of person box is right of right edge of not safe area
        y2 < nsafe_y1 or  # Bottom edge of person box is above top edge of not safe area
        y1 > nsafe_y2     # Top edge of person box is below bottom edge of not safe area
    )

    

# def video_detection(path_x):
#     video_capture = path_x
#     # Create a Webcam Object
#     cap = cv2.VideoCapture(video_capture)
#     frame_width = int(cap.get(3))
#     frame_height = int(cap.get(4))
#     # out=cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P','G'), 10, (frame_width, frame_height))

#     model = YOLO("YOLO-Weights/best5.pt")
#     # classNames = ['Protective Helmet', 'Shield', 'Jacket', 'Dust Mask', 'Eye Wear', 'Glove', 'Protective Boots']
#     classNames = ['boots', 'gloves', 'helmet', 'helmet on',
#         'no boots', 'no glove', 'no helmet', 'no vest', 'person', 'vest']

#     not_safe_area = (0, 100, 300, 400) 
#     # Set colors for drawing
#     not_safe_color = (255, 0, 0)  # Green for safe area



#     while True:
#         success, img = cap.read()
#         # cv2.rectangle(img, (not_safe_area[0], not_safe_area[1]), (not_safe_area[2], not_safe_area[3]), not_safe_color, 2)
#         # cv2.putText(img, "Not Safe Area", (not_safe_area[0], not_safe_area[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, not_safe_color, 2)

#         results=model(img,stream=True)
        

#         for r in results:
#             # print (r)
#             boxes=r.boxes
#             # print(len(boxes))
#             for box in boxes:
#                 x1,y1,x2,y2=box.xyxy[0]
#                 x1,y1,x2,y2=int(x1), int(y1), int(x2), int(y2)
#                 # print(x1,y1,x2,y2)
#                 conf=math.ceil((box.conf[0]*100))/100
#                 cls=int(box.cls[0])
#                 class_name=classNames[cls]
#                 label=f'{class_name}{conf}'
#                 t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
#                 # print(t_size)
#                 c2 = x1 + t_size[0], y1 - t_size[1] - 3
#                 # if class_name == 'gloves':
#                 #     color=(0, 204, 255)
#                 # elif class_name == "helmet":
#                 #     color = (222, 82, 175)
#                 # elif class_name == "boots":
#                 #     color = (0, 149, 255)
#                 # else:
#                 #     color = (85,45,255)

#                 color = (85,45,255)

#                 # if class_name == 'person' and (is_in_not_safe_area((x1, y1, x2, y2), not_safe_area)):
#                 #     for i in boxes:
#                 #         # print(classNames[(int(i.cls[0]))-1])
#                 #         if classNames[int(i.cls[0])] == 'helmet' or classNames[int(i.cls[0])] == 'helmet on':
#                 #             # i coordinates
#                 #             i_x1,i_y1,i_x2,i_y2=i.xyxy[0]
#                 #             i_x1,i_y1,i_x2,i_y2=int(i_x1), int(i_y1), int(i_x2), int(i_y2)

#                 #             # check if the i_coordinates are in person
#                 #             if i_x1>=x1 and i_x1<=x2 and i_y1>=y1 and i_y1<=y2:
#                 #                 color =(0, 255, 0)
#                 #                 print(f'person is in {class_name}')
#                 #                 cv2.putText(img, "Safe", (x1,y1-40),0, 1,[0,255,0], thickness=1,lineType=cv2.LINE_AA)
#                 #                 break
#                 #             else:
#                 #                 color=(255, 0, 0)
#                 #                 # cv2.putText(img, "Not Safe", (x1,y1-40),0, 1,[255,0,0], thickness=1,lineType=cv2.LINE_AA)






#                 if class_name == 'person':
#                     for i in boxes:
#                         if classNames[int(i.cls[0])] == 'helmet' or classNames[int(i.cls[0])] == 'helmet on' and classNames[int(i.cls[0])] == 'vest':
#                             i_x1,i_y1,i_x2,i_y2=i.xyxy[0]
#                             i_x1,i_y1,i_x2,i_y2=int(i_x1), int(i_y1), int(i_x2), int(i_y2)

#                             if i_x1>=x1 and i_x1<=x2 and i_y1>=y1 and i_y1<=y2:
#                                 color =(0, 255, 0)
#                                 print(f'person is in {class_name}')
#                                 cv2.putText(img, "Safe", (x1,y1-40),0, 1,[0,255,0], thickness=1,lineType=cv2.LINE_AA)
#                                 break
#                             else:
#                                 color = (85,45,255)
















#                     if conf>0.5:
#                         cv2.rectangle(img, (x1,y1), (x2,y2), color,3)
#                         cv2.rectangle(img, (x1,y1), c2, color, -1, cv2.LINE_AA)  # filled
#                         cv2.putText(img, label, (x1,y1-2),0, 1,[255,255,255], thickness=1,lineType=cv2.LINE_AA)




#                 # if class_name == 'person':
#                 #     if is_in_safe_area((x1, y1, x2, y2), safe_area):
#                 #         cv2.putText(img, "In Safe Area", (int(x1), int(y1) - 10), 0, 0.5, [0, 255, 0], 2)
#                 #         # Add detection logic here (e.g., drawing bounding boxes, analyzing the person)
#                 #     else:
#                 #         cv2.putText(img, "Not In Safe Area", (int(x1), int(y1) - 10), 0, 0.5, [255, 0, 0], 2)
#                 #         # Skip detection or take other actions if needed




#                 # if conf>0.5:
#                 #     cv2.rectangle(img, (x1,y1), (x2,y2), color,3)
#                 #     cv2.rectangle(img, (x1,y1), c2, color, -1, cv2.LINE_AA)  # filled
#                 #     cv2.putText(img, label, (x1,y1-2),0, 1,[255,255,255], thickness=1,lineType=cv2.LINE_AA)

#         yield img
#         #out.write(img)
#         #cv2.imshow("image", img)
#         #if cv2.waitKey(1) & 0xFF==ord('1'):
#             #break
#     #out.release()


# cv2.destroyAllWindows()
# from ultralytics import YOLO
# import cv2
# import math


# def is_in_not_safe_area(person_box, not_safe_area):
#     x1, y1, x2, y2 = person_box
#     nsafe_x1, nsafe_y1, nsafe_x2, nsafe_y2 = not_safe_area
    
#     # Check if the person's box is within the safe area
#     return (x1 >= nsafe_x1 and y1 >= nsafe_y1 and x2 <= nsafe_x2 and y2 <= nsafe_y2)


def is_in_not_safe_area(person_box, not_safe_area):
    x1, y1, x2, y2 = person_box
    nsafe_x1, nsafe_y1, nsafe_x2, nsafe_y2 = not_safe_area
    
    # Check if any corner of the person's box is within the not safe area
    return not (
        x2 < nsafe_x1 or  # Right edge of person box is left of left edge of not safe area
        x1 > nsafe_x2 or  # Left edge of person box is right of right edge of not safe area
        y2 < nsafe_y1 or  # Bottom edge of person box is above top edge of not safe area
        y1 > nsafe_y2     # Top edge of person box is below bottom edge of not safe area
    )

    

def video_detection(path_x):
    video_capture = path_x
    # Create a Webcam Object
    cap = cv2.VideoCapture(video_capture)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    # out=cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P','G'), 10, (frame_width, frame_height))

    model = YOLO("YOLO-Weights/best5.pt")
    # classNames = ['Protective Helmet', 'Shield', 'Jacket', 'Dust Mask', 'Eye Wear', 'Glove', 'Protective Boots']
    classNames = ['boots', 'gloves', 'helmet', 'helmet on',
        'no boots', 'no glove', 'no helmet', 'no vest', 'person', 'vest']

    not_safe_area = (0, 0, 200, 500) 
    # Set colors for drawing
    not_safe_color = (255, 0, 0)  # Green for safe area



    while True:
        success, img = cap.read()

        #  lines----------------------------------------------------------------
        # cv2.rectangle(img, (not_safe_area[0], not_safe_area[1]), (not_safe_area[2], not_safe_area[3]), not_safe_color, 2)
        # cv2.putText(img, "Not Safe Area", (not_safe_area[0], not_safe_area[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, not_safe_color, 2)

        results=model(img,stream=True)
        

        for r in results:
            # print (r)
            boxes=r.boxes
            # print(len(boxes))
            for box in boxes:
                x1,y1,x2,y2=box.xyxy[0]
                x1,y1,x2,y2=int(x1), int(y1), int(x2), int(y2)
                # print(x1,y1,x2,y2)
                conf=math.ceil((box.conf[0]*100))/100
                cls=int(box.cls[0])
                class_name=classNames[cls]
                label=f'{class_name}{conf}'
                t_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
                # print(t_size)
                c2 = x1 + t_size[0], y1 - t_size[1] - 3
                # if class_name == 'gloves':
                #     color=(0, 204, 255)
                # elif class_name == "helmet":
                #     color = (222, 82, 175)
                # elif class_name == "boots":
                #     color = (0, 149, 255)
                # else:
                #     color = (85,45,255)

                color = (0, 0, 255)

# # helmet and boundery
                # if class_name == 'person' and (is_in_not_safe_area((x1, y1, x2, y2), not_safe_area)):
                #     for i in boxes:
                #         # print(classNames[(int(i.cls[0]))-1])
                #         if classNames[int(i.cls[0])] == 'helmet' or classNames[int(i.cls[0])] == 'helmet on':
                #             # i coordinates
                #             i_x1,i_y1,i_x2,i_y2=i.xyxy[0]
                #             i_x1,i_y1,i_x2,i_y2=int(i_x1), int(i_y1), int(i_x2), int(i_y2)

                #             # check if the i_coordinates are in person
                #             if i_x1>=x1 and i_x1<=x2 and i_y1>=y1 and i_y1<=y2:
                #                 color =(0, 255, 0)
                #                 print(f'person is in {class_name}')
                #                 cv2.putText(img, "Safe", (x1,y1-40),0, 1,[0,255,0], thickness=1,lineType=cv2.LINE_AA)
                #                 warning_sound.stop()
                #                 break
                #             else:
                #                 color=(255, 0, 0)
                #                 # cv2.putText(img, "Not Safe", (x1,y1-40),0, 1,[255,0,0], thickness=1,lineType=cv2.LINE_AA)


                        
                #         if not pygame.mixer.get_busy():  # Check if sound is already playing
                #             warning_sound.play(maxtime=1000,fade_ms=100)


                     

                





#                 # if class_name == 'person':
#                 #     for i in boxes:
#                 #         if   (classNames[int(i.cls[0])] == 'helmet' or classNames[int(i.cls[0])] == 'helmet on'):
#                 #             if classNames[int(i.cls[0])] == 'vest' :
#                 #                 i_x1,i_y1,i_x2,i_y2=i.xyxy[0]
#                 #                 i_x1,i_y1,i_x2,i_y2=int(i_x1), int(i_y1), int(i_x2), int(i_y2)

#                 #                 if i_x1>=x1 and i_x1<=x2 and i_y1>=y1 and i_y1<=y2:
#                 #                     color =(0, 255, 0)
#                 #                     print(f'person is in {class_name}')
#                 #                     cv2.putText(img, "Safe", (x1,y1-40),0, 1,[0,255,0], thickness=1,lineType=cv2.LINE_AA)
#                 #                     break
#                 #                 else:
#                 #                     color = (85,45,255)



#  vest and helmet ----------------------------------------------------

                if class_name == 'person':
                    for i in boxes:
                    # Check if the object is safety equipment
                        obj_class = classNames[int(i.cls[0])]
                        if obj_class in ['helmet', 'helmet on'] and 'vest' in [classNames[int(j.cls[0])] for j in boxes]:
                            # Extract bounding box coordinates
                            i_x1, i_y1, i_x2, i_y2 = map(int, i.xyxy[0])

                            # Check if the safety equipment is within the person's bounding box
                            if i_x1 >= x1 and i_x2 <= x2 and i_y1 >= y1 and i_y2 <= y2:
                                color = (0, 255, 0)
                                print(f'Person is safe with {obj_class} and vest')
                                cv2.putText(img, "Safe", (x1, y1 - 40), 0, 1, [0, 255, 0], thickness=1, lineType=cv2.LINE_AA)
                                # warning_sound.stop()
                                break
                            else:
                                color = (0, 0, 255)

                        # else:
                        #      if not pygame.mixer.get_busy():  # Check if sound is already playing
                        #             warning_sound.play()


                        elif obj_class in ['helmet', 'helmet on']:
                            # Extract bounding box coordinates
                            i_x1, i_y1, i_x2, i_y2 = map(int, i.xyxy[0])

                            # Check if the safety equipment is within the person's bounding box
                            if i_x1 >= x1 and i_x2 <= x2 and i_y1 >= y1 and i_y2 <= y2:
                                color = (18, 241, 248 )
                                # print(f'Person is safe with {obj_class} and vest')
                                # cv2.putText(img, "Safe", (x1, y1 - 40), 0, 1, [0, 255, 0], thickness=1, lineType=cv2.LINE_AA)
                                # warning_sound.stop()
                                print("Helmet")
                                break
                            else:
                                color = (0, 0, 255)


                        # elif 'vest' in [classNames[int(j.cls[0])] for j in boxes]:
                        #     # Extract bounding box coordinates
                        #     i_x1, i_y1, i_x2, i_y2 = map(int, i.xyxy[0])

                        #     # Check if the safety equipment is within the person's bounding box
                        #     if i_x1 >= x1 and i_x2 <= x2 and i_y1 >= y1 and i_y2 <= y2:
                        #         color = (248, 241, 18 )
                        #         # print(f'Person is safe with {obj_class} and vest')
                        #         # cv2.putText(img, "Safe", (x1, y1 - 40), 0, 1, [0, 255, 0], thickness=1, lineType=cv2.LINE_AA)
                        #         # warning_sound.stop()
                        #         print("Vest")
                        #         break
                        #     else:
                        #         color = (85, 45, 255)




# only helmet     ---------------------------------------------------------------------------------------------                           
                # if class_name == 'person':
                #     for i in boxes:
                #         if classNames[int(i.cls[0])] == 'helmet' or classNames[int(i.cls[0])] == 'helmet on':
                #             i_x1,i_y1,i_x2,i_y2=i.xyxy[0]
                #             i_x1,i_y1,i_x2,i_y2=int(i_x1), int(i_y1), int(i_x2), int(i_y2)

                #             if i_x1>=x1 and i_x1<=x2 and i_y1>=y1 and i_y1<=y2:
                #                 color =(0, 255, 0)
                #                 print(f'person is in {class_name}')
                #                 cv2.putText(img, "Safe", (x1,y1-40),0, 1,[0,255,0], thickness=1,lineType=cv2.LINE_AA)
                #                 warning_sound.stop()
                #                 break
                #             else:
                #                 color = (85,45,255)
                               
                #         else:
                #              if not pygame.mixer.get_busy():  # Check if sound is already playing
                #                     warning_sound.play()
                                










# commmon ----------------------------------------------------------------





                    if conf>0.5:
                        cv2.rectangle(img, (x1,y1), (x2,y2), color,3)
                        cv2.rectangle(img, (x1,y1), c2, color, -1, cv2.LINE_AA)  # filled
                        cv2.putText(img, label, (x1,y1-2),0, 1,[255,255,255], thickness=1,lineType=cv2.LINE_AA)
                        # warning_sound.stop()

                # warning_sound.stop()


        yield img
        #out.write(img)
        #cv2.imshow("image", img)
        #if cv2.waitKey(1) & 0xFF==ord('1'):
            #break
    #out.release()

warning_sound.stop()
cv2.destroyAllWindows()