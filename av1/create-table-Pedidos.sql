CREATE TABLE Pedidos (
    order_id INT PRIMARY KEY,
    purchase_date DATE,
    payments_date DATE,
    buyer_email VARCHAR(255),
    buyer_name VARCHAR(255),
    cpf VARCHAR(11),
    buyer_phone_number VARCHAR(20),
    ship_service_level VARCHAR(100),
    recipient_name VARCHAR(255),
    ship_address_1 VARCHAR(255),
    ship_address_2 VARCHAR(255),
    ship_address_3 VARCHAR(255),
    ship_city VARCHAR(100),
    ship_state VARCHAR(100),
    ship_postal_code VARCHAR(20),
    ship_country VARCHAR(100),
    ioss_number VARCHAR(20)

);

