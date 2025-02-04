-- The script creates a trigger that decreases
-- the quantity of an item afer adding a new order
-- 

CREATE TRIGGER decrease_items_quantity
   AFTER INSERT ON orders FOR EACH ROW
   UPDATE items SET quantity = quantity - New.number WHERE name=New.item_name;
