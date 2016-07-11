#!/usr/bin/env python
# encoding: utf-8

import yaml
import os
import edx_lms_rest
import uuid
# 当前项目同一目录下，__file__ ,只有文件运行时才可以
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(BASE_DIR, 'local_lms.yaml'),'r') as f:
    config = yaml.load(f)

class CourseTest():
    def __init__(self,org="test_org",number="121224",run="test_run"):
    #def __init__(self,org="test_org",number="test_number",run="test_run"):

        self.org = org
        #self.number = str(uuid.uuid4().get_hex().upper()[0:6])
        self.number = number
        self.run = run
        self.connection = edx_lms_rest.EdXConnection(server=config["server"] ,
                                       session=config['sessionid'],
                                       csrf=config['csrftoken'])
        self.course = edx_lms_rest.EdXCourse(self.org, self.number, self.run)
        print self.course.course_string
    def test_add_student(self):
        student_email = "wwj,lyx1"
        self.connection.students_update_enrollment(self.course,student_email)



if __name__ == '__main__':
    pass
