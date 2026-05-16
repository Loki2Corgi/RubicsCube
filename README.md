# Rubik's Cube 3D Simulation & Solver

Eine interaktive 3D-Zauberwürfel-Anwendung mit integriertem Lösungsalgorithmus, entwickelt in Python unter Verwendung der **Ursina Engine**.

---

## 🚀 Projektbeschreibung

Dieses Projekt bietet eine vollständige, interaktive 3D-Simulation eines klassischen 3x3 Rubik's Cubes. Die Anwendung kombiniert eine mathematisch präzise Würfel-Logik mit einer benutzerfreundlichen 3D-Oberfläche und einem mächtigen Solver. Entwickler und Anwender können den Würfel manuell manipulieren, über standardisierte Notationen steuern, zufällig mischen lassen oder den optimierten Lösungsweg Schritt für Schritt visuell nachvollziehen.

## ✨ Key Features

- **Interaktive 3D-Grafik:** Flüssige Darstellung, freie Kamera-Rotation (Orbit-Ansicht) und animierte Ebenen-Drehungen über die Ursina Engine.
- **Exakte Rotationslogik:** Fehlerfreie Abbildung aller mathematischen Zustände bei Drehungen nach der offiziellen Singmaster-Notation.
- **Zustands-Validierung:** Automatische Prüfung, ob eine Farbkonstellation (geladen über Asset-Dateien wie `Colors.png`) theoretisch lösbar ist.
- **Zufalls-Scrambler:** Integrierter Algorithmus zur Erzeugung valider, zufälliger Durchmischungen.
- **Integrierter Solver:** Analyse des Würfelzustands mit anschließender Berechnung und grafischer Demonstration der optimalen Lösungsschritte.
- **Move History & Steuerung:** Protokollierung aller Züge mit funktionalem Reset und Undo-System.

---

## 🗺️ Projekt-Roadmap (Meilenstein-Planung)

Die kontinuierliche Entwicklung ist in klare Phasen unterteilt und wird über zeitbasierte GitHub Project-Iterationen gesteuert:

### 📦 Meilenstein 0.3.0: Core Logic & Validation
* **Implementierung der Würfel-Rotationslogik:** Entwicklung der Kernfunktionen zur Drehung aller sechs Ebenen und Manipulation des internen 3D-Arrays.
* **Validierung des Würfel-Zustands:** Prüfung der Farbkacheln auf mathematische und strukturelle Lösbarkeit vor Spielbeginn.
* **Erkennung des gelösten Zustands:** Algorithmus zur kontinuierlichen Prüfung auf Erreichen des "Solved States" (homogene Farbseiten).

### 📦 Meilenstein 0.4.0: Scrambler & Move History
* **Zufallsbasierter Scramble-Algorithmus:** Generierung valider, zufälliger Zugfolgen zum korrekten Durchmischen des Würfels.
* **Zug-Historie (Move History Log):** Chronologische Erfassung aller Rotationen als Basis für Analysen und das Undo-System.
* **Reset- und Revert-Funktion:** Implementierung von Werkzeugen zum sofortigen Zurücksetzen des Würfels oder Rückgängigmachen des letzten Zuges.

### 📦 Meilenstein 0.5.0: Solver Integration
* **Implementierung des Lösungsalgorithmus:** Kern-Integration eines Solvers zur Berechnung des kürzesten Weges zur Lösung.
* **Visuelle Schritt-für-Schritt-Anleitung:** UI-Komponenten zur manuellen Navigation durch die berechneten Lösungsschritte.
* **Auto-Solve Animation:** Vollautomatisches, flüssig animiertes Abspielen der berechneten Lösungsschritte direkt auf dem 3D-Modell.

---

## 🛠️ Installation & Setup

### Voraussetzungen
Stelle sicher, dass **Python 3.8 oder höher** auf deinem System installiert ist.

### 1. Repository klonen
```bash
git clone [https://github.com/dein-benutzername/rubiks-cube-3d.git](https://github.com/dein-benutzername/rubiks-cube-3d.git)
cd rubiks-cube-3d
