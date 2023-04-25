from task_functions import *

the_menu = {"L": "List", "A": "Add", "U": "Update", "D": "Delete", "S": "Save the data to file", "R": "Restore data from file", "Q": "Quit this program"}
all_tasks = [
    {
        "name": "Call XYZ",
        "info": "",
        "priority": 3,
        "duedate": '05/28/2022',
        "done": 'yes'
    },
    {
        "name": "Finish checkpoint 1 for CSW8",
        "info": "Submit to Gradescope",
        "priority": 5,
        "duedate": '06/02/2022',
        "done": 'no'
    },
    {
        "name": "Finish checkpoint 2 for CSW8",
        "info": "Implement the new functions",
        "priority": 5,
        "duedate": '06/05/2022',
        "done": 'no'
    }

]

list_menu = {
    "A": "all tasks",
    "C": "completed tasks",
    "I": "incomplete tasks"
}

priority_scale = {
    1: "Lowest",
    2: "Low",
    3: "Medium",
    4: "High",
    5: "Highest"
}

opt = None

while True:
    print_main_menu(the_menu)
    opt = input("::: Enter a menu option\n> ")
    opt = opt.upper()

    if opt not in the_menu:
        print(f"WARNING: {opt} is an invalid menu option.\n")
        continue

    print(f"You selected option {opt} to > {the_menu[opt]}.")

    if opt == 'Q':
        print("Goodbye!\n")
        break # exit the main `while` loop
            # ----------------------------------------------------------------
    elif opt == 'L':
        if all_tasks == []:
            print("WARNING: There is nothing to display!")
            # Pause before going back to the main menu
            input("::: Press Enter to continue")
            continue
        subopt = get_selection(the_menu[opt], list_menu)
        if subopt == 'A':
            print_tasks(all_tasks, priority_scale)
        elif subopt == 'C':
            print_tasks(all_tasks, priority_scale, completed = 'yes')
        elif subopt == 'I':
            print_tasks(all_tasks, priority_scale, completed = 'no')
            # ----------------------------------------------------------------
    elif opt == 'D':
        continue_action = 'y'
        while continue_action == 'y':
            if all_tasks == []:
                print('WARNING: There is nothing to delete!')
                break
            else:
                print("Which task would you like to delete?")
                print('A - Delete all tasks at once')
                print_tasks(all_tasks, priority_scale, name_only = True, show_idx = True)
                subopt = input(f"::: Enter the number corresponding to the task\n::: or press 'M' to return to the main menu.\n> ")
                if subopt == 'M':
                    break
                if subopt == 'A':
                    subsubopt = input(f"::: WARNING! Are you sure you want to delete All tasks?\n::: Type Yes to continue the deletion.\n> ")
                    if subsubopt == 'Yes':
                        print('Deleted all tasks.')
                        all_tasks = []
                        break
                if (subopt.isdigit() == True) and (int(subopt) <= len(all_tasks)):
                    print('Success!')
                    print(f'Deleted the task |{all_tasks[int(subopt)-1]["name"]}|')
                    del all_tasks[int(subopt)-1]
                    subsubopt = input(f"::: Would you like to delete another task? Enter 'y' to continue.\n> ")
                    continue
                else:
                    print(f'WARNING: |{subopt}| is an invalid task number!')
                    subsubopt = input(f"::: Would you like to delete another task? Enter 'y' to continue.\n> ")
                    continue
            # ----------------------------------------------------------------
    elif opt == 'A':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter each required field, separated by commas.")
            print("::: name, info, priority, MM/DD/YYYY, is task done? (yes/no)")
            new_data = input("> ") # TODO: get and process the data into a list
            new_list = new_data.split(', ')
            result = get_new_task(new_list, priority_scale) # TODO: attempt to create a new task
            if type(result) == dict:
                all_tasks.append(result) # TODO: add a new task to the list of tasks
                print(f"Successfully added a new task!")
                print_task(result, priority_scale)
            elif type(result) == int:
                print(f"WARNING: invalid number of fields!")
                print(f"You provided {result}, instead of the expected 5.\n")
            else:
                print(f"WARNING: invalid task field: {result}\n")

            print("::: Would you like to add another task?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower() 
            # ----------------------------------------------------------------
    elif opt == 'R':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            input_file = input("> ")
            if (load_tasks_from_csv(input_file, all_tasks, priority_scale) == None) or (load_tasks_from_csv(input_file, all_tasks, priority_scale) == -1):
                print(f"WARNING: |{input_file}| was not found!")
                print("::: Would you like to try again? Enter 'y' to try again.")
                continue_action = input("> ")
                continue
            if load_tasks_from_csv(input_file, all_tasks, priority_scale) == []:
                print(f"Successfully stored all tasks to |{input_file}|")
                break
            else:
                print(f"WARNING: |{input_file}| contains invalid data!")
                print("The following rows from the file were not loaded:")
                print(load_tasks_from_csv(input_file, all_tasks, priority_scale))
                print("::: Would you like to load another file? Enter 'y' to try again.")
                continue_action = input("> ")
                continue
            # ----------------------------------------------------------------
    elif opt == 'S':
        continue_action = 'y'
        while continue_action == 'y':
            print("::: Enter the filename ending with '.csv'.")
            filename = input("> ")
            result = save_tasks_to_csv(all_tasks, filename) # TODO: Call the function with appropriate inputs and capture the output
            if result == -1: # TODO
                print(f"WARNING: |{filename}| is an invalid file name!") # TODO
                print("::: Would you like to try again?", end=" ")
                continue_action = input("::: Enter 'y' to try again.\n> ")
            else:
                print(f"Successfully stored all the tasks to |{filename}|")
            #-------------------------------------------------------------------
    elif opt == 'U':
        continue_action = 'y'
        while continue_action == 'y':
            if all_tasks == []: # TODO
                print("WARNING: There is nothing to update!")
                break
            print("::: Which task would you like to update?")
            print_tasks(all_tasks, priority_scale, name_only = True, show_idx = True, start_idx = 1)
            print("::: Enter the number corresponding to the task.")
            user_option = input("> ")
            if is_valid_index(user_option, all_tasks, 1) == True: # TODO
                user_int = int(user_option) -1 # TODO: convert the index appropriately to account for the start_idx = 1
                subopt = get_selection("update", all_tasks[user_int], to_upper = False, go_back = True)
                if subopt == 'M': # if the user changed their mind
                    break
                print(f"::: Enter a new value for the field |{subopt}|") # TODO
                field_info = input("> ")
                result = update_task(all_tasks, user_option, priority_scale, subopt, field_info, start_idx = 1)
                if type(result) == dict:
                    print(f"Successfully updated the field |{subopt}|:")  # TODO
                    print_task(result, priority_scale)  # TODO
                else: # update_task() returned an error
                    print(f"WARNING: invalid information for the field |{subopt}|!")  # TODO
                    print(f"The task was not updated.")
            else: # is_valid_index() returned False
                print(f"WARNING: |{user_option}| is an invalid task number!")  # TODO

            print("::: Would you like to update another task?", end=" ")
            continue_action = input("Enter 'y' to continue.\n> ")
            continue_action = continue_action.lower()      
            # ----------------------------------------------------------------

    # Pause before going back to the main menu
    input("::: Press Enter to continue")

print("Have a nice day!")
