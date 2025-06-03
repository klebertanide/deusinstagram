from insta_utils import postar_no_instagram
import os
import csv

def proxima_imagem():
    imagens = sorted([
        f for f in os.listdir("imagens")
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ])
    postadas = []
    if os.path.exists("post_log.csv"):
        with open("post_log.csv", newline='') as f:
            postadas = [row[0] for row in csv.reader(f)]

    for img in imagens:
        if img not in postadas:
            return img
    return None

def registrar_postagem(nome_arquivo):
    with open("post_log.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([nome_arquivo])

def main():
    imagem = proxima_imagem()
    if not imagem:
        print("Nenhuma imagem nova para postar.")
        return

    legenda = os.path.splitext(imagem)[0].replace("-", " ").replace("_", " ")
    caminho = os.path.join("imagens", imagem)
    sucesso = postar_no_instagram(caminho, legenda)
    if sucesso:
        registrar_postagem(imagem)
        print(f"Postado: {imagem}")
    else:
        print("Erro ao postar imagem.")

if __name__ == "__main__":
    main()
