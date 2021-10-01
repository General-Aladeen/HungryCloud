from pyA20.gpio import gpio as GPIO
button = Button(9)

while true:
  if button.is_pressed:
    print('hi')
  else:
    print('bai')
