from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data
courses = [
    {'id': 1, 'name': 'Python for Beginners', 'description': 'Learn Python from scratch.'},
    {'id': 2, 'name': 'Web Development with Flask', 'description': 'Build web apps using Flask.'},
]

# Home route that lists all courses
@app.route('/')
def home():
    return render_template('index.html', courses=courses)

# View course details
@app.route('/course/<int:course_id>')
def course(course_id):
    course = next((course for course in courses if course['id'] == course_id), None)
    if course:
        return render_template('course.html', course=course)
    return redirect(url_for('home'))

# Add a new course
@app.route('/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        course_name = request.form['name']
        course_description = request.form['description']
        new_course = {
            'id': len(courses) + 1,
            'name': course_name,
            'description': course_description,
        }
        courses.append(new_course)
        return redirect(url_for('home'))
    return render_template('add_course.html')

# Enroll in a course (simple version)
@app.route('/enroll/<int:course_id>')
def enroll(course_id):
    course = next((course for course in courses if course['id'] == course_id), None)
    if course:
        # In a real application, we would save the enrollment in the database
        return f'You have been enrolled in the course: {course["name"]}'
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)