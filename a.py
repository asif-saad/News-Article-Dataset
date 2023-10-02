from datasets.dataset_dict import DatasetDict
from datasets import Dataset
import jsonlines

x=[1,0,6,47,3]
y=[9,8,7,6,5]
d={'train':Dataset.from_dict({'x_train':x,'y_train':y})}
raw_datasets=DatasetDict(d)




with jsonlines.open("raw_datasets.jsonl", "a") as writer:
    writer.write({'x_train':2,'y_train':3})
    # for dataset_name, dataset in raw_datasets.items():
    #     for example in dataset:
    #         writer.write({
    #             **example
    #         })





