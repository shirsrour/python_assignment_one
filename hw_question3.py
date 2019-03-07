def compare_subjects_within_student(subj1_all_students,subj2_all_students):
    for key in subj1_all_students["grades"]:
        subj1_first_grade = subj1_all_students["grades"][key]["first"]
        subj1_second_grade = subj1_all_students["grades"][key]["second"]
        subj1_higher_grade = max(subj1_first_grade,subj1_second_grade)

        if key in subj2_all_students["grades"]:
            subj2_first_grade = subj2_all_students["grades"][key]["first"]
            subj2_second_grade = subj2_all_students["grades"][key]["second"]
            subj2_higher_grade = max(subj2_first_grade,subj2_second_grade)

            if subj1_higher_grade > subj2_higher_grade:
                print("Student: " + key + " has a higher grade in: " + subj1_all_students["name"])
            else:
                print("Student: " + key + " has a higher grade in: " + subj2_all_students["name"])




if __name__ == '__main__':
    # Question 3
    subj1_all_students = {
        "name": "History",
        "grades": {
            "Zahi": {
                "first" : 80,
                "second": 85
            },
            "Sami": {
                "first" : 65,
                "second": 90
            },
            "Rani": {
                "first" : 100,
                "second": 90
            },
            "Dani": {
                "first" : 20,
                "second": 30
            }
        }
    }
    subj2_all_students = {
        "name": "Math",
        "grades": {
            "Zahi": {
                "first" : 75,
                "second": 65
            },
            "Sami": {
                "first" : 100,
                "second": 70
            },
            "Fani": {
                "first" : 80,
                "second": 90
            },
            "Jessica": {
                "first" : 85,
                "second": 95
            }
        }
    }

    print("Running Question 3:")
    compare_subjects_within_student(subj1_all_students,subj2_all_students)