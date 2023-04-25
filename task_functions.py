
def print_main_menu(menu):
    """
    Given a dictionary with the menu,
    prints the keys and values as the
    formatted options.
    Adds additional prints for decoration
    and outputs a question
    "What would you like to do?"
    """
    print('==========================')
    print('What would you like to do?')
    for key, value in menu.items():
        print(f'{key} - {value}')
    print('==========================')

def get_written_date(date_format):
    """
    The function gets a list of integers that
    corresponds to a date and formats it into
    a written format but for this final project,
    the date_list will be a string fomatted like
    MM/DD/YYYY
    """
    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    month = int(date_format[0])
    day = int(date_format[1])
    year = int(date_format[2])
    month1 = month_names[month]
    
    date = month1 + ' ' + str(day) + ', ' + str(year)
    return date

def get_selection(action, suboptions, to_upper = True, go_back = False):
    """
    param: action (string) - the action that the user
            would like to perform; printed as part of
            the function prompt
    param: suboptions (dictionary) - contains suboptions
            that are listed underneath the function prompt.
    param: to_upper (Boolean) - by default, set to True, so
            the user selection is converted to upper-case.
            If set to False, then the user input is used
            as-is.
    param: go_back (Boolean) - by default, set to False.
            If set to True, then allows the user to select the
            option M to return back to the main menu

    The function displays a submenu for the user to choose from. 
    Asks the user to select an option using the input() function. 
    Re-prints the submenu if an invalid option is given.
    Prints the confirmation of the selection by retrieving the
    description of the option from the suboptions dictionary.

    returns: the option selection (by default, an upper-case string).
            The selection be a valid key in the suboptions
            or a letter M, if go_back is True.
    """
    selection = None
    if go_back:
        if 'm' in suboptions or 'M' in suboptions:
            print("Invalid submenu, which contains M as a key.")
            return None
    while selection not in suboptions:
        print(f"::: What would you like to {action.lower()}?")
        for key in suboptions:
            print(f"{key} - {suboptions[key]}")
        if go_back == True:
            selection = input(f"::: Enter your selection "
                              f"or press 'm' to return to the main menu\n> ")
        else:
            selection = input("::: Enter your selection\n> ")
        if to_upper:
            selection = selection.upper() # to allow us to input lower- or upper-case letters
        if go_back and selection.upper() == 'M':
            return 'M'
    if to_upper:    
        print(f"You selected |{selection}| to",
              f"{action.lower()} |{suboptions[selection].lower()}|.")
    else:
        print(f"You selected |{selection}| to",
          f"{action.lower()} |{suboptions[selection]}|.")
    return selection

def print_task(task, priority_map, name_only = False):
    """
    param: task (dict) - a dictionary object that is expected
            to have the following string keys:
    - "name": a string with the task's name
    - "info": a string with the task's details/description
            (the field is not displayed if the value is empty)
    - "priority": an integer, representing the task's priority
        (defined by a dictionary priority_map)
    - "duedate": a valid date-string in the US date format: <MM>/<DD>/<YEAR>
            (displayed as a written-out date)
    - "done": a string representing whether a task is completed or not

    param: priority_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "priority"
            values stored in the task; the stored value is displayed for the
            priority field, instead of the numeric value.
    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the task is printed.
            Otherwise, displays the formatted task fields.

    returns: None; only prints the task values

    Helper functions:
    - get_written_date() to display the 'duedate' field
    """
    if name_only == False:
        print(task["name"])
        if task["info"] != "":
            print(f'  * {task["info"]}')
        print(f'  * Due: {get_written_date(task["duedate"].split("/"))}  (Priority: {priority_map[task["priority"]]})')
        print(f'  * Completed? {task["done"]}')
    if name_only == True:
        print(task["name"])

def print_tasks(task_list, priority_map, name_only = False,
                show_idx = False, start_idx = 0, completed = "all"):
    """
    param: task_list (list) - a list containing dictionaries with
            the task data
    param: priority_map (dict) - a dictionary object that is expected
            to have the integer keys that correspond to the "priority"
            values stored in the task; the stored value is displayed 
            for the priority field, instead of the numeric value.
    param: name_only (Boolean) - by default, set to False.
            If True, then only the name of the task is printed.
            Otherwise, displays the formatted task fields.
            Passed as an argument into the helper function.
    param: show_idx (Boolean) - by default, set to False.
            If False, then the index of the task is not displayed.
            Otherwise, displays the "{idx + start_idx}." before the
            task name.
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets displayed for the first task, if show_idx is True.
    param: completed (str) - by default, set to "all".
            By default, prints all tasks, regardless of their
            completion status ("done" field status).
            Otherwise, it is set to one of the possible task's "done"
            field's values in order to display only the tasks with
            that completion status.

    returns: None; only prints the task values from the task_list

    Helper functions:
    - print_task() to print individual tasks
    """
    print("-"*42)
    for task in task_list: # go through all tasks in the list
        if show_idx: # if the index of the task needs to be displayed
            print(f"{task_list.index(task)+1}.", end=" ")
        if completed == "all":
            print_task(task, priority_map, name_only)
        elif task["done"] == completed:
            print_task(task, priority_map, name_only)

def is_valid_index(idx, in_list, start_idx = 0):
    """
    param: idx (str) - a string that is expected to
            contain an integer index to validate
    param: in_list - a list that the idx indexes
    param: start_idx (int) - an expected starting
            value for idx (default is 0); gets
            subtracted from idx for 0-based indexing

    The function checks if the input string contains
    only digits and verifies that (idx - start_idx) is >= 0,
    which allows to retrieve an element from in_list.

    returns:
    - True, if idx is a numeric index >= start_idx
    that can retrieve an element from in_list.
    - False if idx is not a string that represents an 
    integer value, if int(idx) is < start_idx,
    or if it exceeds the size of in_list.
    """
    if (type(idx) == str) and (idx.isdigit() == True) and (int(idx) >= start_idx) and ((int(idx) - start_idx) < len(in_list)):
        return True
    else:
        return False

def delete_item(in_list, idx, start_idx = 0):
    """
    param: in_list - a list from which to remove an item
    param: idx (str) - a string that is expected to
            contain a representation of an integer index
            of an item in the provided list
    param: start_idx (int) - by default, set to 0;
            an expected starting value for idx that
            gets subtracted from idx for 0-based indexing

    The function first checks if the input list is empty.
    The function then calls is_valid_index() to verify
    that the provided index idx is a valid positive
    index that can access an element from info_list.
    On success, the function saves the item from info_list
    and returns it after it is deleted from in_list.

    returns:
    If the input list is empty, return 0.
    If idx is not of type string or start_idx is not an int, return None.
    If is_valid_index() returns False, return -1.
    Otherwise, on success, the function returns the element
    that was just removed from the input list.

    Helper functions:
    - is_valid_index()
    """
    if in_list == []:
        return 0
    if (type(idx) != str) or (type(start_idx) != int):
        return None
    if is_valid_index(idx, in_list, start_idx) == False:
        return -1
    else:
        return in_list[int(idx) -start_idx]
        del in_list[int(idx) - start_idx]

def is_valid_name(name):
    """
    param1- a string

    returns:
    - true if the string is between 3 and 25 characters inclusive
    - false otherwise
    """
    if 3 <= len(name) <= 25:
        return True
    else:
        return False

def is_valid_priority(priority_value, priority_map):
    """
    param1- a string that should contain an integer priority value
    param2- a dictionary that contains the mapping between the integer
    priority value to its representation

    returns:
    - true if the string contains an integer value that maps to a key
    in the dictionary
    - false otherwise
    """
    if (type(priority_value) == str) and (priority_value.isdigit() == True) and (int(priority_value) in priority_map):
                return True
    else:
        return False

def is_valid_month(date_list):
    """
    The function returns true if the month in the string is valid
    and false otherwise
    """
    if len(date_list) == 3:
        for j in date_list:
            if type(j) != str:
                return False
        if date_list[0].isdigit():
            month = int(date_list[0])
            if (month > 0) and (month < 13):
                return True
    return False

def is_valid_day(date_list):
    """
    The function returns true if the day in the list is valid and
    false otherwise

    helper function:
    is_valid_month()
    """
    num_days = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    if is_valid_month(date_list):
        if date_list[1].isdigit():
            month = int(date_list[0])
            day = int(date_list[1])
            if (day > 0) and (day <= num_days[month]):
                return True
    return False

def is_valid_year(date_list):
    """
    The function returns true if the year in the list is valid
    and false otherwise
    """
    if len(date_list) == 3:
        for j in date_list:
            if type(j) != str:
                return False
        if date_list[2].isdigit():
            year = int(date_list[2])
            if year > 1000:
                return True
    return False

def is_valid_date(date_string):
    """
    param1- a string that should contain a date in the format (MM/DD/YYYY)
    validates each date component
    returns:
    - true if string is valid date in correct format
    - false otherwise

    helper_functions:
    is_valid_month()
    is_valid_day()
    is_valid_year()
    """
    date_list = date_string.split('/')
    if (is_valid_month(date_list) == True) and (is_valid_day(date_list) == True) and (is_valid_year(date_list) == True):
                return True
    else:
        return False

def is_valid_completion(completion):
    """
    param1- a string that should be either 'yes' or 'no'
    if string either, the function will return true and if otherwise
    the function will return false
    """
    if completion == 'yes' or completion == 'no':
        return True
    else:
        return False

def get_new_task(new_task, priority_map):
    """
    param1: a list with 5 strings (check)
    param2: dictionary containing mapping between the integer
    priority value

    returns:
    - integer size of list if the size of list is not correct
    - tuple with ("type", <value>) if any of the elements on the list
    are not of type string
    - if size and str is correct, but validation fails, returns tuple
    with name of parameter and corresponding value/parameter that failed
    - if all passes, returns new dictionary with task keys set to
    provided parameters

    helper functions:
    is_valid_name()
    is_valid_priority()
    is_valid_date()
    is_valid_completion()
    """
    if len(new_task) != 5:
        return len(new_task)
    for element in new_task:
        if type(element) != str:
            return "type", element
    new_entry = {}
    if (is_valid_name(new_task[0]) == True) and (is_valid_priority(new_task[2], priority_map) == True) and (is_valid_date(new_task[3]) == True) and (is_valid_completion(new_task[4]) == True):
        new_entry["name"] = new_task[0]
        new_entry["info"] = new_task[1]
        new_entry["priority"] = int(new_task[2])
        new_entry["duedate"] = new_task[3]
        new_entry["done"] = new_task[4]
        return new_entry
    elif is_valid_name(new_task[0]) == False:
        return "name", new_task[0]
    elif (is_valid_priority(new_task[2], priority_map) == False):
        return "priority", (new_task[2])
    elif is_valid_date(new_task[3]) == False:
        return "duedate", new_task[3]
    elif is_valid_completion(new_task[4]) == False:
        return "done", new_task[4]
    
def load_tasks_from_csv(filename, in_list, priority_map):
    """
    param: filename (str) - A string variable which represents the
            name of the file from which to read the contents.
    param: in_list (list) - A list of task dictionary objects to which
            the tasks read from the provided filename are appended.
            If in_list is not empty, the existing tasks are not dropped.
    param: priority_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the priority value "Highest" or "Low")
            Needed by the helper function.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv` and `import os`.

    If the file exists, the function will use the `with` statement to open the
    `filename` in read mode. For each row in the csv file, the function will
    proceed to create a new task using the `get_new_task()` function.
    - If the function `get_new_task()` returns a valid task object,
    it gets appended to the end of the `in_list`.
    - If the `get_new_task()` function returns an error, the 1-based
    row index gets recorded and added to the NEW list that is returned.
    E.g., if the file has a single row, and that row has invalid task data,
    the function would return [1] to indicate that the first row caused an
    error; in this case, the `in_list` would not be modified.
    If there is more than one invalid row, they get excluded from the
    in_list and their indices will be appended to the new list that's
    returned.

    returns:
    * -1, if the last 4 characters in `filename` are not '.csv'
    * None, if `filename` does not exist.
    * A new empty list, if the entire file is successfully read from `in_list`.
    * A list that records the 1-based index of invalid rows detected when
      calling get_new_task().

    Helper functions:
    - get_new_task()
    """
    import os
    import csv
    if filename[-4:] != '.csv':
        return -1
    if not os.path.exists(filename):
        return None
    else:
        new_list = []
        with open(filename, 'r') as csvfile:
            file_reader = csv.reader(csvfile, delimiter = ',')
            row_num = 1
            for row in file_reader:
                if type(get_new_task(row, priority_map)) == dict:
                    in_list.append(row)
                    return []
                if type(get_new_task(row, priority_map)) != dict:
                    new_list.append(row_num)
                    row_num += 1
            return new_list

def save_tasks_to_csv(tasks_list, filename):
    """
    param: tasks_list - The list of the tasks stored as dictionaries
    param: filename (str) - A string that ends with '.csv' which represents
               the name of the file to which to save the tasks. This file will
               be created if it is not present, otherwise, it will be overwritten.

    The function ensures that the last 4 characters of the filename are '.csv'.
    The function requires the `import csv`.

    The function will use the `with` statement to open the file `filename`.
    After creating a csv writer object, the function uses a `for` loop
    to loop over every task in the list and creates a new list
    containing only strings - this list is saved into the file by the csv writer
    object. The order of the elements in the list is:

    * `name` field of the task dictionary
    * `info` field of the task dictionary
    * `priority` field of the task as a string
    (i.e, "5" or "3", NOT "Lowest" or "Medium")
    * `duedate` field of the task as written as string
    (i.e, "06/06/2022", NOT "June 6, 2022")
    * `done` field of the task dictionary

    returns:
    -1 if the last 4 characters in `filename` are not '.csv'
    None if we are able to successfully write into `filename`
    """
    import csv
    file_list = []
    if filename[-4:] != '.csv':
        return -1
    else:
        with open(filename, 'w', newline='') as csvfile:
            file_reader = csv.reader(csvfile)
            for file_tasks in tasks_list:
                for file_value in file_tasks.items():
                    file_list.append(str(file_value))


def update_task(info_list, idx, priority_map, field_key, field_info, start_idx = 0):
    """
    param: info_list - a list that contains task dictionaries
    param: idx (str) - a string that is expected to contain an integer
            index of an item in the input list
    param: start_idx (int) - by default is set to 0;
            an expected starting value for idx that gets subtracted
            from idx for 0-based indexing
    param: priority_map (dict) - a dictionary that contains the mapping
            between the integer priority value (key) to its representation
            (e.g., key 1 might map to the priority value "Highest" or "Low")
            Needed if "field_key" is "priority" to validate its value.
    param: field_key (string) - a text expected to contain the name
            of a key in the info_list[idx] dictionary whose value needs to 
            be updated with the value from field_info
    param: field_info (string) - a text expected to contain the value
            to validate and with which to update the dictionary field
            info_list[idx][field_key]. The string gets stripped of the
            whitespace and gets converted to the correct type, depending
            on the expected type of the field_key.

    The function first calls one of its helper functions
    to validate the idx and the provided field.
    If validation succeeds, the function proceeds with the update.

    return:
    If info_list is empty, return 0.
    If the idx is invalid, return -1.
    If the field_key is invalid, return -2.
    If validation passes, return the dictionary info_list[idx].
    Otherwise, return the field_key.

    Helper functions:
    The function calls the following helper functions:
    - is_valid_index()
    Depending on the field_key, it also calls:
    - is_valid_name()
    - is_valid_priority()
    - is_valid_date()
    - is_valid_completion()
    """
    if info_list == []:
        return 0
    if is_valid_index(idx, info_list, start_idx) == False:
        return -1
    if field_key == 'name':
        if is_valid_name(field_info) == True:
            info_list[int(idx)-1][field_key] = field_info
            return info_list[int(idx)-1]
        else:
            return field_key
    if field_key == 'info':
        info_list[int(idx)-1][field_key] = field_info
        return info_list[int(idx)-1]
    if field_key == 'priority':
        if is_valid_priority(field_info, priority_map) == True:
            info_list[int(idx)-1][field_key] = int(field_info)
            return info_list[int(idx)-1]
        else:
            return field_key
    if field_key == 'duedate':
        if is_valid_date(field_info) == True:
            info_list[int(idx)-1][field_key] = field_info
            return info_list[int(idx)-1]
        else:
            return field_key
    if field_key == 'done':
        if is_valid_completion(field_info) == True:
            info_list[int(idx)-1][field_key] = field_info
            return info_list[int(idx)-1]
        else:
            return field_key
    else:
        return -2





                          
