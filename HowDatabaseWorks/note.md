# 勉強

## 6章

SQLiteを使う。

(x1...> は、SQL文がまだ続いていて、開いた ( が1個残っていることを示す継続プロンプトです。

(x1：閉じていない ( が1個
...>：続きを入力待ち
);：括弧を閉じて文を終了

Employee表を作成

```sql
CREATE TABLE Employee (
    emp_id CHAR(4) PRIMARY KEY NOT NULL,
    name VARCHAR(20) NOT NULL,
    gender CHAR(1) CHECK(gender IN ('M', 'F')),
    salary INT CHECK(salary >= 0),
    birthday DATE,
    dep_id CHAR(2)
);
```

Department表を作成

```sql
CREATE TABLE Department (
    dep_id CHAR(2) PRIMARY KEY NOT NULL,
    name VARCHAR(40) NOT NULL UNIQUE
);
```

確認

```
sqlite> .table
Department  Employee
```

Employee表に6件のレコードを登録する

```sql
INSERT INTO Employee VALUES ('E001', '日経太郎', 'M', 520000, '1974-01-01', 'D2');
INSERT INTO Employee VALUES ('E002', '出田花子', 'F', 450000, '1979-05-03', 'D1');
INSERT INTO Employee VALUES ('E003', '鈴木次郎', 'M', 380000, '1981-05-05', 'D2');
INSERT INTO Employee VALUES ('E004', '山田良子', 'F', 360000, '1993-11-03', 'D3');
INSERT INTO Employee VALUES ('E005', '田中史郎', 'M', 270000, '1996-11-23', 'D3');
INSERT INTO Employee VALUES ('E006', '佐藤春子', 'F', 250000, '1999-05-04', NULL);
```

Department表に4件のレコードを登録する

```sql
INSERT INTO Department VALUES ('D1', '総務部');
INSERT INTO Department VALUES ('D2', '経理部');
INSERT INTO Department VALUES ('D3', '営業部');
INSERT INTO Department VALUES ('D4', '技術部');
```

エラーを起こしてみる

```sql
INSERT INTO Employee VALUES ('E001', '高橋一郎', 'M', 300000, '2000-01-01', 'D1');
INSERT INTO Employee VALUES ('E007', NULL, 'M', 300000, '2000-01-01', 'D1');
INSERT INTO Department VALUES ('D5', '総務部');
INSERT INTO Employee VALUES ('E007', '高橋一郎', 'M', -100000, '2000-01-01', 'D1');
```

↑の実行結果

```
sqlite> INSERT INTO Employee VALUES ('E001', '高橋一郎', 'M', 300000, '2000-01-01', 'D1');
Runtime error: UNIQUE constraint failed: Employee.emp_id (19)
sqlite> INSERT INTO Employee VALUES ('E007', NULL, 'M', 300000, '2000-01-01', 'D1');
Runtime error: NOT NULL constraint failed: Employee.name (19)
sqlite> INSERT INTO Department VALUES ('D5', '総務部');
Runtime error: UNIQUE constraint failed: Department.name (19)
sqlite> INSERT INTO Employee VALUES ('E007', '高橋一郎', 'M', -100000, '2000-01-01', 'D1');
Runtime error: CHECK constraint failed: salary >= 0 (19)
```

19はSQLiteのエラーコード SQLITE_CONSTRAINT で、「制約に違反した」という意味。

## 7章

Employee表から全ての列を検索する

```sql
SELECT * FROM Employee;
```

実行結果

```
sqlite> SELECT * FROM Employee;
E001|日経太郎|M|520000|1974-01-01|D2
E002|出田花子|F|450000|1979-05-03|D1
E003|鈴木次郎|M|380000|1981-05-05|D2
E004|山田良子|F|360000|1993-11-03|D3
E005|田中史郎|M|270000|1996-11-23|D3
E006|佐藤春子|F|250000|1999-05-04|
```

```sql
SELECT * FROM Department;
```

実行結果

```
sqlite> SELECT * FROM Department;
D1|総務部
D2|経理部
D3|営業部
D4|技術部
```

input

```sql
SELECT name, salary FROM Employee;
```

output

```
sqlite> SELECT name, salary FROM Employee;
日経太郎|520000
出田花子|450000
鈴木次郎|380000
山田良子|360000
田中史郎|270000
佐藤春子|250000
```

input

```sql
SELECT name, gender, birthday FROM Employee;
```

output

```
sqlite> SELECT name, gender, birthday FROM Employee;
日経太郎|M|1974-01-01
出田花子|F|1979-05-03
鈴木次郎|M|1981-05-05
山田良子|F|1993-11-03
田中史郎|M|1996-11-23
佐藤春子|F|1999-05-04
```

salaryが300000以上の条件で検索

```
SELECT name, salary FROM Employee WHERE salary >= 300000;
```

output

```
sqlite> SELECT name, salary FROM Employee WHERE salary >= 300000;
日経太郎|520000
出田花子|450000
鈴木次郎|380000
山田良子|360000
```

input

```sql
SELECT name, birthday FROM Employee WHERE birthday >= '1990-01-01';
```

年代って、`1990-01-01`で比較できるんだ…
まあ、DATE型だからそういうふうに対応してるのか

output

```
sqlite> SELECT name, birthday FROM Employee WHERE birthday >= '1990-01-01';
山田良子|1993-11-03
田中史郎|1996-11-23
佐藤春子|1999-05-04
```

input

```sql
SELECT name, salary FROM Employee
WHERE salary >= 350000 AND gender = 'M';
```

output

```
sqlite> SELECT name, salary FROM Employee
   ...> WHERE salary >= 350000 AND gender = 'M';
日経太郎|520000
鈴木次郎|380000
```

input

```sql
SELECT name, gender, birthday FROM Employee
WHERE birthday >= '1990-01-01' OR gender = 'F';
```

output

```
sqlite> SELECT name, gender, birthday FROM Employee
   ...> WHERE birthday >= '1990-01-01' OR gender = 'F';
出田花子|F|1979-05-03
山田良子|F|1993-11-03
田中史郎|M|1996-11-23
佐藤春子|F|1999-05-04
```

input

```sql
SELECT name, birthday FROM Employee
WHERE birthday BETWEEN '1970-01-01' AND '1979-12-31';
```

output

```
sqlite> SELECT name, birthday FROM Employee
   ...> WHERE birthday BETWEEN '1970-01-01' AND '1979-12-31';
日経太郎|1974-01-01
出田花子|1979-05-03
```

input

```sql
SELECT name, salary FROM Employee
WHERE salary BETWEEN 300000 AND 399999;
```

output

```
sqlite> SELECT name, salary FROM Employee
   ...> WHERE salary BETWEEN 300000 AND 399999;
鈴木次郎|380000
山田良子|360000
```

input

```sql
SELECT name FROM Employee WHERE name LIKE '%田%';
```

output

```
sqlite> SELECT name FROM Employee WHERE name LIKE '%田%';
出田花子
山田良子
田中史郎
```

input

```sql
SELECT name FROM Employee WHERE name LIKE '_田%';
```

output

```
sqlite> SELECT name FROM Employee WHERE name LIKE '_田%';
出田花子
山田良
```

input

```sql
SELECT DISTINCT dep_id FROM Employee;
```

output

```
sqlite> SELECT DISTINCT dep_id FROM Employee;
D2
D1
D3

```

input

```sql
SELECT DISTINCT gender FROM Employee;
```

output

```
sqlite> SELECT DISTINCT gender FROM Employee;
M
F
```

input

```sql
SELECT name, salary FROM Employee ORDER BY salary DESC;
```

output

```
sqlite> SELECT name, salary FROM Employee ORDER BY salary DESC;
日経太郎|520000
出田花子|450000
鈴木次郎|380000
山田良子|360000
田中史郎|270000
佐藤春子|250000
```

input

```sql
SELECT name, birthday FROM Employee ORDER BY birthday ASC;
```

output

```
sqlite> SELECT name, birthday FROM Employee ORDER BY birthday ASC;
日経太郎|1974-01-01
出田花子|1979-05-03
鈴木次郎|1981-05-05
山田良子|1993-11-03
田中史郎|1996-11-23
佐藤春子|1999-05-04
```

input

```sql
SELECT name, salary FROM Employee ORDER BY salary DESC LIMIT 0, 3;
```

output

```
sqlite> SELECT name, salary FROM Employee ORDER BY salary DESC LIMIT 0, 3;
日経太郎|520000
出田花子|450000
鈴木次郎|380000
```

input

```sql
SELECT name, salary FROM Employee ORDER BY salary DESC LIMIT 3, 3;
```

output

```
sqlite> SELECT name, salary FROM Employee ORDER BY salary DESC LIMIT 3, 3;
山田良子|360000
田中史郎|270000
佐藤春子|250000
```

## 8章

input

```
SELECT Employee.name, Department.name FROM Employee, Department WHERE Employee.dep_id = Department.dep_id;
```

input

```
SELECT Department.name, Employee.name, Employee.salary FROM Employee, Department WHERE Employee.dep_id = Department.dep_id ORDER BY Department.dep_id DESC;
```

input

```
SELECT Employee.name, Department.name FROM Employee INNER JOIN Department ON Employee.dep_id = Department.dep_id;
```

input

```
SELECT Department.name, Employee.name, Employee.salary FROM Employee INNER JOIN Department ON Employee.dep_id = Department.dep_id ORDER BY Department.dep_id DESC;
```

input

```
SELECT Employee.name, Department.name FROM Employee LEFT OUTER JOIN Department ON Employee.dep_id = Department.dep_id;
```

```
SELECT Employee.name, Department.name FROM Employee RIGHT OUTER JOIN Department ON Employee.dep_id = Department.dep_id;
```

```
SELECT Employee.name, Department.name FROM Department LEFT OUTER JOIN Employee ON Employee.dep_id = Department.dep_id;
```

```
SELECT SUM(salary), AVG(salary), MAX(salary), MIN(salary) FROM Employee;
```

```
SELECT MIN(birthday), MAX(birthday) FROM Employee;
```

```
SELECT COUNT(*) FROM Employee;
```

```
SELECT COUNT(dep_id) FROM Employee;
```

```
SELECT gender, AVG(salary) FROM Employee GROUP BY gender;
```

```
SELECT dep_id, MAX(birthday) FROM Employee GROUP BY dep_id;
```

```
SELECT dep_id, COUNT(dep_id) FROM Employee GROUP BY dep_id HAVING COUNT(*) >= 2;
```

```
SELECT dep_id, MIN(birthday) FROM Employee GROUP BY dep_id HAVING MAX(birthday) >= '1990-01-01';
```

## 9章

```
SELECT name, salary FROM Employee WHERE salary >= (SELECT AVG(salary) FROM Employee);
```

```
SELECT name, birthday FROM Employee WHERE birthday == (SELECT MAX(birthday) FROM Employee);
```

```
SELECT name FROM Department WHERE dep_id IN (SELECT dep_id FROM Employee WHERE salary >= 400000);
```

```
SELECT name FROM Department WHERE dep_id NOT IN (SELECT dep_id FROM Employee WHERE salary >= 400000);
```

```
SELECT gender, name, salary FROM Employee AS E1 WHERE salary = (SELECT MAX(salary) FROM Employee AS E2 WHERE E1.gender = E2.gender);
```

```
SELECT gender, name, salary FROM Employee AS E1 WHERE salary < (SELECT AVG(salary) FROM Employee AS E2 WHERE E1.gender = E2.gender);
```

```
CREATE VIEW MaleEmployee AS SELECT * FROM Employee WHERE gender = 'M';
```

```
CREATE VIEW PublicEmployee AS SELECT emp_id, name, gender, birthday, dep_id FROM Employee;
```

```
SELECT name, salary FROM MaleEmployee WHERE salary >= 300000;
```

```
SELECT name, gender FROM PublicEmployee WHERE dep_id == 'D3';
```

```
DROP VIEW MaleEmployee;
```

```
DROP VIEW PublicEmployee;
```

## 10章

```
UPDATE Employee SET salary = 400000 WHERE emp_id = 'E003';
```

```
SELECT salary FROM Employee WHERE emp_id = 'E003';
```

```
UPDATE Employee SET dep_id = 'D1' WHERE dep_id is NULL;
```

```
SELECT * FROM Employee;
```

```
UPDATE Employee SET salary = salary * 1.1;
```

```
UPDATE Employee SET salary = salary + 10000;
```

```
UPDATE Employee SET salary = (SELECT AVG(salary) FROM Employee) WHERE emp_id = 'E003';
```

```
SELECT salary FROM Employee WHERE emp_id = 'E003';
```

```
UPDATE Employee SET salary = (SELECT MIN(salary) FROM Employee) + 10000 WHERE salary = (SELECT MIN(salary) FROM Employee);
```

↑でも動くが、↓のほうが美しい。

```
UPDATE Employee SET salary = salary + 10000 WHERE salary = (SELECT MIN(salary) FROM Employee);
```

```
DELETE FROM Employee WHERE emp_id = 'E001';
```

```
DELETE FROM Employee WHERE gender = 'M';
```

```
DELETE FROM Employee;
```

```sql
INSERT INTO Employee VALUES ('E001', '日経太郎', 'M', 520000, '1974-01-01', 'D2');
INSERT INTO Employee VALUES ('E002', '出田花子', 'F', 450000, '1979-05-03', 'D1');
INSERT INTO Employee VALUES ('E003', '鈴木次郎', 'M', 380000, '1981-05-05', 'D2');
INSERT INTO Employee VALUES ('E004', '山田良子', 'F', 360000, '1993-11-03', 'D3');
INSERT INTO Employee VALUES ('E005', '田中史郎', 'M', 270000, '1996-11-23', 'D3');
INSERT INTO Employee VALUES ('E006', '佐藤春子', 'F', 250000, '1999-05-04', NULL);
```

登録し直す

```
CREATE INDEX emp_id_index ON Employee(emp_id);
```

```
.indices
```

```
CREATE INDEX name_index ON Employee(name);
```

```
DROP INDEX emp_id_index;
```

```
DROP INDEX name_index;
```

```
BEGIN TRANSACTION;
UPDATE Employee SET salary = salary - 10000 WHERE emp_id = 'E001';
UPDATE Employee SET salary = salary + 10000 WHERE emp_id = 'E002';
COMMIT TRANSACTION;
```

```
SELECT * FROM Employee WHERE emp_id IN ('E001', 'E002');
```

```
BEGIN TRANSACTION;
UPDATE Employee SET dep_id = 'D1' WHERE emp_id = 'E001';
UPDATE Employee SET dep_id = 'D2' WHERE emp_id = 'E002';
COMMIT TRANSACTION;
```

```
BEGIN TRANSACTION;
DELETE FROM Department;
ROLLBACK TRANSACTION;
```

```
SELECT * FROM Department;
```

```
BEGIN TRANSACTION;
DELETE FROM Employee;
ROLLBACK TRANSACTION;
```

```
SELECT * FROM Employee;
```
