-- criar tabela Produtos
CREATE TABLE [dbo].[Produtos](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[nome] [varchar](50) NOT NULL,
	[SKU] [varchar](50) NOT NULL,
	[quantidade_estoque] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[SKU] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Produtos] ADD  DEFAULT ((0)) FOR [quantidade_estoque]
GO

-- criar tabela clientes
CREATE TABLE [dbo].[Clientes](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[nome] [varchar](50) NOT NULL,
	[email] [varchar](50) NOT NULL,
	[telefone] [varchar](50) NOT NULL,
	[cpf] [varchar](50) NOT NULL,
	[endereco_linha1] [varchar](50) NULL,
	[endereco_linha2] [varchar](50) NULL,
	[endereco_linha3] [varchar](50) NULL,
	[cidade] [varchar](50) NULL,
	[estado] [varchar](50) NULL,
	[codigo_postal] [varchar](50) NULL,
	[pais] [varchar](50) NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[cpf] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

-- criar tabela Pedidos
CREATE TABLE [dbo].[Pedidos](
	[id] [varchar](50) NOT NULL,
	[dataPedido] [datetime] NOT NULL,
	[dataPagamento] [datetime] NOT NULL,
	[moeda] [varchar](50) NULL,
	[valorTotal] [decimal](10, 2) NULL,
	[id_cliente] [int] NOT NULL,
	[status] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Pedidos] ADD  DEFAULT ('Pendente') FOR [status]
GO

ALTER TABLE [dbo].[Pedidos]  WITH CHECK ADD FOREIGN KEY([id_cliente])
REFERENCES [dbo].[Clientes] ([id])
GO

-- criar tabela ItensPedido
CREATE TABLE [dbo].[ItensPedido](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[valor] [decimal](10, 2) NOT NULL,
	[quantidade] [int] NOT NULL,
	[id_pedido] [varchar](50) NOT NULL,
	[id_produto] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[ItensPedido]  WITH CHECK ADD FOREIGN KEY([id_pedido])
REFERENCES [dbo].[Pedidos] ([id])
GO

ALTER TABLE [dbo].[ItensPedido]  WITH CHECK ADD FOREIGN KEY([id_produto])
REFERENCES [dbo].[Produtos] ([id])
GO

-- criar tabela Compras
CREATE TABLE [dbo].[Compras](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[quantidade] [int] NOT NULL,
	[data_compra] [datetime] NOT NULL,
	[id_produto] [int] NOT NULL,
	[id_pedido] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

ALTER TABLE [dbo].[Compras]  WITH CHECK ADD FOREIGN KEY([id_pedido])
REFERENCES [dbo].[Pedidos] ([id])
GO

ALTER TABLE [dbo].[Compras]  WITH CHECK ADD FOREIGN KEY([id_produto])
REFERENCES [dbo].[Produtos] ([id])
GO


-- criar tabela Movimentacoes
CREATE TABLE [dbo].[Movimentacoes](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[quantidade] [int] NOT NULL,
	[dataMovimentacao] [datetime] NOT NULL,
	[id_pedido] [varchar](50) NOT NULL,
	[id_produto] [int] NOT NULL,
	[Transacao] [varchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

