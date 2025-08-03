import pandas as pd

data = {
    'Nome': ['Alice', 'Joao', 'Charlie', 'David', 'Eva', 'Diego', 'Denize', 'Claudio'],
    'Idade': [25, 30, 35, 40, 45, 60, 22, 24],
    'Profissão': ['Engenheiro', 'Médico', 'Professor', 'Advogado', 'Médico','Engenheiro', 'Estudante','Estudante'],
    'Salário': ['4500', '8000', '5000', '10000', '12000','15000', '1200','1500'],
    'Limite_Credito': ['2500', '4000', '4000', '1000', '10000','2000', '500','250'],
    'Historico_Inadimplencia': ['0', '0', '0', '1', '0','1', '0','1'],
    'Estado_Civil': ['Casamento', 'Casamento', 'Solteiro', 'Solteiro', 'Casamento','Solteiro', 'Solteiro','Solteiro'],
    'Imovel_Proprio': ['0', '0', '0', '1', '1','1', '0','0']
}

df = pd.DataFrame(data)
df.head(5)

# 1 - Gráfico de Dispersão: Salário vs Limite de Crédito
import matplotlib.pyplot as plt
import seaborn as sns

df['Salário'] = df['Salário'].astype(float)
df['Limite_Credito'] = df['Limite_Credito'].astype(float)

plt.figure(figsize=(8,6))
sns.scatterplot(data=df, x='Salário', y='Limite_Credito', hue='Profissão', style='Historico_Inadimplencia')
plt.title('Salário vs Limite de Crédito')
plt.xlabel('Salário')
plt.ylabel('Limite de Crédito')
plt.grid(True)
plt.show()
# Porque usar: ajuda a visualizar se há uma correlação entre salário e limite de crédito, e se profissões ou inadimplência impactam.

# 2 - Boxplot de Limite de Crédito por Imóvel Próprio
df['Imovel_Proprio'] = df['Imovel_Proprio'].astype(int)
plt.figure(figsize=(6,5))
sns.boxplot(x='Imovel_Proprio', y='Limite_Credito', data=df)
plt.title('Distribuição do Limite de Crédito por Imóvel Próprio')
plt.xticks([0,1], ['Sem imóvel', 'Com imóvel'])
plt.ylabel('Limite de Crédito')
plt.show()
# Porque usar: mostra se possuir imóvel próprio tende a estar associado a maiores limites.# 2 -

# 3. Gráfico de Barras: Médias de Limite de Crédito por Estado Civil e Histórico de Inadimplência
df['Historico_Inadimplencia'] = df['Historico_Inadimplencia'].astype(int)
grupo = df.groupby(['Estado_Civil', 'Historico_Inadimplencia'])['Limite_Credito'].mean().unstack()
grupo.plot(kind='bar', figsize=(8,5))
plt.title('Limite Médio de Crédito por Estado Civil e Inadimplência')
plt.ylabel('Média do Limite de Crédito')
plt.xlabel('Estado Civil')
plt.legend(title='Inadimplente', labels=['Não', 'Sim'])
plt.grid(True)
plt.show()
# Porque usar: revela como o histórico de inadimplência e estado civil afetam os limites médios.