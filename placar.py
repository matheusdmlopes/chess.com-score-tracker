import requests
import time


username = "matheusdemarcolopes"  
placar_arquivo = "placar.txt"
modo_de_jogo = "chess_rapid"  
intervalo = 60  

def obter_placar(username, modo):
    """Obtém o placar do Chess.com para o modo especificado."""
    try:
        
        url = f"https://api.chess.com/pub/player/{username}/stats"
        headers = {
            "User-agent": "ChessScoreTracker/1.0 (username: matheusdemarcolopes; contact: matheusdemarcolopes@gmail.com)"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        stats = response.json()
        if modo not in stats:
            print(f"Modo de jogo '{modo}' não encontrado para o usuário {username}.")
            return None, None, None

        record = stats[modo]["record"]
        return record["win"], record["loss"], record["draw"]
    except Exception as e:
        print(f"Erro ao obter dados da API: {e}")
        return None, None, None

def atualizar_placar():
    """Atualiza o placar no arquivo."""
    vitorias, derrotas, empates = obter_placar(username, modo_de_jogo)
    if vitorias is None:
        print("Placar não atualizado devido a um erro.")
        return

    with open(placar_arquivo, "w") as f:
        f.write(f"V: {vitorias}\nE: {empates}\nD: {derrotas}")
    print(f"Placar atualizado! V: {vitorias} E: {empates} D: {derrotas}")

while True:
    atualizar_placar()
    time.sleep(intervalo)
