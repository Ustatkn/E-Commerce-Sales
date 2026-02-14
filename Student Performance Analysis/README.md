**Student Performance Analysis System (Pandas / NumPy / Matplotlib)**

This project analyzes a student performance dataset using Pandas, NumPy, and Matplotlib.
It is designed as a menu-driven console application that provides both statistical insights and visual analysis of student academic performance.

**Dataset Overview**
The dataset includes student-level academic and behavioral features such as:

StudentID
Name
Gender
Study Hours
Attendance (%)
MidtermGrade
FinalGrade
Online Classes Taken
ParentalSupport
ExtracurricularActivities

---

**Data Cleaning & Preprocessing**
The following data cleaning decisions were applied:

- Removed Records

Students with missing StudentID
Students with missing Name
These records were removed because the students are not identifiable.

- Gender
Missing values were filled with "Unknown".

- Study Hours
Negative study hours were removed from the dataset.
Missing values were left as NaN (Pandas automatically excludes them in mean calculations).

- Midterm & Final Handling:
Missing MidtermGrade values were filled with 0.
(Students who did not take the midterm were assumed to receive 0.)

- A new column **TookFinal** was created:

True → Student attended the final exam
False → Student did not attend

- Students who did not take the final exam:
FinalGrade set to 0
Automatically marked as Failed
LetterGrade assigned as FF

- Other Missing Values:
Missing values in Online Classes Taken were treated as False.
Missing values in ExtracurricularActivities were filled with 0.
Missing values in ParentalSupport were filled with "Unknown".

- Grade Calculation
Final average grade was calculated as:

AverageGrade = (MidtermGrade * 0.4) + (FinalGrade * 0.6)

**Grading System**
Score Range	Letter Grade
90 – 100	AA
85 – 89	BA
80 – 84	BB
70 – 79	CB
65 – 69	CC
60 – 64	DC
50 – 59	DD
< 50	FF

**Pass Classification**

Three performance categories were defined:

Passed → CC and above
ConditionalPass → DD and DC
Failed → FF or did not attend final

Separate boolean columns were created:

Passed
ConditionalPass
TookFinal

This structure allows flexible statistical analysis.

---

**Menu Features**

The system includes 17 analysis and visualization options:

**Analytical Features**

Dataset summary dashboard
Pass / Conditional Pass / Fail rates
Letter grade distribution
Top 10 students by average grade
Students who did not take final
Gender-based performance
Parental support vs performance
Online classes vs performance
Study hours vs performance (segmented analysis)
Attendance vs performance (segmented analysis)
Risk list (high study hours but failed)
Hidden potential (low study hours but passed)
Conditional pass analysis

**Visualizations**

Histogram: Average Grade distribution
Bar chart: Letter Grade counts
Scatter plot: Study Hours vs Average Grade (with regression line)
Scatter plot: Attendance vs Average Grade (with regression line)

---

**Key Analytical Insights**
The project explores relationships such as:

Does higher study time increase performance?
Does attendance correlate with higher grades?
Are online classes associated with better outcomes?
What characteristics define conditional pass students?
Are there students who work hard but still fail?
Are there students who succeed with minimal study?

---

**Installation**
pip install -r requirements.txt

**Running the Project**
python main.py

Follow the on-screen menu to explore different analysis options.

---

**Technologies Used**

Python
Pandas
NumPy
Matplotlib

**Purpose of the Project**
This project demonstrates:

Data cleaning and preprocessing
Feature engineering
Boolean logic-based classification
Segmented analysis
Correlation and regression visualization
Modular Python project structure
Console-based analytical systems

