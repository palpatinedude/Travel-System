USE od;

-- Insert data into Country table
INSERT IGNORE INTO Country (country_name, continent, currency)
VALUES 
('USA', 'North America', 'USD'),
('Canada', 'North America', 'CAD'),
('France', 'Europe', 'EUR'),
('Germany', 'Europe', 'EUR'),
('Australia', 'Oceania', 'AUD'),
('Japan', 'Asia', 'JPY'),
('Brazil', 'South America', 'BRL'),
('South Africa', 'Africa', 'ZAR'),
('India', 'Asia', 'INR'),
('China', 'Asia', 'CNY'),
('United Kingdom', 'Europe', 'GBP'),
('Italy', 'Europe', 'EUR'),
('Mexico', 'North America', 'MXN'),
('Russia', 'Europe', 'RUB'),
('South Korea', 'Asia', 'KRW');

-- Insert data into City table
INSERT IGNORE INTO City (city_name, country_id, latitude, longitude)
VALUES
('New York', 1, 40.712776, -74.005974),
('Toronto', 2, 43.651070, -79.347015),
('Paris', 3, 48.856613, 2.352222),
('Berlin', 4, 52.520008, 13.404954),
('Sydney', 5, -33.868820, 151.209290),
('Tokyo', 6, 35.689487, 139.691711),
('Rio de Janeiro', 7, -22.906847, -43.172897),
('Cape Town', 8, -33.924870, 18.424055),
('Mumbai', 9, 19.076090, 72.877426),
('Beijing', 10, 39.904202, 116.407394),
('London', 11, 51.507351, -0.127758),
('Rome', 12, 41.902782, 12.496366),
('Mexico City', 13, 19.432608, -99.133209),
('Moscow', 14, 55.755825, 37.617298),
('Seoul', 15, 37.566536, 126.977966);

-- Insert data into Location table
INSERT IGNORE INTO Location (location_name, latitude, longitude, country_id, city_id)
VALUES
('Central Park', 40.785091, -73.968285, 1, 1),
('CN Tower', 43.642566, -79.387057, 2, 2),
('Eiffel Tower', 48.858370, 2.294481, 3, 3),
('Brandenburg Gate', 52.516275, 13.377704, 4, 4),
('Sydney Opera House', -33.856784, 151.215297, 5, 5),
('Tokyo Tower', 35.658581, 139.745433, 6, 6),
('Christ the Redeemer', -22.951916, -43.210487, 7, 7),
('Table Mountain', -33.962824, 18.409810, 8, 8),
('Gateway of India', 18.922000, 72.834652, 9, 9),
('Forbidden City', 39.916344, 116.397155, 10, 10),
('Big Ben', 51.500729, -0.124625, 11, 11),
('Colosseum', 41.890210, 12.492231, 12, 12),
('Zocalo', 19.432608, -99.133209, 13, 13),
('Red Square', 55.753930, 37.620795, 14, 14),
('Gyeongbokgung Palace', 37.579617, 126.977041, 15, 15);

-- Insert data into Membership table
INSERT IGNORE INTO Membership (membership_type, duration, membership_status, description)
VALUES 
('Basic', 'Monthly', 'Active', 'Basic monthly membership with standard benefits'),
('Premium', '6-monthly', 'Active', 'Premium membership with additional benefits'),
('Professional', 'One year', 'Active', 'Professional membership with all benefits'),
('Basic', '6-monthly', 'Inactive', 'Basic membership, currently inactive'),
('Premium', 'One year', 'Active', 'Annual premium membership with maximum benefits');

-- Insert data into User table
INSERT IGNORE INTO User (username, name, lastname, email, address, exact_address, password, role, membership_id)
VALUES 
('john_doe', 'John', 'Doe', 'john.doe@example.com', '123 Main St', 'Apt 4', 'securepassword', 'beneficiary', 1),
('janedoe', 'Jane', 'Doe', 'janedoe@example.com', '456 Elm St', 'Suite 101', 'anothersecurepassword', 'partner', 2),
('admin1', 'Admin', 'One', 'admin1@example.com', '789 Oak St', 'Office 1', 'adminpassword', 'admin', 3),
('mary_smith', 'Mary', 'Smith', 'mary.smith@example.com', '101 Pine St', 'Apt 8', 'marypassword', 'beneficiary', 4),
('robert_brown', 'Robert', 'Brown', 'robert.brown@example.com', '202 Maple St', 'House 5', 'robertpassword', 'beneficiary', 5),
('linda_jones', 'Linda', 'Jones', 'linda.jones@example.com', '303 Birch St', 'Flat 2', 'lindapassword', 'partner', 1),
('william_davis', 'William', 'Davis', 'william.davis@example.com', '404 Cedar St', 'Unit 3B', 'williampassword', 'admin', 2),
('barbara_miller', 'Barbara', 'Miller', 'barbara.miller@example.com', '505 Spruce St', 'Apt 6', 'barbarapassword', 'beneficiary', 3),
('james_wilson', 'James', 'Wilson', 'james.wilson@example.com', '606 Redwood St', 'Suite 200', 'jamespassword', 'partner', 4),
('patricia_taylor', 'Patricia', 'Taylor', 'patricia.taylor@example.com', '707 Cypress St', 'Bungalow 9', 'patriciapassword', 'admin', 5);

-- Insert data into BusinessPartner table
INSERT IGNORE INTO BusinessPartner (user_id, tax_code, registration_number)
VALUES 
(2, '123456789', 'REG001'),
(6, '987654321', 'REG002'),
(9, '112233445', 'REG003');

-- Insert data into Admin table
INSERT IGNORE INTO Admin (user_id, role, phone_number, status, last_login, creation_date, notes, profile_picture)
VALUES 
(3, 'Super Admin', '123-456-7890', 'active', NOW(), NOW(), 'Top-level admin', 'profile1.jpg'),
(7, 'Admin Assistant', '234-567-8901', 'active', NOW(), NOW(), 'Assistant to main admin', 'profile2.jpg'),
(10, 'Support Admin', '345-678-9012', 'active', NOW(), NOW(), 'Handles support queries', 'profile3.jpg');

-- Insert data into Business table
INSERT IGNORE INTO Business (partner_id, business_name, business_type, location_id, advertisement_details, price)
VALUES 
(1, 'Doe Cafe', 'Food and Beverage', 1, 'Best coffee in town', 'Moderate'),
(1, 'Doe Market', 'Market', 2, 'Fresh produce available', 'Moderate'),
(2, 'Smith Bakery', 'Food and Beverage', 3, 'Freshly baked goods', 'Cheap'),
(3, 'Jones Hotel', 'Hotels', 4, 'Luxury stay', 'Expensive'),
(1, 'Brown Bar', 'Bars', 5, 'Great drinks and ambiance', 'Moderate'),
(2, 'Miller Flea Market', 'Market', 6, 'Unique finds', 'Cheap'),
(3, 'Wilson Restaurant', 'Food and Beverage', 7, 'Fine dining experience', 'Expensive'),
(2, 'Davis Supermarket', 'Market', 8, 'All your daily needs', 'Moderate'),
(1, 'Taylor Pub', 'Bars', 9, 'Friendly atmosphere', 'Moderate'),
(3, 'Williams Fast Food', 'Food and Beverage', 10, 'Quick bites', 'Cheap');

-- Insert data into Market table
INSERT IGNORE INTO Market (business_id, market_type, market_specific_attribute)
VALUES 
(2, 'Supermarket', 'Open 24/7'),
(6, 'Flea Market', 'Only on weekends'),
(8, 'Supermarket', 'Discounts on weekdays');

#######################

-- Insert data into FoodAndBeverage table
INSERT IGNORE INTO FoodAndBeverage (business_id, food_type, food_beverage_specific_attribute)
VALUES 
(1, 'Cafe', 'Free Wi-Fi available');

-- Insert data into Beneficiary table
INSERT IGNORE INTO Beneficiary (user_id, beneficiary_type, date_of_birth, address, contact_number, location_id)
VALUES 
(1, 'user', '1985-05-15', '123 Main St', '123-456-7890', 1),
(2, 'service_provider', '1990-08-25', '456 Elm St', '987-654-3210', 2),
(4, 'user', '1980-10-15', '122 Main St', '123-456-7854', 1),
(5, 'user', '1990-09-18', '125 Main St', '123-456-7823', 1),
(6, 'user', '2000-02-19', '15 Main St', '123-456-7843', 1),
(7, 'user', '1981-07-14', '153 Main St', '123-456-7853', 1);

-- Insert data into SimpleUser table
INSERT IGNORE INTO SimpleUser (beneficiary_id, bistory, privacy_settings)
VALUES 
(1, 'History of user', 'Private'),
(2, 'Service provider history', 'Public');

-- Insert data into ServiceProvider table
INSERT IGNORE INTO ServiceProvider (beneficiary_id, languages_spoken, specialties, certifications)
VALUES 
(2, 'English, Spanish', 'IT Services', 'Certified IT Specialist');

-- Insert data into Service table
INSERT IGNORE INTO Service (provider_id, description, service_name, location_id)
VALUES 
(1, 'IT support and services', 'IT Support', 1);

-- Insert data into Accommodation table
INSERT IGNORE INTO Accommodation (service_id, num_rooms, facilities)
VALUES 
(1, 10, 'Free Wi-Fi, Pool, Gym');

-- Insert data into Car table
INSERT IGNORE INTO Car (service_id, car_model, year_of_manufacture, car_type, rental_rate)
VALUES 
(1, 'Toyota Camry', 2020, 'sedan', 50.00);

-- Insert data into Activity table
INSERT IGNORE INTO Activity (service_id, activity_name, age_requirement, duration_hours, activity_description)
VALUES 
(1, 'City Tour', 18, 2, 'Guided city tour');

-- Insert data into Card table
INSERT IGNORE INTO Card (beneficiary_id, cardnumber, barcode, expiration_date)
VALUES 
(1, '1234567890123456', '1234567890', '2025-12-31');

-- Insert data into Points table
INSERT IGNORE INTO Points (card_id, points, available_coupons)
VALUES 
(1, 100, '10% off next purchase');

-- Insert data into PointsHistory table
INSERT IGNORE INTO PointsHistory (points_id, transaction_type, points_change, transaction_date)
VALUES 
(1, 'earn', 50, NOW());

-- Insert data into Booking table
INSERT IGNORE INTO Booking (booker_id, service_id, booking_status, booking_details)
VALUES 
(1, 1, 'confirmed', 'Booking for IT support');

-- Insert data into Review table
INSERT IGNORE INTO Review (reviewer_id, reviewee_id, rating, review_text)
VALUES 
(1, 2, 5, 'Excellent service and highly recommended!');

-- Insert data into Response table
INSERT IGNORE INTO Response (review_id, replier_id, reply_text)
VALUES 
(1, 2, 'Thank you for your feedback!');

-- Insert data into ChatMessage table
INSERT IGNORE INTO ChatMessage (sender_id, receiver_id, message_text)
VALUES 
(1, 2, 'Hello, I need some help with my service.');

-- Insert data into SavedBusiness table
INSERT IGNORE INTO SavedBusiness (beneficiary_id, business_id)
VALUES 
(1, 1);

-- Insert data into SavedService table
INSERT IGNORE INTO SavedService (beneficiary_id, service_id)
VALUES 
(1, 1);

-- Insert data into Application table
INSERT IGNORE INTO Application (user_id, additional_info, admin_notes)
VALUES 
(1, 'Application for premium membership', 'Reviewed by admin');

-- Insert data into FriendRequest table
INSERT IGNORE INTO FriendRequest (user1_id, user2_id, status, accepted_at)
VALUES 
(1, 2, 'accepted', NOW());
