from system.core.model import Model
class Courses(Model):
    def __init__(self):
        super(Courses, self).__init__()

    def get_all_courses(self):
        return self.db.query_db("SELECT * FROM courses")

    def get_course_by_id(self, course_id):
        return self.db.query_db("SELECT * FROM courses WHERE id = {}").format(course_id)

    def delete_course(self, course_id):
        return self.db.query_db("DELETE FROM courses WHERE id = {}").format(course_id)
