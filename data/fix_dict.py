file_path = 'american.txt'
with open(file_path, 'r') as file:
    lines = file.readlines()

# each line to remove text after '/' and filter out empty lines
processed_lines = [line.split('/')[0].strip() + '\n' for line in lines if line.split('/')[0].strip()]

with open(file_path, 'w') as file:
    file.writelines(processed_lines)
