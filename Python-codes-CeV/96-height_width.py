'''
This function will show the area from a land height x width

Land control
---------------
Width (m):
Height (m):
The area of a land A x B is Y m²
'''


def size(w, h):
    
    area = w * h
    print(f'The area of the land {w} x {h} is {area}m²')


w = float(input('Type the width value: '))
h = float(input('Type the height value: '))
size(w, h)

