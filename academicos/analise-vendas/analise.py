import pandas as pd
import matplotlib.pyplot as plt

# Leitura do CSV
df = pd.read_csv('dados_vendas.csv', parse_dates=['data'])

# Criar coluna de receita total
df['receita'] = df['quantidade'] * df['preco_unitario']

# Receita total por produto
receita_por_produto = df.groupby('produto')['receita'].sum()

# Receita mensal
df['mes'] = df['data'].dt.to_period('M')
receita_mensal = df.groupby('mes')['receita'].sum()

plt.figure(figsize=(8, 5))
receita_por_produto.plot(kind='bar', color='skyblue')
plt.title('Receita por Produto', fontsize=16)
plt.xlabel('Produto', fontsize=12)
plt.ylabel('Receita (R$)', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('grafico_receita_produto.png')
plt.clf()

plt.figure(figsize=(8, 5))
receita_mensal.plot(marker='o', color='seagreen')
plt.title('Receita por Mês', fontsize=16)
plt.xlabel('Mês', fontsize=12)
plt.ylabel('Receita (R$)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('grafico_receita_mensal.png')

# Gráfico 1 – Receita por produto
receita_por_produto.plot(kind='bar', title='Receita por Produto')
plt.xlabel('Produto')
plt.ylabel('Receita (R$)')
plt.tight_layout()
plt.savefig('grafico_receita_produto.png')
plt.clf()

# Gráfico 2 – Receita por mês
receita_mensal.plot(kind='line', marker='o', title='Receita por Mês')
plt.xlabel('Mês')
plt.ylabel('Receita (R$)')
plt.tight_layout()
plt.savefig('grafico_receita_mensal.png')

print("✅ Análise concluída. Gráficos salvos.")
