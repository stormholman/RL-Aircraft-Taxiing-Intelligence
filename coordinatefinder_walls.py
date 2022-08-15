# importing the module
import cv2
import pandas as pd


# function to display the coordinates of
# of the points clicked on the image


def making_csv(mycoordinates):
    rows = []
    for i in range(len(mycoordinates['x1'])):
        mystring = "wall " + str(i + 1)
        rows.append(mystring)

    mycoor = pd.DataFrame(mycoordinates, index=rows)

    mycoor.to_csv('coordinates_walls.csv')
    return mycoor


def making_dict(listx, listy):
    mycoordinates = {"x1": [], "y1": [], "x2": [], "y2": []}

    for i in range(len(listx)):

        if i < len(listx) - 1:
            mycoordinates["x1"].append(listx[i])
            mycoordinates["y1"].append(listy[i])
            mycoordinates["x2"].append(listx[i + 1])
            mycoordinates["y2"].append(listy[i + 1])
        else:
            pass

    return mycoordinates


def click_event(event, x, y, flags, params):
    count = 0

    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
        mycoorlistx.append(x)
        mycoorlisty.append(y)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(x) + ',' +
                    str(y), (x, y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', img)
        count = count + 1

    # checking for right mouse clicks    
    if event == cv2.EVENT_RBUTTONDOWN:
        print(mycoorlistx, mycoorlisty)
        mycoordict = making_dict(mycoorlistx, mycoorlisty)
        mycoor = making_csv(mycoordict)
        print(mycoor)


# driver function
if __name__ == "__main__":
    mycoorlistx = []
    mycoorlisty = []
    # reading the image
    img = cv2.imread('taximap.png', 1)

    # displaying the image
    cv2.imshow('image', img)

    # setting mouse handler for the image
    # and calling the click_event() function
    cv2.setMouseCallback('image', click_event)

    # wait for a key to be pressed to exit
    cv2.waitKey(0)

    # close the window
    cv2.destroyAllWindows()
