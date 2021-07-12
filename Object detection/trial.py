# # # # import numpy as np 
# # # # import pandas as pd
# # # # import matplotlib.pyplot as plt

# # # # # %matplotlib inline 
# # # # # plt.margins(x=0)

# # # # arr_1 = np.linspace(0,5,11)
# # # # arr_2 = arr_1**2
# # # # arr_3 = arr_1*arr_2

# # # # plt.plot(arr_1,arr_2)
# # # # plt.xlabel("X Axis")
# # # # plt.ylabel("Y Axis")
# # # # plt.title('Title')
# # # # plt.show()

# # # from imageai.Detection import ObjectDetection

# # # detector = ObjectDetection()

# # # model_path = "./models/yolo-tiny.h5"
# # # input_path = "./input/test45.jpg"
# # # output_path = "./output/newimage.jpg"

# # # detector.setModelTypeAsTinyYOLOv3()
# # # detector.setModelPath(model_path)
# # # detector.loadModel()
# # # detection = detector.detectObjectsFromImage(input_image=r'C:\Users\varun\OneDrive\Desktop\Tensorflow Obejct Detection\img\my_img.jpg', output_image_path=r'C:\Users\varun\OneDrive\Desktop\Tensorflow Obejct Detection\img\new_img.jpg')

# # # for eachItem in detection:
# # #     print(eachItem["name"] , " : ", eachItem["percentage_probability"])


# # from imageai.Detection import ObjectDetection
# # import os

# # execution_path = os.getcwd()

# # detector = ObjectDetection()
# # detector.setModelTypeAsRetinaNet()
# # detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.1.0.h5"))
# # detector.loadModel()
# # detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"))

# # for eachObject in detections:
# #     print(eachObject["name"] , " : " , eachObject["percentage_probability"] )

# from imageai.Detection import ObjectDetection

# detector = ObjectDetection()

# model_path = "./Object detection/models/yolo-tiny.h5"
# input_path = "./Object detection/input/image.jpg"
# output_path = "./Object detection/output/newimage.jpg"

# detector.setModelTypeAsTinyYOLOv3()
# detector.setModelPath(model_path)
# detector.loadModel()

# detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)

# for eachItem in detection:
#     print(eachItem['name'] , ' : ', eachItem['percentage_probabili
