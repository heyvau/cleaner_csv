# CSV Data Cleaner


## Annotation

Class CleanerCSV contains set of methods to proceed and clean your dataset,
which should be represented as a CSV file.

All you need to run this app is a spec file in JSON with required
parameters for data cleaning.

In case when custom spec is not provided, "default_specs.json" will be used.


## How to use spec file


1. Set path to source CSV file and file where you want to write clean data. Also specify a delimiter.
   
```json
    "input_file" : "files/my_data.csv",
    "output_file" : "files/my_data_clean1.csv",
    "delimiter": ",",
```


2. Set path to HTML profiles for original and cleaned data. Summary file show you comparison of both data sets, but it's possible only when data types in columns are equal (not after data type correction).

```json
    "input_file_profile": "profiles/input_file.html",
    "output_file_profile": "profiles/output_file.html",
    "summary_file": "profiles/summary.html",
```


3. Here you can choose, which methods to use:
   
  * Remove duplicate rows (*true* / *false*)
  
```json
    "drop_duplicates" : true,
```

  * Remove NaN values-containig rows (*true* / *false*)

```json
    "drop_na" : true,
```
    
  * Trimm white spaces in string columns specified in **"str_col"** (*true* / *false*)
  
```json
    "clean_str_columns" : true,
```
    
  * Remove rows idential to header row (*true* / *false*)

```json
    "drop_row_title": true,
```
    
  * Replace characters (*true* / *false*), specifying columns and characters to change in **"replace_row_char_details"**

```json
    "replace_row_char": true,

    "replace_row_char_details": {
        "col": ["Order ID"],
        "change": {"@":""}
    }
```

  * Clean outliers (*true* / *false*), specifying columns in **"col_outlier"**

```json
    "clean_outliers": true,

    "col_outlier" : ["Price Each"],
```

  * Export cleaned data set to CSV file (*true* / *false*)

```json
    "export_output_file": true,
```

  * Specify columns to remove 

```json
    "drop_col" : [],
```

4. Convert columns data to specific data types

```json
    "str_col": ["Product","Purchase Address"],
    "float_col": [],
    "int_col": [],
    "numeric_col": ["Order ID", "Quantity Ordered", "Price Each"],
    "datetime_col": ["Order Date"],
```
    

## Run the App

1. Install all required libraries in your virtual environment:


```console
> pip install -r requirements.txt
```

2. Then run python script 'cleaner_csv.py' as follows (make sure you are in project's folder ):

```console
> python cleaner_csv.py
```

3. The program progress will be displayed in the **"cleaner.log"** file.
