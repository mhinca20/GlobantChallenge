# GlobantChallenge


# Requirements
[docker](https://www.docker.com/get-docker)
[docker-compose](https://docs.docker.com/compose/install/)

# Usage
Clone this repository
```
git clone https://github.com/mhinca20/GlobantChallenge.git
```

Run docker-compose
```
docker-compose up --build
```

Test localhost api in your browser by navigating to
```
http://localhost:5000
```

Upload the 3 files, employees, jobs and departments


Try to get the number of employees hired for each job and department in 2021 divided by quarter. The
table must be ordered alphabetically by department and job.
```
http://localhost:5000/employeesbyq
```

Try to get the list of ids, name and number of employees hired of each department that hired more
employees than the mean of employees hired in 2021 for all the departments, ordered
by the number of employees hired (descending).
```
http://localhost:5000/higerhiresdep
```

Chose wich table you want to backup as avro format.
```
http://localhost:5000/backup
```

Chose wich table you want to restore from avro format.
```
http://localhost:5000/restore
```

Chose wich table you want to get the count.
```
http://localhost:5000/getTableCount
```

Chose wich table you want to clean.
```
http://localhost:5000/cleanTable
```