# Data Science in Production Project


## Starting Commands ##

```bash
$ git init
$ git branch -M main
$ git remote add origin https://github.com/mohamedelmesawy/RAM_Project_DS_PROD.git
$ dvc init
$ git status
$ git commit -m "initialize repo"


$ dvc remote add -d dvc-RAM-remote gdrive://1vSVT0oq6I4rb6Ho2AzQMKQ7Z6X_nUwqy/data
$ cat .dvc/config
$ git commit .dvc/config -m "configure remote storage"
```


## Create data Directory ## 
```bash
$ mkdir data
$ copy file to data folder
$ ls ./data
$ dvc add ./data/Mall_Customers.csv


$ cat ./data/Mall_Customers.csv.dvc
$ git add data/Mall_Customers.csv.dvc data/.gitignore
$ git commit -m "data: track"
$ git tag -a 'v1' -m "raw data"
$ git push origin main --tags
$ dvc push
```



## Updating the Data Source [Removing lines from CSV] ##
```bash
$ dvc add ./data/Mall_Customers.csv
$ git add ./data/Mall_Customers.csv.dvc
$ git tag -a 'v2' -m 'removed 50 lines'
$ git push origin main --tags
$ dvc push


$ git add .
$ git commit -m 'adding second version tag of csv'
$ git push origin main --tags


$ dvc remote add -d dvc-PC-remote '../../Remote_Data'
$ dvc remote list
$ git add .dvc/config
$ git commit -m 'adding another DVC_REPO'
$ git push origin
```

<hr>


## RUN the Project ##

```bash
# Clone this project
$ git clone https://github.com/mohamedelmesawy/RAM_Project_DS_PROD.git

# Start ML-FLow Server
$ mlflow ui

# Run the FLASK Linear Regression Application 
$ python ./main.py

# Run the ML Pipeline [GIT + DVC + MLFlow] 
$ python ./ML_Pipeline.py
```

![screen_01](https://user-images.githubusercontent.com/28452932/144993391-a565d398-7804-4a60-8edf-9696c86b19f8.jpg)

![screen_02](https://user-images.githubusercontent.com/28452932/144993409-39a02e9d-3995-4859-a302-7363d417677e.jpg)

![screen_03](https://user-images.githubusercontent.com/28452932/144993421-76f15b29-0302-40c4-b2eb-24146ac0ca6e.jpg)

![screen_04](https://user-images.githubusercontent.com/28452932/144995475-1e8545bb-7e48-4fa6-94bc-d85e1336aeac.jpg)
