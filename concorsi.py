import feedparser
import smtplib
from email.mime.text import MIMEText
import os
from datetime import datetime
import feedparser
import smtplib
from email.mime.text import MIMEText
import os
from datetime import datetime
import ssl

def cerca_concorsi():
    feed_url = "https://www.gazzettaufficiale.it/rss/S4"
    ssl._create_default_https_context = ssl._create_unverified_context
    feed = feedparser.parse(feed_url) #<<WORKS!!

    parole_chiave = [
        "ingegneria informatica",
        "informatica",
        "laurea magistrale",
        "laurea in informatica",
        "ingegneria"
    ]

    trovati = []

    for entry in feed.entries:
        titolo = entry.title.lower()
        descrizione = entry.description.lower()

        if any(kw in titolo or kw in descrizione for kw in parole_chiave):
            trovati.append(f"{entry.title}\n{entry.link}\n")

    return trovati

def invia_email(messaggio):
    mittente = os.environ.get("EMAIL_MITTENTE")
    password = os.environ.get("EMAIL_PASSWORD")
    destinatario = os.environ.get("EMAIL_DESTINATARIO")

    msg = MIMEText(messaggio)
    msg['Subject'] = "📢 Concorsi per Ingegneria Informatica trovati"
    msg['From'] = mittente
    msg['To'] = destinatario

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(mittente, password)
            server.send_message(msg)
        print("✅ Email inviata con successo.")
    except Exception as e:
        print("❌ Errore nell'invio email:", e)

if __name__ == "__main__":
    print(f"Esecuzione: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    risultati = cerca_concorsi()

    if risultati:
        testo = "\n\n".join(risultati)
        print("🔎 Concorsi trovati:\n" + testo)
        invia_email(testo)
    else:
        print("✅ Nessun concorso pertinente trovato questa settimana.")

def cerca_concorsi():
    feed_url = "https://www.gazzettaufficiale.it/rss/S4"
    feed = feedparser.parse(feed_url)

    parole_chiave = [
        "ingegneria informatica",
        "informatica",
        "laurea magistrale",
        "laurea in informatica"
    ]

    trovati = []

    for entry in feed.entries:
        titolo = entry.title.lower()
        descrizione = entry.description.lower()

        if any(kw in titolo or kw in descrizione for kw in parole_chiave):
            trovati.append(f"{entry.title}\n{entry.link}\n")

    return trovati

def invia_email(messaggio):
    mittente = os.environ.get("EMAIL_MITTENTE")
    password = os.environ.get("EMAIL_PASSWORD")
    destinatario = os.environ.get("EMAIL_DESTINATARIO")

    msg = MIMEText(messaggio)
    msg['Subject'] = "📢 Concorsi per Ingegneria Informatica trovati"
    msg['From'] = mittente
    msg['To'] = destinatario

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(mittente, password)
            server.send_message(msg)
        print("✅ Email inviata con successo.")
    except Exception as e:
        print("❌ Errore nell'invio email:", e)

if __name__ == "__main__":
    print(f"Esecuzione: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    risultati = cerca_concorsi()

    if risultati:
        testo = "\n\n".join(risultati)
        print("🔎 Concorsi trovati:\n" + testo)
        invia_email(testo)
    else:
        print("✅ Nessun concorso pertinente trovato questa settimana.")
