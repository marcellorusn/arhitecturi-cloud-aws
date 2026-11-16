# Proiect AWS S3 cu LocalStack și Python

## 1. Descriere

Acest proiect demonstrează utilizarea serviciului Amazon Simple Storage Service (S3), folosind LocalStack pentru simularea infrastructurii AWS pe calculatorul local.

Aplicația este realizată în Python și utilizează biblioteca Boto3 pentru comunicarea cu serviciul S3.

## 2. Tehnologii utilizate

- Python
- Amazon Web Services (AWS) – S3
- LocalStack
- Docker și Docker Compose
- Boto3

## 3. Funcționalități

Programul execută următoarele operații:

1. Creează un bucket S3.
2. Creează un fișier text de test.
3. Încarcă fișierul în bucket.
4. Afișează obiectele existente în bucket.
5. Descarcă fișierul.
6. Șterge obiectul din bucket.

## 4. Structura proiectului

```text
arhitecturi-cloud-aws/
│
├── docker-compose.yml
├── requirements.txt
├── main.py
├── README.md
├── .gitignore
├── .env
└── files/
    ├── exemplu.txt
    └── descarcat.txt
```

## 5. Instalare și configurare

Este necesară instalarea Python și Docker Desktop.

### Pornirea LocalStack

Se configurează tokenul LocalStack în fișierul `.env`, apoi se execută:

```powershell
docker compose up -d
```

### Instalarea dependențelor Python

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### Rularea aplicației

```powershell
python main.py
```

## 6. Rezultatul demonstrației

La executarea programului sunt realizate operațiile de creare a bucketului, încărcare, listare, descărcare și ștergere a fișierului.

Demonstrația confirmă funcționarea comunicării dintre aplicația Python și serviciul S3 simulat prin LocalStack.

## 7. Concluzie

Proiectul prezintă un exemplu practic de utilizare a unui serviciu de stocare în cloud AWS. LocalStack permite testarea operațiilor S3 într-un mediu local, fără utilizarea unui bucket S3 real în AWS.
