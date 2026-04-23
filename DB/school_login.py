import sqlite3

# imported to work with the database

# -------------------------------------------
# this is the main function that does everything
# login, fetching results, everything is here
# -------------------------------------------
def login_and_get_credits():

    # first take username and birthday from user
    # birthday is used as the password in our system
    print("====== Student Portal ======")
    username = input("INSERT THE USERNAME ")
    password = input("INSERT THE PASSWORD (BIRTHDAY): ")

    # open the database
    # schools.db is the file where all student data is stored
    conn = sqlite3.connect('schools.db')
    cursor = conn.cursor()

    # now check if this user actually exists
    # ? is used to prevent SQL injection (safe way to pass values)
    login_query = """
        SELECT id, name FROM Students 
        WHERE name = ? AND birthday = ?
    """
    cursor.execute(login_query, (username, password))
    user = cursor.fetchone()
    # if user is found, data will be in 'user'
    # if not, it will return None

    # if login is successful
    if user:

        # user[0] means the first value → id
        # user[1] means the second value → name
        student_id = user[0]
        student_name = user[1]

        print(f"\n YOU ARE LOGGED IN, WELCOME {student_name}")

        # now find all courses of this student
        # three tables are connected:
        # Students → creditst → Course
        # LEFT JOIN is used so it doesn't break if no courses exist
        credits_query = """
            SELECT Course.name, creditst.credits, creditst.grade, creditst.date
            FROM Students
            LEFT JOIN creditst ON creditst.id_student = Students.id
            LEFT JOIN Course ON creditst.id_course = Course.id
            WHERE Students.id = ?
        """
        cursor.execute(credits_query, (student_id,))
        rows = cursor.fetchall()
        # fetchall means get all rows as a list

        # now print results if any exist
        if rows and rows[0][0] is not None:
            # rows[0][0] is checked to ensure course name exists
            # and it's not just an empty row
            print("\nYOUR COURSES ARE:")
            print("---------------------------")

            for row in rows:
                # each row contains 4 values:
                # course name, credits, grade, and date
                course_name, credits, grade, date = row
                print(f"course: {course_name} | grade: {grade} | credits: {credits} | date: {date}")

            print("---------------------------")

        else:
            # means the student has not enrolled in any courses yet
            print("\nNO COURSES TILL NOW ")

    else:
        # means username or birthday was incorrect
        print("\nLOGIN FAILED, PLEASE CHECK YOUR NAME OR BIRTHDAY")

    # close the database connection
    # this is important to avoid leaving it open
    conn.close()


# program starts from here
# directly calling the function
login_and_get_credits()