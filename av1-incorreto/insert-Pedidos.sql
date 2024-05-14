
INSERT INTO Pedidos (order_id, purchase_date, payments_date, buyer_email, buyer_name, cpf, buyer_phone_number, ship_service_level, recipient_name, ship_address_1, ship_address_2, ship_address_3, ship_city, ship_state, ship_postal_code, ship_country, ioss_number)
SELECT DISTINCT [order-id], [purchase-date], [payments-date], [buyer-email], [buyer-name], cpf, [buyer-phone-number], [ship-service-level], [recipient-name], [ship-address-1], [ship-address-2], [ship-address-3], [ship-city], [ship-state], [ship-postal-code], [ship-country], [ioss-number]
FROM carga;

