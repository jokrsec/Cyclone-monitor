# Cyclone-monitor
Cyclone detection and Alerting System using Deep Learning algorithms.
For training we have used RESNET-50 So that we could caoture every minute feature for the images.
And we extracted an total of 90MB.

The working of site:
https://docs.google.com/presentation/d/e/2PACX-1vT_dsOo_W-7gwalEBhlFwf01s_GOqq3_cc_4Hv2P3Mf4w7qu_3hsbSyKuu_d7cPXpDFf1kLPVKgB9bB/embed?start=false&loop=false&delayms=3000
## Pravega

###### Presentation on:

Dealing with natural disasters and their aftermath.



##### The Deep Learning Model in Detail

we developed an automated calamity detection system using deep learning, which can

predict disasters in real-time and send an alert message. For this purpose, we trained

ResNet50 CNN model, and performance is measured by calculating the confusion matrix.

Model is also tested with pre-captured images acquired from satellites and drones.

Experimental results yield 97% accuracy and performed well when tested with videos

collected from YouTube...


#### Deep learning model

Our model consists of two phases:

```
1) Classification part
2) Visualizing heatmaps of class activation
```
**Classification model --**

**Dataset:**

Data set contains satellite images of different calamities such as cyclones (928 images), wildfires (1077 images),
earthquake (1350 images) and flood (1070 images).

**Preprocessing:**

Dataset images of varying spatial resolutions are resized to the image of size 224 x 224 followed by conversion
into RGB format. To avoid overfitting/underfitting, we follow the data augmentation approach and applied
transformations such as rotation (30), zoom (0.15), width shift and height shift (0.2), shear range (0.15) and
horizontal flip randomly to each image. This augmented image is taken as an input to the convolutional neural
network (CNN) model.


**Model training:**

We have used the transfer learning technique using pre-trained ImageNet weights. We used

ResNet50 is the backbone model, all the internal layers up to global average pooling

(GAP) layer remains unchanged. We have removed the FC layer and added the average pooling

(pool_size = (7, 7)), Flatten, Dense layer (512), Dropout layer (0.5) and Dense layer

followed by Activation (softmax). Illustration of similar architecture we have used.


### The

### trained

### Model


Visualizing heatmaps of class activation

We have used GRAD CAM Mapping to find the intensity of the cyclones.

To visualize the heatmap, we have used use a technique called Grad-CAM (Gradient Class

Activation Map).

The idea behind it is quite simple; to find the importance of a certain class in our model, we

simply take its gradient with respect to the final convolutional layer and then weigh it against

the output of this layer.

Grad-CAM function can accurately and precisely show us the activation heatmap of the model,

telling us what the neural network “sees” and what it values when making its prediction. This

could not only improve model explainability but accuracy as well.


##### Working model representation

```
Classification model
And predictions
```
```
Images/video
```
```
Visualizing heatmaps of
class activation
Using GRADCAM
```
```
Model successfully
detected cyclone in video
```
```
Heatmap + image= intensity Heatmap activation of object in image^
```

The model Accuracy and Loss of While Training.


The output of trained Model


**Web Application**

● To allow the users to interact with the Machine learning model which was used to

detect the cyclone and its intensity, we have come up with a Web Application.

● The Web application has a cyclone monitoring feature which is useful to check

the current intensity of the cyclone along with other details.

● Also, users can register themselves on the website to get notified about the

intensity levels and alerts about the cyclones nearby.


**Technologies**

We have used frameworks and technologies to -

1. Build the webserver
2. Integrate the Machine learning model into the webserver
3. Send alerts and details about cyclones to users.

Below are the frameworks -

```
● Flask (webserver)
● Python-pickle (serialisation module)
● Vonage (SMS API)
```

**Website components**


**Real time Data Web Server**^^ **Users**^

**Messaging API**

```
Data collection
&
Preprocessing
```
```
Trained
Model
```
**Work Flow Of The Complete System**


The Final output After integrating the model with the server


Alert message initiated as our model detected cyclone


**Targeted Audience**

● This model is useful for governments to detect cyclones and alert their

citizens and prioritize their safety.

● Farmer can know about cyclones early and will be able to take sufficient

precautions.

● Users can get an idea of the ocean’s condition at a specific location

```
which will be helpful for businesses that operate at a particular
location on oceans.
```
● Businesses that are sensitive to weather conditions can use this

model to track weather conditions from time to time.


Cost Approximation

```
● Getting the satellite footage of the ocean is the costliest thing in this entire
System Which will cost us around 50,000 to 1,00,000 Rupees.
● Processing the ocean’s satellite footage using machine learning models is a
bit costly. But nowadays we can do that using cloud computing services like
Amazon SageMaker at a reasonable price.
● Hosting the web application and sending the alert messages to the users will
barely cost 10,000 rupees per month.
```

OUR TEAM( CODEBREWERS)

❖ **_N. JAYADITYA_**

❖ **_L. ABHIJEETH BABA_**

❖ **_J. HEMANTH KUMAR_**

❖ **_T. VIJAYA KUMAR REDDY_**


## Thank you

# THE END







<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vT_dsOo_W-7gwalEBhlFwf01s_GOqq3_cc_4Hv2P3Mf4w7qu_3hsbSyKuu_d7cPXpDFf1kLPVKgB9bB/embed?start=false&loop=false&delayms=3000" frameborder="0" width="960" height="569" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
