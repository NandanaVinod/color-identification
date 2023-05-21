import cv2
import pandas as pd

img_path = 'assests/image.jpg'
img = cv2.imread(img_path)

clicked = False
r = g = b = x_pos = y_pos = 0

index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

def get_color_name(R, G, B):
    minimum = float('inf')
    cname = ''
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

def draw_function(event, x, y, flags, param):
    global b, g, r, x_pos, y_pos, clicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        clicked = True
        x_pos, y_pos = x, y
        b, g, r = img[y, x]

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
    cv2.imshow('image', img)

    if clicked:
        color = [int(b), int(g), int(r)]
        color_name = get_color_name(r, g, b)
        print(f"Selected Color: {color_name} (R={r}, G={g}, B={b})")
        clicked = False

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
