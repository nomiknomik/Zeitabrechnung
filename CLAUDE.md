# Arbeitsnotizen

Öffentliches Repo, nur wegen GitHub Pages. **Keine personenbezogenen oder
konkreten Daten committen** (Namen, Beträge, Sätze, Tätigkeiten, Backups).
Im Code und in Commits nur neutrale Begriffe: „Person“, „Tätigkeit“, „Konto“.
README bleibt ein Satz.

## Projektbeschreibung
Konzept und Entscheidungen liegen im privaten Repo
`nomiknomik/tagesdoku-backup` unter `zeitabrechnung/KONZEPT.md`.
Zu Beginn jeder Sitzung dieses Repo per `add_repo` (access: push) hinzufügen
und das Konzept lesen; Konzeptänderungen dort pflegen.

## Arbeitsweise
- Direkt auf `main` (Pages liefert aus `main`). Kein PR.
- `app/`: bei jeder Änderung `APP_VERSION` in `index.html` **und** `CACHE`
  in `sw.js` hochzählen.
- Vor dem Push rendern: Playwright gegen `app/index.html` bei 390 × 844,
  hell und dunkel; Chromium unter `/opt/pw-browsers/chromium`,
  `serviceWorkers:'block'`.
