create database ClassicModels;

use ClassicModels;

CREATE TABLE CustomerInfo
(BookName varchar(50),
PurchaseDate date,
Amount int(50),
Location varchar(50)
);

INSERT INTO CustomerInfo values("Selenium",current_date(),350,'Africa');
INSERT INTO CustomerInfo values("Java",current_date(),200,'Asia');
INSERT INTO CustomerInfo values("Python",current_date(),250,'Australia');
INSERT INTO CustomerInfo values("JMeter",current_date(),150,'Europe');
INSERT INTO CustomerInfo values("C#",current_date(),300,'Americas');

select * from CustomerInfo where PurchaseDate=curdate()