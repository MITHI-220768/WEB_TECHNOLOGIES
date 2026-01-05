class Student:
    """Class to manage student data and calculate grades"""
    
    def __init__(self, student_id, name, marks):
        """
        Initialize student with ID, name, and marks
        
        Args:
            student_id: Unique student identifier
            name: Student's name
            marks: Total marks obtained
        """
        self.student_id = student_id
        self.name = name
        self.marks = marks
        self.percentage = 0
        self.grade = None
    
    def calculate_percentage(self, total_marks=100):
        """
        Calculate percentage based on marks obtained
        
        Args:
            total_marks: Total marks (default: 100)
        
        Returns:
            float: Calculated percentage
        """
        if total_marks <= 0:
            raise ValueError("Total marks must be greater than 0")
        
        self.percentage = (self.marks / total_marks) * 100
        return self.percentage
    
    def assign_grade(self):
        """
        Assign grade based on percentage
        
        Returns:
            str: Grade (A, B, C, or D)
        """
        if self.percentage >= 90:
            self.grade = 'A'
        elif self.percentage >= 80:
            self.grade = 'B'
        elif self.percentage >= 70:
            self.grade = 'C'
        else:
            self.grade = 'D'
        
        return self.grade
    
    def display_info(self):
        """Display student information including percentage and grade"""
        print("\n" + "="*50)
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        print(f"Percentage: {self.percentage:.2f}%")
        print(f"Grade: {self.grade}")
        print("="*50 + "\n")


def main():
    """Main function to run the student management program"""
    
    print("Student Grade Management System")
    print("-" * 50)
    
    # Take input from user
    try:
        student_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        marks = float(input("Enter Marks Obtained: "))
        total_marks = float(input("Enter Total Marks (default 100): ") or "100")
        
        # Create student object
        student = Student(student_id, name, marks)
        
        # Calculate percentage and assign grade
        student.calculate_percentage(total_marks)
        student.assign_grade()
        
        # Display student information
        student.display_info()
        
    except ValueError as e:
        print(f"Error: {e}")
        print("Please enter valid numeric values for marks.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
