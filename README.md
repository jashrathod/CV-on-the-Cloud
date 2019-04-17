# CV on the Cloud

The aim of this project is to develop and provide state-of-the-art AI tool, putting the latest machine learning technologies to work for the Users. With its ability to handle compute and data analytics at any scale, Cloud computing accelerates the capabilities of machine learning to the next level.

## Introduction

During the last years, the nature of the Internet was constantly changing from a place used to read web pages to an environment that allows end-users to run software applications. Interactivity and collaboration have become the keywords of the new web content. This new environment supports the creation of a new generation of applications that are able to run on a wide range of hardware devices, like mobile phones or PDAs, while storing their data inside the cloud.

Artificial Intelligence is changing the face of a lot many industries. Image processing and Computer Vision have helped the world in solving problems that could not be done before. This project focuses on solving one such problem. It mainly focuses on using Artificial Intelligence to identify digits (0 to 9) by applying cutting-edge image processing techniques on the image of a digit. This project has the potential to change millions of lives all around the world and help numerous industries work better.

## Diagram

<img src="/static/documentation_images/Diagram.png" width=500>

## Objective

The mission is to develop and provide state-of-the-art AI tool, putting the latest machine learning technologies to work for the Users. With its ability to handle compute and data analytics at any scale, Cloud computing accelerates the capabilities of machine learning at an unprecedented level.

## Methodology

### Communication and Networking

HTTP means Hyper Text Transfer Protocol. HTTP is the underlying protocol used by the World Wide Web and this protocol defines how messages are formatted and transmitted, and what actions Web servers and browsers should take in response to various commands.

### Machine Learning and Computer Vision

Machine learning is an application of Artificial Intelligence that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. A Support Vector Machine (SVM) is a discriminative classifier formally defined by a separating hyperplane. In other words, given labeled training data (supervised learning), the algorithm outputs an optimal hyperplane which categorizes new examples. Computer vision is concerned with the automatic extraction, analysis and understanding of useful information from a single image or a sequence of images. It involves the development of a theoretical and algorithmic basis to achieve automatic visual understanding.

### Database Management System
NoSQL is an approach to database design that can accomodate a wide variety of data models, including key-value, document, columnar and graph formats. NoSQL, which stand for "not only SQL," is an alternative to traditional relational databases. In this project, we have used MongoDB (a noSQL database). MongoDB is a cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with schemata.

## Implementation

### Back-End and Data Transmission

We will Setup a Server on Local Network on Remote Computing Device. In computing, POST is a request method supported by HTTP used by the World Wide Web. By design, the POST request method requests that a web server accepts the data enclosed in the body of the request message, most likely for storing it.

It is often used when uploading a file or when submitting a completed web form. Server will be Setup using the Python Framework “Flask” which will call the Driver Code as a Subroutine and Return the Result as a Web Page to the User.
The route() decorator in Flask is used to bind URL to a function. For example - 

```python
@app.route(‘/hello’) 
def hello_world():
    return ‘hello world’
 ```
 
Here, URL ‘/hello’ rule is bound to the hello_world() function. As a result, if a user visits http://localhost:1000/hello URL, the output of the hello_world() function will be rendered in the browser. The Return Value of the Function is an HTML Element. We can also use HTML Template to Render the Layout and Pass Any Variables/Placeholders as Parameters.

### Image Processing

The data set used here is MNIST dataset as well as a custom data set. The MNIST database (Modified National Institute of Standards and Technology database) is a large database of handwritten digits (0 to 9). The database contains 60,000 training images and 10,000 testing images each of size 28x28. The first step is to load the dataset. Now, to prepare the data we need some processing on the images like resizing images, normalizing the pixel values etc. Now our dataset is ready for training. We use Support Vector Machines (SVM) for training the model. Once the training is done, we feed the test set to know how well does our model perform on new data. We can also use custom dataset for testing. A similar procedure was performed for a custom training dataset. It was observed that the latter produced better real-time results. Hence, in this project, the custom training dataset is used.

### Front End

Initially, the user needs to log in to avail the services of Digit recognition. One can also register if he/she is a new user. The Website will then allow the User to add image and send it to the Server using POST Request. The resultant image will be displayed back to the User with the corresponding digits highlighted with recognised number. If there are multiple digits, the application will try to address and process all of them. The user is then prompted to identify whether the highlighted digit is rightly identified. If not, then the image is stored in database for further analysis. If all predictions were right, the user is redirected to the page where another file can be uploaded for predictions. The user can also logout of the site and/or delete their account. Upon opting for any of these, the necessary operations are performed and the user is redirected to the login page.

### Database

A noSQL database consists of multiple collections. These collections are analogous to tables in an RDBMS Database. The database we created consists of two collections. One for storing the user login details, and the other one for storage and retieval of images on which image processing techniques were performed. Hence, we have used Python MongoDB for this purpose. A user can ’Sign up’ and register, which adds user’s ’username’ and ’password’ to the database. Once, logged in, the user can go ahead with the Digit Recognition process. Once, predictions are made, the user is prompted to let us know if the predictions were right. Upon wrong predictions, the image is stored in the database and can also be viewed by the user. Also, a user can log out or even delete his/her account. Upon deletion of account, the user’s login data is erased from the database.

## Output

<img src="/static/documentation_images/image1.png">
<img src="/static/documentation_images/image2.png">
<img src="/static/documentation_images/image3.png">

### Result

Users will be able to get On-Demand Handwritten Digit Recognition without performance Taxing on their own device and Databases can be used to store the Input Images for further studies.

### Future Scope

Future studies might consider designing such more systems for handwritten characters recognition, object recognition, image segmentation, handwriting recognition and future studies also might consider on hardware implementation on online digit recognition system with more performance and efficiency with live results from live testing case scenarios. This can also be extended for the purpose of text language recognition and translation, proving to be beneficial for translation of regional languages for tourists. Also, this project has great potential to be used for helping the Blind by using image to text to speech techniques. Also, even better results can be obtained by using vari- ous other classes of Neural Networks for improving the Recognition accuracy. The stored images can be further processed and used for training our model. This can help us get better results with time and a massive training dataset to cover all different types of hand written digits.

### Conclusion

Using the Communication Technology, Open Source Tools and Databases, we can successfully employ the power of Cloud Computing to provide backbone for the rapidly emerging AI Industry.
