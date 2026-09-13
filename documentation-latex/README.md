# Documentation LaTeX — IBM RAG and Agentic AI Spezialisierung

Projet LaTeX regroupant, en **un chapitre par cours** (10 chapitres au total), une
documentation détaillée — en **allemand** — de ce qui a été vu dans chaque cours de la
spécialisation : objectifs, notions clés expliquées en profondeur, mise en pratique
(labs/projet), points d'attention, et une synthèse finale. L'objectif est de pouvoir
relire ce document plus tard et comprendre en profondeur ce qui a été fait et pourquoi —
indépendamment des README "portfolio" (en anglais) du reste du dépôt.

## Structure du projet

```
documentation-latex/
├── main.tex              # Document principal, \input de chaque chapitre
├── PROMPT.md              # Prompt réutilisable pour générer un chapitre
└── chapters/
    ├── kapitel01_generative_ai_get_started.tex   # Rédigé (cours 1, terminé)
    ├── kapitel02_build_rag_applications.tex      # En attente du contenu du cours 2
    ├── kapitel03_vector_databases.tex            # ...
    ├── kapitel04_advanced_rag_retrievers.tex
    ├── kapitel05_multimodal_generative_ai.tex
    ├── kapitel06_fundamentals_ai_agents.tex
    ├── kapitel07_agentic_langchain_langgraph.tex
    ├── kapitel08_agentic_langgraph_crewai_autogen_beeai.tex
    ├── kapitel09_ai_agents_mcp.tex
    └── kapitel10_capstone_project.tex
```

Chaque chapitre placeholder contient une boîte `luecke` ("en attente du contenu") et les
`\section{}` attendues en commentaire, pour rappel de la structure à respecter.

## Workflow pour chaque nouveau cours

1. Copier le prompt de [`PROMPT.md`](./PROMPT.md).
2. Remplacer `[NUMMER]`, `[TITEL]` et `[HIER KURSINHALT EINFÜGEN]` par le numéro, le titre
   et le contenu du cours (chapitres, notes, code, exercices — tout ce que tu as).
3. Donner ce prompt rempli à un LLM (ou le coller directement dans la conversation ici).
4. Coller le résultat (uniquement le contenu LaTeX du chapitre, sans préambule) dans le
   fichier `chapters/kapitelNN_....tex` correspondant, à la place du contenu placeholder.
5. `main.tex` référence déjà les 10 fichiers — rien à changer là si les noms de fichiers
   restent identiques.

## Compiler le PDF

Nécessite une distribution LaTeX (TeX Live, MiKTeX, ...) avec `pdflatex` et les paquets
utilisés (`babel`, `tcolorbox`, `listings`, `hyperref`, ... — tous standards).

```bash
cd documentation-latex
pdflatex main.tex
pdflatex main.tex   # deuxième passe pour la table des matières
```

## Pourquoi l'allemand ?

Choix fait le 2026-09-13 : la documentation sert à la compréhension personnelle en
profondeur, en allemand, avec les termes techniques anglais usuels (LangChain, embedding,
retriever, agent, prompt, chunking, ...) conservés tels quels. Ce projet est indépendant
des README (en anglais) du reste du dépôt, qui restent le "portfolio" public.
