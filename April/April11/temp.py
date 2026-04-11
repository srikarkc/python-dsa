lists = [[1,2,4],[1,3,5],[3,6]]
output_list = []

for l in lists:
    for i in l:
        output_list.append(i)

print(sorted(output_list))