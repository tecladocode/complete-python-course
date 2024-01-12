---
group: Intermediate
hidden: true
---
# Working with Files in Python

In this section we build a project that stores data in two types of file: CSV and JSON.

CSV files are similar to tables. Below is a CSV file that represents 3 columns. It has 1 row with the column headers, and 4 rows of data.

```
name,title,salary
Bob,Software Engineer,35000
Anne,Software Engineer II,67000
Jen,Manager,52000
Chris,Technical Analyst,55000
```

JSON allows us to store key-value pairs inside **objects** and multiple values inside **lists**. Other than that, it supports native values such as strings, numbers, booleans, or `null`.

Here's an example of a JSON file that stores the same data as the CSV file above:

```json
{
    "employees": [
        {
            "name": "Bob",
            "title": "Software Engineer",
            "salary": 35000
        },
        {
            "name": "Anne",
            "title": "Software Engineer II",
            "salary": 67000
        },
        {
            "name": "Jen",
            "title": "Manager",
            "salary": 52000
        },
        {
            "name": "Chris",
            "title": "Technical Analyst",
            "salary": 55000
        }
    ]
}
```

Depending on what type of data you want to store, one file or another may be more suitable. JSON is more flexible, but can be more verbose.