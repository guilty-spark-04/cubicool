import cv2
import time
import io
import os

cam = cv2.VideoCapture(0)

def imagecapture():
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
    time.sleep(0.8)
    img_name = "opencv_frame_{}.png".format(0)
    cv2.imwrite(img_name, frame)
    print("{} written!".format(img_name))
    time.sleep(0.2)
    print("Closing...")
    cam.release()
    return img_name

def localize_objects(path):
    """Localize objects in the local image.
    Args:
    path: The path to the local file.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with open(path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    objects = client.object_localization(image=image).localized_object_annotations

    print('Number of objects found: {}'.format(len(objects)))
    for object_ in objects:
        print('\n{} (confidence: {})'.format(object_.name, object_.score))
        print('Normalized bounding polygon vertices: ')
        for vertex in object_.bounding_poly.normalized_vertices:
            print(' - ({}, {})'.format(vertex.x, vertex.y))

imagecapture()
localize_objects(r"./opencv_frame_0.png")


    