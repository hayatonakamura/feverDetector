# feverDetector
https://iotcolumbia2020naka.weebly.com/

## Server
Contains AWS EC2 server code, in charge of processing thermal data, cleaning up images, and detecting faces using AWS Rekognition. 

## Board
Reads temperature data from the MLX90640 sensor using the driver (C++) at a rate of 4FPS. Whenever there is a heat signature match, the data is sent to dynamoDB, and S3.

## Cloud Vision
AWS Rekognition is used to detect faces, and crop them so that the iOS application can display the target's face only.

