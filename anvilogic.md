# Anvilogic SIEM Query Tutorial and Cheatsheet

## Basic Query Syntax

### Selecting Data

Use the `search` statement to select data from logs.

```cmd
search *
```

### Filtering Data

Use the `where` clause to filter records.

```cmd
search * | where condition
```

## Advanced Query Techniques

### Aggregations

Use aggregate functions to summarize data.

```cmd
search * | stats count() by field
```

## Common Use Cases

### Searching for Specific Events

```cmd
search * | where event_type == "login" and username == "john.doe"
```

### Identifying Failed Login Attempts

```cmd
search * | where event_type == "failed_login" | stats count() by username | where count > 5
```

### Analyzing Traffic by Source IP

```cmd
search * | stats count() by source_ip | sort count desc
```

### Detecting Large Data Transfers

```cmd
search * | stats sum(data_transferred) by source_ip, destination_ip | where sum > 1000000
```

# Tips and Best Practices

1. Use Efficient Filters: Apply filters early in your query to reduce the amount of data processed.
2. Aggregate Data: Use aggregation functions to summarize and gain insights from large datasets.
3. Test Queries: Test queries on smaller datasets to ensure accuracy and performance.
4. Document Queries: Add comments to complex queries for better understanding and maintenance.

```cmd
// This query retrieves the top 10 source IPs with the most traffic
search * | stats count() by source_ip | sort count desc | limit 10
```


# Anvilogic SIEM Query Tutorial and Cheatsheet

## Introduction

Anvilogic SIEM (Security Information and Event Management) provides powerful querying capabilities to analyze and respond to security events. This tutorial and cheatsheet will guide you through the basics and advanced features of Anvilogic SIEM queries.

## Basic Query Syntax

### Select Statement

The `SELECT` statement is used to select data from one or more tables.

```sql
SELECT column1, column2, ...
FROM table_name;
```

### Filtering Data

Use the `WHERE` clause to filter records.

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

### Sorting Data

Use the `ORDER BY` clause to sort the result set.

```sql
SELECT column1, column2, ...
FROM table_name
ORDER BY column1, column2, ... ASC|DESC;
```

### Limiting Data
Use the `LIMIT` clause to specify the number of records to return.

```sql
SELECT column1, column2, ...
FROM table_name
LIMIT number;
```

## Advanced Query Techniques

### Joins

Combine rows from two or more tables based on a related column.

#### Inner Join

```sql
SELECT columns
FROM table1
INNER JOIN table2
ON table1.common_column = table2.common_column;
```

#### Left Join

```sql
SELECT columns
FROM table1
LEFT JOIN table2
ON table1.common_column = table2.common_column;
```

### Aggregations

Use aggregate functions to summarize data.

#### Count

```sql
SELECT COUNT(column)
FROM table_name
WHERE condition;
```

#### Sum

```sql
SELECT SUM(column)
FROM table_name
WHERE condition;
```

#### Average

```sql
SELECT AVG(column)
FROM table_name
WHERE condition;
```

#### Min and Max

```sql
SELECT MIN(column), MAX(column)
FROM table_name
WHERE condition;
```

### Group By

Group rows that have the same values into summary rows.

```sql
SELECT column1, COUNT(column2)
FROM table_name
GROUP BY column1;
```

### Having

Use the `HAVING` clause to filter groups.

```sql
SELECT column1, COUNT(column2)
FROM table_name
GROUP BY column1
HAVING COUNT(column2) > number;
```

## Common Use Cases

### Searching for Specific Events

```sql
SELECT *
FROM events
WHERE event_type = 'login' AND username = 'john.doe';
```

### Identifying Failed Login Attempts

```sql
SELECT username, COUNT(*)
FROM events
WHERE event_type = 'failed_login'
GROUP BY username
HAVING COUNT(*) > 5;
```

### Analyzing Traffic by Source IP

```sql
SELECT source_ip, COUNT(*)
FROM network_traffic
GROUP BY source_ip
ORDER BY COUNT(*) DESC;
```

### Detecting Large Data Transfers

```sql
SELECT source_ip, destination_ip, SUM(data_transferred)
FROM network_traffic
GROUP BY source_ip, destination_ip
HAVING SUM(data_transferred) > 1000000;
```

# Tips and Best Practices

1. Index Your Data: Index commonly queried columns to speed up query performance.
2. Use Aliases: Use aliases for table and column names to make queries more readable.
3. *Avoid Select : Specify the columns you need to reduce the amount of data processed.*
4. Test Queries: Always test queries on a small dataset before running them on large datasets.
5. Use Comments: Add comments to complex queries for better understanding and maintenance.

```sql
-- This query retrieves the top 10 source IPs with the most traffic
SELECT source_ip, COUNT(*)
FROM network_traffic
GROUP BY source_ip
ORDER BY COUNT(*) DESC
LIMIT 10;
```






