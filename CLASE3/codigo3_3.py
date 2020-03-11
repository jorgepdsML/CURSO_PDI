import cv2
#lectura de video previamente creado
cap=cv2.VideoCapture("video1.avi")
#conseguir información sobre el video , fps
fps=cap.get(cv2.CAP_PROP_FPS)
#mostrar fps
print(fps)
estado=True
while estado:
    estado,frame=cap.read()
    if estado==False or cv2.waitKey(int(1000/fps))==ord("q"):
        cap.release()
        cv2.destroyAllWindows()
        break
    cv2.imshow("IMAGEN",frame)


