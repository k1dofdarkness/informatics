def main():
    input_file = open('timetable.yml', 'r', encoding = "utf-8")

    newline = input_file.readline()

    data = []
    lines = 0
    helpstring = []

    while newline:
        data.append(newline)
        lines += 1
        newline = input_file.readline()
    
    input_file.close()

    k1 = len(data[0]) - len(data[0].lstrip())

    output_file = open('timetable.json','w', encoding = "utf-8")
    output_file.write("{\n")

    for i in range(0, lines - 1):
    
        helpstring = data[i].lstrip().split(':', maxsplit = 1)
        output_file.write(' "' + helpstring[0] + '":' + helpstring[1].lstrip())
    
        k2 = len(data[i + 1]) - len(data[i + 1].lstrip())
    
        if k2 < k1:
            output_file.write("  },"'\n')
        if k2 > k1:
            output_file.write(" {"'\n')
        
        k1 = k2
    
    output_file.write('  }\n  }\n}')
    output_file.close()
main()
