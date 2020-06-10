# Recipe Analytics
## Analysing Recipe Data Using PySpark

## Description
To use PySpark to Filter recipes with beef as a ingredient and calculate the average cooking time then Classify with its difficulty levels (cooking time).


**Formula :** ``` total_cook_time = cookTime + prepTime ```

**Criteria** | **total_cook_time**
------------ | -------------
easy | less than 30 mins
medium | between 30 and 60 mins
hard | more than 60 mins.



### prerequisite & assumption
**for local deployment**
  <p> Assuming that Python version 3, PySpark and Hadoop-home and winUtils configured </p>

### Code Outline
**High-level Overview**
* Load Data
* Transform Data
* Filter data
* Difficulty metrics

Following file structure is advised: (in case of errors, please consult this)
```
./
... HelloFresh.py
... Readme.md
... requirements.txt
... test_isoTimeToMin.py
... UtilsETL.py
... input/
... ... recipes.json
... output/
... ... report.csv

```
### Required Libraries
You can install necessary packages to run these codes by running the following:
```pip install -r requirements.txt```

## Note
- Make sure install the required packages

- To run ```HelloFresh.py``` use the run locally command


- - - -
### Unit tests 
**High-level Overview**

*Unit test cases have been created using unit-test module of python

Dataframe comparitor using padas testing has been created to check transformtion and metrics 
TODO: testfiles>


### Errors handling

* Most of the known exceptions are handled 
* Extra functionality has been added to filter the null and bad records coming from the source
 

### To run locally
```   

python HelloFresh.py --inputPath input/recipes.json --outputPath output/ --filterColumn ingredients --filterValue beef


```

## Config handling

* Used config with spark to pass the requied params in Json format


### Logging and alerting

* Log4j has also be configued with spark configuration.
* Application Level logs can be captured.
* Also, the Bad records from source can be logged for the further refinement of the process flow.

* CPU and memory level logs also can be captured and logged.
  ⋅⋅⋅then Cloud watch can be used along with SNS Alerting.  
  ⋅⋅⋅SNS can further be used to handle based on the scenarios.
* using email notification or Lamda function for any imediate actions 


## Consider scaling of your application

* This application can be scaled by deploying to AWS EMR Or Yarn 
* dynamic scaling feature can be used to save the cost 


CI/CD explained

* Infrastructure can be created from code based on the size and usage of data using terraform or cloudformation 

* Deployment of code to Environments right from repository Jenkins on an EC2 instance or AWS CodePipeline

## Performance tuning explained

Used Cache for the initial transformation to avoid further re-compution 

```
--num-executors

--executor-cores

--executor-memory

```

These settings can be further configured based on the size and amount of parallelism needed to process.

Also based on the amount of Diver memory configuration the amount of data collected back to the driver from executor have to be estimated to prevent error.

- - - -
