import os
import requests
import time
import random

# Dados fixos
IG_USER_ID = os.environ.get("IG_USER_ID")
IG_ACCESS_TOKEN = os.environ.get("IG_ACCESS_TOKEN")
GITHUB_USER = os.environ.get("GITHUB_USER")
GITHUB_REPO = os.environ.get("GITHUB_REPO")
LEGENDA_PADRAO = "Deus te enviou isso! 🙏 Mande para alguém que também precisa ler isso! Siga @DeusTeEnviouIsso #Fé #Motivação #Deus"

# Caminho das imagens no repositório
IMAGENS_DIR = "imagens"

def listar_imagens():
    return sorted([f for f in os.listdir(IMAGENS_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])

def postar_imagem(filename):
    image_url = f"https://raw.githubusercontent.com/{GITHUB_USER}/{GITHUB_REPO}/main/{IMAGENS_DIR}/{filename}"
    print(f"Fazendo upload: {image_url}")

    # 1. Cria o contêiner de mídia
    media_payload = {
        "image_url": image_url,
        "caption": LEGENDA_PADRAO,
        "access_token": IG_ACCESS_TOKEN,
    }

    media_req = requests.post(
        f"https://graph.facebook.com/v18.0/{IG_USER_ID}/media", data=media_payload
    )
    media_res = media_req.json()

    if "id" not in media_res:
        print("Erro no upload:", media_res)
        return

    creation_id = media_res["id"]

    # 2. Publica a mídia
    publish_payload = {
        "creation_id": creation_id,
        "access_token": IG_ACCESS_TOKEN,
    }

    time.sleep(5)  # aguarda o upload completar
    publish_req = requests.post(
        f"https://graph.facebook.com/v18.0/{IG_USER_ID}/media_publish", data=publish_payload
    )
    publish_res = publish_req.json()

    if "id" in publish_res:
        print(f"Post publicado com sucesso: ID {publish_res['id']}")
    else:
        print("Erro ao publicar:", publish_res)

def main():
    imagens = listar_imagens()
    if not imagens:
        print("Nenhuma imagem encontrada.")
        return

    imagem_escolhida = random.choice(imagens)
    postar_imagem(imagem_escolhida)

if __name__ == "__main__":
    main()
