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