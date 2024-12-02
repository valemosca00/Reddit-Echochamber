import praw
import csv
import time
from prawcore.exceptions import TooManyRequests
from tqdm import tqdm

# Configurazione API
reddit = praw.Reddit(
    client_id="---",
    client_secret="---",
    user_agent="script"
)

# Nome del subreddit
subreddit_name = "sports"
subreddit = reddit.subreddit(subreddit_name)

data = []
posts = list(subreddit.hot(limit=100))  # Limita a 100 post per test
total_posts = len(posts)

print(f"Estrazione dei post 'hot' dal subreddit r/{subreddit_name}...")

# Contatore commenti
comment_counter = 0

for post in tqdm(posts, desc="Estrazione dei post", unit="post", ncols=100):
    try:
        # Dettagli del post
        post_data = {
            "type": "post",
            "post_id": post.id,
            "title": post.title,
            "author": str(post.author),
            "score": post.score,
            "flair": post.link_flair_text or "N/A",
            "body": post.selftext or "N/A",
        }
        data.append(post_data)

        # Recupera i commenti, sostituendo fino a 10 MoreComments
        post.comments.replace_more(limit=10)  # Carica fino a 10 blocchi di MoreComments
        for comment in post.comments.list():
            if isinstance(comment, praw.models.Comment):  # Filtra solo i commenti validi
                comment_data = {
                    "type": "comment",
                    "post_id": post.id,
                    "title": f"Commento su: {post.title}",
                    "author": str(comment.author),
                    "score": comment.score,
                    "flair": "N/A",
                    "body": comment.body,
                }
                data.append(comment_data)

                # Incrementa il contatore
                comment_counter += 1

                # Pausa ogni 50 commenti
                if comment_counter % 50 == 0:
                    time.sleep(1)

        # Pausa per evitare limiti (tra i post)
        time.sleep(1)

    except TooManyRequests:
        print("Superato il limite di richieste! Attendo 60 secondi...")
        time.sleep(60)  # Pausa più lunga in caso di errore 429
    except Exception as e:
        print(f"Errore durante l'elaborazione di un post: {e}")

# Salvataggio in CSV
output_file = "reddit_data.csv"
fields = ["type", "post_id", "title", "author", "score", "flair", "body"]

with open(output_file, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data)

print(f"Dati salvati in {output_file}!")
