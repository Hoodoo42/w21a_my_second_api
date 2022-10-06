SELECT id, name, description, in_stock_quantity, created_at 
FROM item;
CALL get_items();



INSERT INTO item (name, description, in_stock_quantity) VALUES(name_input, description_input, quantity_input);
SELECT id FROM item
ORDER BY id DESC 
LIMIT 1;
commit;
CALL new_item('tent', 'for anywhere camping', 32);


UPDATE item SET in_stock_quantity = stock_input WHERE id = id_input;
CALL add_stock(10, 12);


DELETE FROM item WHERE id = id_input;
CALL delete_item(12);