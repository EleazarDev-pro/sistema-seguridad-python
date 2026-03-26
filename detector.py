import cv2

# Abrir la camara de la canaima
cap = cv2.VideoCapture(0)

print("iniciando camara de seguridad...")

while true:
    ret, frame = cap.read()
    if not ret:
        break

  # Mostrar lo que ve la camara
  cv2.imshow('sistema de seguridad - EleazarDev-pro',frame)

  # si presiona 'q', el programa se cierra
  if cv2.waitkey(1) & 0xff == ord('q'):
      break

cap.release()
cv2.destroyAllwindows()
