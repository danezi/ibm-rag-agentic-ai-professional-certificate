"""
similarity_search.py

Demonstriert die Grundfunktionen einer Vector Database am Beispiel von ChromaDB:

1. Eine Collection mit einer SentenceTransformer-Embedding-Funktion anlegen
   (cosine similarity als Distanzmetrik, HNSW als Suchindex).
2. Text-Dokumente (Lebensmittel) inkl. Metadaten in die Collection einfügen.
   ChromaDB wandelt jeden Text automatisch über das Embedding-Modell
   "all-MiniLM-L6-v2" in einen Vektor um.
3. Alle gespeicherten Dokumente abrufen.
4. Eine semantische Ähnlichkeitssuche (similarity search) für den Suchbegriff
   "apple" durchführen und die Top-3-Treffer inkl. Distanz-Score ausgeben.

Voraussetzungen:
    pip install chromadb sentence-transformers
"""

import chromadb
from chromadb.utils import embedding_functions

# --------------------------------------------------------------------------
# Embedding-Funktion definieren
# --------------------------------------------------------------------------
# Wandelt Text in Vektoren (Embeddings) um. "all-MiniLM-L6-v2" ist ein
# kleines, schnelles SentenceTransformer-Modell, das für semantische
# Ähnlichkeitssuche gut geeignet ist.
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Neue In-Memory-Instanz des ChromaDB-Clients erstellen.
client = chromadb.Client()

# Name der Collection, die angelegt bzw. verwendet werden soll.
collection_name = "my_grocery_collection"


def main() -> None:
    """
    Hauptablauf: Collection anlegen, Beispieldaten einfügen, abrufen
    und eine Ähnlichkeitssuche darauf ausführen.
    """
    try:
        # ------------------------------------------------------------
        # Collection erstellen
        # ------------------------------------------------------------
        # - name: eindeutiger Name der Collection (wie eine Tabelle)
        # - metadata: frei wählbare Beschreibung der Collection
        # - configuration:
        #     * hnsw.space "cosine": Cosine-Distanz als Ähnlichkeitsmaß
        #     * embedding_function: automatische Vektorisierung neuer
        #       Dokumente über das oben definierte SentenceTransformer-Modell
        collection = client.create_collection(
            name=collection_name,
            metadata={"description": "A collection for storing grocery data"},
            configuration={
                "hnsw": {"space": "cosine"},
                "embedding_function": ef
            }
        )
        print(f"Collection created: {collection.name}")

        # Beispielhafte Lebensmittel-Texte, die in die Collection
        # eingefügt werden sollen.
        texts = [
            'fresh red apples',
            'organic bananas',
            'ripe mangoes',
            'whole wheat bread',
            'farm-fresh eggs',
            'natural yogurt',
            'frozen vegetables',
            'grass-fed beef',
            'free-range chicken',
            'fresh salmon fillet',
            'aromatic coffee beans',
            'pure honey',
            'golden apple',
            'red fruit'
        ]

        # Eindeutige IDs für jedes Text-Element erzeugen, im Format
        # "food_<Index>", beginnend bei 1 (z. B. "food_1", "food_2", ...).
        ids = [f"food_{index + 1}" for index, _ in enumerate(texts)]

        # ------------------------------------------------------------
        # Dokumente in die Collection einfügen
        # ------------------------------------------------------------
        # Jeder Text wird beim Einfügen automatisch über die konfigurierte
        # Embedding-Funktion in einen Vektor umgewandelt und zusammen mit
        # ID und Metadaten gespeichert.
        collection.add(
            documents=texts,
            metadatas=[{"source": "grocery_store", "category": "food"} for _ in texts],
            ids=ids
        )

        # ------------------------------------------------------------
        # Alle gespeicherten Dokumente abrufen
        # ------------------------------------------------------------
        # get() liefert die Rohdaten (IDs, Texte, Metadaten) ohne
        # Ähnlichkeitssuche - vergleichbar mit einem "SELECT *".
        all_items = collection.get()
        print("Collection contents:")
        print(f"Number of documents: {len(all_items['documents'])}")

        def perform_similarity_search(collection, all_items) -> None:
            """
            Führt eine semantische Ähnlichkeitssuche für einen festen
            Suchbegriff ("apple") in der übergebenen Collection durch
            und gibt die Top-3-Treffer mit Distanz-Score aus.

            Args:
                collection: Die ChromaDB-Collection, in der gesucht wird.
                all_items: Zuvor abgerufene Sammlung aller Dokumente
                    (wird hier nicht direkt verwendet, dient als Kontext/
                    möglicher Vergleichswert für spätere Erweiterungen).
            """
            try:
                # Suchbegriff, für den ähnliche Dokumente gefunden werden sollen.
                query_term = "apple"

                # query() wandelt den Suchbegriff ebenfalls über die
                # Embedding-Funktion in einen Vektor um und vergleicht ihn
                # per Cosine-Distanz mit allen gespeicherten Vektoren.
                # n_results=3 begrenzt die Ausgabe auf die 3 ähnlichsten
                # Dokumente.
                results = collection.query(
                    query_texts=[query_term],
                    n_results=3
                )
                print(f"Query results for '{query_term}':")
                print(results)

                # Prüfen, ob überhaupt Ergebnisse zurückgegeben wurden.
                if not results or not results['ids'] or len(results['ids'][0]) == 0:
                    print(f'No documents found similar to "{query_term}"')
                    return

                print(f'Top 3 similar documents to "{query_term}":')
                # results ist verschachtelt (Liste von Listen), da query_texts
                # mehrere Suchanfragen gleichzeitig verarbeiten kann.
                # [0] greift hier auf die Ergebnisse der ersten (und einzigen)
                # Anfrage zu.
                for i in range(min(3, len(results['ids'][0]))):
                    doc_id = results['ids'][0][i]      # ID des Treffers
                    score = results['distances'][0][i]  # Distanz-Score (niedriger = ähnlicher)
                    text = results['documents'][0][i]   # Ursprünglicher Text des Treffers

                    if not text:
                        print(f' - ID: {doc_id}, Text: "Text not available", Score: {score:.4f}')
                    else:
                        print(f' - ID: {doc_id}, Text: "{text}", Score: {score:.4f}')
            except Exception as error:
                print(f"Error in similarity search: {error}")

        # Ähnlichkeitssuche mit den zuvor erstellten Daten ausführen.
        perform_similarity_search(collection, all_items)

    except Exception as error:
        # Fängt alle Fehler im Hauptablauf ab (z. B. beim Erstellen der
        # Collection oder beim Einfügen der Dokumente) und gibt sie aus.
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
