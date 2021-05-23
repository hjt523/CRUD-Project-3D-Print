# CRUD-Project-3D-Print

This is the GIT repository for my QA Training Academy project due on the 24th of May.

My Idea is a CRUD application for keeping track of 3D prints for my personal printer. Effectively, it has to be able to start a print project ( create), do test runs with the material (create), at different temperatures and retraction settings depending upon outcome ( update), maybe hold some comments on prior temperatures (create/update), so i can monitor the progress of the task (read) and finally close down the tests and print project when complete ( delete).

![ERD](ERD-QA-Project.jpeg)
- Table1: ERD for the SQL databases used in the project

The ERD Table shown above shows a many to many relationship for the overall project ( i.e. Printing a rubber duck) to the the Tasks ( i.e. calibrating the print bed, baking the PLA, test calibration prints) because things like calibration and preparing of the filament can be done for one project and aslong as the test prints come back fine don't need to be repeated for the next project(s). 
There are a lot of tasks in 3D printing that when broken down for a individual print eliminate work done for several projects, as well as the fact that several projects can be printed at once provided there is room on the print bed, to reduce user input time when setting up prints.
With respect to Project_status and Task_status, these have the options of ongoing or complete as options as there's little point in having string input for something that can be one or the other.
Task_details is optional because naming a task " clean the nozzle" is self evident, but when running say a extruder temperature test on the PLA filament, its useful to add details like temperature range currently considered, because you will often start off low, then high, and split the difference around the manufacturers quoted temp ranges due to things like moisture and room temperature affecting the behaviour of the material.

## Design

In terms of design, I want the index page to Welcome people to the site, explain to them how the site works / maybe show some examples, with some buttons to send people to a list of current projects with their active tasks, to the list of Tasks in more detail, and directly to the add project page.
The add project page should send them to the current projects page, where they can either add new tasks and assign them to that project, or ammend existing tasks to also be assigned to the new project where applicable.

SO in terms of design, there are 8 html pages:
- Index
- Add Project
- View Current Projects
- Update Current Tasks
- Add Task
- View Current Tasks
- Update Current Tasks
- layout

Overall, the plan is for the website to follow this Flow:

![sitemodel](https://github.com/hjt523/CRUD-Project-3D-Print/blob/586f41ccb332515bd2f25121a6aa8df461c11e1b/Site%20Map.jpeg)

Could potentially merge Add project and Task into one add page with a dropdown option to which it adds to.

The code, HTML templates, and Testing code should be kept in seperate folders.
## Use Examples

## Risk Assessments

![Risk](https://github.com/hjt523/CRUD-Project-3D-Print/blob/7ad788446525e2889972538e2c12dd4bf051fe03/Riskassessment1.jpg)

## Code Flowcharts

## Code Documentation

- Implement Jenkins to deploy.

![kan](https://github.com/hjt523/CRUD-Project-3D-Print/blob/aab7f824869eede41c2efd28a33339d707773d87/KanbanBoard1.jpg)

An example of the Kanban Boards used to plan this project.

![kan2](https://github.com/hjt523/CRUD-Project-3D-Print/blob/d6112dbf6dd9c39412bbaa448c642b4b84f77491/postsprint1.jpg)
Kanban board post sprint

## PyTest Unit Testing

![Pytest](https://github.com/hjt523/CRUD-Project-3D-Print/blob/fdf2b8a6f9e94d8c4cd9ec71a358086c1ff80d52/Unittest.jpg)

### Setup
! Todo, this should describe what to install / to run in order to get the app to work.
! If term permits, shell script to install necessary packages?
! A shell script would be especially advantages as i could input optional things like remote host through it but use a default local host otherwise without
! users needing to mess with terminal or my python files.

## Dependencies/ Languages
- Python3.7
- Flask
- flask_sqlalchemy
- flask_wtf
- flaskform
- html
- sql
- googlecloud or AWS sql for database hosting ( alternatively host locally with sqlite)







