# Hospital Appointment Booking System

# Dictionary to simulate doctor schedules
# Key: doctor name, Value: list of booked dates
doctor_schedule = {
    "Dr. Smith": ["2025-10-05", "2025-10-06"],
    "Dr. Lee": ["2025-10-03"],
    "Dr. Adams": []
}

# Function to check availability
def is_doctor_available(doctor, date):
    # Check if the date is already booked
    return date not in doctor_schedule.get(doctor, [])

# Function to book appointment
def book_appointment(patient, doctor, date):
    doctor_schedule[doctor].append(date)
    print(f"Appointment booked for {patient} with {doctor} on {date}.")

# Main program
patient_name = input("Enter your name: ")
doctor_name = input("Enter doctor's name (Dr. Smith, Dr. Lee, Dr. Adams): ")
preferred_date = input("Enter preferred date (YYYY-MM-DD): ")

# Check and book
if is_doctor_available(doctor_name, preferred_date):
    book_appointment(patient_name, doctor_name, preferred_date)
else:
    print("Sorry, the doctor is not available on that date.")

