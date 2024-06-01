INSERT INTO Country (country_name, continent, currency) VALUES ('Greece', 'Europe', 'Euro');

INSERT INTO City (city_name, country_id, latitude, longitude) VALUES
('Patras', 1, 38.2466, 21.7346),
('Athens', 1, 37.9838, 23.7275);

INSERT INTO User (username, name, lastname, email, password, role, country_id, city_id) VALUES
('partner1', 'John', 'Doe', 'partner1@example.com', 'password1', 'partner', 1, 1),
('partner2', 'Jane', 'Smith', 'partner2@example.com', 'password2', 'partner', 1, 1),
('partner3', 'Alice', 'Johnson', 'partner3@example.com', 'password3', 'partner', 1, 2),
('partner4', 'Bob', 'Brown', 'partner4@example.com', 'password4', 'partner', 1, 2),
('beneficiary1', 'Emily', 'Davis', 'beneficiary1@example.com', 'password5', 'beneficiary', 1, 2),
('beneficiary2', 'Michael', 'Wilson', 'beneficiary2@example.com', 'password6', 'beneficiary', 1, 1),
('beneficiary3', 'Sophia', 'Martinez', 'beneficiary3@example.com', 'password7', 'beneficiary', 1, 1),
('beneficiary4', 'James', 'Anderson', 'beneficiary4@example.com', 'password8', 'beneficiary', 1, 2),
('beneficiary5', 'Olivia', 'Taylor', 'beneficiary5@example.com', 'password9', 'beneficiary', 1, 2),
('beneficiary6', 'William', 'Moore', 'beneficiary6@example.com', 'password10', 'beneficiary', 1, 1),
('beneficiary7', 'Will', 'More', 'beneficiary7@example.com', 'password11', 'beneficiary', 1, 1);


INSERT INTO BusinessPartner (user_id, tax_code, registration_number, website, description) 
VALUES 
    (1, '123ABC', 'REG123', 'www.partner1.com', 'Description for Partner 1'),
    (2, '456DEF', 'REG456', 'www.partner2.com', 'Description for Partner 2'),
    (3, '789GHI', 'REG789', 'www.partner3.com', 'Description for Partner 3'),
    (4, 'ABC123', 'REGABC', 'www.partner4.com', 'Description for Partner 4');
    
    
INSERT INTO Beneficiary (user_id, beneficiary_type, date_of_birth, address, contact_number, location_status, membership_id) 
VALUES 
    (5, 'Simple User', '2000-01-01', 'Address 1', '1234567890', 'Active', NULL),
    (6, 'Service Provider', '1995-05-15', 'Address 2', '9876543210', 'Inactive', NULL),
    (7, 'Simple User', '1988-10-20', 'Address 3', '5555555555', 'Active', NULL),
    (8, 'Service Provider', '1975-12-31', 'Address 4', '7777777777', 'Inactive', NULL),
    (9, 'Simple User', '1992-03-08', 'Address 5', '9999999999', 'Active', NULL),
    (10, 'Service Provider', '1980-07-25', 'Address 6', '3333333333', 'Inactive', NULL),
    (11, 'Service Provider', '1980-08-25', 'Address 7', '1111111111', 'Inactive', NULL); 
    
    
INSERT INTO ServiceProvider (beneficiary_id, languages_spoken, specialties, certifications) 
VALUES 
    (6, 'English, Greek', 'Web Development', 'Certified Web Developer'),
    (8, 'English, Spanish', 'Legal Services', 'Bar Certified Lawyer'),
    (10, 'English, French', 'Healthcare', 'Medical Doctor'),
    (11, 'English, German', 'Consulting', 'Consultancy Certificate');    

INSERT INTO SimpleUser (beneficiary_id, bistory, preferences) 
VALUES 
    (5, 'This is the bio for simple user 1', 'Preferences for simple user 1'),
    (7, 'This is the bio for simple user 2', 'Preferences for simple user 2'),
    (9, 'This is the bio for simple user 3', 'Preferences for simple user 3');
    
INSERT INTO Service (provider_id, description, service_name, country_id, city_id)
VALUES
    (6, 'Bar Service Description', 'Bar Service', 1, 1),
    (8, 'Hotel Service Description', 'Hotel Service', 1, 1),
    (10, 'Food & Beverage Service Description', 'Food & Beverage Service', 1, 1),
    (11, 'Market Service Description', 'Market Service', 1, 1);

INSERT INTO Activity (service_id, activity_name, age_requirement, duration_hours, activity_description)
VALUES
    (1, 'Hiking', 10, 3, 'Guided hiking tour in the nearby mountains.');

INSERT INTO Accommodation (service_id, num_rooms, facilities)
VALUES
    (2, 50, 'WiFi, Parking, Pool');
    
INSERT INTO Car (service_id, car_model, year_of_manufacture, car_type, rental_rate)
VALUES
    (3, 'Toyota Camry', 2022, 'sedan', 50.00),
    (4, 'Honda CR-V', 2021, 'SUV', 60.00);    
    
INSERT INTO ServiceAvailability (service_id, available_date)
VALUES
    (1, '2024-05-29'),
    (1, '2024-05-30'),
    (1, '2024-05-31'),
    (1, '2024-06-01');


INSERT INTO ServiceAvailability (service_id, available_date)
VALUES
    (2, '2024-05-29'),
    (2, '2024-05-30'),
    (2, '2024-05-31'),
    (2, '2024-06-01');


INSERT INTO ServiceAvailability (service_id, available_date)
VALUES
    (3, '2024-05-29'),
    (3, '2024-05-30'),
    (3, '2024-05-31'),
    (3, '2024-06-01');


INSERT INTO ServiceAvailability (service_id, available_date)
VALUES
    (4, '2024-05-29'),
    (4, '2024-05-30'),
    (4, '2024-05-31'),
    (4, '2024-06-01');    
    
INSERT INTO AvailableHours (service_id, available_date, time_range)
VALUES 
    (1, '2024-05-30', '12:00-14:00'),
    (1, '2024-05-30', '17:00-19:00'),
    (2, '2024-05-31', '10:00-12:00'),
    (2, '2024-05-31', '15:00-17:00'),
    (3, '2024-06-01', '09:00-11:00'),
    (3, '2024-06-01', '14:00-16:00'),
    (4, '2024-06-02', '11:00-13:00'),
    (4, '2024-06-02', '16:00-18:00'),
    (5, '2024-06-03', '08:00-10:00'),
    (5, '2024-06-03', '13:00-15:00'),
    (6, '2024-06-04', '10:00-12:00'),
    (6, '2024-06-04', '15:00-17:00'),
    (7, '2024-06-05', '11:00-13:00'),
    (7, '2024-06-05', '16:00-18:00'),
    (8, '2024-06-06', '09:00-11:00'),
    (8, '2024-06-06', '14:00-16:00'),
    (9, '2024-06-07', '12:00-14:00'),
    (9, '2024-06-07', '17:00-19:00'),
    (10, '2024-06-08', '10:00-12:00'),
    (10, '2024-06-08', '15:00-17:00'),
    (11, '2024-06-09', '11:00-13:00'),
    (11, '2024-06-09', '16:00-18:00'),
    (12, '2024-06-10', '08:00-10:00'),
    (12, '2024-06-10', '13:00-15:00');
        
    
INSERT INTO Business (partner_id, business_name, business_type, advertisement_details, price, country_id, city_id)
VALUES
    (1, 'John\'s Bar', 'Bars', 'Best cocktails in town!', 'Moderate', 1, 1),
    (2, 'Jane\'s Hotel', 'Hotels', 'Luxurious stay with amazing views!', 'Expensive', 1, 1),
    (3, 'Alice\'s Food & Beverage', 'Food and Beverage', 'Delicious food for everyone!', 'Moderate', 1, 1),
    (4, 'Bob\'s Market', 'Market', 'Fresh produce and local specialties!', 'Cheap', 1, 1);

INSERT INTO Market (business_id, market_type, market_specific_attribute)
VALUES
    (4, 'Supermarket', 'Local produce and groceries');


INSERT INTO FoodAndBeverage (business_id, food_type, food_beverage_specific_attribute)
VALUES
    (3, 'Restaurant', 'Mediterranean cuisine');

INSERT INTO Hotels (business_id, hotel_filters, hotel_stars, hotel_floors, hotel_specific_attribute)
VALUES
    (2, 'Free WiFi, Breakfast included', 5, 10, 'Sea view rooms');

INSERT INTO Bars (business_id, age_boundary, bar_type, bar_specific_attribute)
VALUES
    (1, 18, 'Cocktail Bar', 'Live music on weekends');    
    