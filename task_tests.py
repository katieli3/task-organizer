from task_functions import *

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

priority_scale = {
    1: "Lowest",
    2: "Low",
    3: "Medium",
    4: "High",
    5: "Highest"
}

 assert get_written_date(["01", "01", "1970"]) == "January 1, 1970"
assert get_written_date(["02", "03", "2000"]) == "February 3, 2000"
assert get_written_date(["10", "15", "2022"]) == "October 15, 2022"
assert get_written_date(["12", "31", "2021"]) == "December 31, 2021"

assert delete_item([], 1, 1) == 0
assert delete_item([1], '-2') == -1
assert delete_item([1, 2, 3], '2') == 3

assert is_valid_index('0', ["Quizzes", 25.5]) == True
assert is_valid_index('1', ["Quizzes", 25.5]) == True
assert is_valid_index('2', ["Quizzes", 25.5]) == False
assert is_valid_index('2', ["Quizzes", 25.5], 1) == True

assert is_valid_name('hey') == True
assert is_valid_name('no') == False
assert is_valid_name('name name name name name ') == True
assert is_valid_name('name name name name name n') == False

assert is_valid_month([12, 31, 2021]) == False
assert is_valid_day([12, 31, 2021]) == False
assert is_valid_year([12, 31, 2021]) == False

assert is_valid_month(["01", "01", "1970"]) == True
assert is_valid_month(["12", "31", "2021"]) == True
assert is_valid_day(["02", "03", "2000"]) == True
assert is_valid_day(["12", "31", "2021"]) == True
assert is_valid_year(["10", "15", "2022"]) == True
assert is_valid_year(["12", "31", "2021"]) == True

assert is_valid_month(["21", "01", "1970"]) == False
assert is_valid_month(["-2", "31", "2021"]) == False
assert is_valid_month(["March", "31", "2021"]) == False
assert is_valid_day(["02", "33", "2000"]) == False
assert is_valid_day(["02", "31", "2021"]) == False
assert is_valid_day(["02", "1st", "2021"]) == False
assert is_valid_day(["14", "1st", "2021"]) == False
assert is_valid_year(["10", "15", "22"]) == False
assert is_valid_year(["12", "31", "-21"]) == False

assert is_valid_date("1/1/1950") == True
assert is_valid_date("13/1/2000") == False
assert is_valid_date("1/32/2000") == False
assert is_valid_date("12/1/22") == False

assert is_valid_completion('yes') == True
assert is_valid_completion('no') == True
assert is_valid_completion('anything else') == False

sample_task_list = ['Book tickets', 'Verify dates', '3', '05/05/2022', 'no']
expected_result = {'name': 'Book tickets', 'info': 'Verify dates', 'priority': 3, 'duedate': '05/05/2022', 'done': 'no'}
assert get_new_task(sample_task_list , priority_scale) == expected_result

new_task_list = ["Destroy the ring", "Go to Mount Doom and throw it in", "5", "03/25/3019", "yes"]
new_task_list_fail_name = new_task_list[:]
new_task_list_fail_name[0] = 42
assert get_new_task(new_task_list_fail_name, priority_scale) == ("type", 42)
new_task_list_fail_name[0] = ("hello", "world")
assert get_new_task(new_task_list_fail_name, priority_scale) == ("type", ("hello", "world"))

new_task_list_fail_date = new_task_list[:]
new_task_list_fail_date[3] = 20
assert get_new_task(new_task_list_fail_date, priority_scale) == ("type", 20)
new_task_list_fail_date[3] = ("hello", "world")
assert get_new_task(new_task_list_fail_date, priority_scale) == ("type", ("hello", "world"))

priority_scale = {11: "The one and only"}
assert is_valid_priority('11', priority_scale) == True
assert is_valid_priority(11, priority_scale) == False

empty_list = []
assert update_task(all_tasks, '30', priority_scale, 'name', 'new_name') == -1
assert update_task(empty_list, '1', priority_scale, 'priority', 3) == 0
assert update_task(all_tasks, '2', priority_scale, 'invalid_key', 'anyinfo') == -2

assert load_tasks_from_csv('invalid', all_tasks, priority_scale) == -1
assert load_tasks_from_csv('doesntexist.csv', all_tasks, priority_scale) == None

assert save_tasks_to_csv(all_tasks, 'invalid') == -1
assert save_tasks_to_csv(all_tasks, 'combined.csv') == None
