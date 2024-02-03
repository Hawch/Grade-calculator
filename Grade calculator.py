def calculate_grade(score, max_score):
    if score > max_score:
        print("Error: Score cannot be greater than maximum score.")
        return None
    percentage = (score / max_score) * 100
    grade = ""
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade, percentage

def get_score_and_max_score(i):
    while True:
        score = float(input(f"Enter the score for assignment/exam {i+1}: "))
        max_score = float(input(f"Enter the maximum score for assignment/exam {i+1}: "))
        if score > max_score:
            print("Error: Score cannot be greater than maximum score.")
        else:
            return score, max_score

def main():
    num_assignments = int(input("Enter the number of assignments/exams: "))
    total_score = 0
    total_max_score = 0

    for i in range(num_assignments):
        score, max_score = get_score_and_max_score(i)
        total_score += score
        total_max_score += max_score

    overall_grade, overall_percentage = calculate_grade(total_score, total_max_score)
    if overall_grade is not None:
        print(f"Your overall grade is: {overall_grade}")
        print(f"Your overall percentage is: {overall_percentage:.2f}%")

if __name__ == "__main__":
    main()