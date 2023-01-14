import pandas as pd

columns = ["name", "info"]

records = [
    ["normal text", "Student"],
    ["a comma", "Prof. at USA, and UK"],
    ["one double quote", 'Traveller from "A to B'],
    ["double-quoted text", 'Traveller from "A to B"'],
    ["one single quote", "Traveller from 'A to B"],
    ["single-quoted text", "Traveller from 'A to B'"],
    ["double-quoted text and comma", 'I am actually, testing "pandas, ability"']
]

df = pd.DataFrame(records, columns=columns)

print(df)

# You will see the following output in CSV
# name,info
# normal text,Student
# a comma,"Prof. at USA, and UK"
# one double quote,"Traveller from ""A to B"
# double-quoted text,"Traveller from ""A to B"""
# one single quote,Traveller from 'A to B
# single-quoted text,Traveller from 'A to B'
# double-quoted text and comma,"I am actually, testing ""pandas, ability"""
with open("valid_csv.csv", "w") as f:
    df.to_csv(f, index=False)
