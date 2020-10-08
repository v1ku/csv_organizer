First install pandas using pip. Pip should be installed along with python. Try the following command

```sh
$ pip install pandas --user
```

if pip isnt installed follow directions on https://phoenixnap.com/kb/install-pip-windows, or uninstall python and install the latest python version. Then, to run code use one of the following commands after navigating to where the python file is downloaded. 

```sh
$ python organizer.py -o <output_file_name> -i <input_folder_name> -c <csv_with_criteria>
```

or

```sh
$ python organizer.py --output <output_file_name> --inputs <input_folder_name> --criteria <csv_with_criteria>
```

(output_file_name) is to be in the format 'path/to/output/folder/output_file_name.csv' or alternatively 'path/to/output/folder', with or without single quotes. If output folder is given without filename it will create and store output in csv file with current time as name.

(input_folder_name) is the path to the folder containing all the input files, given as 'path/to/input/folder'.
(csv_with_criteria) should contain path to the csv file containing the criteria.



