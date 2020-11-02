In this project, we implement methods to identify if an individual is statistically indistinguishable when compared to his/her own internet utilization whereas statistically distinguishable when compared to the internet users of others. For this purpose I have used just a few parameters which I will mention in the rest of the workflow. Also we are supposed to calculate the data flow for three different time windows: 10 seconds, 227 seconds and 5 minutes. Based on these results we will have to calculate for P and Z for the final results.

Workflow summary:
My project is divided in three files: main_file.py, create_new_df.py, Calculations.py
The code is to be executed as follows:
1.	Run the main_file.py to get the filtered data from the .xlsx format in .csv form
2.	Run the create_new_df.py to get the Data splitting per day in form of .csv files
3.	Run the Calculations.py to obtain the outputs using spearman correlation

Workflow:

1.	main_file.py: This file consists of two functions namely, function_file_list() and function_processed_data(). In order to keep the code simple I have avoided using one main function and call different functions in that one. This file basically filters all the data and keeps the necessary parameters in the form of the .csv file. The function function_file_list() gives the list of the files in the folder files material, which holds the downloaded data in the form of .xlsx format. This function makes use of the inbuilt function imported from os called the listdir() and the parameter path in this function the path for the same folder mentioned above. The print() in this function is just to double check, you may also comment the function. The function function_processed_data() first reads the excel files with the help of a DataFrame object df already pre-defined in the library pandas. Now, I have deleted the parameters that are of no use to me for any further calculation and hence I have only included Real First Packet and also calculated octets/duration by using the given two parameters and hence I have made use of just these two parameters for the rest of the project. The below shown snippet from the code is just to remove the .xlsx extension and add the .csv extension to save the dataframe
```
new_file_name = filename.strip('xlsx')
new_file_name = new_file_name + 'csv'
```
Now I have called the function_file_list() that lists the file and calls the function_processed_data() in order to save the .csv files one by one with all the mentioned changes. I have stored all the preprocessed files in the folder processed_material.


2.	create_new_df.py: This file performs the major preprocessing part i.e., computing the flow durations and data splitting per day. I have used in total three functions for the same. I have defined a function called create_window_size() which takes time window as value and hence one can pass 10, 227 or 300 in order to obtain flow durations for these different windows. The two for  loops are used to iterate for 5 days i.e., from Monday to Friday for two different weeks. The first for loop is for the first week and I have considered the first week from Feb 11 2013 to Feb 15 2013 and the second week from Feb 18 2013 to Feb 22 2013. I have made use of a list called list_window which stores all the windows for the required duration and I have used the append() to store the values for windows in this list. The function read_files() takes the window as a parameter from the user and this is because I need this information for the rest of my program. This function lists all the .csv files one by one with the help of the first for loop and after obtaining the file this function uses laddered elif conditions to save the prepared files(these files are prepared under the function check_window which I will be explaining later in this section) in their dedicated folders. For saving files for 10secs window size, I have used the folder windowsize10, for 227 secs(windowsize227 folder) and for 300secs/5mins(windowsize300 folder). The check_window() function takes three parameters as input and these are provided by the read_files() functions. The processed_list is a list consisting of Real First Packet obtained from the .csv files, templist_docperdur is a list consisting of doctets/duration obtained from the same csv file and the  windowsize is the time window. This functions works as: the whole function works for the length of the list_window and condition checked(shown below) compares if the epoch time of the Real First Packet falls under the time window size and if it does, it takes the doctets/duration of that row.

``` if list_window[i] <= processedlist[row] < (list_window[i] + windowsize): ```

 After obtaining the total rows for a time frame, the function then calculates the average of the obtained doctets/duration. If there aren’t obtained any doctets/duration for a time frame then the function places the average as 0.001. Now this whole process is repeated for every file(54 files) in the folder for 10seconds, 227 seconds and 300seconds under the function read_files(). 



3.	Calculations.py: In this file, first I have collected all the data using the function get_data(). This function obtains the list of week1 and week2 and the octets/duration corresponding to the days(a snippet for obtaining this is shown below). 

``` for i in range(5):
   print(win_size)
   start = mon_11 + i * 86400
   for j in range(windows):
       x = start + j * win_size
       list_week.append('week1')
```
Later in the same function, I have managed to get octets/duration of all users for all the window sizes in the folder spearman and the files for window size 10, window size 227 and window size 300 are win10, win227 and win300 respectively. Then I have called this same function to obtain all these values to their respective files. The spearman_calculations performs all the calculations necessary to obtain the required outputs and all these outputs are stored in the folder spearman_outputs. The outputs for the window size 10,227,300 are stored in ten.csv, twotwoseven.csv, threehundred.csv respectively. 
