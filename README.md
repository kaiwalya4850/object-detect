# object-detect
Identify an object(leaves in this case) and check its presence for certain duration and return output if its present or not.
The drive link for the model files: https://drive.google.com/open?id=1JyXEKT8ALXr151RD79AW6legVZjow9n1

For running the model, a user needs a raspberry pi with a pi cam or USB camera attached to it. As the user issues the label_iamge.py file from the scripts folder, the raspberry pi clicks the picture of an object. 

This is passed through the trained model. And we get an output. 

This is checked again and again at certain intervals, if the same object is present at certain amount of time, we conclue the object is present there since a long time. 

As raspberry pi is a micro computer it lacks in computational power, so, same thing can be hosted on any server(say floydhub). In those cases, the pi sends the output to the server and everything is processed on serverside and we get an API key to get the outputs(we can send requests to it by POSTMAN)

The model would soon be trained on car images. More and more would be added.

The model is now trained even to identify the difference between car and motorcycle, all a person needs to do is download a file from above drive link. If it is for leaf detection, go for RETRAINED_GRAPHS.PB and RETRAINED_LABELS.TXT and f you want to detect cars, use the files, OUTPUT_GRAPHS_CAR.PB and OUTPUT_LABELS_CARS.TXT. (Dont forget to configure raspberry pi properly!)

Open code_data folder for license plate code, there exract the training data files and open LPOCR.ipynb, make sure to keep evertything in one folder and just run as it is. HOPE SO TESERACT WORKS! else use imread function from openCV, it worked.
