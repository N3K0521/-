'''
DO NOT CHANGE THE NAME OF THIS FILE, or else the tester will not work. 
The first function requires that you replace the given strings with
your personal details. It is important that you enter your student number
and your student email correctly. If your number and email do not match we
will then check your name, so your name acts as a failsafe.
'''

# Student details
def details():
    student_number = '' #write your student number as a string
    student_email = '' + '@student.monash.edu' #write your student email
    name = '' #write your name as it appears on Moodle
    return str(student_number), student_email, name
