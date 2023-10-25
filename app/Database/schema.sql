DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Image;
DROP TABLE IF EXISTS Product_Has_Image;
DROP TABLE IF EXISTS Review;
DROP TABLE IF EXISTS Category;
DROP TABLE IF EXISTS Category_Has_Product;
DROP TABLE IF EXISTS `Order`;
DROP TABLE IF EXISTS Order_Has_Product;
DROP TABLE IF EXISTS Cart;
DROP TABLE IF EXISTS Wishlist;

    CREATE TABLE User
    (
        ID INTEGER primary key AUTOINCREMENT,
        Username varchar(50) not null unique,
        Password binary(64) not null,
        Name varchar(256) not null,
        PhoneNumber varchar(15),
        Email varchar(256), 
        Age int not null,
        Role varchar(10) not null
    );

    CREATE TABLE Product
    (
        Name varchar(50) not null primary key,
        Description varchar(300),
        Price int not null,
        Qty int not null
    );

    CREATE TABLE Image
    (  
        ID INTEGER primary key AUTOINCREMENT,
        Link varchar(400) not null
    );

    CREATE TABLE Product_Has_Image
    (  
        PName varchar(50) not null,
        ID int not null ,
        FOREIGN KEY (Pname) REFERENCES Product(Name),
        FOREIGN KEY (ID) REFERENCES [Image](ID),
        primary key(Pname,ID) 
    );

    CREATE TABLE Review
    (  
        ID INTEGER primary key AUTOINCREMENT,
        PName varchar(50) not null ,
        ReviewBody varchar(400) not null,
        FOREIGN KEY (Pname) REFERENCES Product(Name)

    );

    CREATE TABLE Category
    (  
        Name varchar(50) not null primary key,
        Description varchar(300)
    );

    CREATE TABLE Category_Has_Product
    (  
        CName varchar(50) not null ,
        PName varchar(50) not null ,
        FOREIGN KEY (Cname) REFERENCES Category(Name),
        FOREIGN KEY (Pname) REFERENCES Product(Name),
        primary key(Cname,Pname) 
    );


    CREATE TABLE `Order`
    (  
        ID INTEGER primary key AUTOINCREMENT,
        Client varchar(50) not null,
        Date datetime not null,
        ConcDate datetime,
        Description varchar(300),
        FOREIGN KEY (Client) REFERENCES User(Username)

    );


    CREATE TABLE Order_Has_Product
    (  
        `Order` int not null ,
        PName varchar(50) not null ,
        Qty int not null,
        FOREIGN KEY (`Order`) REFERENCES `Order`(ID),
        FOREIGN KEY (Pname) REFERENCES Product(Name),
        primary key(`Order`,Pname) 
    );

    CREATE TABLE Cart
    (  
        ID INTEGER primary key AUTOINCREMENT,
        Client varchar(50) not null,
        PName varchar(50) not null ,
        FOREIGN KEY (Client) REFERENCES User(Username)
    );

    CREATE TABLE Wishlist
    (  
        Client varchar(50) not null,
        PName varchar(50) not null ,
        FOREIGN KEY (Client) REFERENCES User(Username)
        FOREIGN KEY (Pname) REFERENCES Product(Name)
        primary key(Client,Pname) 

    );