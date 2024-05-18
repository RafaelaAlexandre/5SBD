CREATE PROCEDURE preencher_tabela
AS
BEGIN
    -- Inserção na tabela Clientes
    INSERT INTO Clientes (nome, email, telefone, cpf, endereco_linha1, endereco_linha2, endereco_linha3, cidade, estado, codigo_postal, pais)
    SELECT DISTINCT
        [buyer-name],
        [buyer-email],
        [buyer-phone-number],
        cpf,
        [ship-address-1],
        [ship-address-2],
        [ship-address-3],
        [ship-city],
        [ship-state],
        [ship-postal-code],
        [ship-country]
    FROM TEMP;

    -- Inserção na tabela Produtos
    INSERT INTO Produtos (nome, SKU, quantidade_estoque)
    SELECT DISTINCT
        [product-name],
        sku,
        0
    FROM TEMP;

    -- Inserção na tabela Pedidos
    INSERT INTO Pedidos (id, dataPedido, dataPagamento, moeda, valorTotal, id_cliente, status)
    SELECT
        [order-id],
        CONVERT(DATETIME, [purchase-date], 103) AS dataPedido,
        CONVERT(DATETIME, [payments-date], 103) AS dataPagamento,
        currency AS moeda,
        SUM(CONVERT(DECIMAL(10,2), REPLACE([item-price], ',', '.') * CAST([quantity-purchased] AS DECIMAL(10,2)))) AS valorTotal,
        c.id AS id_cliente,
        'Em andamento' AS status
    FROM TEMP t
    JOIN Clientes c ON t.cpf = c.cpf
    GROUP BY [order-id], [purchase-date], [payments-date], currency, c.id;

    -- Inserção na tabela ItensPedido
    INSERT INTO ItensPedido (valor, quantidade, id_pedido, id_produto)
    SELECT
        CONVERT(DECIMAL(10,2), REPLACE(t.[item-price], ',', '.')) AS valor,
        CAST(t.[quantity-purchased] AS INT) AS quantidade,
        p.id AS id_pedido,
        prd.id AS id_produto
    FROM TEMP t
    JOIN Pedidos p ON t.[order-id] = p.id
    JOIN Produtos prd ON t.sku = prd.SKU;
END;
