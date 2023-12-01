import cv2
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
imgBackground = cv2.imread('C:/Users/USER/Desktop/face-attendance-system-master/Resources/background.PNG')
folderModePath = 'C:\\Users\\USER\\Desktop\\face-attendance-system-master\\Resources\\Modes'  # Double backslashes for Windows paths
modePathList = os.listdir(folderModePath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

#print(len(imgModeList))  # Corrected variable name

while True:
    success, img = cap.read()

    # Vérifier que la capture vidéo a réussi
    if not success:
        print("Échec de la capture d'image.")
        break

    # Vérifier les dimensions de l'image capturée
    if img is not None and img.shape[0] > 0 and img.shape[1] > 0:
        imgBackground[162:162+480, 55:55+640] = img
        imgBackground[44:44+ 633, 808:808+414] = imgModeList[0]

        cv2.imshow("Webcam", img)
        cv2.imshow("Face Attendence", imgBackground)

    # Attendre 1 milliseconde et vérifier si une touche est pressée
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libérer la capture vidéo et détruire toutes les fenêtres OpenCV
cap.release()
cv2.destroyAllWindows()
