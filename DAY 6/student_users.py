total_users = int(input("Total Users: "))
staff_users = int(input("Staff Users: "))
non_teaching_staff = staff_users // 3
student_users = total_users - staff_users - non_teaching_staff
print("Student Users:", student_users)
