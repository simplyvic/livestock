
DELIMITER //
DROP TRIGGER IF EXISTS after_djangoapp_computer_insert//
CREATE TRIGGER after_djangoapp_computer_insert AFTER INSERT ON djangoapp_computer FOR EACH ROW
BEGIN
INSERT INTO djangoapp_computerhistory(id, computer_name, IP_address, MAC_address, operating_system_id, users_name,
			location, purchase_date, timestamp) 
            
            VALUES(new.id, new.computer_name, new.IP_address, new.MAC_address, new.operating_system_id, new.users_name, 
			new.location, new.purchase_date, new.timestamp);
END//
DROP TRIGGER IF EXISTS after_djangoapp_computer_update//
CREATE TRIGGER after_djangoapp_computer_update AFTER UPDATE ON djangoapp_computer FOR EACH ROW
BEGIN
INSERT INTO djangoapp_computerhistory(id, computer_name, IP_address, MAC_address, operating_system_id, users_name,
			location, purchase_date, timestamp) 
            
            VALUES(new.id, new.computer_name, new.IP_address, new.MAC_address, new.operating_system_id, new.users_name, 
			new.location, new.purchase_date, new.timestamp);
END//
DELIMITER ;
