#!/usr/bin/python3
def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text after each line containing a specific string"""
    with open(filename, 'r') as file:
        temp_filename = filename + '.tmp'
        with open(temp_filename, 'w') as temp_file:
            for line in file:
                temp_file.write(line)
                if search_string in line:
                    temp_file.write(new_string)

    os.replace(temp_filename, filename)
