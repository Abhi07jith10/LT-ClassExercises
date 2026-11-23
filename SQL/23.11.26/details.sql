create database Details;
use details;
create table students(id int auto_increment primary  key ,
                      name char(50) not null ,
                      age int check(age >18) not null,
                      gender enum("male","female","others") not null,
                      email char (100) unique,
                      course varchar(100) default "Django",
                      status enum("active","dropped") default "active");

show tables from details;

-- insert queries

insert into students(name,age,gender,email,course,status) values("Arun",28,"male","a@gmail,com","python","active"),
                                                                ("rahul",27,"male","r@gmail.com","python","active"),
																("anu",26,"female","anu@gmail,com","javascript","dropped"),
                                                                ("ramu",31,"male","ramu@gmail.com","python","active"),
                                                                ("sajith",27,"male","sajith@gmail.com","python","active");

select * from students;		

select name,course from students;

-- select a specific record		
select  * from students where id=8;

-- select record of students who is active

select * from students where status="active";

-- display name and age of students having active in status and python in course

select name, age  from students where status = "active" and course="python"		

-- display students name,course and status where age above 25 and gender is male

select students,name,status where age>25 and gender="male"	;

-- select all of students having age between 23 and 30	

select * from students where age between 23 and 30	

-- display name,age,email from students where course="python"	order by age asc;

select name,age,email from students where course="python" order by age asc limit 1;	    