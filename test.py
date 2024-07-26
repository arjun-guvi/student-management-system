import pytest
from app import User, Student, PerformanceReport, StudentPerformanceSystem 

def test_user_sign_up():
    system = StudentPerformanceSystem()
    user = system.sign_up("teacher", "password123")
    assert user.username == "teacher"
    assert user.check_password("password123")

def test_user_login():
    system = StudentPerformanceSystem()
    system.sign_up("teacher", "password123")
    user = system.login("teacher", "password123")
    assert user is not None
    assert user.username == "teacher"

def test_add_student():
    system = StudentPerformanceSystem()
    user = system.sign_up("teacher", "password123")
    student = system.add_student(user, 1, "John Doe")
    assert student.student_id == 1
    assert student.name == "John Doe"

def test_update_student():
    system = StudentPerformanceSystem()
    user = system.sign_up("teacher", "password123")
    system.add_student(user, 1, "John Doe")
    updated_student = system.update_student(user, 1, "John Smith")
    assert updated_student.name == "John Smith"

def test_delete_student():
    system = StudentPerformanceSystem()
    user = system.sign_up("teacher", "password123")
    student = system.add_student(user, 1, "John Doe")
    deleted_student = system.delete_student(user, 1)
    assert deleted_student.student_id == 1
    assert deleted_student.name == "John Doe"

def test_record_grade():
    system = StudentPerformanceSystem()
    user = system.sign_up("teacher", "password123")
    student = system.add_student(user, 2, "Jane Doe")
    student.add_grade("Math", 95)
    assert student.grades["Math"] == 95

def test_update_grade():
    system = StudentPerformanceSystem()
    user = system.sign_up("teacher", "password123")
    student = system.add_student(user, 2, "Jane Doe")
    student.add_grade("Math", 95)
    student.update_grade("Math", 98)
    assert student.grades["Math"] == 98

def test_delete_grade():
    system = StudentPerformanceSystem()
    user = system.sign_up("teacher", "password123")
    student = system.add_student(user, 2, "Jane Doe")
    student.add_grade("Math", 95)
    student.delete_grade("Math")
    assert "Math" not in student.grades

def test_average_grade():
    system = StudentPerformanceSystem()
    user = system.sign_up("teacher", "password123")
    student = system.add_student(user, 2, "Jane Doe")
    student.add_grade("Math", 95)
    student.add_grade("Science", 85)
    assert student.get_average_grade() == pytest.approx(90.0, 0.01)

def test_performance_report():
    system = StudentPerformanceSystem()
    user = system.sign_up("teacher", "password123")
    student = system.add_student(user, 2, "Jane Doe")
    student.add_grade("Math", 95)
    student.add_grade("Science", 85)
    report = PerformanceReport(student)
    generated_report = report.generate_report()
    expected_report = "Performance Report for Jane Doe:\nMath: 95\nScience: 85\nAverage Grade: 90.0"
    assert generated_report == expected_report

# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()
