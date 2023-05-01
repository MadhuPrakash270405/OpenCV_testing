
# Python OpenCV Testing

OpenCV is an open-source computer vision and machine learning library that provides developers with tools for building applications related to image and video processing, object detection, machine learning, and more. Widely used in various industries such as robotics, automotive, healthcare, security and entertainment.

Testing the functionality of your OpenCV application is essential to ensure that it works as expected and meets the required quality standards. One way to test the functionality of your OpenCV application is to use the pytest framework, a popular testing framework for Python applications.

To test the functionality of your OpenCV application using pytest, you can create test cases covering different scenarios and edge cases. For example, you can write test cases to determine whether your application can read and write images and videos in various formats, whether it can perform basic image processing operations such as resizing and cropping, and whether objects can be viewed accurately under different lighting conditions. You can check if it can be recognized by environment.

You can use pytest fixtures to set up your test environment and provide test data for your test cases. For example, you can use fixtures to load test images and videos, create synthetic test data, and initialize OpenCV objects and functions used in test cases.

Overall, using pytest to test the functionality of your OpenCV application helps ensure that your application is robust, reliable, and meets the required quality standards. 


## Authors

- [@MadhuPrakash270405](https://www.github.com/MadhuPrakash270405)
- Sai Rohith Avula
- Ajay Motharapu


## Installation


To install and run OpenCV with Python, you will need the following system requirements:

#### Operating System: 
    -   Windows, 
    -   Linux, 
    -   macOS, or Android.

#### Python: 
-   Python 3.x is recommended. OpenCV 4.x supports Python 3.5-3.8, while OpenCV 3.x supports Python 2.7 and 3.x.


#### Package Manager: 
-   pip is the most common package manager used for installing Python libraries, including OpenCV.

#### Dependencies: 
-   OpenCV has several dependencies, such as NumPy, Matplotlib, and SciPy. These dependencies can be installed using pip.

## To install OpenCV with Python, follow these steps:

-   Install Python if it is not already installed on your system.

-   Install pip if it is not already installed on your system.

-   Install the required dependencies using pip. 
####   To install NumPy, run the command:

```
pip install numpy
```
#### Install OpenCV using pip. For example, to install OpenCV 4.x, run the command:

```
pip install opencv-python-headless
```

The opencv-python-headless package is a minimal package that does not include the GUI components of OpenCV, which are not required for most computer vision applications.

Verify the installation by importing OpenCV in a Python script and running a simple OpenCV program to test its functionality.

That's it! Once you have installed OpenCV with Python, you can start using it for your computer vision projects.
## Run Locally

Clone the project

```bash
  git clone https://github.com/MadhuPrakash270405/OpenCV_testing.git
```

Go to the project directory

```bash
  cd OpenCV_testing
```

####  Install dependencies

Install Python on your computer, if it is not already installed. You can download the latest version of Python from the official Python website.

- Decide on a project directory and create a new folder to hold your project files.

- Open a command prompt or terminal window and navigate to the project directory.

- Create a new virtual environment using a tool like venv or conda. This is an optional step, but it is recommended to keep your project dependencies isolated from your system Python installation.

- Activate the virtual environment using the appropriate command for your environment. For example, in venv, you can run:

bash
```
source <venv>/bin/activate
```

- Install the project dependencies using a package manager like pip. You can create a requirements.txt file to list all the required packages and their versions. For example:

```
pip install -r requirements.txt
```

- When you are finished working on the project, deactivate the virtual environment using the appropriate command. For example:
```
deactivate
```


## Running Tests

To run tests, run the following command

-   Test the code by running 

```
pytest
```
- If you want to run the testing Individually You can do it by

```
pytest <filename>
```


