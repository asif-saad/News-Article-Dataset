import json

data_list = []

with open('C:/Users/asifs/OneDrive/Desktop/dataset/ittefaq.jsonl', "r",encoding='utf-8') as file:
    for line in file:
        # Load each line as a JSON object
        data = json.loads(line)
        data_list.append(data)
        print(len(data_list))

# Now, data_list contains all the JSON objects from the JSONL file
