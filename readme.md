> The structure of this project is made by Udacity Full Stack Nanodegree, see requirements [here](https://review.udacity.com/#!/rubrics/277/view).

## What is this project, anyway?

This project is for developers who are willing to get the basic knowledge of SQL Queries by using Python as a background programming language. Plenty of practices and achievabilities during doing the process.

## How to Run

1. Check [this instruction](https://classroom.udacity.com/nanodegrees/nd004/parts/8d3e23e1-9ab6-47eb-b4f3-d5dc7ef27bf0/modules/bc51d967-cb21-46f4-90ea-caf73439dc59/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0) to install the virtual machine.
2. Run `vagrant up` then `vagrant ssh`.
3. Download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip), unzip the file into `vagrant` directory.
4. Load the data by typing this `psql -d news -f newsdata.sql`
5. Run this code to create a view(**important**):

 ```sql
 CREATE view article_title AS
 SELECT replace(path, '/article/', '')
 FROM log
 WHERE log.path like '/article/%;
 ```

6. `cd vagrant/news` and run `python newsdb.py`
7. You'll get the results.
