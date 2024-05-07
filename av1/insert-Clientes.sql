-- Inserindo dados na tabela de Clientes
INSERT INTO Clientes (cpf, buyer_email, buyer_name, buyer_phone_number, ship_address_1, ship_address_2, ship_address_3, ship_city, ship_state, ship_postal_code, ship_country)
SELECT DISTINCT cpf, [buyer-email], [buyer-name], [buyer-phone-number], [ship-address-1], [ship-address-2], [ship-address-3], [ship-city], [ship-state], [ship-postal-code], [ship-country]
FROM carga
WHERE cpf NOT IN (SELECT cpf FROM Clientes);

