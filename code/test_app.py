import pytest
from flask import url_for , redirect, render_template, request
from flask_testing import TestCase
from flask_sqlalchemy import SQLAlchemy 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

# import the app's classes and objects
from app import app, project, task, jointable,projadd, taskadd,db, project_complete

# Create the base class
class TestBase(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        # Create test Entries
        sample1 = project(name="flowerpot")
        sample2 = task(name="level print bed")

        # save users to database
        db.session.add(sample2)
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

# Create the base class
class TestBase2(TestCase):
    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

        # Create test Entries
        sample1 = project(name="flowerpot", staatus = True)
        sample2 = task(name="level print bed", complete = True)

        # save users to database
        db.session.add(sample2)
        db.session.add(sample1)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()



# Write a test class for testing that the index / about page loads.
class TestViews(TestBase):

    def test_index_get(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'CRUD', response.data)

# Test adding 
class projAdd(TestBase):
    def test_add_project(self):
        response = self.client.post(
            url_for('add_project'),
            data = dict(name="penholder"),
            follow_redirects=True
        )
        self.assertIn(b'penholder',response.data)

class taskAdd(TestBase):
    def test_add_task(self):
        response = self.client.post(
            url_for('add_task', projid = 1),
            data = dict(name="bakepla"),
            follow_redirects=True
        )
        
        self.assertIn(b'bakepla', response.data)

class currentproj(TestBase):
    def test_current_projects_get(self):
        response = self.client.get(url_for('current_projects'))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'flowerpot', response.data)
         
class currenttask(TestBase):
    def test_current_tasks_get(self):
        response = self.client.get(url_for('current_tasks'))
        self.assertEqual(response.status_code,200)
        self.assertIn(b'level print bed', response.data)

class  projup(TestBase):
    def test_up_project(self):
        response = self.client.post(
            url_for('up_project', projid = 1),
            data = dict(name="smashedpot"),
            follow_redirects=True
        )
        
        self.assertIn(b'smashedpot', response.data)   
        self.assertNotIn(b'flowerpot', response.data)   

class  projcomp(TestBase):
    def test_complete_project(self):
        response = self.client.post(
            url_for('project_complete', projid = 1),
            follow_redirects=True)
        self.assertEqual(response.status_code,200) 
        self.assertNotIn(b'Unfinished', response.data)  

class  projincomp(TestBase2):
    def test_complete_project(self):
        response = self.client.post(
            url_for('project_incomplete', projid = 1),
            follow_redirects=True)
        self.assertEqual(response.status_code,200)   
        self.assertIn(b"Unfinished", response.data)

class  taskcomp(TestBase):
    def test_complete_task(self):
        response = self.client.post(
            url_for('task_complete', taskid = 1),
            follow_redirects=True)
        self.assertEqual(response.status_code,200)  
        self.assertNotIn(b'Unfinished', response.data) 

class  taskincomp(TestBase2):
    def test_complete_task(self):
        response = self.client.post(
            url_for('task_incomplete', taskid = 1),
            follow_redirects=True)
        self.assertEqual(response.status_code,200) 
        self.assertIn(b'Unfinished', response.data)

class  delproj(TestBase):
    def test_del_project(self):
        response = self.client.post(
            url_for('deletep', projid = 1),
            follow_redirects=True
        )
         
        self.assertNotIn(b'flowerpot', response.data)  

class  deltest(TestBase):
    def test_del_task(self):
        response = self.client.post(
            url_for('deletet', taskid = 1),
            follow_redirects=True
        )
         
        self.assertNotIn(b'level print bed', response.data)


class  taskup(TestBase):
    def test_up_task(self):
        response = self.client.post(
            url_for('up_task', taskid = 1),
            data = dict(name="bakepla"),
            follow_redirects=True
        )
        
        self.assertIn(b'bakepla', response.data)   
        self.assertNotIn(b'test print bed', response.data)   

class testjoin(TestBase):
    def test_glue(self):
        response = self.client.post(
            url_for('glue', projectid = 1, taskid = 1),
            follow_redirects = True
        )

        self.assertIn(b'flowerpot', response.data)
        self.assertIn(b'level print bed', response.data)