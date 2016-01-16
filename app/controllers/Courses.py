from flask import flash
from system.core.controller import *

class Courses(Controller):
    def __init__(self, action):
        super(Courses, self).__init__(action)
        self.load_model('Course')

    def index(self):
        courses = self.models['Course'].get_all_courses()
        return self.load_view('index.html', courses=courses)

    def process(self):
        error = False
        name = request.form.get('name')
        description = request.form.get('description')

        if len(name) < 1:
            error = True
            flash('ERROR: course name must have at least 15 characters')

        if error:
            return redirect('/')

        self.models['Course'].add_course(name, description)
        return redirect('/')

    def remove(self, id):
        course = self.models['Course'].get_course_by_id(id)
        print course
        return self.load_view('remove.html', course=course)

    def delete(self, id):
        self.models['Course'].delete_course(id)
        return redirect('/')
