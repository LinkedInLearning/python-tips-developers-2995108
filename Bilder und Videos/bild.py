import cv2 
import os

def bildAnzeigen():
      print(os.path.dirname(os.path.realpath(__file__)))
      image = cv2.imread(os.path.dirname(os.path.realpath(__file__)) + '/bild.jpg',1)
      if image is None:
          print("Fehler beim Öffnen von " + image)
          exit(-1) 
      cv2.imshow("Der Blick von oben",image)
      cv2.waitKey(0)
      cv2.destroyAllWindows()     
bildAnzeigen()      
