CREATE TABLE EmployeeDemographics
(EmployeeID int,
FirstName varchar(50),
LastName varchar (50),
Age int,
Gender varchar (50),
HomeOffice varchar (50)
)

CREATE TABLE EmployeeSalary
(EmployeeID int,
JobTitle varchar (50),
Salary int
)

INSERT INTO EmployeeDemographics VALUES
(1001, 'Michael' , 'Scott' , 50 , 'Male' , 'Scranton'),
(1002, 'Robert' , 'Parr' , 45 , 'Male' , 'Metro City'),
(1003, 'Jim' , 'Halpert' , 30 , 'Male' , 'Scranton'),
(1004, 'Pam' , 'Beasley' , 28 , 'Female' , 'Scranton'),
(1005, 'Wanda' , 'Maximoff' , 27 , 'Female' , 'Sokovia'),
(1006, 'Bruce' , 'Banner' , 44 , 'Male' , 'Albuquerque'),
(1007, 'Peter' , 'Griffin' , 43 , 'Male' , 'Quahog'),
(1008, 'Diana' , 'Prince' , 36 , 'Female' , 'Themyscira'),
(1009, 'Harry' , 'Potter' , 21 , 'Male' , 'London')

INSERT INTO EmployeeSalary VALUES
(1001, 'Regional Manager' , 88000),
(1002, 'Assistant Regional Manager' , 75000),
(1003, 'Salesman' , 45000),
(1004, 'Receptionist' , 38000),
(1005, 'HR Lead' , 55000),
(1006, 'Security Officer' , 48000),
(1007, 'Accountant' , 53500),
(1008, 'Supplier Relations' , 64000),
(1009, 'Mailroom Attendant' , 36000)