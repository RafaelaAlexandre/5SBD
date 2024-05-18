CREATE PROCEDURE faturar_pedido
AS
BEGIN
    DECLARE @PedidoID VARCHAR(50);
    DECLARE @ValorTotal DECIMAL(10,2);
    DECLARE @PedidoStatus VARCHAR(50);
    DECLARE @QuantidadeFaltando INT;

    -- Cursor para percorrer os pedidos com status diferente de 'Processado'
    DECLARE PedidoCursor CURSOR FOR
    SELECT id, valorTotal
    FROM Pedidos
    WHERE status != 'Processado'
    ORDER BY valorTotal DESC;

    -- Abrindo o cursor
    OPEN PedidoCursor;

    -- Iterando sobre cada pedido
    FETCH NEXT FROM PedidoCursor INTO @PedidoID, @ValorTotal;
    WHILE @@FETCH_STATUS = 0
    BEGIN
        SET @PedidoStatus = 'Processado'; -- Inicializa o status como Processado

        -- Verifica se há estoque para todos os itens do pedido
        IF EXISTS (
            SELECT 1
            FROM ItensPedido ip
            JOIN Produtos p ON ip.id_produto = p.id
            WHERE ip.id_pedido = @PedidoID AND p.quantidade_estoque < ip.quantidade
        )
        BEGIN
            SET @PedidoStatus = 'Pendente'; -- Se não há estoque suficiente, o status é Pendente

            -- Insere na tabela de compras a quantidade necessária para compra de cada item do pedido
            INSERT INTO Compras (quantidade, data_compra, id_produto, id_pedido)
            SELECT ip.quantidade - p.quantidade_estoque, GETDATE(), ip.id_produto, @PedidoID
            FROM ItensPedido ip
            JOIN Produtos p ON ip.id_produto = p.id
            WHERE ip.id_pedido = @PedidoID AND p.quantidade_estoque < ip.quantidade;

            -- Calcula a quantidade total faltando para compra
            SELECT @QuantidadeFaltando = SUM(ip.quantidade - p.quantidade_estoque)
            FROM ItensPedido ip
            JOIN Produtos p ON ip.id_produto = p.id
            WHERE ip.id_pedido = @PedidoID AND p.quantidade_estoque < ip.quantidade;

            -- Adiciona a quantidade total faltando à tabela de compras
            INSERT INTO Compras (quantidade, data_compra, id_produto, id_pedido)
            VALUES (@QuantidadeFaltando, GETDATE(), NULL, @PedidoID); -- Aqui você pode inserir na tabela de compras com um ID de produto NULL, ou pode definir uma lógica específica para isso
        END
        ELSE
        BEGIN
            -- Subtrai a quantidade dos itens do pedido do estoque de produtos
            UPDATE p
            SET quantidade_estoque = quantidade_estoque - ip.quantidade
            FROM Produtos p
            JOIN ItensPedido ip ON p.id = ip.id_produto
            WHERE ip.id_pedido = @PedidoID;

            -- Insere informações na tabela de movimentações
            INSERT INTO Movimentacoes (quantidade, dataMovimentacao, id_pedido, id_produto, Transacao)
            SELECT ip.quantidade, GETDATE(), @PedidoID, ip.id_produto, 'Vendido'
            FROM ItensPedido ip
            WHERE ip.id_pedido = @PedidoID;
        END;

        -- Atualiza o status do pedido
        UPDATE Pedidos
        SET status = @PedidoStatus
        WHERE id = @PedidoID;

        -- Avança para o próximo pedido
        FETCH NEXT FROM PedidoCursor INTO @PedidoID, @ValorTotal;
    END;

    -- Fecha o cursor
    CLOSE PedidoCursor;
    DEALLOCATE PedidoCursor;
END;
