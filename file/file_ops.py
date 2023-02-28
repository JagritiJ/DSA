

def read_ops():

    # f = open("small.txt", "r")
    # print(f.read())
    # print("Notice the difference between the two")
    # f.close()
    with open("small.txt", "r") as f:
        # print(f.read())
        # print(f.readline())
        # print(f.readlines())

        mylist = f.readlines()
        print(mylist)

    mylist.sort()
    print(mylist)

    file1 = open('small.txt', 'r')
    count =0
    while True:
        count +=1
#         Get the next line
        line = file1.readline()
#         break if eof or line is empty
        if not line:
            break
        print(count, line.strip())

def write_append_ops():

    # with open("small.txt", "w") as f:
    #     f.write("Using the write operation")

    with open("small.txt", "a") as f:
        f.write("Using the write operation, this time using the append operation")

def read_write_ops():

    # with open("small.txt", "w") as f:
    #     f.write("Using the write operation")

    with open("small.txt", "r+") as f:

        f.write("Using the write operation, this time using the append operation")
        print(f.readline())

def main():

    # read_ops()
    # write_append_ops()
    read_write_ops()

main()

'''
f.read() - This is a small file created for working with file operations in Python.
Run multiple experiments

f.readline() - This is a small file created for working with file operations in Python.

f.readlines() - ['This is a small file created for working with file operations in Python.\n', 'Run multiple experiments']

For large log files - never go for read() or readlines()

with open("small.txt", "w") as f:
f.write("Using the write operation") -- overwrites the file



'''