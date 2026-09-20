# Deployment-Anleitung · GitHub (Browser) & Streamlit Cloud

> ⚠️ **Wichtig:** Alle GitHub-Schritte hier im Browser mit dem privaten Account
> `joelkamber@ggs.ch` durchführen – **nicht** mit GitHub Desktop (dort ist dein
> `solarify.ch`-Business-Account eingeloggt).

## 1 · Repo im Browser anlegen (privater Account)

1. Browser öffnen und sicherstellen, dass auf **github.com** oben rechts das
   Profilbild des **privaten Accounts** angezeigt wird. Falls nicht: rechts oben
   ausloggen und mit `joelkamber@ggs.ch` einloggen.
2. Rechts oben `+` → **New repository**.
3. Ausfüllen:
   - **Owner:** dein privater User (`joelkamber` o.ä.)
   - **Repository name:** `sobv-instrumentenparcours`
   - **Description:** *Interaktiver Instrumentenparcours zum 125-Jahr-Jubiläum SOBV*
   - **Visibility:** *Private* (empfohlen)
   - **Add a README, .gitignore, license:** **alle drei leer lassen** (haben wir schon)
4. **Create repository** klicken.

## 2 · Lokale Dateien hochladen (ohne CLI, ohne GitHub Desktop)

Auf der leeren Repo-Seite → Button **„uploading an existing file"** (Link mitten
im Screen). Alternative URL:
`https://github.com/<user>/sobv-instrumentenparcours/upload/main`

1. **Finder öffnen** und im Ordner
   `/Users/joelkamber/Desktop/SOBV/Instrumentenparcours` alle Dateien und
   Ordner **ausser** diese hier auswählen:
   - `.venv/`, `venv/` (falls vorhanden)
   - `__pycache__/`
   - `.DS_Store`
   - `data/` (nur den Inhalt, `.gitkeep` bleibt)
   - Falls vorhanden: private Sound-Rohdateien
2. Ausgewählte Dateien ins **Drop-Feld ziehen** (unterstützt Ordner).
3. Ganz unten: Commit-Message `Initial project setup`, dann **Commit changes**.

## 3 · Streamlit Community Cloud verbinden

1. **share.streamlit.io** öffnen, mit **GitHub** einloggen – wieder darauf achten,
   dass der **private Account** aktiv ist.
2. Falls Streamlit noch nicht auf den Account autorisiert wurde, den OAuth-Dialog
   akzeptieren.
3. **New app** → **From existing repo**.
4. Auswählen:
   - **Repository:** `<user>/sobv-instrumentenparcours`
   - **Branch:** `main`
   - **Main file path:** `Home.py`
5. **Deploy!** klicken. Der erste Build dauert 1–2 Minuten.
6. Streamlit liefert eine URL wie `https://sobv-instrumentenparcours.streamlit.app`.

## 4 · Änderungen künftig einspielen

Da wir kein GitHub Desktop nutzen: Änderungen im Browser hochladen.

- **Kleine Änderungen:** Datei im GitHub-UI öffnen → ✏️-Icon → editieren → *Commit*.
- **Neue oder ersetzte Dateien** (z.B. Sound-Files):
  1. Im Repo in den Ordner navigieren (`assets/sounds/memory/`).
  2. Rechts oben **Add file → Upload files**.
  3. Files reinziehen → *Commit*.
- Streamlit Cloud deployt automatisch neu, sobald `main` sich ändert (~30–60 s).

## 5 · Sound-Files für Station 6 nachreichen

Sobald du die Instrumentensounds bereit hast:

1. Auf GitHub in `assets/sounds/memory/` navigieren.
2. **Add file → Upload files** → deine `trompete.mp3`, `posaune.mp3`, … reinziehen.
3. Commit. Streamlit deployt neu, das Memory funktioniert sofort.

Konventionen für Dateinamen siehe [`assets/sounds/memory/README.md`](assets/sounds/memory/README.md).

## Troubleshooting

| Problem | Lösung |
|---------|--------|
| Streamlit Cloud zeigt „ModuleNotFoundError" | Modul in `requirements.txt` ergänzen und committen. |
| Ich sehe im GitHub-UI meinen Business-Account | Rechts oben ausloggen, mit `joelkamber@ggs.ch` einloggen, privates Fenster hilft ebenfalls. |
| App startet, aber Sidebar-Links zeigen alle Seiten | Beabsichtigt in der lokalen Dev-Ansicht (versteckt via CSS für Kiosk-Betrieb). |
| Highscore verschwindet nach Redeploy | Streamlit Cloud hat kein persistentes FS. Für persistente Highscores kommt später eine externe Storage-Lösung dazu (z. B. Google Sheet oder Supabase). |
