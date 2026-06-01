# Webanwendungsentwicklung mit Django – ein Python-basierter Ansatz

Dieses Projekt entstand im Rahmen meines Studiums als **Teamprojekt zusammen mit zwei Kommilitonen**. Ziel war die Entwicklung einer Webanwendung zur Erfassung und Verwaltung von Softwarefehlern (Bug-Tracking-System) unter Verwendung des Python-Frameworks Django. Zusätzlich wurde der Python-basierte Ansatz mit alternativen Web-Technologien verglichen.

## Projektaufgaben im Team
* **Backend-Entwicklung:** Implementierung der serverseitigen Logik und des Routings mit dem Django-Framework.
* **Datenbankmodellierung:** Entwurf und Umsetzung der relationalen Datenbankstruktur zur strukturierten Speicherung von Bug-Tickets.
* **Frontend-Entwicklung:** Umsetzung dynamischer Weboberflächen für die Erstellung, Bearbeitung und Verwaltung der Fehlerberichte.
* **Evaluation:** Technologischer Vergleich der Architektur und Effizienz zwischen Django und klassischen Ansätzen wie PHP.

## Hochgeladene Projektstruktur
Dieses Repository enthält die Kernkomponenten der Webanwendung:

* `buglist/` – Die Haupt-App mit der gesamten Geschäftslogik (Modelle, Views, Templates).
* `nader_django/` – Die globalen Projekteinstellungen und das Haupt-Routing.
* `static/` – Statische Dateien (wie z. B. CSS).
* `manage.py` – Das zentrale Kommandozeilen-Tool von Django.

*Hinweis: Aus Best-Practice-Gründen wurden die lokale Datenbankdatei (`db.sqlite3`) sowie temporäre Cache-Ordner (`__pycache__`) bewusst nicht in dieses Repository hochgeladen.*
