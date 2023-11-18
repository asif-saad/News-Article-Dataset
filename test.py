# import json

# data_list = []

# with open('C:/Users/asifs/OneDrive/Desktop/dataset/ittefaq.jsonl', "r",encoding='utf-8') as file:
#     for line in file:
#         # Load each line as a JSON object
#         data = json.loads(line)
#         data_list.append(data)
#         print(len(data_list))

# # Now, data_list contains all the JSON objects from the JSONL file

with open('output1.txt','r') as file1:
    data1=file1.read()

with open('output2.txt','r') as file2:
    data2=file2.read()

with open('output.txt','w') as file:
    file.write(data1)
    # file.write('\n')
    file.write(data2)
    # file.write('\n')
