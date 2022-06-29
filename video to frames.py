import cv2 
  
def FrameCapture(path): 
    
    vidObj = cv2.VideoCapture(path) 
    
    count = 0
    
    success = 1
  
    while success: 

        success, image = vidObj.read() 
  
        cv2.imwrite("frame%d.jpg" % count, image)
  
        count += 1
  
if __name__ == '__main__': 

    FrameCapture("y2mate.com - Rick Astley Never Gonna Give You Up Official Music Video_v144P.mp4")
