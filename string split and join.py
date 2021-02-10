def split_and_join(line):
    # write your code here
    line = line.split()
    line = '-'.join(line)
    return line

line = input("Enter sentence: ")
result = split_and_join(line)
print(result)
