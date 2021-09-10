# Kalman-Filter-Test

The Kalman Filter is used in any place where you have uncertain infromation about a dynamic system and you can make an educated guess of what the system will do next. The filter will provide an estimated sensor reading from a noisy measurement. 

There will be two main steps:
 
1.) The prediction: The filter produces estimates of the current state variables and their uncertainities. 

2.) The update: Updates the variables with a weighted average, where greater weight is awarded to the estimates with greater certainity. 

The blue line represents the real vector x (location and velocity) while the red line demonstrates the kalman filter.
<img width="643" alt="Screen Shot 2021-09-09 at 7 35 28 PM" src="https://user-images.githubusercontent.com/26367708/132790129-f3d87eb1-ab37-4ef3-8318-69e3826972d9.png">


This program also contains a test script labeld test_kf.py.
  
