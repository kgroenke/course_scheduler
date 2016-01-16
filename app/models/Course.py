from system.core.model import Model
class Course(Model):
    def __init__(self):
        super(Course, self).__init__()

    def get_all_courses(self):
        return self.db.query_db("SELECT * FROM courses")

    def get_course_by_id(self, id):
        query = "SELECT * FROM courses WHERE id = '{}'".format(id)
        return self.db.query_db(query)

    def add_course(self, name, description):
        
        query = "INSERT INTO courses (name, description, created_at, updated_at) VALUES('{}', '{}', NOW(), NOW())".format(name, description)
        return self.db.query_db(query)

    def delete_course(self, id):
        query= "DELETE FROM courses WHERE id = {}".format(id)
        return self.db.query_db(query)
