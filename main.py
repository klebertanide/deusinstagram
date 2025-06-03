from insta_utils import postar_no_instagram
import os
import csv

LEGENDA_PADRAO = "Deus te enviou isso! 🙏 Mande para alguém que também precisa ler isso! Siga @DeusTeEnviouIsso #Fé #Motivação #Deus"

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

    caminho = os.path.join("imagens", imagem)
    sucesso = postar_no_instagram(caminho, LEGENDA_PADRAO)
    if sucesso:
        registrar_postagem(imagem)
        print(f"Postado: {imagem}")
    else:
        print("Erro ao postar imagem.")

if __name__ == "__main__":
    main()
