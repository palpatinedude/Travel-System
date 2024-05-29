use odyssey;

select * from review;
select * from response;
select * from membership;
select * from user;
select * from ChatMessage;
select * from Friendrequest;
-- SELECT * FROM Beneficiary;
select * from review;
SELECT * FROM Beneficiary;
select * from friendrequest;

SELECT u.username FROM FriendRequest fr JOIN User u ON fr.user2_id = u.user_id WHERE fr.user1_id = '4' AND fr.status = 'accepted';
    
select * from chatmessage;
select * from business;

SELECT business_id FROM Business WHERE business_name = 'Smith Bakery';



SELECT 'mysql' dbms,t.TABLE_SCHEMA,t.TABLE_NAME,c.COLUMN_NAME,c.ORDINAL_POSITION,c.DATA_TYPE,c.CHARACTER_MAXIMUM_LENGTH,n.CONSTRAINT_TYPE,k.REFERENCED_TABLE_SCHEMA,k.REFERENCED_TABLE_NAME,k.REFERENCED_COLUMN_NAME FROM INFORMATION_SCHEMA.TABLES t LEFT JOIN INFORMATION_SCHEMA.COLUMNS c ON t.TABLE_SCHEMA=c.TABLE_SCHEMA AND t.TABLE_NAME=c.TABLE_NAME LEFT JOIN INFORMATION_SCHEMA.KEY_COLUMN_USAGE k ON c.TABLE_SCHEMA=k.TABLE_SCHEMA AND c.TABLE_NAME=k.TABLE_NAME AND c.COLUMN_NAME=k.COLUMN_NAME LEFT JOIN INFORMATION_SCHEMA.TABLE_CONSTRAINTS n ON k.CONSTRAINT_SCHEMA=n.CONSTRAINT_SCHEMA AND k.CONSTRAINT_NAME=n.CONSTRAINT_NAME AND k.TABLE_SCHEMA=n.TABLE_SCHEMA AND k.TABLE_NAME=n.TABLE_NAME WHERE t.TABLE_TYPE='BASE TABLE' AND t.TABLE_SCHEMA NOT IN('INFORMATION_SCHEMA','mysql','performance_schema');