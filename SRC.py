import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import matplotlib.pyplot as plt


def openFile():
    filepath = filedialog.askopenfilename(initialdir="")
    file = open(filepath)
    print(file.name)
    ispath = file.name
    return ispath


def make_coordinates(image, line_parameters):
    slope, intercept = line_parameters
    y1 = image.shape[0]
    #y2 = int(y1*(3/5))
    y2 = int(y1 - 150)
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1,y1,x2,y2])


# finding the average slope
def average_slope_intercept(image, lines):
    right_fit = []
    left_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1,x2),(y1,y2),1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope,intercept))
    left_fit_average = np.average(left_fit, axis = 0)
    right_fit_average = np.average(right_fit, axis = 0)
    left_lines = make_coordinates(image, left_fit_average)
    right_line = make_coordinates(image, right_fit_average)
    return np.array([left_lines, right_line])


# set where is the area the lines are
def region_of_interest(image):
    height = image.shape[0]
    width = image.shape[1]

    #polygons = np.array([
    #    [(0, height), (1100, height), (560, 400)]
    #
    #])
    polygons = np.array([
        [(0, height), (800, height), (380, 290)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


# draw the line into the image
def display_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for x1,y1,x2,y2 in lines:

            cv2.line(line_image,(x1,y1),(x2,y2),(255,0,0),5)
    return line_image


# convert the input into canny image
def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    cannyImg = cv2.Canny(blur, 50, 150)
    return cannyImg


def run():

    window = Tk()
    window.withdraw()
    window.title('Choose the video')
    window.geometry('300x200')
    button = Button(text="Open", command=openFile)
    button.pack()

    cap = cv2.VideoCapture(openFile())
    while cap.isOpened():

        _, frame = cap.read()
        canny1 = canny(frame)
        cropped_image = region_of_interest(canny1)
        lines = cv2.HoughLinesP(cropped_image, 2, np.pi / 180, 100, np.array([]), minLineLength=100, maxLineGap=50)
        average_lines = average_slope_intercept(frame, lines)
        line_image = display_lines(frame, average_lines)
        combo_image = cv2.addWeighted(frame, 0.9, line_image, 1, 1)
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        cv2.imshow("result", combo_image)
        if cv2.waitKey(10) & 0xFF == ord('q') or 0xFF == ord('Q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    window.mainloop()


# main function
if __name__ == '__main__':
    run();

