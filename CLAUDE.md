# Arbeitsnotizen

Öffentliches Repo, nur wegen GitHub Pages. **Keine personenbezogenen oder
konkreten Daten committen** (Namen, Beträge, Sätze, Tätigkeiten, Backups,
Testdaten). Im Code und in Commits nur neutrale Begriffe: „Person“,
„Tätigkeit“, „Konto“. README bleibt ein Satz.

## Projektbeschreibung
Konzept, Entscheidungen und Tests liegen im privaten Repo
`nomiknomik/tagesdoku-backup` unter `zeitabrechnung/` (KONZEPT.md, tests/).
Zu Beginn jeder Sitzung dieses Repo per `add_repo` (access: push) hinzufügen
und das Konzept lesen; Konzeptänderungen dort pflegen.

## Arbeitsweise
- Direkt auf `main` (Pages liefert aus `main`, App unter `/app/`). Kein PR.
- `app/`: bei jeder Änderung `APP_VERSION` + `APP_BUILD` in `index.html`
  **und** `CACHE` in `sw.js` hochzählen.
- Vor dem Push testen: die Playwright-Skripte aus dem privaten Repo
  (`zeitabrechnung/tests/`, Anleitung dort) – Chromium unter
  `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`, `serviceWorkers:'block'`.
- Icon: `python3 make_icon.py` (Pillow).

## Fallen
- Alles in einer Datei `app/index.html`. Geld in Cent, Zeit in Minuten,
  Datum als 'YYYY-MM-DD' über UTC-Tagesnummern (`dnum`/`vonNum`).
- Synchronisiert wird `D` (Bereiche in `BEREICHE`), gerätelokal `L`
  (Name, Thema, aktive Person) und `za_sync` (Zugangsdaten, nie im Backup).
- Sync: Drei-Wege-Merge je Datensatz-ID gegen Basis (IndexedDB `kv/basis`);
  Löschen = Datensatz fehlt, keine Tombstones nötig. Neue Bereiche in
  `BEREICHE` aufnehmen, sonst werden sie nicht abgeglichen.
- Einträge speichern ihren Stundensatz (`cent`); `satzAm()` nur beim
  Erfassen bzw. nach Rückfrage bei Satzänderung.
- Wischen/Halten: `touchend` mit `preventDefault` + `klickSperre`, sonst
  schließt der Nach-Klick das gerade geöffnete Sheet.
- Service Worker: Seite network-first, `api.github.com` nie über den SW.
