import pandas as pd
import numpy as np
import io

def load_and_clean_data():
    df = pd.read_csv('data/students_data.csv')

    # we deleted students from data set who has no StudentID and Nome, because these students are not identifiable and we can't use them in our analysis.
    df = df.dropna(subset=["StudentID"])
    df = df.dropna(subset=["Name"])

    # we filled empty gender sections with 'Unknown'.
    df['Gender'] = df['Gender'].fillna('Unknown')

    # we filled empty extracurricular activities sections with 0.
    df['ExtracurricularActivities'] = df['ExtracurricularActivities'].fillna(0.0)

    # we filled empty parental support sections with 'Unknown'.
    df['ParentalSupport'] = df['ParentalSupport'].fillna('Unknown')

    # we filled empty online classes taken sections with False.
    df['Online Classes Taken'] = df['Online Classes Taken'].fillna(False).astype(bool)

    # we converted these columns to appropriate data types for analysis.
    df['StudentID'] = df['StudentID'].astype(int)
    df['MidtermGrade'] = df['MidtermGrade'].astype(float)
    df['FinalGrade'] = df['FinalGrade'].astype(float)
    df['Study Hours'] = df['Study Hours'].astype(float)

    # we deleted negatif study hours from data set
    df = df[df['Study Hours'] >= 0]

    # we filled missing midterm grades with 0, because students who didn't take midterm exam will get 0 grade for midterm exam
    df['MidtermGrade'] = df['MidtermGrade'].fillna(0)

    df['Passed'] = False
    df['LetterGrade'] = 'FF'
    df['ConditionalPass'] = False

    # we filtered students who took the final exam and who didn't take the final exam
    df['TookFinal'] = False
    df.loc[df['FinalGrade'].isnull()==False,'TookFinal'] = True
    df.loc[df['TookFinal']==False,['FinalGrade','Passed','LetterGrade']] = [0,False,'FF']

    # we calculated average grades of students.
    df['AverageGrade'] = (df['MidtermGrade']*4 + df['FinalGrade']*6)/10

    # we assigned letter grades and pass/conditional pass/fail status based on the average grade for students who took the final exam.
    df.loc[(df['TookFinal']==True) & (df['AverageGrade']<50),['Passed','LetterGrade']]=[False,'FF']
    df.loc[(df['AverageGrade']>=50) & (df['AverageGrade']<60) & (df['TookFinal']==True),['ConditionalPass','LetterGrade']]=[True,'DD']
    df.loc[(df['AverageGrade']>=60) & (df['AverageGrade']<65) & (df['TookFinal']==True),['ConditionalPass','LetterGrade']]=[True,'DC']
    df.loc[(df['TookFinal']==True) & (df['AverageGrade']>=65),['Passed','LetterGrade']]=[True,'CC']
    df.loc[(df['TookFinal']==True) & (df['AverageGrade']>=70),['Passed','LetterGrade']]=[True,'CB']
    df.loc[(df['TookFinal']==True) & (df['AverageGrade']>=80),['Passed','LetterGrade']]=[True,'BB']
    df.loc[(df['TookFinal']==True) & (df['AverageGrade']>=85),['Passed','LetterGrade']]=[True,'BA']
    df.loc[(df['TookFinal']==True) & (df['AverageGrade']>=90),['Passed','LetterGrade']]=[True,'AA']

    return df

def dataset_summary(df):
    data_describe = df.describe(include='all').to_string()
    buffer = io.StringIO()
    df.info(buf=buffer)                 # df.info() method is not returnable so we used this method to capture the output of df.info() into a string buffer and then we can get the string value from the buffer.
    data_info = buffer.getvalue()

    return f"Dataset Summary:\n{data_describe}\nDataset Info:\n{data_info}\n"

def pass_conditional_fail_counts_rates(df):
    total_students = len(df)
    passed_students = (df['Passed']==True).sum()
    cond_passed_students = (df['ConditionalPass']==True).sum()
    failed_students = ((df['Passed']==False) & (df['ConditionalPass']==False)).sum()

    passed_rate = (passed_students/total_students)*100
    cond_passed_rate = (cond_passed_students/total_students)*100
    failed_rate = (failed_students/total_students)*100

    return (f"Total {total_students} students\n\n"
            f"Passed Students: {passed_students} - {passed_rate:.2f}%\n"
            f"Conditional Passed Students: {cond_passed_students} - {cond_passed_rate:.2f}%\n"
            f"Failed Students: {failed_students} - {failed_rate:.2f}%\n"
            )

def letter_grade_distribution(df):
    total_grades = len(df)
    aa_total = (df['LetterGrade']=='AA').sum()
    ba_total = (df['LetterGrade']=='BA').sum()
    bb_total = (df['LetterGrade']=='BB').sum()
    cb_total = (df['LetterGrade']=='CB').sum()
    cc_total = (df['LetterGrade']=='CC').sum()
    dc_total = (df['LetterGrade']=='DC').sum()
    dd_total = (df['LetterGrade']=='DD').sum()
    ff_total = (df['LetterGrade']=='FF').sum()

    aa_ratio = (aa_total/total_grades)*100
    ba_ratio = (ba_total/total_grades)*100
    bb_ratio = (bb_total/total_grades)*100
    cb_ratio = (cb_total/total_grades)*100
    cc_ratio = (cc_total/total_grades)*100
    dc_ratio = (dc_total/total_grades)*100
    dd_ratio = (dd_total/total_grades)*100
    ff_ratio = (ff_total/total_grades)*100

    return (
        f"Total AA ratio: {aa_ratio:.2f}%\n"
        f"Total BA ratio: {ba_ratio:.2f}%\n"
        f"Total BB ratio: {bb_ratio:.2f}%\n"
        f"Total CB ratio: {cb_ratio:.2f}%\n"
        f"Total CC ratio: {cc_ratio:.2f}%\n"
        f"Total DC ratio: {dc_ratio:.2f}%\n"
        f"Total DD ratio: {dd_ratio:.2f}%\n"
        f"Total FF ratio: {ff_ratio:.2f}%\n"
    )

def top_ten_students(df):
    df_sorted = df.sort_values(by='AverageGrade',ascending=False).head(10)
    return f"Top 10 Studens (by Average Grade)\n\n{df_sorted[['StudentID','Name','MidtermGrade','FinalGrade']]}\n"

def not_take_final(df):
    students_not_take_final = df.loc[df['TookFinal']==False,['StudentID','Name','MidtermGrade','AverageGrade']]
    return f"{students_not_take_final}\n"

def gender_based_performance(df):
    total_male_students = (df['Gender']=='Male').sum()
    total_female_students = (df['Gender']=='Female').sum()
    total_unknown_students = (df['Gender']=='Unknown').sum()

    male_students_performance = df.loc[df['Gender']=='Male','AverageGrade'].mean()
    female_students_performance = df.loc[df['Gender']=='Female','AverageGrade'].mean()
    unknown_students_performance = df.loc[df['Gender']=='Unknown','AverageGrade'].mean()

    return (f"There are {total_male_students} male students in the data and their average grade: {male_students_performance:.2f}\n"
            f"There are {total_female_students} female students in the data and their average grade: {female_students_performance:.2f}\n"
            f"There are {total_unknown_students} unknown gender students in the data and their average grade: {unknown_students_performance:.2f}\n")

def parental_sup_performance(df):
    low_parental_sup = (df['ParentalSupport']=='Low').sum()
    medium_parental_sup = (df['ParentalSupport']=='Medium').sum()
    high_parental_sup = (df['ParentalSupport']=='High').sum()
    unknown_parental_sup = (df['ParentalSupport']=='Unknown').sum()

    perf_low = df.loc[df['ParentalSupport']=='Low','AverageGrade'].mean()
    perf_medium = df.loc[df['ParentalSupport']=='Medium','AverageGrade'].mean()
    perf_high = df.loc[df['ParentalSupport']=='High','AverageGrade'].mean()
    perf_unknown = df.loc[df['ParentalSupport']=='Unknown','AverageGrade'].mean()

    return (f"Parental Support Summary:\n"
            f"Total High Parental Supported: {high_parental_sup} and Mean Average Grade: {perf_high:.2f}\n"
            f"Total Medium Parental Supported: {medium_parental_sup} and Mean Average Grade: {perf_medium:.2f}\n"
            f"Total Low Parental Supported: {low_parental_sup} and Mean Average Grade: {perf_low:.2f}\n"
            f"Total Unknown Parental Supported: {unknown_parental_sup} and Mean Average Grade: {perf_unknown:.2f}\n")

def online_classes_taken(df):
    total_online_class_take = (df['Online Classes Taken']==True).sum()
    total_online_class_nontake = (df['Online Classes Taken']==False).sum()

    perf_take = df.loc[df['Online Classes Taken']==True,'AverageGrade'].mean()
    perf_nontake = df.loc[df['Online Classes Taken']==False,'AverageGrade'].mean()

    return (f"There are {total_online_class_take} students who took online classes and their performance: {perf_take:.2f}\n"
            f"There are {total_online_class_nontake} students who did not take online classes and their performance: {perf_nontake:.2f}\n")

def study_hours_vs_performance(df):
    total_low = len(df[df['Study Hours']<=2])
    total_moderate = len(df[(df['Study Hours']>2) & (df['Study Hours']<=3)])
    total_high = len(df[(df['Study Hours']>3) & (df['Study Hours']<=4)])
    total_very_high = len(df[df['Study Hours']>4])

    low_effort = df.loc[df['Study Hours']<=2,'AverageGrade'].mean()
    moderate_effort = df.loc[(df['Study Hours']>2) & (df['Study Hours']<=3),'AverageGrade'].mean()
    high_effort = df.loc[(df['Study Hours']>3) & (df['Study Hours']<=4),'AverageGrade'].mean()
    very_high_effort = df.loc[df['Study Hours']>4,'AverageGrade'].mean()

    passed_low = df.loc[df['Study Hours']<=2,'Passed'].mean()*100
    passed_moderate = df.loc[(df['Study Hours']>2) & (df['Study Hours']<=3),'Passed'].mean()*100
    passed_high = df.loc[(df['Study Hours']>3) & (df['Study Hours']<=4),'Passed'].mean()*100
    passed_very_high = df.loc[df['Study Hours']>4,'Passed'].mean()*100

    return (f"Study Hours vs Performance - (0-2 Low Effort, 2-3 Moderate Effort, 3-4 High Effort, 4- Very High Effort --> Passed Rate CC+)\n"
            f"Number of students in this low hours group: {total_low} - Average Grade for this group: {low_effort:.2f} - Passed Rate: {passed_low:.2f}%\n"
            f"Number of students in this moderate hours group: {total_moderate} - Average Grade for this group: {moderate_effort:.2f} - Passed Rate: {passed_moderate:.2f}%\n"
            f"Number of students in this high hours group: {total_high} - Average Grade for this group: {high_effort:.2f} - Passed Rate: {passed_high:.2f}%\n"
            f"Number of students in this very high hours group: {total_very_high} - Average Grade for this group: {very_high_effort:.2f} - Passed Rate: {passed_very_high:.2f}%\n")

def attendance_vs_performance(df):
    total_low_attendance = len(df[df['Attendance (%)']<60])
    total_medium_attendance = len(df[(df['Attendance (%)']>=60) & (df['Attendance (%)']<75)])
    total_high_attendance = len(df[(df['Attendance (%)']>=75) & (df['Attendance (%)']<90)])
    total_very_high_attendance = len(df[df['Attendance (%)']>=90])

    low_attendance = df.loc[df['Attendance (%)']<60,'AverageGrade'].mean()
    medium_attendance = df.loc[(df['Attendance (%)']>=60) & (df['Attendance (%)']<75),'AverageGrade'].mean()
    high_attendance = df.loc[(df['Attendance (%)']>=75) & (df['Attendance (%)']<90),'AverageGrade'].mean()
    very_high_attendance = df.loc[df['Attendance (%)']>=90,'AverageGrade'].mean()

    passed_low = df.loc[df['Attendance (%)']<60,'Passed'].mean()*100
    passed_medium = df.loc[(df['Attendance (%)']>=60) & (df['Attendance (%)']<75),'Passed'].mean()*100
    passed_high = df.loc[(df['Attendance (%)']>=75) & (df['Attendance (%)']<90),'Passed'].mean()*100
    passed_very_high = df.loc[df['Attendance (%)']>=90,'Passed'].mean()*100

    return (f"Attendance vs Performance - (-60 Low Attendance, 60-75 Medium Attendance, 75-90 High Attendance, 90- Very High Attendance --> Passed Rate CC+)\n"
            f"Number of students in this low attendance group: {total_low_attendance} - Average Grade for this group: {low_attendance:.2f} - Passed Rate: {passed_low:.2f}%\n"
            f"Number of students in this medium attendance group: {total_medium_attendance} - Average Grade for this group: {medium_attendance:.2f} - Passed Rate: {passed_medium:.2f}%\n"
            f"Number of students in this high attendance group: {total_high_attendance} - Average Grade for this group: {high_attendance:.2f} - Passed Rate: {passed_high:.2f}%\n"
            f"Number of students in this very high attendance group: {total_very_high_attendance} - Average Grade for this group: {very_high_attendance:.2f} - Passed Rate: {passed_very_high:.2f}%\n")

def risk_list(df):
    total_high_study_hours = len(df[df['Study Hours']>=4])
    high_hour_low_grade = len(df[(df['Study Hours']>=4) & (df['Passed']==False)])
    total_rate = (high_hour_low_grade/total_high_study_hours)*100

    return f"There are {total_high_study_hours} students who study for high hours. However, {total_rate:.2f}% students did not pass the examination!\n"

def hidden_potential(df):
    total_low_study_hours = len(df[df['Study Hours']<=0.5])
    low_hour_high_grade = len(df[(df['Study Hours']<=0.5) & (df['Passed']==True)])
    total_rate = (low_hour_high_grade/total_low_study_hours)*100

    return f"There are {total_low_study_hours} students who study for low hours. Although they study for low hours, {total_rate:.2f}% students pass the examination!\n"

def conditional_passed(df):
    total_cond_passed = len(df[df['ConditionalPass']==True])
    avrg_study_hours = df.loc[df['ConditionalPass']==True,'Study Hours'].mean()
    avrg_attendance = df.loc[df['ConditionalPass']==True,'Attendance (%)'].mean()

    return (f"There are total {total_cond_passed} students who conditionally passed the examination.\n"
            f"Their average study hours: {avrg_study_hours:.2f}\n"
            f"Their average attendane to classes: {avrg_attendance:.2f}\n")

