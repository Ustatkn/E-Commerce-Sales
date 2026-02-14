import analysis as asis
import visualization as vs

def main():
    print("-------Student Performance Analysis-------")

    df = asis.load_and_clean_data()
    
    while True:
        print("1- Dataset Summary Dashboard")
        print("2- Pass / Conditional Pass / Fail Counts & Rates")
        print("3- Letter Grade Distribution")
        print("4- Top 10 Students (by Average Grade)")
        print("5- Students Who Didn't Take Final (List / Count)")
        print("6- Gender-based Performance")
        print("7- Parental Support vs Performance")
        print("8- Online Classes Taken vs Performance")
        print("9- Study Hours vs Performance (Grouped Insights)")
        print("10- Attendance vs Performance (Grouped Insights)")
        print("11- Risk List: High Study Hours but Low Grades")
        print("12- Hidden Potential: Low Study Hours but High Grades")
        print("13- Conditional Pass Focus")
        print("14- Histogram: AverageGrade Distribution")
        print("15- Bar: Letter Grade Counts")
        print("16- Scatter: Study Hours vs AverageGrade")
        print("17- Scatter: Attendance vs AverageGrade")
        print("0- Exit\n")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                print(asis.dataset_summary(df))
            elif choice == 2:
                print(asis.pass_conditional_fail_counts_rates(df))
            elif choice == 3:
                print(asis.letter_grade_distribution(df))
            elif choice == 4:
                print(asis.top_ten_students(df))
            elif choice == 5:
                print(asis.not_take_final(df))
            elif choice == 6:
                print(asis.gender_based_performance(df))
            elif choice == 7:
                print(asis.parental_sup_performance(df))
            elif choice == 8:
                print(asis.online_classes_taken(df))
            elif choice == 9:
                print(asis.study_hours_vs_performance(df))
            elif choice == 10:
                print(asis.attendance_vs_performance(df))
            elif choice == 11:
                print(asis.risk_list(df))
            elif choice == 12:
                print(asis.hidden_potential(df))
            elif choice == 13:
                print(asis.conditional_passed(df))
            elif choice == 14:
                vs.average_grade_distribution_hist(df)
            elif choice == 15:
                vs.letter_grade_counts_bar(df)
            elif choice == 16:
                vs.study_hours_performance_scatter(df)
            elif choice == 17:
                vs.attendance_performance_scatter(df)
            elif choice == 0:
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid choice!")
        input("\nPress Enter to continue...")

    return

if __name__ == "__main__":
    main()