# Singnal-Detection-on-Road
This is Single detection or any object like (Board on road, turn on road etc). It is being used in self driving car. 

***********************************************************0000************************************************************************************
All you need a image of road side having some sort of signal and boards and so on...
Libraries are Open cv for images analisys and numpy for neumerical calculation.

# Step:-1
Import libraries open cv and numpy
Read the image into three variable.
let say 1,2 3 are my var(remebmber these three are image datatype itself)

convert BGR to Gray Scale image of 1 var

# step:-2

Now we calculate low_red values and upper_red values using numpy.
Then mask there red with you grayscaled image using opencv.
Now initialize kernal and erode using open cv and numpy..
Now initialize/find counters from that erode using opencv.

# step:-3

Now for each cnt in counter we try to find area of image having signal board..... with appropriate color.
save it into a var and draw rectangle on the all fund boards right....

and now find text written on that board in rectagle...


now here 2 thing u can do you can dispaly them or ask the owner to perform some action

2nd is To perform action automaticll by taking this text as input to other ML model..






****************************************************************************************Thank You**********************************************************************
