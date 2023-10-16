file_path='C:/Users/asifs/OneDrive/Desktop/News-Article-Dataset/test.py'
while True:
    with open(file_path,'r') as file:
        python_code=file.read()
        exec(python_code)
        print("ok, done")