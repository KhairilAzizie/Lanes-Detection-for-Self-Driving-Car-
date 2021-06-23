# Lanes Detection for Self Driving Car 

## A. PROJECT SUMMARY

**Project Title:** Lanes Detection for Self Driving Car 

**Team Members:** 
- [Amirul Aizat Bin Rosli 	B031910118]
- [Ahmad Firdaus bin Mohamad	B031910133]
- [Mohammad Syauqi bin Abdul latiff	B031910393]
- [Khairil Nur Azizie Bin Shafirudin	B031910249]



- [ ] **Objectives:**
- Break out the project goal into more specific objectives
- Minimize the road accident due to human error
- Provide clearer vision to pick lane during driver if the weather is bad

##  B. ABSTRACT 

Detecting lane lines while driving on the road is a task for autonomous vehicles.Despite the fact that it appears to be a simple task, it is a critical component of the project. Lane line detection is a vehicle-based system that will assist and give a self-driving car system. It will maintain the automobile on track and assist the drivers with safe driving by employing image processing to do recognition on the road lane. The developer will do the machine training by using Neural Network technique to build the line detector and then build a system that detect lane lines in real-time. The project will need computer vision to do the detection and the available computer vision at the moment is OpenCV library.



![Coding](https://github.com/KhairilAzizie/Lanes-Detection-for-Self-Driving-Car-/blob/main/Lane%20Line/Lane%20line%201.jpg)

Figure 1 shows how the AI  work to detect lane to pick



## C.   PROJECT STRUCTURE
C:\Users\BSSE\PycharmProjects\pythonProject
- ├── video
- │   ├── input.mp4
- │   ├── 
- 1 directories, 2 files



## D.  IMPLEMENTATION,RESULT 

Every image is essentially a numpy array at the end of the day, with values containing pixel intensities, 0 denoting complete black(dark) and 1 denoting complete white(bright), considering a grayscale image.The technique that we use to run the system is :

### 1.Gaussian Blur

![Coding](https://github.com/KhairilAzizie/Lanes-Detection-for-Self-Driving-Car-/blob/main/Lane%20Line/gradient.png)

Figure 2 show the gradient use to detect road line on the road.The above image shows a Strong gradient on the left and a Weak Gradient on the right.

### 2. Canny Edge Detection

As the name imply, it is an algorithm to detect edges in our image.A change in intensity of pixel will gives us an edge.

![Coding](https://github.com/KhairilAzizie/Lanes-Detection-for-Self-Driving-Car-/blob/main/Lane%20Line/code%201.PNG)

Figure 3 show the code used in implementing the canny edge detection.

where blur represent blur image, 50 = low threshold ,150 = high treshold.

### 3. Hough Transform

After detecting the edge in the image using technique above, we will use the technique call hough transform to detect the lane lines.But before that, we need to find **region of interest** in our image by using certain code.

once its done,we create a polygon over as shown 

![Coding](https://github.com/KhairilAzizie/Lanes-Detection-for-Self-Driving-Car-/blob/main/Lane%20Line/gradient1.PNG)

0000 represents the black pixels and 11111111 represents the white pixels, denoting the polygon. Now, we apply the bitwise_and in the original image and the mask to obtain the masked_image, which essentially will contain only the region on interest.

![Coding](https://github.com/KhairilAzizie/Lanes-Detection-for-Self-Driving-Car-/blob/main/Lane%20Line/combine.PNG)

### Result 

The result that we get by combining the hough transform and gaussian blur able to make the system detect and highlight the line in the road lane as shown in the image below.

From this.

![Coding](https://github.com/KhairilAzizie/Lanes-Detection-for-Self-Driving-Car-/blob/main/Lane%20Line/actual.PNG)

To this.

![Coding](https://github.com/KhairilAzizie/Lanes-Detection-for-Self-Driving-Car-/blob/main/Lane%20Line/result.PNG)

![Coding](https://github.com/KhairilAzizie/Lanes-Detection-for-Self-Driving-Car-/blob/main/Lane%20Line/result%202.PNG)










## E.   PROJECT PRESENTATION 




