-- Insert data into the User table
INSERT INTO User (Username, Password, Name, PhoneNumber, Email, Age, Role)
VALUES
    ('john_doe', 'hashed_password1', 'John Doe', 1234567890, 'john.doe@example.com', 30, 'Customer'),
    ('jane_smith', 'hashed_password2', 'Jane Smith', NULL, 'jane.smith@example.com', 25, 'Customer'),
    ('admin_user', 'admin_password', 'Admin User', NULL, 'admin@example.com', 35, 'Admin'),
    ('alice_wonderland', 'alice_password', 'Alice Wonderland', 9876543210, 'alice@example.com', 28, 'Customer'),
    ('bob_smith', 'bob_password', 'Bob Smith', NULL, 'bob@example.com', 40, 'Customer'),
    ('sarah_connor', 'sarah_password', 'Sarah Connor', 5551234567, 'sarah@example.com', 35, 'Customer'),
    ('clark_kent', 'clark_password', 'Clark Kent', NULL, 'clark@example.com', 30, 'Customer'),
    ('linda_parker', 'linda_password', 'Linda Parker', 1239874560, 'linda@example.com', 22, 'Customer'),
    ('carol_jones', 'carol_password', 'Carol Jones', NULL, 'carol@example.com', 45, 'Customer'),
    ('mike_adams', 'mike_password', 'Mike Adams', 7890123456, 'mike@example.com', 29, 'Customer'),
    ('emma_smith', 'emma_password', 'Emma Smith', NULL, 'emma@example.com', 27, 'Customer'),
    ('james_anderson', 'james_password', 'James Anderson', 5557891230, 'james@example.com', 33, 'Customer'),
    ('olivia_martin', 'olivia_password', 'Olivia Martin', NULL, 'olivia@example.com', 31, 'Customer'),
    ('william_jackson', 'william_password', 'William Jackson', 1235557890, 'william@example.com', 39, 'Customer'),
    ('ava_miller', 'ava_password', 'Ava Miller', NULL, 'ava@example.com', 24, 'Customer'),
    ('michael_johnson', 'michael_password', 'Michael Johnson', 9998887777, 'michael@example.com', 37, 'Customer'),
    ('sophia_wilson', 'sophia_password', 'Sophia Wilson', NULL, 'sophia@example.com', 28, 'Customer'),
    ('david_clark', 'david_password', 'David Clark', 1239998888, 'david@example.com', 36, 'Customer'),
    ('oliver_martin', 'oliver_password', 'Oliver Martin', NULL, 'oliver@example.com', 26, 'Customer'),
    ('lucy_hall', 'lucy_password', 'Lucy Hall', 5554443333, 'lucy@example.com', 29, 'Customer');

-- Insert data into the Product table
INSERT INTO Product (Name, Description, Price, Qty)
VALUES
    ('Mug', 'Ceramic coffee mug with a classic design', 10, 100),
    ('Cup', 'Glass cup for hot and cold beverages', 5, 200),
    ('T-Shirt', 'Cotton t-shirt with a stylish print', 20, 50),
    ('Hoodie', 'Warm and comfortable hoodie for all seasons', 30, 30),
    ('Travel Mug', 'Insulated travel mug for on-the-go', 15, 150),
    ('Teacup', 'Elegant teacup for tea lovers', 8, 120),
    ('V-Neck T-Shirt', 'Casual v-neck t-shirt in various colors', 18, 70),
    ('Zip-Up Hoodie', 'Zip-up hoodie with fleece lining', 35, 20),
    ('Espresso Cup', 'Small espresso cup for coffee enthusiasts', 6, 80),
    ('Polo Shirt', 'Classic polo shirt for a smart-casual look', 25, 60),
    ('Travel Pillow', 'Soft travel pillow for comfortable journeys', 12, 100),
    ('Coffee Mug Set', 'Set of 4 ceramic coffee mugs', 35, 40),
    ('Ceramic Plate', 'Durable ceramic plate for daily use', 10, 90),
    ('Canvas Tote Bag', 'Reusable canvas tote bag for shopping', 15, 70),
    ('Pullover Hoodie', 'Cozy pullover hoodie with front pocket', 28, 25),
    ('Latte Mug', 'Tall latte mug for coffee with frothed milk', 9, 60),
    ('Graphic T-Shirt', 'Graphic print t-shirt in various designs', 22, 45),
    ('Fleece Jacket', 'Warm fleece jacket for cold weather', 40, 15),
    ('Soup Bowl', 'Deep soup bowl for soups and stews', 7, 75),
    ('Ceramic Vase', 'Elegant ceramic vase for floral arrangements', 18, 30);

-- Insert data into the Image table


-- Insert data into the Product_Has_Image table


-- Insert data into the Review table
INSERT INTO Review (PName, ReviewBody)
VALUES
    ('Mug', 'Love this mug!'),
    ('Cup', 'Great for hot beverages.'),
    ('T-Shirt', 'Comfortable and stylish.'),
    ('Hoodie', 'Keeps me warm in winter.'),
    ('Travel Mug', 'Perfect for travel.'),
    ('Teacup', 'Elegant design.'),
    ('V-Neck T-Shirt', 'Nice fit.'),
    ('Zip-Up Hoodie', 'Cozy and warm.'),
    ('Espresso Cup', 'Ideal for espresso lovers.'),
    ('Polo Shirt', 'Classic look.'),
    ('Travel Pillow', 'Very comfortable for long trips.'),
    ('Coffee Mug Set', 'Great value for the set.'),
    ('Ceramic Plate', 'Durable and versatile.'),
    ('Canvas Tote Bag', 'Sturdy and eco-friendly.'),
    ('Pullover Hoodie', 'My favorite hoodie.'),
    ('Latte Mug', 'Perfect size for lattes.'),
    ('Graphic T-Shirt', 'Cool designs.'),
    ('Fleece Jacket', 'Warm and stylish.'),
    ('Soup Bowl', 'Deep and practical.'),
    ('Ceramic Vase', 'Adds elegance to any room.');

-- Insert data into the Category table
INSERT INTO Category (Name, Description)
VALUES
    ('Drinkware', 'Mugs and cups for beverages'),
    ('Apparel', 'T-shirts and hoodies'),
    ('Other', 'Other types of miscellany');


-- Insert data into the Category_Has_Product table
INSERT INTO Category_Has_Product (CName, PName)
VALUES
    ('Drinkware', 'Mug'),
    ('Drinkware', 'Cup'),
    ('Apparel', 'T-Shirt'),
    ('Apparel', 'Hoodie'),
    ('Drinkware', 'Travel Mug'),
    ('Drinkware', 'Teacup'),
    ('Apparel', 'V-Neck T-Shirt'),
    ('Apparel', 'Zip-Up Hoodie'),
    ('Drinkware', 'Espresso Cup'),
    ('Apparel', 'Polo Shirt'),
    ('Other', 'Travel Pillow'),
    ('Drinkware', 'Coffee Mug Set'),
    ('Drinkware', 'Ceramic Plate'),
    ('Other', 'Canvas Tote Bag'),
    ('Apparel', 'Pullover Hoodie'),
    ('Drinkware', 'Latte Mug'),
    ('Apparel', 'Graphic T-Shirt'),
    ('Apparel', 'Fleece Jacket'),
    ('Drinkware', 'Soup Bowl');


-- Insert data into the `Order` table
INSERT INTO `Order` (Client, Date, ConcDate, Description)
VALUES
    ('john_doe', '2023-09-29 10:00:00', '2023-09-30 15:00:00', 'Order for Drinkware'),
    ('jane_smith', '2023-09-29 11:00:00', '2023-09-30 14:00:00', 'Order for Apparel'),
    ('alice_wonderland', '2023-09-29 12:00:00', '2023-09-30 16:00:00', 'Order for Drinkware'),
    ('bob_smith', '2023-09-29 13:00:00', '2023-09-30 17:00:00', 'Order for Apparel'),
    ('sarah_connor', '2023-09-29 14:00:00', '2023-09-30 18:00:00', 'Order for Drinkware'),
    ('clark_kent', '2023-09-29 15:00:00', '2023-09-30 19:00:00', 'Order for Apparel'),
    ('linda_parker', '2023-09-29 16:00:00', '2023-09-30 20:00:00', 'Order for Drinkware'),
    ('carol_jones', '2023-09-29 17:00:00', '2023-09-30 21:00:00', 'Order for Apparel'),
    ('mike_adams', '2023-09-29 18:00:00', '2023-09-30 22:00:00', 'Order for Drinkware'),
    ('emma_smith', '2023-09-29 19:00:00', '2023-09-30 23:00:00', 'Order for Apparel');

-- Insert data into the Order_Has_Product table
INSERT INTO Order_Has_Product (`Order`, PName, Qty)
VALUES
    (1, 'Mug', 2),
    (1, 'Cup', 3),
    (2, 'T-Shirt', 4),
    (2, 'Hoodie', 1),
    (3, 'Travel Mug', 2),
    (3, 'Teacup', 3),
    (4, 'V-Neck T-Shirt', 4),
    (4, 'Zip-Up Hoodie', 1),
    (5, 'Espresso Cup', 2),
    (5, 'Polo Shirt', 3),
    (6, 'Travel Pillow', 1),
    (6, 'Coffee Mug Set', 2),
    (7, 'Ceramic Plate', 3),
    (7, 'Canvas Tote Bag', 1),
    (8, 'Pullover Hoodie', 2),
    (8, 'Latte Mug', 3),
    (9, 'Graphic T-Shirt', 4),
    (9, 'Fleece Jacket', 1),
    (10, 'Soup Bowl', 2),
    (10, 'Ceramic Vase', 3);

-- Insert data into the Cart table
INSERT INTO Cart (Client, PName)
VALUES
    ('john_doe', 'Mug'),
    ('john_doe', 'T-Shirt'),
    ('jane_smith', 'Hoodie'),
    ('jane_smith', 'Travel Mug'),
    ('alice_wonderland', 'Teacup'),
    ('alice_wonderland', 'V-Neck T-Shirt'),
    ('bob_smith', 'Zip-Up Hoodie'),
    ('bob_smith', 'Espresso Cup'),
    ('sarah_connor', 'Polo Shirt'),
    ('clark_kent', 'Travel Pillow'),
    ('clark_kent', 'Coffee Mug Set'),
    ('linda_parker', 'Ceramic Plate'),
    ('linda_parker', 'Canvas Tote Bag'),
    ('carol_jones', 'Pullover Hoodie'),
    ('carol_jones', 'Latte Mug'),
    ('mike_adams', 'Graphic T-Shirt'),
    ('emma_smith', 'Fleece Jacket'),
    ('emma_smith', 'Soup Bowl'),
    ('sarah_connor', 'Ceramic Vase');

-- Insert data into the Wishlist table
INSERT INTO Wishlist (Client, PName)
VALUES
    ('john_doe', 'Cup'),
    ('jane_smith', 'T-Shirt'),
    ('alice_wonderland', 'Hoodie'),
    ('bob_smith', 'Travel Mug'),
    ('sarah_connor', 'Teacup'),
    ('clark_kent', 'Espresso Cup'),
    ('linda_parker', 'Polo Shirt'),
    ('carol_jones', 'Travel Pillow'),
    ('mike_adams', 'Coffee Mug Set'),
    ('emma_smith', 'Ceramic Plate'),
    ('clark_kent', 'Canvas Tote Bag'),
    ('linda_parker', 'Pullover Hoodie'),
    ('carol_jones', 'Latte Mug'),
    ('mike_adams', 'Graphic T-Shirt'),
    ('emma_smith', 'Fleece Jacket'),
    ('sarah_connor', 'Soup Bowl'),
    ('john_doe', 'Ceramic Vase'),
    ('jane_smith', 'Travel Mug'),
    ('alice_wonderland', 'Cup'),
    ('bob_smith', 'Mug');
