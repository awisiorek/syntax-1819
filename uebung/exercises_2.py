from questions import SingleChoice, OpenQuestion, SelectionList, Lueckentext, MultipleChoice
from questions import single, multiple, offen, selection, luecke





blatt2_1a = [
    [SingleChoice("Warum gibt die parse-Funktion des Skripts vermutlich eine Sequenz zurück?", "Ambiguität", "Reflexivität", "Dependenz", sonst=True, inst= single)],
    [SingleChoice("Die Alternative <code>tree = parser.parse(sent)</code> ist weniger wünschenswert, da im Allgemeinen ________ Parse-Tree möglich ist.", "mehr als ein", "kein", "genau ein", sonst=True, inst=single)]
    ]

blatt2_1b = [
    [MultipleChoice("Zu welcher Phrase kann die Präpositionalphrase \"in my pajamas\" gehören?", correct=["Nominalphrase", "Verbalphrase"],wrong=["Adverbialphrase","Präpositionalphrase"],sonst=False, inst=multiple )]
    ]

blatt2_1c = [
    [SelectionList("Was ist der Fall, wenn die PP ein Adverbial ist?", "die im Verb ausgedrückte Tätigkeit wird modifiziert","die PP wird dem Substantiv beigefügt", "der Ort des Geschehens wird festgelegt", sonst=True, inst=selection)],
    [SelectionList("Was ist der Fall, wenn die PP ein Attribut ist?", "die PP wird dem Substantiv beigefügt", "der Ort des Geschehens wird festgelegt", "die im Verb ausgedrückte Tätigkeit wird modifiziert", sonst=True, inst=selection)]
        #   ],"Der gegebene Satz ist ambig, da aus der Oberflächensyntax nicht ersichtlich ist, welche syntaktische Funktion die PP einnimmt.")
    ]




blatt2_2a = [
    [SingleChoice("Welcher Grammatikbegriff liegt Satz 1 zugrunde?","Regelsystem","Regelbuch", "formale Grammatik","Theorie der Sprachstruktur", "Wissen um Sprachstruktur", sonst=False, inst=single)],
    [SingleChoice("Welcher Grammatikbegriff liegt Satz 2 zugrunde?","Regelbuch", "Regelsystem", "formale Grammatik","Theorie der Sprachstruktur", "Wissen um Sprachstruktur", sonst=False, inst=single)],
    [SingleChoice("Welcher Grammatikbegriff liegt Satz 3 zugrunde?","Theorie der Sprachstruktur", "Regelbuch", "Regelsystem", "formale Grammatik", "Wissen um Sprachstruktur", sonst=False, inst=single)]
    ]

blatt2_2b = [
    [MultipleChoice("Welche Gesetzmäßigkeiten umfasst die Grammatik als Regelsystem?", correct=["phonologische", "morphologische", "syntaktische"],wrong=["semantische"],sonst=False, inst=multiple)],
    [Lueckentext("Die Syntax ist ein Teilbereich der Grammatik, der sich auf die syntaktischen Regularitäten bezieht.", {"Teilbereich":["Oberbegriff","Synonym"], "syntaktischen":["morphologischen","phonologischen","semantischen"]},inst=luecke)]
    ]




blatt2_3a = [
#      [Anleitung("<br><h2>Aufgabe 3  &nbsp;&nbsp;&nbsp; Linguistische Strukturbeschreibung</h2>")],
     [MultipleChoice("Welche Hierachie-Ebenen lassen sich in der Beschreibung des Aufbaus sprachlicher Strukturen unterscheiden?", correct=["Lautebene", "Wortebene", "Satzebene"],wrong=["Morphemebene","Phrasenebene"],sonst=False, inst=multiple)]
     ]

blatt2_3b = [
#     [Anleitung("<h4>Wo liegt der Unterschied zwischen dem Wortbegriff einer natürlichen Sprache und dem Wortbegriff einer formalen Sprache?<br> (Was sind die Blätter des Syntaxbaums einer Ableitung eines natürlichsprachlichen Satzes in einer die Sprache modellierenden formalen Grammatik?)</h4>")],
    [Lueckentext("Für die Blätter gilt: natürlichsprachliche Wörter sind eine Teilmenge aus dem Alphabet der Grundsymbole der formalen Sprache; ein analysierter natürlichsprachlicher Satz ist ein in der formalen Grammatik ableitbares Wort der formalen Sprache.", {"Wort":["Morphem","Symbol"], "Grundsymbole":["Nicht-Terminale"]},inst=luecke)]
    ]    




blatt2_4a = [
    [MultipleChoice("Welche formalen Repräsentationen der syntaktischen Struktur eines natürlichsprachlichen Satzes haben Sie in der Vorlesung kennengelernt?", correct=["Syntaxbaum", "Parsebaum", "Ableitungsbaum","Dependenzgraph"],wrong=[],sonst=True, inst=multiple)]
    ]

blatt2_4b = [
    [SingleChoice("In welcher Form wird die syntaktische Struktur eines Satzes beim Aufruf von NLTK print(tree) erstellt?","Klammernotation","Baumdiagramm", sonst=True, inst=single)],
    [SingleChoice("In welcher Form wird die syntaktische Struktur eines Satzes beim Aufruf von NLTK tree.draw() erstellt?","Baumdiagramm", "Klammernotation", sonst=True, inst=single)]
    ]

blatt2_4c_tree = """
(I-shot-an_elephant-in_my_pajamas
  I
  (shot-an_elephant-in_my_pajamas
    shot
    (an_elephant-in_my_pajamas
      an_elephant
      in_my_pajamas
    )
  )
)
"""

blatt2_4d_tree = """

(I-shot-an_elephant-in_my_pajamas
  I
  (shot-an_elephant-in_my_pajamas
    (shot-an_elephant
      shot
      an_elephant
    )
    (in_my_pajamas)
  )
)
"""




blatt2_5 = [
    [SingleChoice("Was ist der Ursprung der Ambiguität?","Strukturelle Ambiguität","andere Gründe", "lexikalische Ambiguität", "morphologisch ambige Formen", sonst=False, inst=single)],
    [MultipleChoice("In Bezug auf das Gerundium, welche Funktion können die Nomen haben?", correct=["Subjekt", "direktes Objekt"],wrong=["indirektes Objekt", "Argens", "Partiens"],sonst=False, inst=multiple)]    
    ]



    
blatt2_6a = [
    [MultipleChoice("Hinsichtlich welcher syntaktischen Grundprinzipien werden natürliche Sprachen mit formalen Methoden analysiert?", correct=["Konstituenz", "Dependenz", "Phrasenstruktur","Abhängigkeitsstruktur"],wrong=["Wortstruktur"],sonst=True, inst=multiple)],
    [SingleChoice("Konstituenz ist synonym zu:","Phrasenstruktur","Dependenz", "Abhängigkeitsstruktur", "Wortstruktur", sonst=True, inst=single)],
    [SingleChoice("Dependenz ist synonym zu:","Abhängigkeitsstruktur", "Phrasenstruktur", "Konstituenz",  "Wortstruktur", sonst=True, inst=single)],
    ]

blatt2_6b = [
    [MultipleChoice("Mit welchen Mitteln werden natürliche Sprachen analysiert?", correct=["formale Grammatik", "Parser"],wrong=["Bäume"],sonst=True, inst=multiple)],
    ]

blatt2_6c = [
    [SingleChoice("Bei einer solchen Analyse wird welche ja/nein-Entscheidung unweigerlich getroffen?","Wohlgeformtheit", "Sinnhaftigkeit", "Korrektheit", sonst=True, inst=single)],
    ]

blatt2_6d = [
    [MultipleChoice("Welche Vorteile hat die Modellierung der Satzstruktur mit Hilfe einer formalen Grammatik?", correct=["Eine unendliche Menge an Sätzen kann mit endlichen Mitteln beschrieben werden.", "Eine automatische Strukturanalyse wird möglich."], wrong=["Eine endliche Menge an Sätzen kann mit unendlichen Mitteln beschrieben werden."], inst=multiple)]
    ]

