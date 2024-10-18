import psycopg2
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


# Conectar ao banco de dados PostgreSQL
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname="estatisticas", # nome do banco de dados
            user="postgres", 
            password="root",
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None


# Função para buscar o número de usuários do banco
def fetch_user_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT num_usuarios FROM pesquisasatisfacao;")
    data = cursor.fetchall()
    cursor.close()
    return [num for (num,) in data]  # Retorna uma lista de números de usuários


# Função para calcular as medidas de posição e dispersão usando biblioteca numpy
def calcular_medidas(expanded_data):
    media = np.mean(expanded_data)  # Média
    mediana = np.median(expanded_data)  # Mediana
    
    # Calcula a moda e lida com a possibilidade de retorno de valor escalar ou array
    resultado_moda = stats.mode(expanded_data, keepdims=True)  # Garante que o retorno seja um array
    moda = resultado_moda.mode[0]  # Pega a moda correta
    
    variancia = np.var(expanded_data, ddof=0)  # Variância populacional
    desvio = np.std(expanded_data, ddof=0)   # Desvio padrão populacional
    coeficiente_var = (desvio / media) * 100  # Coeficiente de variação em porcentagem
    
    return media, mediana, moda, variancia, desvio, coeficiente_var
 

# Função para plotar gráficos com matplotlib
def plot_statistics(user_data, mean, median, mode, variance, std_dev):
    # Configurações do gráfico
    fig, ax = plt.subplots(2, 3, figsize=(15, 10))

    # Histograma do número de usuários
    ax[0, 0].hist(user_data, bins=10, edgecolor='black', color='lightblue')
    ax[0, 0].set_title("Histograma do Número de Usuários")
    ax[0, 0].set_xlabel("Número de Usuários")
    ax[0, 0].set_ylabel("Frequência")

    # Gráfico de Média
    ax[0, 1].bar(['Média'], [mean], color='blue')
    ax[0, 1].set_title(f"Média: {mean:.2f}")

    # Gráfico de Mediana
    ax[0, 2].bar(['Mediana'], [median], color='green')
    ax[0, 2].set_title(f"Mediana: {median:.2f}")

    # Gráfico de Moda
    ax[1, 0].bar(['Moda'], [mode], color='orange')
    ax[1, 0].set_title(f"Moda: {mode}")

    # Gráfico de Variância
    ax[1, 1].bar(['Variância'], [variance], color='purple')
    ax[1, 1].set_title(f"Variância: {variance:.2f}")

    # Gráfico de Desvio Padrão
    ax[1, 2].bar(['Desvio Padrão'], [std_dev], color='red')
    ax[1, 2].set_title(f"Desvio Padrão: {std_dev:.2f}")

    plt.tight_layout()
    plt.show()


# Main
if __name__ == "__main__":
    conn = connect_db()
    if conn:
        # Busca o número de usuários da pesquisa de satisfação
        user_data = fetch_user_data(conn)

        # Calcula as estatísticas
        mean, median, mode, variance, std_dev, coef_var = calcular_medidas(user_data)

        # Exibe as estatísticas no console
        print(f"Média: {mean:.2f}")
        print(f"Mediana: {median:.2f}")
        print(f"Moda: {mode}")
        print(f"Variância: {variance:.2f}")
        print(f"Desvio Padrão: {std_dev:.2f}")
        print(f"Coeficiente de Variação: {coef_var:.2f}%")

        # Plota os gráficos
        plot_statistics(user_data, mean, median, mode, variance, std_dev)

        # Fecha a conexão com o banco
        conn.close()
