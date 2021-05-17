# CRUD-Project-3D-Print

This is the GIT repository for my QA Training Academy project due on the 24th of May.

My Idea is a CRUD application for keeping track of 3D prints for my personal printer. Effectively, it has to be able to start a print project ( create), do test runs with the material (create), at different temperatures and retraction settings depending upon outcome ( update), maybe hold some comments on prior temperatures (create/update), so i can monitor the progress of the task (read) and finally close down the tests and print project when complete ( delete).

![ERD](ERD-QA-Project.jpeg)
- Table1: ERD for the SQL databases used in the project

The ERD Table shown above shows a many to many relationship for the overall project ( i.e. Printing a rubber duck) to the the Tasks ( i.e. calibrating the print bed, baking the PLA, test calibration prints) because things like calibration and preparing of the filament can be done for one project and aslong as the test prints come back fine don't need to be repeated for the next project(s). 
There are a lot of tasks in 3D printing that when broken down for a individual print eliminate work done for several projects, as well as the fact that several projects can be printed at once provided there is room on the print bed, to reduce user input time when setting up prints.
With respect to Project_status and Task_status, these have the options of ongoing or complete as options as there's little point in having string input for something that can be one or the other.
Task_details is optional because naming a task " clean the nozzle" is self evident, but when running say a extruder temperature test on the PLA filament, its useful to add details like temperature range currently considered, because you will often start off low, then high, and split the difference around the manufacturers quoted temp ranges due to things like moisture and room temperature affecting the behaviour of the material.



#### Use Examples

#### Code Flowcharts

#### Code Documentation








