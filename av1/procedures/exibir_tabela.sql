CREATE PROCEDURE exibir_tabela
AS
BEGIN
    -- Exibir tabela Pedidos
    PRINT 'Tabela Pedidos:';
    SELECT * FROM Pedidos;

    -- Exibir tabela ItensPedido
    PRINT 'Tabela ItensPedido:';
    SELECT * FROM ItensPedido;

    -- Exibir tabela Clientes
    PRINT 'Tabela Clientes:';
    SELECT * FROM Clientes;

    -- Exibir tabela Produtos
    PRINT 'Tabela Produtos:';
    SELECT * FROM Produtos;

    -- Exibir tabela Compras
    PRINT 'Tabela Compras:';
    SELECT * FROM Compras;

    -- Exibir tabela Movimentacoes
    PRINT 'Tabela Movimentacoes:';
    SELECT * FROM Movimentacoes;
END;
