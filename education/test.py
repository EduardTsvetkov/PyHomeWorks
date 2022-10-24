import my_function as my

d = my.file_to_dct("test1.txt", "utf-8", ";")
print(d)

my.dct_to_file("test_1.txt", "w", "utf-8", ";", d)