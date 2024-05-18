# Passo a Passo para execução da tarefa

## 1. Etapa: Import do Arquivo Carga

Para a fase incial do projeto foi utilizado um aqruivo .csv com os dados que foram usados nessa atividade com a seguinte estrutura:


|order-id|order-item-id|purchase-date|payments-date|buyer-email|buyer-name|cpf|buyer-phone-number|sku|product-name|quantity-purchased|currency|item-price|ship-service-level|recipient-name|ship-address-1|ship-address-2|ship-address-3|ship-city|ship-state|ship-postal-code|ship-country|ioss-number|
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|

Para essa tarefa, foi utilizado a ferramenta  **Ferramenta de Importanção e Exportação do sql server** 

Essa ferramenta gera um arquivo dtsx como resultado da execução que está contido no repositósio.

Nessa etapa é criado a tabela Temporaria que receberá contém as informações que são distribuidas e processadas entre as tabelas.

## 2. Etapa: Criação das Tabelas

Nessa etapa foi criada a estrututa das Tabelas:
- Pedidos 

|id|dataPedido|dataPagamento|moeda|valorTotal|id_cliente|status|
|-|-|-|-|-|-|-|

- Produtos

|id|nome|SKU|quantidade_estoque|
|-|-|-|-|
- Clientes

|id|nome|email|telefone|cpf|endereco_linha1|endereco_linha2|endereco_linha3|cidade|estado|codigo_postal|pais|
|-|-|-|-|-|-|-|-|-|-|-|-|
- ItensPedidos

|id|valor|quantidade|moeda|id_pedido|id_produto|
|-|-|-|-|-|-|
- Movimentação de estoque

|id|quantidade|dataMovimentacao|id_pedido|id_produto|Transacao|
|-|-|-|-|-|-|
- Compras

|id|quantidade|data_compra|id_produto|id_pedido|
|-|-|-|-|-|

utilizando o scirpt **criar_tabela** contida no caminho:
`.\av1\scirpt\criar_tabela.sql`

## 3. Etapa: Preencher Dados nas tabelas

Nessa etapa, são preenchidas as tabelas *Pedidos*, *Produtos*, *Clientes*, *ItensPedidos*. Os campos das tabelas são preenchidas com as informações contidas na tabela Carga.

### - Pedidos:

    - id: preenchido pelo campo [order-id]
    - dataPedido: preenchido pelo campo [purchase-date]
    - dataPagamento: preenchido pelo campo [payments-date]
    - Moeda: preenchido pelo campo [currency]
    - valorTotal: é o resultado do somatorio de [item-price]*[quantity-purchased]
    - id_cliente: preenchido pelo campo id da tabela Clientes
    - status: preenchida com 'em andamento'

### - Produtos:

    - id: primery key
    - name: preenchido por [product-name]
    - SKU: Preenchido por [sku]
    - quantidade_estoque: preenchido com 0

### - Clientes:
    
    - nome: preenchido por [buyer-name]
    - email: preenchido por [buyer-email]
    - telefone: preenchido por [buyer-phone-number]
    - cpf: preenchido por cpf
    - endereco_linha1: preenchido por [ship-address-1]
    - endereco_linha2: preenchido por [ship-address-2]
    - endereco_linha3: preenchido por [ship-address-3]
    - cidade: preenchido por [ship-city]
    - estado: preenchido por [ship-state]
    - codigo_postal: preenchido por [ship-postal-code]    
    - pais: preenchido por [ship-country]

### - ItensPedidos:

    - valor: preenchido por [item-price]
    - quantidade: preenchido por [quantity-purchased]
    - id_pedido: preenchido por id da tabela Pedidos
    - id_produto; preenchido por id da tabela Produtos

Utilizando a procedure **preencher_tabela** contida no caminho: `.\av1\procedure\preencher_tabela.sql`

Nessa etapa, as tabelas *Movimentação de estoque* e *Compras* não são preenchidas.

## 4. Etapa: Processar os Pedidos

Nessa etapa os pedidos são faturados. 

Essa procedure é responsável por processar pedidos na tabela `Pedidos`, verificando o estoque disponível para cada item do pedido e realizando as operações necessárias de movimentação de estoque e atualização de status. Segue os seguintes passos:

1. **Declaração de Variáveis**:
    - `@PedidoID` (VARCHAR(50)): armazena o ID do pedido atual.
    - `@ValorTotal` (DECIMAL(10,2)): armazena o valor total do pedido atual.
    - `@PedidoStatus` (VARCHAR(50)): armazena o status atual do pedido.
    - `@QuantidadeFaltando` (INT): armazena a quantidade total de itens faltantes para compra.

2. **Declaração e Abertura do Cursor**:
    - **Cursor**: Um cursor chamado `PedidoCursor` é declarado para percorrer todos os pedidos na tabela `Pedidos` que possuem status diferente de 'Processado', ordenados pelo valor total em ordem decrescente.
    - **Abertura do Cursor**: O cursor é aberto para iniciar a iteração sobre os pedidos.

3. **Iteração sobre os Pedidos**:
    - **Primeiro Pedido**: A primeira linha do cursor é lida, armazenando `id` e `valorTotal` nos parâmetros `@PedidoID` e `@ValorTotal`, respectivamente.
    - **Loop**: Um loop `WHILE` continua enquanto houver pedidos a serem processados (`@@FETCH_STATUS = 0`).

4. **Processamento de Cada Pedido**:
    - **Inicialização do Status**: O status do pedido é inicialmente definido como 'Processado'.
    
    - **Verificação de Estoque**:
        - **Consulta de Estoque**: Verifica-se se há estoque suficiente para todos os itens do pedido. Se algum produto do pedido tem quantidade em estoque menor que a quantidade solicitada (`p.quantidade_estoque < ip.quantidade`), o status do pedido é definido como 'Pendente'.
        
        - **Inserção na Tabela de Compras**: Se o estoque for insuficiente:
            - Insere-se na tabela `Compras` a quantidade necessária para cada item do pedido que precisa ser comprado.
            - Calcula-se a quantidade total faltante e insere-se na tabela `Compras`.

    - **Movimentação de Estoque**:
        - **Subtração de Estoque**: Se há estoque suficiente, subtrai-se a quantidade dos itens do pedido do estoque de produtos.
        - **Inserção na Tabela de Movimentações**: Registra-se a movimentação de saída na tabela `Movimentacoes` para cada item do pedido.

5. **Atualização do Status do Pedido**:
    - **Atualização de Status**: Atualiza-se o status do pedido na tabela `Pedidos` para 'Processado' ou 'Pendente', dependendo do resultado da verificação de estoque.

6. **Iteração para Próximo Pedido**:
    - **Próximo Pedido**: Avança-se para o próximo pedido no cursor e repete-se o processo.

7. **Fechamento e Desalocação do Cursor**:
    - **Fechamento do Cursor**: Fecha-se o cursor após a conclusão do loop.
    - **Desalocação do Cursor**: Desaloca-se o cursor para liberar os recursos.

### Resumo

A procedure `faturar_pedido` percorre pedidos não processados, verifica o estoque disponível para os itens do pedido, atualiza o estoque e o status do pedido, insere registros nas tabelas de compras e movimentações conforme necessário, e finalmente atualiza o status do pedido na tabela `Pedidos`. Se faltar estoque, registra-se a necessidade de compra.

Utilizando a procedure *faturar_pedido* contida no caminho `.\av1\procedure\faturar_pedido.sql`

## 5. Etapa: Processar Compras

Nessa etapa os itens que estão pendentes são comprados.

A procedure SQL chamada `efetuar_compra` tem como objetivo atualizar o estoque de produtos com base nas compras registradas na tabela `Compras`, registrar essas movimentações na tabela `Movimentacoes` e então remover os registros processados da tabela `Compras`. Vamos detalhar o funcionamento desta procedure passo a passo:

1. **Declaração de Variáveis**:
    - `@CompraID` (INT): armazena o ID da compra atual.
    - `@Quantidade` (INT): armazena a quantidade da compra atual.
    - `@DataMovimentacao` (DATETIME): armazena a data da compra.
    - `@ProdutoID` (INT): armazena o ID do produto da compra atual.
    - `@PedidoID` (VARCHAR(50)): armazena o ID do pedido associado à compra atual.

2. **Declaração e Abertura do Cursor**:
    - **Cursor**: Um cursor chamado `CompraCursor` é declarado para percorrer todos os registros na tabela `Compras`.
    - **Abertura do Cursor**: O cursor é aberto para iniciar a iteração sobre as compras.

3. **Iteração sobre as Compras**:
    - **Primeira Compra**: A primeira linha do cursor é lida, armazenando `id`, `quantidade`, `data_compra`, `id_produto` e `id_pedido` nos parâmetros `@CompraID`, `@Quantidade`, `@DataMovimentacao`, `@ProdutoID` e `@PedidoID`, respectivamente.
    - **Loop**: Um loop `WHILE` continua enquanto houver compras a serem processadas (`@@FETCH_STATUS = 0`).

4. **Processamento de Cada Compra**:
    - **Atualização de Estoque**:
        - O estoque do produto (`Produtos`) é atualizado, aumentando a quantidade em estoque com a quantidade comprada (`@Quantidade`).

    - **Inserção na Tabela de Movimentações**:
        - Uma nova entrada é inserida na tabela `Movimentacoes` para registrar a compra, incluindo a quantidade comprada, a data da movimentação, o ID do pedido e do produto, e o tipo de transação ('Comprado').

    - **Remoção do Registro de Compra**:
        - O registro processado é removido da tabela `Compras` usando o ID da compra (`@CompraID`).

5. **Iteração para Próxima Compra**:
    - **Próxima Compra**: Avança-se para o próximo registro de compra no cursor e repete-se o processo.

6. **Fechamento e Desalocação do Cursor**:
    - **Fechamento do Cursor**: Fecha-se o cursor após a conclusão do loop.
    - **Desalocação do Cursor**: Desaloca-se o cursor para liberar os recursos.

### Resumo

A procedure `efetuar_compra` efetua o processo de atualização do estoque de produtos com base nas compras registradas, registra essas movimentações na tabela `Movimentacoes` e remove os registros processados da tabela `Compras`. Este procedimento assegura que o estoque seja incrementado conforme as compras são processadas e que as movimentações sejam registradas para rastreabilidade.

Utilizando a procedure *efetuar_compra* contida no caminho: `.\av1\procedure\efetuar_compra.sql`

## Finalização:

As etapas **4** e **5** devem ser repetidas até que todos os pedidos estejam com o status *processado*. Para evitar esse processo Manual foi criada a procedure `automatizar_processo` descrita na **Etapa Extra**

## Etapa Extra: Essa etapa substitui as etapas de 3 - 5

Nesta etapa, executamos uma procedure que repete os processos descritos até que todos os pedidos sejam Faturados. 

A procedure `automatizar_processo` é uma rotina que automatiza a integração de várias outras procedures para gerenciar pedidos, atualizar o estoque e exibir resultados. Vamos detalhar o funcionamento desta procedure passo a passo:

1. **Execução Inicial**:
    - **Execução da Procedure `preencher_tabela`**:
      - A procedure `preencher_tabela` é chamada. Esta procedure insere ou atualiza dados na tabela que serão utilizados no processo subsequente **[etapa 3]**.

2. **Declaração e Inicialização de Variável**:
    - **Declaração de Variável**: 
      - `@PedidosPendentes` (INT): armazena o número de pedidos com status diferente de 'Processado'.
    - **Inicialização da Variável**:
      - `@PedidosPendentes` é definido como o número de registros na tabela `Pedidos` onde o status não é 'Processado'.

3. **Loop de Processamento**:
    - **Condição de Loop**: O loop `WHILE` continua enquanto houver pedidos pendentes (`@PedidosPendentes > 0`).
    - **Dentro do Loop**:
        - **Execução da Procedure `faturar_pedido`**:
          - A procedure `faturar_pedido` é chamada para processar os pedidos, verificando o estoque e atualizando o status dos pedidos **[Etapa 4]**.
        - **Execução da Procedure `efetuar_compra`**:
          - A procedure `efetuar_compra` é chamada para atualizar o estoque com base nas compras registradas e remover esses registros da tabela  `Compras` **[Etapa 5]**.
        - **Atualização de Pedidos Pendentes**:
          - `@PedidosPendentes` é atualizado para refletir o novo número de pedidos com status diferente de 'Processado'.

4. **Execução Final**:
    - **Execução da Procedure `exibir_tabela`**:
      - A procedure `exibir_tabela` é chamada, presumivelmente para exibir ou listar os dados resultantes do processamento. Essa procedure esta contida no caminho `.\av1\procedure\exibir_tabela`

### Resumo

A procedure `automatizar_processo` integra e automatiza um fluxo de trabalho completo, executando as seguintes ações:

1. **Inicialização e Preparação**:
   - Insere ou atualiza dados iniciais necessários.
   
2. **Processamento em Loop**:
   - Enquanto houver pedidos pendentes:
     - Processa os pedidos para verificar estoque e atualizar status (`faturar_pedido`).
     - Atualiza o estoque com base nas compras registradas (`efetuar_compra`).
     - Recalcula o número de pedidos pendentes.

3. **Finalização**:
   - Exibe os dados resultantes do processo para análise ou relatório.

Este procedimento facilita a automação e integração das várias etapas do processamento de pedidos e gestão de estoque, assegurando que todas as operações necessárias sejam executadas de forma coordenada e contínua até que todos os pedidos sejam processados.

