
CREATE TABLE ItensPedido (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    FOREIGN KEY (order_id) REFERENCES Pedidos(order_id),
    sku VARCHAR(50),
    product_name VARCHAR(255),
    quantity_purchased INT,
    currency VARCHAR(3),
    item_price DECIMAL(10, 2)
  
);

