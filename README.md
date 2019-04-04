# object-detect
Identify an object(leaves in this case) and check its presence for certain duration and return output if its present or not.
The drive link for the model files: https://drive.google.com/open?id=1JyXEKT8ALXr151RD79AW6legVZjow9n1

For running the model, a user needs a raspberry pi with a pi cam or USB camera attached to it. As the user issues the label_iamge.py file from the scripts folder, the raspberry pi clicks the picture of an object. 

This is passed through the trained model. And we get an output. 

This is checked again and again at certain intervals, if the same object is present at certain amount of time, we conclue the object is present there since a long time. 
