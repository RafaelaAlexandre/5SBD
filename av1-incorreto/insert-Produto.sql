
-- Inserindo dados na tabela de Produtos
INSERT INTO Produto (sku, product_name, quantity_in_stock, unit_price)
SELECT DISTINCT sku, [product-name], 0 , 500 -- Inicializando a quantidade em estoque como 0
FROM carga
WHERE sku NOT IN (SELECT sku FROM Produto);

