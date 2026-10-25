import math

ang = float(input('Digite um angulo qualquer: '))
seno = (math.sin(math.radians(ang)))
cos = (math.cos(math.radians(ang)))
tan = (math.tan(math.radians(ang)))
print(f'O angulo {ang:.2f} tem: \nSeno: {seno:.2f} \nCosseno: {cos:.2f}\nTangente: {tan:.2f}')
