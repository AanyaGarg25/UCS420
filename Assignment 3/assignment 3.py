import pandas as pd
import numpy as np


# Q1

data = {
    "Name": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
    "Age": [20, 21, 22, 23, 24, 25, 26, 27, 28],
    "Marks": [85, 90, 78, 88, 95, 76, 89, 92, 81],
    "Grade": ["A", "A+", "B", "A", "A+", "B", "A", "A+", "B"]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# Q2

print("\nRows 0, 4, 7 and 8:")
print(df.loc[[0, 4, 7, 8]])


# Q3(a)

print("\nRows from index 3 to 7:")
print(df.loc[3:7])


# Q3(b)

print("\nRows from index 4 to 8 and columns 2 to 4:")
print(df.iloc[4:9, 2:5])


# Q3(c)

print("\nAll rows with column index 1 to 3:")
print(df.iloc[:, 1:4])


# Q4

iris_df = pd.read_csv("iris.csv")

print("\nFirst five rows of Iris dataset:")
print(iris_df.head())


# Q5

iris_modified = iris_df.drop(index=4)
iris_modified = iris_modified.drop(iris_modified.columns[3], axis=1)

print("\nIris dataset after deleting row 4 and column 3:")
print(iris_modified)


# Q6

employees_df = pd.read_csv("employees.csv")

print("\nEmployees dataset:")
print(employees_df)


# Q6(a)

print("\nShape of the DataFrame:")
print(employees_df.shape)


# Q6(b)

print("\nSummary of the DataFrame:")
employees_df.info()


# Q6(c)

print("\nDescriptive statistics:")
print(employees_df.describe())


# Q6(d)

print("\nFirst five rows:")
print(employees_df.head(5))

print("\nLast three rows:")
print(employees_df.tail(3))


# Q6(e)(i)

average_salary = employees_df["Salary"].mean()

print("\nAverage salary of employees:", average_salary)


# Q6(e)(ii)

total_bonus = employees_df["Bonus"].sum()

print("Total bonus paid to all employees:", total_bonus)


# Q6(e)(iii)

youngest_age = employees_df["Age"].min()

print("Youngest employee's age:", youngest_age)


# Q6(e)(iv)

highest_rating = employees_df["Rating"].max()

print("Highest performance rating:", highest_rating)


# Q6(f)

sorted_employees = employees_df.sort_values(
    by="Salary",
    ascending=False
)

print("\nEmployees sorted by salary in descending order:")
print(sorted_employees)


# Q6(g)

employees_df["Performance_Category"] = np.where(
    employees_df["Rating"] >= 4.5,
    "Excellent",
    np.where(
        employees_df["Rating"] >= 4.0,
        "Good",
        "Average"
    )
)

print("\nEmployees with performance category:")
print(employees_df)


# Q6(h)

print("\nMissing values in the DataFrame:")
print(employees_df.isnull().sum())


# Q6(i)

employees_df = employees_df.rename(
    columns={"Employee_ID": "ID"}
)

print("\nDataFrame after renaming Employee_ID to ID:")
print(employees_df)


# Q6(j)(i)

experienced_employees = employees_df[
    employees_df["Years_of_Experience"] > 5
]

print("\nEmployees having more than 5 years of experience:")
print(experienced_employees)


# Q6(j)(ii)

IT_employees = employees_df[
    employees_df["Department"] == "IT"
]

print("\nEmployees belonging to the IT department:")
print(IT_employees)


# Q6(k)

employees_df["Tax"] = employees_df["Salary"] * 0.10

print("\nDataFrame after adding Tax column:")
print(employees_df)


# Q6(l)

employees_df.to_csv(
    "employees_modified.csv",
    index=False
)

print("\nModified employee dataset saved as employees_modified.csv")
