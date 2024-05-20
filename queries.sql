select * from review;
select * from response;
select * from membership;
select * from user;
select * from ChatMessage;
select * from Friendrequest;
-- SELECT * FROM Beneficiary;

INSERT IGNORE INTO Beneficiary (user_id, beneficiary_type, date_of_birth, address, contact_number, location_id)
VALUES 
(4, 'user', '1980-10-15', '122 Main St', '123-456-7854', 1),
(5, 'user', '1990-09-18', '125 Main St', '123-456-7823', 1),
(6, 'user', '2000-02-19', '15 Main St', '123-456-7843', 1),
(7, 'user', '1981-07-14', '153 Main St', '123-456-7853', 1);

SELECT * FROM Beneficiary;