import cv2

# Print/show the image
# Print -- print in console and show is displayof image on the screen
img = cv2.imread('image.png')


# To import the datasets automatically instead of normally
# Stores the data in the array called classNames
classNames= []
# Strip and split it by a new line output is a single array called classNames
# of all the elements of the dataset
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
# print(classNames)

# Import the Configuration file and weights
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

# Pass the image -- Bounding box -- Ids of objects -- Names
net = cv2.dnn_DetectionModel(weightsPath,configPath)
# Default Parameters
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# Send the image to the model
#  First define the classids, confidance and bounding box


# Confidance Threshold is the percentage where the object can confirmly detect that the
# the object it detects is a sure or else it ignores
classIds, confs, bbox = net.detect(img,confThreshold=0.5)
print(classIds,bbox)

# bbox is the rectangle that forms around the object amd
# gives it name from the classIds

# for classID in classIds is the method you can use to get
# one variable that is class id but if we need more than we use the zip function

for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
    cv2.rectangle(img,box,color=(0,255,0), thickness=2)
    # After detection, Give names to the names by Id-1 as indexed above starts with 0
    # changing the text to uppercase and distances the box sizes from eachother on scale
    cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),
                # font name,scale/size of text,color,thickness
                cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0),2)

cv2.imshow("Output",img)
cv2.waitKey(0)
