CREATE PROCEDURE automatizar_processo
AS
BEGIN
    -- Executa a procedure para inserir os dados
    EXEC preencher_tabela;

    DECLARE @PedidosPendentes INT;
    SET @PedidosPendentes = (SELECT COUNT(*) FROM Pedidos WHERE status != 'Processado');

    -- Enquanto houver pedidos pendentes, continua o processamento
    WHILE @PedidosPendentes > 0
    BEGIN
        -- Executa a procedure para faturar os pedidos
        EXEC faturar_pedido;

        -- Executa a procedure para atualizar o estoque
        EXEC efetuar_compra;

        -- Atualiza a contagem de pedidos pendentes
        SET @PedidosPendentes = (SELECT COUNT(*) FROM Pedidos WHERE status != 'Processado');
    END;

	-- Executa a procedure para exibir os dados
	EXEC exibir_tabela;
END;
