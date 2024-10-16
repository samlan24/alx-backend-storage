-- SQL script that creates a trigger that decreases the quantity of an item 
-- after adding a new order.
DELIMETER $$
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
        SET quantity = quantity - NEW.number
        WHERE item_id = NEW.item_name;
END $$
DELIMETER ;
