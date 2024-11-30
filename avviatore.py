import requests
import subprocess
import time
import random
from PIL import Image
from io import BytesIO
import cloudinary
import cloudinary.api
import cloudinary.uploader

# Sostituisci con le tue credenziali API di Cloudinary
cloudinary.config(
  cloud_name = 'xxxx',
  api_key = 'xxxx',
  api_secret = 'xxxx'
)

def verifica_esistenza_immagine_su_cloudinary(image_id):
    try:
        # Verifica l'esistenza dell'immagine su Cloudinary
        risultato = cloudinary.api.resource_by_asset_id(image_id)
        return True
    except cloudinary.exceptions.Error as e:
        print(f"Errore durante la verifica dell'esistenza dell'immagine su Cloudinary: ")
        return False

def recupera_url_immagine_da_cloudinary(image_id):
    try:
        risultato = cloudinary.api.resource_by_asset_id(image_id)
        return risultato['secure_url']
    except Exception as e:
        print(f"Errore durante il recupero dell'URL dell'immagine da Cloudinary: ")
        return None

def visualizza_immagine_da_url(image_url):
    try:
        # Visualizza l'immagine dal suo URL
        image_content = requests.get(image_url).content
        image = Image.open(BytesIO(image_content))
        image.show()
    except Exception as e:
        print(f"Errore durante la visualizzazione dell'immagine: {e}")

def mostra_messaggio_vbs(testo_messaggio):
    # Puoi personalizzare il tuo file VBS o sostituire con il tuo codice VBS
    codice_vbs = f'MsgBox "{testo_messaggio}", 0, "Messaggio"'

    try:
        # Scrivi il codice VBS in un file temporaneo
        with open('temp_script.vbs', 'w') as file_vbs:
            file_vbs.write(codice_vbs)

        # Esegui il file VBS
        subprocess.run(['wscript', 'temp_script.vbs'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Errore durante l'esecuzione del file VBS: {e}")

# Main
api_key = 'xxxx'  # Sostituisci con la tua chiave API da Pastebin
paste_code = 'xxxx'  # Sostituisci con il codice della tua paste su Pastebin
#aspetta un tempo casuale per avviare il programma
casuale = random.randrange(60,500)
time.sleep(casuale)
i=0
j=0
while True and i==0:
    contenuto = requests.get(f'https://pastebin.com/raw/{paste_code}', params={'api_dev_key': api_key}).text
    print(f"ciao:{contenuto}")
    if (len(contenuto) < 200):
        image_id = contenuto.strip()
        # Cerca l'URL dell'immagine su Cloudinary utilizzando l'ID dell'immagine

        if verifica_esistenza_immagine_su_cloudinary(image_id) != False:
            image_url = recupera_url_immagine_da_cloudinary(image_id)
            # Visualizza l'immagine
            visualizza_immagine_da_url(image_url)
            i=1
        else:
            mostra_messaggio_vbs(contenuto)
            exit()
    else:
        # Se il recupero non ha successo, aspetta 1 minuto prima di riprovare
        print("Attesa 1 minuto prima del nuovo tentativo...")
        time.sleep(60)
        if(j==1):
            # Se il secondo tentativo non ha successo, scegli casualmente un messaggio predefinito
            messaggi_predefiniti = ["xx", "xx", "xx"]
            messaggio_casuale = random.choice(messaggi_predefiniti)
            mostra_messaggio_vbs(messaggio_casuale)
            exit()
        j=1
        
