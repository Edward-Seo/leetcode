SELECT a.name AS Employee
FROM Employee AS a, Employee AS b
WHERE a.salary > b.salary AND a.managerId=b.id
