select * from review;
select * from response;
select * from membership;
select * from user;
select * from ChatMessage;
select * from Friendrequest;
SELECT * FROM Beneficiary;

-- INSERT IGNORE INTO Beneficiary (user_id, beneficiary_type, date_of_birth, address, contact_number, location_id)
-- VALUES 
-- (1, 'user', '1985-05-15', '123 Main St', '123-456-7890', 1),
-- (4, 'user', '1985-05-15', '123 Main St', '123-456-7890', 1),
-- (5, 'user', '1985-05-15', '123 Main St', '123-456-7890', 1),
-- (6, 'user', '1985-05-15', '123 Main St', '123-456-7890', 1),
-- (7, 'user', '1985-05-15', '123 Main St', '123-456-7890', 1),
-- (2, 'service_provider', '1990-08-25', '456 Elm St', '987-654-3210', 2);