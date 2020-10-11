# Capturing mouse events
import cv2 as cv

# Opening the text file named coords.txt
# to store the co-ordinates
f = open("coords.txt", "w")


# mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        # img[:] = 0
        cv.putText(img, "coordinates (%d,%d)" % (x, y), (60, 60), 2, 1, (0, 255, 0))
        # Select location of Text(Trial & Error)
        f.write(str(x)+"\n")
        # Select text's top left corner's co-ordinates
        f.write(str(y)+"\n")
        # Double click to select
        # Co-ordinates with blue text will be displayed


# Create a black image, a window and bind the function to window
img = cv.imread("ce4.jpg")

# cv.imshow('image',img)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)

while True:
    cv.imshow('image', img)
    if cv.waitKey(10) & 0xFF == 27:   # Press Escape Key to terminate window
        break
cv.destroyAllWindows()   

f.close()
