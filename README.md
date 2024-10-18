
# SatisMetrics 📊

![SatisMetrics Logo](https://via.placeholder.com/200x100.png) <!-- Placeholder for logo, replace with actual if needed -->

## 📝 Resumo

**SatisMetrics** é uma aplicação voltada para a análise estatística de dados de satisfação de usuários, utilizando um banco de dados PostgreSQL. O objetivo principal é calcular e visualizar as principais medidas de posição e dispersão dos dados de uma pesquisa de satisfação. A aplicação calcula métricas como média, mediana, moda, variância, desvio padrão e coeficiente de variação. Além disso, fornece gráficos para facilitar a interpretação dos resultados.

## 🚀 Funcionalidades

- 🔗 Conexão com o banco de dados PostgreSQL para buscar dados de satisfação.
- 📐 Cálculo das principais medidas estatísticas:
  - 📊 **Média**
  - 🔄 **Mediana**
  - 🔢 **Moda**
  - 🎯 **Variância (populacional)**
  - 📏 **Desvio padrão (populacional)**
  - 📉 **Coeficiente de variação**
- 📊 Visualização de dados por meio de gráficos com `matplotlib`.
- 👥 Análise tanto das notas quanto do número de usuários que participaram da pesquisa.

## 🛠️ Tecnologias Utilizadas

- **Python** 🐍: Linguagem principal utilizada para implementar cálculos e visualizações.
- **PostgreSQL** 🗄️: Banco de dados relacional utilizado para armazenar os dados da pesquisa.
- **Psycopg2** 🧩: Biblioteca Python para integração com o PostgreSQL.
- **NumPy** 🔢: Biblioteca para cálculos matemáticos e estatísticos avançados.
- **SciPy** 📊: Biblioteca para cálculos de moda e outras estatísticas.
- **Matplotlib** 📈: Biblioteca para visualização gráfica de dados e estatísticas.

## 🔧 Pré-requisitos

Antes de executar o projeto, você precisará:

1. **Python 3.7+** 🐍
2. **PostgreSQL** 🎛️ instalado localmente
3. Instalar as dependências do projeto:

```bash
pip install psycopg2 numpy scipy matplotlib
```

## ⚙️ Configuração

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/SatisMetrics.git
cd SatisMetrics
```

2. Configure o banco de dados PostgreSQL. Crie a tabela `pesquisasatisfacao` com as colunas `nota` e `num_usuarios`.

```sql
CREATE TABLE pesquisasatisfacao (
    id SERIAL PRIMARY KEY,
    nota INTEGER NOT NULL,
    num_usuarios INTEGER NOT NULL
);
```

3. Configure a conexão com o banco de dados no código Python:

```python
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="estatisticas",  
            user="postgres",        
            password="root",        
            host="localhost",       
            port="5432"             
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
```

4. Execute o script principal:

```bash
python main.py
```

## 📊 Como Usar

1. Execute o script e ele buscará os dados do banco de dados, calculando as estatísticas.
2. No terminal, você verá a saída com a média, mediana, moda, variância e desvio padrão.
3. Gráficos serão exibidos visualmente para mostrar a distribuição e os dados estatísticos.

## 📈 Exemplos de Gráficos

### Gráfico de Distribuição de Notas
![Distribuição de Notas](https://via.placeholder.com/500x300.png) <!-- Placeholder, replace with actual image -->

### Gráfico de Estatísticas
![Estatísticas](https://via.placeholder.com/500x300.png) <!-- Placeholder, replace with actual image -->

## 🔮 Futuras Melhorias

- 🖥️ Adicionar uma interface gráfica (GUI) para facilitar a interação.
- 🔍 Mais opções de filtragem e análise de dados.
- 🌐 Suporte a outros bancos de dados além de PostgreSQL.

## 🤝 Contribuições

Contribuições são bem-vindas! Abra uma issue ou envie um pull request se desejar colaborar.
