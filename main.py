# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def collection_testing():
    # figure lists
    # allow duplicates, allows different types, modifiable, ordered
    student_list = ["s1","s2","s3"]
    nsn_list_10 = [1234, 12457,45654, 243657,756, 2348]
    # figure out how to print the lists
    print(student_list)
    print(type(student_list))

    # tuples in python
    # ordered, unchangeable - cannot add new items, allow duplicates
    thistuple = ("apple", "banana", "cherry", "apple", "cherry")
    print(thistuple)



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    collection_testing()
