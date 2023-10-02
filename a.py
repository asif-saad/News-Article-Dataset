from datasets.dataset_dict import DatasetDict
from datasets import Dataset
import jsonlines
# d = {'train':Dataset.from_dict({'labels':y_train,'review':X_train}),'validation':Dataset.from_dict({'labels':y_test,'review':X_test})}
# raw_datasets=DatasetDict(d)
# print(raw_datasets)
x=[1,0,6,47,3]
y=[9,8,7,6,5]
d={'train':Dataset.from_dict({'x_train':x,'y_train':y})}
raw_datasets=DatasetDict(d)




with jsonlines.open("raw_datasets.jsonl", "a") as writer:
    for dataset_name, dataset in raw_datasets.items():
        for example in dataset:
            writer.write({
                **example
            })


