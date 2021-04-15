import cv2 
import os


def videoAnzeigen():
      pfad = os.path.dirname(os.path.realpath(__file__)) + "/safetyfirst.mp4"
      print(pfad)
      cap = cv2.VideoCapture(pfad)
      if (cap.isOpened()== False):  
        print("Fehler beim Öffnen") 
        
        # Lesen bis Video komplett
      while(cap.isOpened()): 
            
        # Capture frame-by-frame 
            ret, frame = cap.read() 
            if ret == True: 
            
                # Frame anzeigen
                cv2.imshow('Frame', frame) 
            
                # Ende mit q
                if cv2.waitKey(25) & 0xFF == ord('q'): 
                    break
            
            # Break Schleife 
            else:  
                break
            
        # video capture object freigeben
      cap.release() 
        
        # Alle Frames schließen
      cv2.destroyAllWindows() 

videoAnzeigen()      

      
