students = [
    {
        "id": 1,
        "name": "Arun Kumar",
        "course": "Python",
        "attendance": 82,
        "marks": 76
    },
    {
        "id": 2,
        "name": "Priya Sharma",
        "course": "Data Analytics",
        "attendance": 68,
        "marks": 81
    },
    {
        "id": 3,
        "name": "Rahul Raj",
        "course": "AI",
        "attendance": 91,
        "marks": 45
    },
    {
        "id": 4,
        "name": "Sneha Devi",
        "course": "Python",
        "attendance": 74,
        "marks": 62
    }
]


def get_all_students():
    return students


def get_student_by_id(student_id):
    for student in students:
        if student["id"] == student_id:
            return student

    return None


def calculate_student_status(student):
    if student["attendance"] >= 75 and student["marks"] >= 50:
        return "Eligible for Exam"

    return "Not Eligible"
