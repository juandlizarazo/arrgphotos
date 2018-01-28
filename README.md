# ARrg photos
Hack@Brown 2018 Submission

ARrg photos is an exploration of viewing images in AR, comprised of two smaller projects, TourAR and Egg

[![ARrg, Photos!](https://img.youtube.com/vi/430MjjQhaqw/0.jpg)](https://www.youtube.com/watch?v=430MjjQhaqw&feature=youtu.be)
### Team members:
Gabriela Asuncion, Zhizhong (Isaac) Chen, Jessica Cheng, Nomin Khishigsuren, Juan David Lizarazo
## TourAR
### About
TourAR allows users to walk through Providence in a new way.  It maps images from four locations in Providence (Downtown, RISD, Main Green, and Barus and Holley) into arrays of images spread in a 3D space the size of Sayles Hall.
### Process
We created TourAR using Google Streetview API, Google Static Maps API, Three.js, coding on Python, Javascript, and Mathematica.

Using Python we looped through different latitude and longitude values and which we set as parameters in requests to Google Streetview API. The images returned by the request were saved and used in the AR. We plotted the positions of each image as markers on a satellite map using Google Static Maps API.

![](markers.png)


## Egg
### About
Egg explores the effects of density and spherical object distribution surrounding a central image of interest. It uses 2,000 white images which were placed around a Hack@Brown logo.
### Process

