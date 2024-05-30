-- USE odyssey;

-- -- Insert data into Country table
-- INSERT IGNORE INTO Country (country_name, continent, currency)
-- VALUES 
-- ('USA', 'North America', 'USD'),
-- ('Canada', 'North America', 'CAD'),
-- ('France', 'Europe', 'EUR'),
-- ('Germany', 'Europe', 'EUR'),
-- ('Australia', 'Oceania', 'AUD'),
-- ('Japan', 'Asia', 'JPY'),
-- ('Brazil', 'South America', 'BRL'),
-- ('South Africa', 'Africa', 'ZAR'),
-- ('India', 'Asia', 'INR'),
-- ('China', 'Asia', 'CNY'),
-- ('United Kingdom', 'Europe', 'GBP'),
-- ('Italy', 'Europe', 'EUR'),
-- ('Mexico', 'North America', 'MXN'),
-- ('Russia', 'Europe', 'RUB'),
-- ('South Korea', 'Asia', 'KRW');

-- -- Insert data into City table
-- INSERT IGNORE INTO City (city_name, country_id, latitude, longitude)
-- VALUES
-- ('New York', 1, 40.712776, -74.005974),
-- ('Toronto', 2, 43.651070, -79.347015),
-- ('Paris', 3, 48.856613, 2.352222),
-- ('Berlin', 4, 52.520008, 13.404954),
-- ('Sydney', 5, -33.868820, 151.209290),
-- ('Tokyo', 6, 35.689487, 139.691711),
-- ('Rio de Janeiro', 7, -22.906847, -43.172897),
-- ('Cape Town', 8, -33.924870, 18.424055),
-- ('Mumbai', 9, 19.076090, 72.877426),
-- ('Beijing', 10, 39.904202, 116.407394),
-- ('London', 11, 51.507351, -0.127758),
-- ('Rome', 12, 41.902782, 12.496366),
-- ('Mexico City', 13, 19.432608, -99.133209),
-- ('Moscow', 14, 55.755825, 37.617298),
-- ('Seoul', 15, 37.566536, 126.977966);

-- -- Insert data into Membership table
-- INSERT IGNORE INTO Membership (membership_type, duration, membership_status)
-- VALUES 
-- ('Basic', 'Monthly', 'Active'),
-- ('Premium', '6-monthly', 'Active'),
-- ('Professional', 'One year', 'Active'),
-- ('Basic', '6-monthly', 'Inactive'),
-- ('Premium', 'One year', 'Active');

-- -- Insert data into User table
-- INSERT IGNORE INTO User (username, name, lastname, email, password, role, country_id, city_id)
-- VALUES 
-- ('john_doe', 'John', 'Doe', 'john.doe@example.com', 'securepassword', 'beneficiary', 1, NULL),
-- ('janedoe', 'Jane', 'Doe', 'janedoe@example.com', 'anothersecurepassword', 'partner', 2, NULL),
-- ('admin1', 'Admin', 'One', 'admin1@example.com', 'adminpassword', 'admin', 3, NULL),
-- ('mary_smith', 'Mary', 'Smith', 'mary.smith@example.com', 'marypassword', 'beneficiary', 4, NULL),
-- ('robert_brown', 'Robert', 'Brown', 'robert.brown@example.com', 'robertpassword', 'beneficiary', 5, NULL),
-- ('linda_jones', 'Linda', 'Jones', 'linda.jones@example.com', 'lindapassword', 'partner', 1, NULL),
-- ('william_davis', 'William', 'Davis', 'william.davis@example.com', 'williampassword', 'admin', 2, NULL),
-- ('barbara_miller', 'Barbara', 'Miller', 'barbara.miller@example.com', 'barbarapassword', 'beneficiary', 3, NULL),
-- ('james_wilson', 'James', 'Wilson', 'james.wilson@example.com', 'jamespassword', 'partner', 4, NULL),
-- ('patricia_taylor', 'Patricia', 'Taylor', 'patricia.taylor@example.com', 'patriciapassword', 'admin', 5, NULL);


-- -- Insert data into BusinessPartner table
-- INSERT IGNORE INTO BusinessPartner (user_id, tax_code, registration_number)
-- VALUES 
-- (2, '123456789', 'REG001'),
-- (6, '987654321', 'REG002'),
-- (9, '112233445', 'REG003');

-- -- Insert data into Admin table
-- INSERT IGNORE INTO Admin (user_id, role, phone_number, status, last_login, creation_date, notes, profile_picture)
-- VALUES 
-- (3, 'Super Admin', '123-456-7890', 'active', NOW(), NOW(), 'Top-level admin', 'profile1.jpg'),
-- (7, 'Admin Assistant', '234-567-8901', 'active', NOW(), NOW(), 'Assistant to main admin', 'profile2.jpg'),
-- (10, 'Support Admin', '345-678-9012', 'active', NOW(), NOW(), 'Handles support queries', 'profile3.jpg');

-- -- Insert data into Business table
-- INSERT IGNORE INTO Business (partner_id, business_name, business_type, advertisement_details, price)
-- VALUES 
-- (6, 'Doe Cafe', 'Food and Beverage', 'Best coffee in town', 'Moderate'),
-- (6, 'Doe Market', 'Market', 'Fresh produce available', 'Moderate'),
-- (1, 'Smith Bakery', 'Food and Beverage','Freshly baked goods', 'Cheap'),
-- (5, 'Jones Hotel', 'Hotels', 'Luxury stay', 'Expensive'),
-- (4, 'Brown Bar', 'Bars', 'Great drinks and ambiance', 'Moderate'),
-- (8, 'Miller Flea Market', 'Market',  'Unique finds', 'Cheap'),
-- (9, 'Wilson Restaurant', 'Food and Beverage',  'Fine dining experience', 'Expensive'),
-- (2, 'Davis Supermarket', 'Market',  'All your daily needs', 'Moderate'),
-- (10, 'Taylor Pub', 'Bars',  'Friendly atmosphere', 'Moderate'),
-- (NULL, 'Williams Fast Food', 'Food and Beverage', 'Quick bites', 'Cheap');

-- -- Insert data into Market table
-- INSERT IGNORE INTO Market (business_id, market_type, market_specific_attribute)
-- VALUES 
-- (2, 'Supermarket', 'Open 24/7'),
-- (6, 'Flea Market', 'Only on weekends'),
-- (8, 'Supermarket', 'Discounts on weekdays');

-- #######################

-- -- Insert data into FoodAndBeverage table
-- INSERT IGNORE INTO FoodAndBeverage (business_id, food_type, food_beverage_specific_attribute)
-- VALUES 
-- (1, 'Cafe', 'Free Wi-Fi available');

-- -- Insert data into Beneficiary table
-- INSERT IGNORE INTO Beneficiary (user_id, beneficiary_type, date_of_birth, address, contact_number)
-- VALUES 
-- (1, 'user', '1985-05-15', '123 Main St', '123-456-7890'),
-- (4, 'service_provider', '1990-08-25', '456 Elm St', '987-654-3210'),
-- (5, 'user', '1980-10-15', '101 Pine St', '123-456-7854'),
-- (6, 'user', '1990-09-18', '202 Maple St', '123-456-7823'),
-- (8, 'user', '2000-02-19', '303 Birch St', '123-456-7843'),
-- (9, 'user', '1981-07-14', '404 Cedar St', '123-456-7853');


-- -- Insert data into SimpleUser table
-- INSERT IGNORE INTO SimpleUser (beneficiary_id, bistory, preferences)
-- VALUES 
-- (1, 'History of user', 'Private'),
-- (4, 'Service provider history', 'Public');

-- -- Insert data into ServiceProvider table
-- INSERT IGNORE INTO ServiceProvider (beneficiary_id, languages_spoken, specialties, certifications)
-- VALUES 
-- (4, 'English, German', 'Translating Services', 'GOETHE C2');

-- -- Insert data into Service table
-- INSERT IGNORE INTO Service (provider_id, description, service_name)
-- VALUES 
-- (4, 'Translating Services', 'German Translator');

-- -- Insert data into Accommodation table
-- INSERT IGNORE INTO Accommodation (service_id, num_rooms, facilities)
-- VALUES 
-- (1, 10, 'Free Wi-Fi, Pool, Gym');

-- -- Insert data into Car table
-- INSERT IGNORE INTO Car (service_id, car_model, year_of_manufacture, car_type, rental_rate)
-- VALUES 
-- (1, 'Toyota Camry', 2020, 'sedan', 50.00);

-- -- Insert data into Activity table
-- INSERT IGNORE INTO Activity (service_id, activity_name, age_requirement, duration_hours, activity_description)
-- VALUES 
-- (1, 'City Tour', 18, 2, 'Guided city tour');

-- -- Insert data into Card table
-- INSERT IGNORE INTO Card (beneficiary_id, cardnumber, barcode, expiration_date)
-- VALUES 
-- (1, '1234567890123456', '1234567890', '2025-12-31');

-- -- Insert data into Points table
-- INSERT IGNORE INTO Points (card_id, points, available_coupons)
-- VALUES 
-- (1, 100, '10% off next purchase');

-- -- Insert data into PointsHistory table
-- INSERT IGNORE INTO PointsHistory (points_id, transaction_type, points_change, transaction_date)
-- VALUES 
-- (1, 'earn', 50, NOW());

-- -- Insert data into Booking table
-- INSERT IGNORE INTO Booking (booker_id, service_id, booking_status, booking_details)
-- VALUES 
-- (1, 1, 'confirmed', 'Booking for IT support');

-- -- Insert data into Review table
-- INSERT IGNORE INTO Review (reviewer_id, reviewee_id, rating, review_text)
-- VALUES 
-- (1, 4, 5, 'Excellent service and highly recommended!');

-- -- Insert data into Response table
-- INSERT IGNORE INTO Response (review_id, replier_id, reply_text)
-- VALUES 
-- (1, 4, 'Thank you for your feedback!');

-- -- Insert data into ChatMessage table
-- INSERT IGNORE INTO ChatMessage (sender_id, receiver_id, message_text)
-- VALUES 
-- (1, 4, 'Hello, I need some help with my service.');

-- -- Insert data into SavedBusiness table
-- INSERT IGNORE INTO SavedBusiness (beneficiary_id, business_id)
-- VALUES 
-- (1, 1);

-- -- Insert data into SavedService table
-- INSERT IGNORE INTO SavedService (beneficiary_id, service_id)
-- VALUES 
-- (1, 1);

-- -- Insert data into Application table
-- INSERT IGNORE INTO Application (user_id, additional_info, admin_notes)
-- VALUES 
-- (1, 'Application for premium membership', 'Reviewed by admin');

-- -- Insert data into FriendRequest table
-- INSERT IGNORE INTO FriendRequest (user1_id, user2_id, status, accepted_at)
-- VALUES 
-- (1, 4, 'accepted', NOW()),  -- John Doe and Mary Smith
-- (1, 5, 'pending', NULL),    -- John Doe and Robert Brown
-- (2, 7, 'pending', NULL),    -- Jane Doe and Linda Jones
-- (4, 6, 'accepted', NOW()),  -- Mary Smith and Linda Jones
-- (3, 9, 'pending', NULL),    -- Admin1 and Patricia Taylor
-- (8, 10, 'pending', NULL);   -- Barbara Miller and James Wilson
