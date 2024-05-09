-- Create the items table
CREATE TABLE IF NOT EXISTS items (
    name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL DEFAULT 10
);

-- Create the orders table
CREATE TABLE IF NOT EXISTS orders (
    item_name VARCHAR(255) NOT NULL,
    number INT NOT NULL
);

-- Insert initial data into items table
INSERT INTO items (name) VALUES ("apple"), ("pineapple"), ("pear");

-- Create the trigger
DELIMITER //
CREATE TRIGGER decrease_quantity AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE name = NEW.item_name;
END //
DELIMITER ;
