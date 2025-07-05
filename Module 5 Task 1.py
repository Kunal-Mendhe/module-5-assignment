try:
    file_name = open("sample.txt", "r")
    print("Reading file content:")
    lines = file_name.readlines()
    for i, line in enumerate(lines, start=1):
        print(f"Line {i}: {line.strip()}")
    file_name.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")