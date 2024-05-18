CREATE PROCEDURE efetuar_compra
AS
BEGIN
    DECLARE @CompraID INT;
    DECLARE @Quantidade INT;
    DECLARE @DataMovimentacao DATETIME;
    DECLARE @ProdutoID INT;
    DECLARE @PedidoID VARCHAR(50);

    -- Cursor para percorrer as compras
    DECLARE CompraCursor CURSOR FOR
    SELECT id, quantidade, data_compra, id_produto, id_pedido
    FROM Compras;

    -- Abrindo o cursor
    OPEN CompraCursor;

    -- Iterando sobre cada compra
    FETCH NEXT FROM CompraCursor INTO @CompraID, @Quantidade, @DataMovimentacao, @ProdutoID, @PedidoID;
    WHILE @@FETCH_STATUS = 0
    BEGIN
        -- Atualiza o estoque do produto com a quantidade da compra
        UPDATE Produtos
        SET quantidade_estoque = quantidade_estoque + @Quantidade
        WHERE id = @ProdutoID;

        -- Insere informações na tabela de movimentações
        INSERT INTO Movimentacoes (quantidade, dataMovimentacao, id_pedido, id_produto, Transacao)
        VALUES (@Quantidade, @DataMovimentacao, @PedidoID, @ProdutoID, 'Comprado');

        -- Exclui o registro da tabela de compras
        DELETE FROM Compras WHERE id = @CompraID;

        -- Avança para a próxima compra
        FETCH NEXT FROM CompraCursor INTO @CompraID, @Quantidade, @DataMovimentacao, @ProdutoID, @PedidoID;
    END;

    -- Fecha o cursor
    CLOSE CompraCursor;
    DEALLOCATE CompraCursor;
END;
