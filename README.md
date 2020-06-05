# EasyCodingGUI
This is a python-based GUI interface, which is designed to provide easy coding for high school student.

# Setup
You need to install the following python packages first to run this GUI
1. `pyqt5`. Install it using `pip install PyQt5`.
2. `qscintilla??`
  

# GUI structure and How to use it
## 1. Initial Page - Course/Mode Selection
- Run the `main.py` file. Then the initial GUI will pop up.

- Choose the **course** and **mode**. Courses content can be modified in **CourseCode** files, and others can be modified in **ui** files. Modes includes multiple choice and fill in the blanks.


## 2. Second Page - Coding 
  ### 2.1 Layout:
  - For multiple choice：
  This page is composed of three elements: **unfinished codes** on the left, **options** on the right, **menu** on the top.

  - For fill in the blanks：
  This page is composed of three elements: **unfinished codes** on the left, **partial codes** on the right, **menu** on the top.
  
  ### 2.2 Elements:
  Unfinished Codes:
  This is **read** only. It will display the real time codes you are writing.
 
  Options/Partial Codes: 
  This is **modifiable**. You can choose your answer of fill in the blank of the sub code block.
  
  Menu:
  Menu has four buttons from left to right: **Import Answer**, **Export Codes**, **Export Answer**, and **Return to Initial Page**.
  
    - `Import Answer`: you can import the answer you export last time and continue to write your code.
  
    - `Export Codes`: you can export the codes you write to a py file.
  
    - `Export Answer`: you can export the answer only if you encounter some trouble and need to stop. Next time, you can import this answer by `Import Answer` and continue.
  
      `Return to Initial Page`: you will return to the initial page to reselect the course/mode, in the case that you choose the wrong one before.
