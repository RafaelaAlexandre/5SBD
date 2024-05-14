
INSERT INTO ItensPedido (order_item_id, order_id, sku, product_name, quantity_purchased, currency, item_price)
SELECT [order-item-id], [order-id], sku, [product-name], [quantity-purchased], currency, [item-price]
FROM carga;
