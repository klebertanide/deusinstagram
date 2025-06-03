import requests
import os

TOKEN = os.getenv("IG_ACCESS_TOKEN")
IG_ID = os.getenv("IG_USER_ID")

def postar_no_instagram(imagem_path, legenda):
    print(f"Fazendo upload: {imagem_path}")
    with open(imagem_path, 'rb') as img:
        upload = requests.post(
            f"https://graph.facebook.com/v18.0/{IG_ID}/media",
            params={"access_token": TOKEN},
            data={"caption": legenda},
            files={"image": img}
        )

    resposta = upload.json()
    if "id" not in resposta:
        print("Erro no upload:", resposta)
        return False

    creation_id = resposta["id"]

    publish = requests.post(
        f"https://graph.facebook.com/v18.0/{IG_ID}/media_publish",
        params={"access_token": TOKEN},
        data={"creation_id": creation_id}
    )

    if publish.status_code == 200:
        return True
    else:
        print("Erro ao publicar:", publish.json())
        return False
