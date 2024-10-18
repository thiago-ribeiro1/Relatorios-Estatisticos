
# Relatórios Estatísticos 📊

## 📝 Resumo

Aplicação voltada para a análise estatística de dados de satisfação de usuários, utilizando um banco de dados PostgreSQL. O objetivo principal é calcular e visualizar as principais medidas de posição e dispersão dos dados de uma pesquisa de satisfação. A aplicação calcula métricas como média, mediana, moda, variância, desvio padrão e coeficiente de variação. Além disso, fornece gráficos para facilitar a interpretação dos resultados.

## 🚀 Funcionalidades

- 🔗 Conexão com o banco de dados PostgreSQL para buscar dados de satisfação de usuários.
- 📐 Cálculo das principais medidas estatísticas:
  - 📊 **Média**
  - 🔄 **Mediana**
  - 🔢 **Moda**
  - 🎯 **Variância (populacional)**
  - 📏 **Desvio padrão (populacional)**
  - 📉 **Coeficiente de variação**
- 📊 Visualização de dados por meio de gráficos com `matplotlib`.

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
git clone https://github.com/thiago-ribeiro1/Relatorios-Estatisticos.git
```

2. Configure o banco de dados PostgreSQL. Crie a base de dados, e a tabela `pesquisasatisfacao` com as colunas `nota` e `num_usuarios`.

```sql
create database estatisticas;

create table pesquisasatisfacao (
    id SERIAL PRIMARY KEY,
    nota INTEGER NOT NULL CHECK (nota >= 0 AND nota <= 10)        
    num_usuarios INTEGER NOT NULL CHECK (num_usuarios > 0) -- Número de usuários que participaram da pesquisa
);
```

3. Insira os valores na tabela:

```sql
INSERT INTO pesquisasatisfacao (nota, num_usuarios)
VALUES
    (10, 5),   -- 5 usuários deram nota 10
    (9, 10),   -- 10 usuários deram nota 9
    (8, 8),    -- 8 usuários deram nota 8
    (7, 12),   -- 12 usuários deram nota 7
    (6, 7),    -- 7 usuários deram nota 6
    (5, 9),    -- 9 usuários deram nota 5
    (4, 8),    -- 8 usuários deram nota 4
    (3, 4),    -- 4 usuários deram nota 3
    (2, 3),    -- 3 usuários deram nota 2
    (1, 2);    -- 2 usuários deram nota 1
```

4. Configure a conexão com o banco de dados no código Python:

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

5. Execute o script principal:

```bash
python main.py
```
## Visualização dos gráficos

![medidas](https://github.com/user-attachments/assets/31557d61-8783-4a7c-b819-bc574f3866ab)
