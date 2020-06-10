import cv2
import numpy as np

bgr=cv2.imread('SPMN.png')
rgb=cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)
escgris=cv2.cvtColor(rgb,cv2.COLOR_BGR2GRAY)
rojo=np.copy(rgb)
rojo[:,:,0] = 0;
verde=np.copy(rgb)
verde[:,:,1] = 0;
azul=np.copy(rgb)
azul[:,:,2]=0;
rgb=cv2.cvtColor(bgr,cv2.COLOR_BGR2RGB)
rojo=cv2.cvtColor(rojo,cv2.COLOR_BGR2RGB)
verde=cv2.cvtColor(verde,cv2.COLOR_BGR2RGB)
azul=cv2.cvtColor(azul,cv2.COLOR_BGR2RGB)
cv2.imshow("ORIGINAL-RGB",bgr) #Original
cv2.imshow("ESCALA-DE-GRISES",escgris) #Escala De Grises
cv2.imshow('SIN-ROJO',rojo) #Rojo a 0
cv2.imshow('SIN-VERDE',verde) #Verde a 0
cv2.imshow('SIN-AZUL',azul) #Azul a 0
cv2.imwrite('ESCGR.jpg', escgris)
cv2.imwrite('NOR.jpg', rojo)
cv2.imwrite('NOB.jpg', azul)
cv2.imwrite('NOG.jpg', verde)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.waitKey(0)
cv2.destroyAllWindows()