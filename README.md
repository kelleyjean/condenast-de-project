# condenast-de-project

This README contains an overview of what is contained within the Data Pipeline program and how to run it.

First, install requirements.txt by running pip install -r requirements.txt to make sure all dependences are accounted for. If you are already running some of these packages, please set up a virtual environment so as to not change any versions you may have.

The folder "EDA" contains a script that will write the names of the columns in each sample Formula One Championship csv and their respective datatypes to a separate csv file that can be referenced quickly when needing to do transformations or apply business logic to a column. To get that csv, simply run eda_script.py in your terminal. Please note, this step is optional and is not required to run the rest of the program.

Kindly note that a significant amount of time was spent trying to install PySpark on my local machine. I kept running into the "SPARK_HOME was not found error," after setting many environment variables locally. I would be happy to discuss this further and how it impacted the scalability component of this project.

The extract.py module runs through each sample csv, converts it to a dataframe, and temporarily stores it locally as a pickle file.

The transform.py module has three functions which correlate with the three transformation requests within the project's original README. Each function writes the results to a csv file, with proper encoding to ensure no alphabets are lost.

Unfortunately the third function was not able to be completed due to time constraints, however pseudologic was written to explain how it would be completed.