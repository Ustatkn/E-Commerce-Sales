import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def average_grade_distribution_hist(df):
    df['AverageGrade'].plot(kind='hist',bins=20,title='Average Grade Distribution',xlabel='Average Grade',)
    plt.tight_layout()
    plt.savefig("outputs/plots/average_grade_distribution_hist.png")
    plt.show()

def letter_grade_counts_bar(df):
    df['LetterGrade'].value_counts().sort_index().plot(kind='bar',title='Letter Grade Counts',xlabel='Letter Grades',ylabel='Number of Students')
    plt.tight_layout()
    plt.savefig("outputs/plots/letter_grade_counts_bar.png")
    plt.show()

def study_hours_performance_scatter(df):
    df.plot(kind='scatter',x='Study Hours',y='AverageGrade',title='Relationship between Study Hours and Performance')
    z = np.polyfit(df['Study Hours'],df['AverageGrade'],1)
    p = np.poly1d(z)
    x_sorted = np.sort(df['Study Hours'])

    plt.plot(x_sorted,p(x_sorted),color = 'red')
    plt.xlabel('Study Hours')
    plt.ylabel('Average Grade')
    plt.tight_layout()
    plt.savefig("outputs/plots/study_hours_performance_scatter.png")
    plt.show()

def attendance_performance_scatter(df):

    df = df.dropna(subset=['Attendance (%)'])
    df.plot(kind='scatter',x='Attendance (%)',y='AverageGrade',title='Relationship between Attendance and Performance')
    z = np.polyfit(df['Attendance (%)'],df['AverageGrade'],1)
    p = np.poly1d(z)
    x_sorted = np.sort(df['Attendance (%)'])

    plt.plot(x_sorted,p(x_sorted),color = 'red')
    plt.xlabel('Attendance')
    plt.ylabel('Average Grade')
    plt.tight_layout()
    plt.savefig("outputs/plots/attendance_performance_scatter.png")
    plt.show()