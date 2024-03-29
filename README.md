# CI-CD-Pipeline-for-house-prediction
[![Python application test with Github Actions](https://github.com/Rbaibi/CI-CD-Pipeline-for-house-prediction/actions/workflows/pythonapp.yml/badge.svg)](https://github.com/Rbaibi/CI-CD-Pipeline-for-house-prediction/actions/workflows/pythonapp.yml)

CI/CD Pipeline for house price prediction

## Project Plan

* A link to a [Trello board](https://trello.com/b/iabbTYwG/ci-cd-flask-azure-web-app) for the project
* A link to a [Spreadsheet](https://docs.google.com/spreadsheets/d/1cYg9aeNhqRpSTXk2ArI2On4Emg_dwG5LRVx6bBLDWrE/edit?usp=sharing) that includes the original and final project plan

## Instructions
  
* Architectural Diagram that shows how key parts of the system work
![Architectural Diagram ](https://raw.githubusercontent.com/Rbaibi/CI-CD-Pipeline-for-house-prediction/main/Screenshots/Architectural%20Overview.png)


Instructions for running the Python project.

* Project running on Azure App Service
![img](https://raw.githubusercontent.com/Rbaibi/CI-CD-Pipeline-for-house-prediction/main/Screenshots/Screenshot4%20showing%20Azure%20App%20Service.png)

First start by cloning this repository

```console
foo@bar:~$ git clone https://github.com/Rbaibi/CI-CD-Pipeline-for-house-prediction.git
```

* Project cloned into Azure Cloud Shell
![img](https://raw.githubusercontent.com/Rbaibi/CI-CD-Pipeline-for-house-prediction/main/Screenshots/Screenshot1%20showing%20project%20cloned%20into%20Azure%20Cloud%20Shell.png)

Run the `make all` command in azure bash

```console
foo@bar:~$ make all
```

* Passing tests that are displayed after running the `make all` command from the `Makefile`
![img](https://raw.githubusercontent.com/Rbaibi/CI-CD-Pipeline-for-house-prediction/main/Screenshots/Screenshot2%20showing%20the%20passing%20test.png)

Create the serverless webapp by running the following command

```console
foo@bar:~$ az webapp up --name flaskserverlesswebapp --resource-group Azuredevops --runtime "PYTHON:3.7"
```

To get an output of the streamed log files use

```console
foo@bar:~$ az webapp log tail
```

* Output of streamed log files from deployed application
![img](https://raw.githubusercontent.com/Rbaibi/CI-CD-Pipeline-for-house-prediction/main/Screenshots/log.png)


Test out whether you can make a prediction

```console
foo@bar:~$ ./make_predict_azure_app.sh 
```

* Successful prediction from deployed flask app in Azure Cloud Shell. 

The output should look similar to this:
![img](https://raw.githubusercontent.com/Rbaibi/CI-CD-Pipeline-for-house-prediction/main/Screenshots/Screenshot5%20showing%20a%20successful%20prediction%20in%20Azure%20Cloud%20Shell.png)


* Output of a test run
![img](https://raw.githubusercontent.com/Rbaibi/CI-CD-Pipeline-for-house-prediction/main/Screenshots/Screenshot3%20showing%20passing%20GitHub%20Actions%20build.png)


* Successful deploy of the project in Azure Pipelines.  
![img](https://raw.githubusercontent.com/Rbaibi/CI-CD-Pipeline-for-house-prediction/main/Screenshots/Screenshot6.3%20showing%20a%20successful%20run%20of%20the%20project%20in%20Azure%20Pipelines.png)


* Running Azure App Service from Azure Pipelines automatic deployment
![img](https://raw.githubusercontent.com/Rbaibi/CI-CD-Pipeline-for-house-prediction/main/Screenshots/Screenshot6.1%20showing%20a%20successful%20run%20of%20the%20project%20in%20Azure%20Pipelines.png)




* Locust test
![img](https://raw.githubusercontent.com/Rbaibi/CI-CD-Pipeline-for-house-prediction/main/Screenshots/Screenshot7.2%20locust%20test.png)
![img](https://raw.githubusercontent.com/Rbaibi/CI-CD-Pipeline-for-house-prediction/main/Screenshots/Screenshot7.1%20locust%20test.png)



## Enhancements

How to improve the project in the future
* Collect more data
* Improve the ML model
* Create a Graphical User Interface


## Demo 

[Link Screencast on YouTube](https://youtu.be/J6-ItUf_qK0)

