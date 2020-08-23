*** Settings ***

Library  SeleniumLibrary
Library  DatabaseLibrary
Library  OperatingSystem

Suite Setup     Connect To Database     pymysql     ${DBName}   ${DBUser}   ${DBPass}   ${DBHost}   ${DBPort}
Suite Teardown  Disconnect From Database

*** Variables ***

${DBName}   mydb
${DBUser}   root
${DBPass}   root
${DBHost}   127.0.0.1
${DBPort}   3306

*** Test Cases ***
Create person table
    ${output}=  execute sql string  Create table person(id integer,first_name varchar(20),last_name varchar(20))
    log to console  ${output}
    #The output should return None and we verify the same in below step
    should be equal as strings  ${output}   None

Insert data to person table
    #This will insert only one record
    ${output}=  execute sql string  Insert into person values(101,"Sandeep","Parihar");
    log to console  ${output}
    should be equal as strings  ${output}   None

Insert multiple records to person table from .sql file
    ${output}=  execute sql script  TestData/mydb_person_insertdata.sql
    log to console  ${output}
    should be equal as strings  ${output}   None

Check if record exist in DB
    check if exists in database  select * from mydb.person where first_name='Sandeep';

Check if record doesn't exist in DB
    check if not exists in database  select * from mydb.person where first_name='Rahul';

Check if table exist in DB
    table must exist  person;

Verify Row count is zero
    row count is 0  select * from mydb.person where first_name='Rahul';

Verify Row count is equal to some value
    row count is equal to x  select * from mydb.person where first_name is not NULL;    5

Verify Row count is greater than some value
    row count is greater than x  select * from mydb.person where first_name is not NULL;    2

Verify Row count is less than some value
    row count is less than x  select * from mydb.person where first_name is not NULL;    6

Update a record in person table
    ${output}=  execute sql string  update person set id=108 where first_name='Lewis'
    log to console  ${output}
    should be equal as strings  ${output}   None

Retrieve all records from person table
    @{queryResults}=    query  select * from mydb.person;
    #To print all the values from list use many keyword
    log to console  many  @{queryResults}

Delete records from person table
    ${output}=  execute sql string  delete from mydb.person;
    log to console  ${output}
    should be equal as strings  ${output}   None

*** Keywords ***

