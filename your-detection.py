import jetson.inference
import jetson.utils

# Load SSD-MobileNet-v2 detection model
net = jetson.inference.detectNet("ssd-mobilenet-v2", threshold=0.2)

# Load image
img = jetson.utils.loadImage("/home/nvidia/Desktop/2.jpg")

# Detect objects
detections = net.Detect(img,overlay="box,labels,conf")

# Print the number of detected objects
print("Number of objects detected:", len(detections))
print()

# Print detection results
for detection in detections:
    print("ClassID:", detection.ClassID)
    print("Class:", net.GetClassDesc(detection.ClassID))
    print("Confidence:", detection.Confidence)
    print("Left:", detection.Left)
    print("Top:", detection.Top)
    print("Right:", detection.Right)
    print("Bottom:", detection.Bottom)
    print("Width:", detection.Width)
    print("Height:", detection.Height)
    print("Area:", detection.Area)
    print("Center:", detection.Center)
    print("-----------------------------")



# Save the detected image with bounding boxes
jetson.utils.saveImage(
    "/home/nvidia/Desktop/banana_0_detected.jpg",
    img
)

print()
print("Detection finished!")
print("Detected image saved to:")
print("/home/nvidia/Desktop/banana_0_detected.jpg")
