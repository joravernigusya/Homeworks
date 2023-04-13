from HW4 import (
    activity_with_var,
    positive_num,
    count_positive_num,
    days_in_year,
    day_of_week,
    body_mass,
    sum_of_numbers,
    sum_of_numbers2,
    mult_sum_count_num,
    best_swimmer,
    list_uniq_num,
    mult_nums,
    field_years,
    count_sum_num,
    gf_gs_ages,
    school_changes,
    two_lists,
    common_elements,
    uniq_elem_list,
    logical_operation,
    changing_string,
    slices_from_string,
    change_name,
    actions_string,
    string_to_array,
    greeting,
    list_to_string,
    changing_list,
    join_dict,
)

activity_with_var(10, 8.4, "No")

positive_num(10)

print(count_positive_num([2, 5, -6]))

print(days_in_year(300))

print(day_of_week(1))

body_mass(2, 1000)

print(sum_of_numbers(1, 8))

sum_of_numbers2(1, 9)

print(mult_sum_count_num(1, 2, -1, -2))

print(
    best_swimmer(
        {
            "Бекиш Александр": 21.07,
            "Будник Алексей": 20.34,
            "Гребень Анастасия": 22.12,
            "Давидович Татьяна": 30,
            "Дешук Дмитрий": 24.01,
            "Казак Анна": 28.17,
        }
    )
)

print(list_uniq_num(1, 5, 2, 9, 2, 9, 1))

print(mult_nums(5))

print(field_years(10, 11))

print(count_sum_num(12345))

gf_gs_ages(10, 1)

school_changes()

two_lists([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])

print(
    common_elements(
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    )
)

print(uniq_elem_list([1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]))

logical_operation(10, 20, "string1", "string22")

print(changing_string("wildermade"))

slices_from_string("desentigration")

print(change_name("my name is name", "Yan"))

actions_string("Hello world!")

print(string_to_array("Robin Singh", "I love arrays they are my favorite"))

greeting(["Ivan", "Ivanou"], "Belarus", "Minsk")

print(list_to_string(["I", "love", "arrays", "they", "are", "my", "favorite"]))

print(changing_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

print(join_dict({"a": 1, "b": 2, "c": 3}, {"c": 3, "d": 4, "e": 5}))
