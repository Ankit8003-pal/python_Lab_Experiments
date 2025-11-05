# Student Attendance Tracker

import datetime

# List to store attendance records
attendance_records = []

def validate_timestamp(timestamp_str):
    """Validate timestamp in HH:MM format."""
    try:
        datetime.datetime.strptime(timestamp_str, "%H:%M")
        return True
    except ValueError:
        return False

def input_attendance():
    """Input daily names and automatically pick current timestamp."""
    while True:
        try:
            name = input("Enter student name (or 'quit' to stop): ").strip()
        except EOFError:
            break
        if name.lower() == 'quit':
            break
        if not name:
            print("Name cannot be empty. Please try again.")
            continue
        # Automatically pick current time
        now = datetime.datetime.now()
        timestamp = now.strftime("%H:%M")
        # Store in dictionary
        record = {'name': name, 'timestamp': timestamp}
        attendance_records.append(record)
        print(f"Added: {name} at {timestamp}")

def generate_summary():
    """Generate formatted attendance summaries."""
    if not attendance_records:
        print("No attendance records.")
        return
    print("\nAttendance Summary:")
    print("-" * 30)
    for record in attendance_records:
        print(f"Name: {record['name']}, Time: {record['timestamp']}")
    print("-" * 30)

# Main execution
if __name__ == "__main__":
    print("Welcome to Student Attendance Tracker")
    input_attendance()
    generate_summary()
