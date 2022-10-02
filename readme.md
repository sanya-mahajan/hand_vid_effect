HAND CONTROLLED WEBCAM FILTERS

use your fingers to change the filter applied to live webcam.
implemented using openCV (python) and python libraries - numPy and mediapipe for real time 
detection of hand.

the user can raise the number of fingers depending on the required effect.

mediapipe is used to determine a hand object. The model is already trained to determine
location of the hand and 
different landmarks on the fingers. There are mainly 21 points which are indicated by filled dots
and can be used to study the action performed.Then we draw lines to connect the landmarks.

a counter is maintained to track the number of fingers raised and accordingly the 
corresponding effect option is chosen.

the options are as follows:
![guidebox](https://user-images.githubusercontent.com/88281057/193452239-75330265-3333-4a76-af0f-27d25fcaf8b8.png)





the inbuilt functions of openCV are used to apply the filter on the captured 
frame and the result is seen in real time.




