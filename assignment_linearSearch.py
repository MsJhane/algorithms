def LinearSearch(Dataset,keyword):
    for Data in Dataset:
        if(Data.lower()== keyword.lower()):
            return True
    return False

sentence="I lost my ball"
words=sentence.split(" ")
print(words)
result=LinearSearch(words,"ball")
print(result)
