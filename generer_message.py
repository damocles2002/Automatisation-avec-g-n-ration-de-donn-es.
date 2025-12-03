# generateur_messages.py
import pandas as pd
from anthropic import Anthropic
import time

# ============================================================
# ⚠️ REMPLACEZ ICI PAR VOTRE CLÉ API
# ============================================================
CLE_API = "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"

def generer_message_personnalise(prospect):
    client = Anthropic(api_key=CLE_API)

    prompt = f"""Bonjour [Prénom],

En tant que [Poste] chez [Entreprise], vous jonglez probablement avec de nombreux défis liés à la génération de leads et au suivi des prospects dans le secteur [Secteur].

Nous aidons des entreprises comme la vôtre à automatiser leurs processus marketing grâce à l'IA, ce qui permet de gagner jusqu'à 10 heures par semaine et d'améliorer la qualité de qualification des leads de 40%.

Seriez-vous disponible pour un échange rapide de 15 minutes la semaine prochaine ? J'aimerais comprendre vos défis actuels et voir comment nous pourrions vous aider concrètement."""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=300,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text.strip()
    except Exception as e:
        print(f"Erreur : {e}")
        return f"[Erreur pour {prospect['prenom']}]"

# PROGRAMME PRINCIPAL
if __name__ == "__main__":
    print("=" * 60)
    print("GÉNÉRATEUR DE MESSAGES IA")
    print("=" * 60)
    print()

    # Charger les potentiels clients = prostects
    print("Chargement des prospects...")
    try:
        df = pd.read_csv("prospects.csv")
        print(f"{len(df)} prospects chargés\n")
    except FileNotFoundError:
        print("ERREUR : prospects.csv introuvable")
        print("Exécutez d'abord simulation_prospects.py\n")
        exit()

    # Générer les messages
    print(f"Génération de {len(df)} messages...")
    print(f"Durée estimée : {len(df) * 2} secondes\n")

    messages = []

    for index, prospect in df.iterrows():
        print(f"[{index+1}/{len(df)}]  {prospect['prenom']} {prospect['nom']}...")

        message = generer_message_personnalise(prospect)
        messages.append(message)

        # ce qui est vu
        apercu = message[:60] + "..." if len(message) > 60 else message
        print(f"  {len(message)} caractères")
        print(f"\"{apercu}\"\n")

        # Pause entre appels API
        if index < len(df) - 1:
            time.sleep(2)

    # Sauvegarder
    print("Sauvegarde...")
    df['message_ia'] = messages
    df.to_csv("prospects_avec_messages.csv", index=False, encoding='utf-8-sig')

    print("\n" + "=" * 60)
    print("TERMINÉ !")
    print("=" * 60)
    print(f"\n {len(messages)} messages générés")
    print(f"Fichier : prospects_avec_messages.csv\n")

    # test
    print("=" * 60)
    print("EXEMPLE DE MESSAGE")
    print("=" * 60)
    exemple = df.iloc[0]
    print(f"\n{exemple['prenom']} {exemple['nom']}")
    print(f"   {exemple['poste']} chez {exemple['entreprise']}")
    print(f"\n Message :\n")
    print("-" * 60)
    print(exemple['message_ia'])
    print("-" * 60)
    print()