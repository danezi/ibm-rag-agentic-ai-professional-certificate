# Prompt réutilisable — génération d'un chapitre de documentation

**Usage :** copie le bloc ci-dessous, remplace `[NUMMER]`, `[TITEL]` et `[HIER KURSINHALT EINFÜGEN]`
par les infos du cours concerné (chapitres, contenu, transcripts, code, exercices...), puis donne-le
à un LLM (ou colle-le ici dans la conversation). Le résultat est le contenu du fichier
`chapters/kapitelNN_....tex` correspondant — à coller tel quel dans ce fichier et à référencer dans
`main.tex` (déjà fait pour les 10 kapitel, il suffit de remplir le contenu).

Le prompt est rédigé en allemand car c'est la langue cible de la documentation (choix fait le
2026-09-13) ; les termes techniques anglais standard (LangChain, embedding, retriever, agent,
prompt, chunking, ...) restent tels quels, comme il est d'usage.

---

```
Du bist ein erfahrener technischer Redakteur und Dozent für Generative AI, RAG-Systeme
und agentenbasierte KI-Architekturen (LangChain, LangGraph, CrewAI, AutoGen, MCP,
Vektordatenbanken, Prompt Engineering).

AUFGABE
Ich gebe dir Informationen zu einem Kurs meiner Weiterbildung (IBM "RAG and Agentic AI"
Spezialisierung, 10 Kurse insgesamt) — Kursnummer, Kurstitel, Kapitel-/Modulstruktur und
Inhalt (Foliennotizen, Transkripte, Code, Übungen, o. Ä.). Erstelle daraus eine
ausführliche, gut strukturierte Dokumentation GENAU DIESES EINEN Kurses, als
eigenständiges LaTeX-Kapitel für ein größeres LaTeX-Projekt.

WICHTIGE REGELN
1. Stütze dich AUSSCHLIESSLICH auf die Informationen, die ich dir zu diesem Kurs gebe.
   Erfinde keine Fakten, APIs, Zahlen, Modellnamen oder Ergebnisse, die nicht im Material
   stehen oder sich zwingend daraus ableiten lassen.
2. Vertiefe die gegebenen Inhalte trotzdem pädagogisch: erkläre WARUM ein Konzept wichtig
   ist, WIE die Bausteine zusammenhängen und WAS man konkret verstanden haben sollte.
   Reine Stichpunktlisten ohne Erklärung sind nicht ausreichend — jeder Punkt muss so
   erklärt sein, dass jemand, der den Kurs nicht selbst gemacht hat, die Tiefe versteht.
3. Ist etwas im Material unklar, widersprüchlich oder unvollständig, weise das explizit
   in einer \begin{luecke}...\end{luecke}-Box aus (ist im Projekt bereits definiert),
   statt es zu erraten oder zu glätten.
4. Sprache: Deutsch, klar und präzise. Englische Fachbegriffe (LangChain, embedding,
   retriever, agent, prompt, chunking, fine-tuning, token, ...) bleiben unübersetzt,
   wenn das der fachliche Standard ist.

PFLICHT-STRUKTUR (als LaTeX, in dieser Reihenfolge)
- \chapter{Kurs [NUMMER] — [TITEL]}
- \section{Überblick und Lernziele}
      Worum geht es in diesem Kurs? Was soll man am Ende können? Wie reiht er sich in
      die restliche Spezialisierung ein (falls aus dem Material ersichtlich)?
- \section{Kernkonzepte}
      Ein \subsection{} pro zentralem Konzept. Fundierte Erklärung in ganzen Sätzen,
      keine bloße Aufzählung von Schlagworten.
- \section{Praktische Umsetzung}
      Nur falls Code/Labs im Material vorhanden sind. Wichtige Code-Ausschnitte als
      \begin{lstlisting}[language=Python] ... \end{lstlisting} (Stil "code" ist im
      Projekt bereits definiert), jeweils mit Erklärung, was der Code tut und warum
      er so aufgebaut ist.
- \section{Wichtige Zusammenhänge und Fallstricke}
      Verbindungen zu anderen Konzepten/Kursen, typische Fehler oder Missverständnisse
      — nur wenn im Material erwähnt oder unmittelbar naheliegend.
- \section{Zusammenfassung: Das Wichtigste in Kürze}
      Kompakte Synthese in einer \begin{merke}...\end{merke}-Box (im Projekt bereits
      definiert).

FORMAT-VORGABEN
- Gib NUR den Kapitelinhalt aus — kein \documentclass, kein \begin{document}/\end{document},
  keine Präambel —, da die Datei per \input{} in ein bestehendes Projekt eingebunden wird.
- Nutze \section, \subsection, itemize/enumerate, lstlisting, merke, luecke wie oben
  beschrieben. Achte auf korrektes Escaping von LaTeX-Sonderzeichen (_, %, &, #) außerhalb
  von lstlisting.
- Kapitelnummer und -titel exakt wie im Kursprogramm angeben.
- Keine zusätzlichen Erklärungen außerhalb des LaTeX-Codes, außer ich frage explizit danach.

Hier sind die Informationen zu Kurs [NUMMER] – [TITEL]:

[HIER KURSINHALT EINFÜGEN]
```
