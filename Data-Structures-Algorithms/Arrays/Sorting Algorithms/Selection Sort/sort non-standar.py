"""
Suppose you have a list of tuples where each tuple contains a student's name and their grade. Your task is to sort the list based on the grades in ascending order. If two students have the same grade, they should be sorted by their names in alphabetical order.

students = [("Alice", 88), ("Bob", 75), ("Charlie", 88), ("David", 75)]
# Sort this list using Selection Sort first by grade, then by name if grades are equal.

"""


example = [("Alice", 88), ("Bob", 75), ("Charlie", 88), ("David", 75)]

example[1][0] > example[2][0]
def selection_sort(students):
    for i in range(len(students)):
        min_index = i
        for j in range(i+1,len(students)):
            if students[j][1] < students[min_index][1]:
                min_index = j
            elif students[j][1] == students[min_index][1] and students[j][0] < students[min_index][0]:
                min_index = j

        if min_index != i:
            students[min_index], students[i] = students[i], students[min_index]
    return students
selection_sort(example)