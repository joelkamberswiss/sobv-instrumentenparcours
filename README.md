# Interaktiver Instrumentenparcours · SOBV

Web-Apps für den Interaktiven Instrumentenparcours zum 125-Jahr-Jubiläum des **Solothurnischen Blasmusikverbands (SOBV)**.

Diese Streamlit-App hostet die Software-Stationen des Parcours:

| # | Station | Prinzip |
|---|---------|---------|
| 2 | Flappy Bird Blasinstrument | Blasen statt Tippen |
| 3 | Lautstärkeduell | Wer spielt am lautesten? |
| 4 | Langton-Blasen | Wer hält am längsten? |
| 6 | Instrumente-Memory | Hören statt Sehen |

## Lokal starten

```bash
pip install -r requirements.txt
streamlit run Home.py
```

## Deployment

Deployed auf **Streamlit Community Cloud**, verbunden mit diesem GitHub-Repo.

## Struktur

```
.
├── Home.py                 # Landingpage mit Kacheln
├── pages/                  # Streamlit Multi-Page-Apps (Stationen)
├── assets/
│   ├── sounds/memory/      # Instrumentensounds für Station 6
│   └── images/
├── data/                   # Highscore-Persistenz (lokal, git-ignored)
└── .streamlit/config.toml  # SOBV-Theme
```
