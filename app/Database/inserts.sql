-- Insert data into the User table
INSERT INTO User (Username, Password, Name, PhoneNumber, Email, Age, Role)
VALUES
    ('john_doe', 'scrypt:32768:8:1$ktYR2pTKDPWTivre$3eefabb308d4e42dbe4098f861e96505245ad6a0b801762b6ceca980ed7be60d919ff02145451394201c1d35f8f83a3d36a2dcbf059aab4b9ed1794b074beb3b', 'John Doe', 1234567890, 'john.doe@example.com', 30, 'Customer'),
    ('jane_smith', 'scrypt:32768:8:1$sHedLeOgqmC8NMuI$c0e94f4f5bbdae816943f1451436a4094775c420397ab82e6c74ad5daa9c6f2d8c0bccc3259288c4ea9c749932a23db3c9e2ff841ca7bc7d1128fd8700690ab0', 'Jane Smith', 0, 'jane.smith@example.com', 25, 'Customer'),
    ('admin_user', 'scrypt:32768:8:1$88JWKlAGfjPTftKJ$0d22b66c9078542fe7e5a08b192dcef34d1d8ce4b9f478eb17b438bf09700bf035682c726cfcb756e2f6d48814ed024d499ce9c96feb9ed83df4b62cb8e5881f', 'Admin User', 0, 'admin@example.com', 35, 'Admin'),
    ('alice_wonderland', 'scrypt:32768:8:1$jYw8SE1Vtpe8DJTx$0866a6f60928cade393c052b1404b9d45544815170b3fdc118af7fbc97b4b74dd8b64f4ebffa8515334de3061428470ef8a031d4b4709b0a0e2a381e715f2632', 'Alice Wonderland', 9876543210, 'alice@example.com', 28, 'Customer'),
    ('bob_smith', 'scrypt:32768:8:1$j3wYRTUrZEOheCvo$cfc034e6cad41744e2e427e40be6c628408fad1bdc3df7b302cc0c8ce4241acd883c92d600984e37be4e1ce2bd9cca84a4864dbc4dc710f2fbac7cb814f50f80', 'Bob Smith', 0, 'bob@example.com', 40, 'Customer'),
    ('sarah_connor', 'scrypt:32768:8:1$v9DizR5oFxj6MuTq$4087fbd36518a3dfbcb364ec8d4f717d83e3306c5d3a8fa18e661086efaf343125820487cc7ed4cb537eda723e29b60cca1aa60b6c97598881be7152ce29a4f8', 'Sarah Connor', 5551234567, 'sarah@example.com', 35, 'Customer'),
    ('clark_kent', 'scrypt:32768:8:1$LjeNYes62oBggmqa$bb94d447f7431dc2ef358c69a6241bac9228e65f02742e12913a52afc736ea3f13fe10e248b239baaab027ca70468798ad8ad538881c40e9d887e0245471b06e', 'Clark Kent', 0, 'clark@example.com', 30, 'Customer'),
    ('linda_parker', 'scrypt:32768:8:1$y85qITBYP34kf3vV$ff47fbb851ffa4ef460344f9f2c7abcab5f16e8c4f9c7c78db5ea347884bf3447e90b28c7141d68b7d8a275f5cbb10a92c6a2c00bcc4bc1dde93345cab4bcf98', 'Linda Parker', 1239874560, 'linda@example.com', 22, 'Customer'),
    ('carol_jones', 'scrypt:32768:8:1$BKlpq4YhLJm9jnfO$4afcb0145bf255ba5a85f0cf4e32b65edec275ad16d077714e5ccdc9f6cbd814e17054176691b7baa8835bb6bd9902939ed5b9409d36abed4f8bb157665998bc', 'Carol Jones', 0, 'carol@example.com', 45, 'Customer'),
    ('mike_adams', 'scrypt:32768:8:1$pYql0iWb23RdArrF$e3403f0f29db8622307118b3ecfa059a3a29a4425ca8499b7aa07f8f04d07cd75b2d48e909b9859d5124ea3595cd69942c8589cfa4edca50fa02982d51a9aec6', 'Mike Adams', 7890123456, 'mike@example.com', 29, 'Customer'),
    ('emma_smith', 'scrypt:32768:8:1$8agp4MtEBZSyqjgB$e8141a29054205a4e43b2f7f2ccdba925cc530c2f2b06051f01ec33a419fa28e37a4081174eccbbe853dd8a5f326538ae7d8517739956ea298f1fc12da2108e9', 'Emma Smith', 0, 'emma@example.com', 27, 'Customer'),
    ('james_anderson', 'scrypt:32768:8:1$a7EfRCtllHbK5WRz$abeb8d7b3ae9164fdd052e68f0b68660f2ec5d3f595b000822f65273082b0abf15586fb1dce0c3a1b435f3ac1ccad973e9f8d6610c657ae037e4d044074772a2', 'James Anderson', 5557891230, 'james@example.com', 33, 'Customer'),
    ('olivia_martin', 'scrypt:32768:8:1$dUnton3haaZc5xJ9$c61d3e5c9c54bf89d589521434a226f6eb9d86ecd805f44e43f12317913394eecd2efa65d1cc54b00d62c902c8ccba02bcae13e411b1089c5cffcf4b4aa4e6dd', 'Olivia Martin', 0, 'olivia@example.com', 31, 'Customer'),
    ('william_jackson', 'scrypt:32768:8:1$nUbTdje80PFyTVMm$8361c0f63cdd115f154b8ca0f4bd4f53e2587f946aa15283b94e82264bc8d2aebaa640e8b199940f8eee3b931aa757e3b8eb3d2e690765364346b3f4e96c212c', 'William Jackson', 1235557890, 'william@example.com', 39, 'Customer'),
    ('ava_miller', 'scrypt:32768:8:1$hIrUeoCUljdGqqRy$13121f8d468e902ea9cb6d42ee107bb3c80b8845a0ac170e3846b8e49505456c8704fde7a531a99a3df069cc9b689e9b7a4b6a3ca91d0ccc2317ad2fbd022bd0', 'Ava Miller', 0, 'ava@example.com', 24, 'Customer'),
    ('michael_johnson', 'scrypt:32768:8:1$OdYzZC2Wb4ZJ1il9$35ebf44371a3a2844c3f8540de93b9129d54f5560f147b22b192d8a93d24c0ad91fc44a492b358c21b029a9f8c95d481cc9d238c746d976b6066e3e41075727a', 'Michael Johnson', 9998887777, 'michael@example.com', 37, 'Customer'),
    ('sophia_wilson', 'scrypt:32768:8:1$JQ5L6MBRiGY5qIRR$a2077ea3f7aa2ac8fb413e17e92bd92250f506de5644ae5932ff0908c1191cc7500de26eb1f6c35d4b785dcb8f8004ea88c19bddbd4bfbd02e5b4e6db7cdc3a5', 'Sophia Wilson', 0, 'sophia@example.com', 28, 'Customer'),
    ('david_clark', 'scrypt:32768:8:1$Fz1kv3GYLy8IzkfS$9c3419fe3a2ce1aa2a50520e3d8c08080bfe8f5b8a11436044f2efc8d7883efbd9d9cdb25e9be5144353b57cd8a1b2bada2ec5f8a2cb3a530b737bac793e2e43', 'David Clark', 1239998888, 'david@example.com', 36, 'Customer'),
    ('oliver_martin', 'scrypt:32768:8:1$xeXr4yZR4p6ZxBMH$9f751ba1bef42f38e93f88aca245fa636491d8487e0cf1698c8177ccd526e4cce143789ac7b16681fbb1eee89e678a3c4f6363b557aa6fbd3605da0ba0b09770', 'Oliver Martin', 0, 'oliver@example.com', 26, 'Customer'),
    ('lucy_hall', 'scrypt:32768:8:1$qfSgfTDtyEzBvg3i$c890ae66d6df3d5b73024c71af6f7303027d2440e6c2f042bc4466ce06235b30f4a389467584bf9c474f5ad4184c94ba99cd3635c1c89942aedaac1d8d025e59', 'Lucy Hall', 5554443333, 'lucy@example.com', 29, 'Customer');
/* unhashed passes
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
*/
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