# simulation_prospects.py
import pandas as pd
import random

def generer_prospects(nombre=20):
    prenoms = ["Sophie", "Thomas", "Marie", "Lucas", "Emma", "Nicolas", "Julie", "Alexandre"]
    noms = ["Martin", "Bernard", "Dubois", "Laurent", "Simon", "Michel", "Lefebvre", "Moreau"]
    postes = ["Directeur Marketing", "Responsable Commercial", "CEO", "CMO", "Directeur des Ventes"]
    entreprises = ["TechCorp", "InnovSolutions", "DataPro", "CloudServices", "GrowthLab"]
    secteurs = ["SaaS", "E-commerce", "Consulting", "Tech", "Services"]

    prospects = []
    for i in range(nombre):
        prenom = random.choice(prenoms)
        nom = random.choice(noms)
        entreprise = random.choice(entreprises)

        prospect = {
            "prenom": prenom,
            "nom": nom,
            "poste": random.choice(postes),
            "entreprise": entreprise,
            "secteur": random.choice(secteurs),
            "linkedin_url": f"https://linkedin.com/in/{prenom.lower()}-{nom.lower()}",
            "email": f"{prenom.lower()}.{nom.lower()}@{entreprise.lower()}.com"
        }
        prospects.append(prospect)

    return pd.DataFrame(prospects)

# pour afficher dans le tableau CSV
print("Génération des prospects...")
df = generer_prospects(20)
df.to_csv("prospects.csv", index=False)
print("20 prospects générés !")
print(df.head())