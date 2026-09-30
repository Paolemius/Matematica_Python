# Laboratorio di Matematica con Python – Algoritmi, simulazioni e applicazioni
coderdojo 2026-27
Durata: 8 incontri da 3 ore

Destinatari: ragazzi che hanno già frequentato un percorso introduttivo di Python, indicativamente dai 13-14 anni in su.

Prerequisiti: conoscenze di base di Python e familiarità con l'utilizzo del computer.
Ambiente: Visual Studio Code, Python, GitHub, SQLite e, nella parte finale, Django.
Obiettivo del laboratorio

Il laboratorio propone un percorso di approfondimento di Python attraverso problemi matematici, algoritmi, simulazioni e sviluppo di applicazioni.

L'obiettivo non è insegnare principalmente nuova sintassi Python, ma sviluppare la capacità di:
leggere e comprendere codice già funzionante;
analizzare un problema e individuare un algoritmo;
modificare e sperimentare programmi;
eseguire test e interpretare i risultati;
utilizzare Python per esplorare problemi matematici e scientifici;
gestire dati attraverso un database SQL;
comprendere come un programma Python possa diventare un'applicazione accessibile via web.
Una parte importante del laboratorio sarà lasciata alla sperimentazione autonoma e alla proposta di problemi da parte dei partecipanti.

## Incontro 1 – Python come laboratorio matematico
Introduzione all'ambiente di lavoro comune e breve ripresa di Python attraverso problemi matematici.
Utilizzo di NumPy e Matplotlib per trasformare semplici algoritmi in esperimenti computazionali.
Esempi:
stima di π con il metodo Monte Carlo;
esplorazione della congettura di Collatz;
visualizzazione e analisi dei risultati.
L'obiettivo è introdurre il concetto di esperimento computazionale: il computer non viene utilizzato soltanto per calcolare una risposta, ma per esplorare un problema e formulare ipotesi.
In parole semplici: Non faremo semplici calcoli, ma useremo il computer come strumento di esplorazione per fare esperimenti e verificare ipotesi. Attraverso il lancio di dadi virtuali o il disegno di sequenze numeriche, vedremo come poche righe di codice possano mostrare visivamente proprietà matematiche affascinanti, dalla stima del Pi Greco fino a enigmi come la congettura di Collatz, dove numeri che schizzano in alto e si dimezzano finiscono poi incredibilmente tutti a 1!

Incontro 2 – Caos, frattali e sistemi dinamici
Partendo da regole matematiche molto semplici, si esplorano comportamenti complessi e apparentemente imprevedibili.
Possibili attività:
successioni e sistemi dinamici;
caos deterministico;
sensibilità alle condizioni iniziali;
generazione di frattali;
insieme di Mandelbrot e insiemi di Julia.
I partecipanti potranno modificare i parametri, visualizzare i risultati e, nei casi più avanzati, sviluppare semplici strumenti interattivi per esplorare i frattali.
In parole semplici: Esploriamo la "teoria del caos", ovvero come regole matematiche semplicissime possano generare comportamenti complessi e imprevedibili. Genereremo frattali, ovvero strutture geometriche che si ripetono all'infinito, simili a fiocchi di neve o cavolfiori, cercando di capire come piccole variazioni iniziali cambino del tutto il risultato finale. Avete presente la farfalla che batte le ali a Pechino e a New York arriva la pioggia invece del sole? 

Incontro 3 – Algoritmi di ricerca e grafi
Introduzione al concetto di grafo e ai problemi di ricerca di un percorso.
Attraverso un labirinto o una mappa vengono presentati e confrontati diversi algoritmi:
ricerca in ampiezza (BFS);
ricerca in profondità (DFS);
Dijkstra;
eventualmente A*.
Gli algoritmi vengono visualizzati mentre vengono eseguiti, permettendo di confrontare comportamento, prestazioni e risultati.
Possibile attività finale: progettare un proprio labirinto e confrontare diversi algoritmi nella ricerca del percorso.
In parole semplici: Mettiamo a confronto diversi algoritmi con cui esplorare uno spazio e trovare la strada migliore per uscire da un labirinto o collegare due punti. È il principio su cui si basano i navigatori o la logica dei videogiochi quando un personaggio deve muoversi su una mappa evitando gli ostacoli.

Incontro 4 – Simulazioni e metodo Monte Carlo
Introduzione alla simulazione di fenomeni casuali e all'utilizzo del computer per affrontare problemi difficili da risolvere analiticamente.
Possibili esempi:
random walk;
stima di probabilità;
problemi geometrici;
metodo Monte Carlo;
simulazione di fenomeni fisici o biologici.
Come attività di approfondimento, si potrà costruire una semplice simulazione di diffusione o di epidemia, osservando come cambiano i risultati modificando i parametri.
In parole semplici: "Dio non gioca a dadi con l'universo", diceva Einstein. Ma noi con Python sì! Ricreiamo fenomeni reali basati sul caso, per prevedere cosa succederà quando la soluzione matematica è troppo complessa da calcolare a mano. Attraverso migliaia di prove casuali, simuleremo scenari reali, come la diffusione di un'epidemia in una popolazione o il movimento casuale di molecole nell'aria.
(Piccolo spoiler: i numeri generati dal computer non sono davvero casuali! E per chi vuole la vera casualità pura? Proprio all'Università di Padova hanno realizzato un Generatore Quantistico di Numeri Casuali basato sulla fisica delle particelle!) 

Incontro 5 – Algoritmi di ottimizzazione
Introduzione ai problemi nei quali non è immediato trovare la soluzione migliore.
Problema guida: Travelling Salesman Problem (TSP).
Partendo dalla ricerca esaustiva, si mostra come il numero di possibili soluzioni cresca rapidamente e si introducono strategie alternative:
algoritmi greedy;
ricerca locale;
simulated annealing;
eventualmente algoritmi genetici.
L'attività sarà strutturata come una piccola sfida: i partecipanti potranno confrontare le soluzioni ottenute dai diversi algoritmi.
In parole semplici: Affrontiamo problemi in cui le combinazioni possibili sono troppe per essere esplorate tutte, e occorre trovare una soluzione sufficientemente buona in poco tempo. Come nel famoso problema del commesso viaggiatore, dovremo capire come visitare 20 città diverse facendo il tragitto più breve possibile. Riusciremo a trovare la rotta migliore?

Incontro 6 – SQL e database con SQLite
Introduzione pratica ai database relazionali attraverso SQLite.
I partecipanti lavoreranno con un database contenente, ad esempio:
partecipanti;
algoritmi;
esperimenti;
risultati.
Verranno introdotti i principali comandi SQL:
SELECT;
INSERT;
UPDATE;
DELETE;
WHERE;
ORDER BY;
GROUP BY;
funzioni di aggregazione;
semplici JOIN.
Le interrogazioni verranno eseguite direttamente in Visual Studio Code e/o attraverso Python, osservando immediatamente come cambiano i dati nel database.
L'obiettivo è comprendere come un programma possa memorizzare e interrogare dati, più che approfondire la teoria dei database.
In parole semplici: I programmi reali non dimenticano i dati quando li chiudiamo. Impariamo a organizzare, salvare e consultare grandi quantità di informazioni in modo strutturato. Vedremo come creare un archivio digitale (aka database) e come interrogarlo per estrarre velocemente solo le informazioni che ci servono.

Incontro 7 – Da Python a una Web App con Django
Introduzione al funzionamento di una semplice applicazione web.
Partendo dagli algoritmi e dal database sviluppati negli incontri precedenti, si costruirà una piccola applicazione Django nella quale l'utente possa:
scegliere un algoritmo;
impostare alcuni parametri;
eseguire l'algoritmo sul server;
visualizzare il risultato;
eventualmente salvare il risultato nel database.
Verranno introdotti, in modo pratico:
client e server;
HTTP;
HTML e CSS;
Django;
URL e view;
template;
database e modelli;
collegamento fra frontend, backend e codice Python.
L'obiettivo è far comprendere la struttura di una vera applicazione web, senza trasformare il laboratorio in un corso completo di sviluppo web.
In parole semplici: Trasformiamo gli script e i dati creati durante l’anno in una applicazione web, con cui un utente può interagire da browser. Collegheremo la logica di Python a una schermata: potremo cliccare pulsanti, inserire dati, far partire gli algoritmi e vederne subito i risultati sullo schermo.

Incontro 8 – Pubblicazione e progetto finale
Completamento e pubblicazione dell'applicazione.
Introduzione al concetto di deploy:
Codice Python
      ↓
    Django
      ↓
   Database
      ↓
     Server
      ↓
    Internet
I partecipanti lavoreranno quindi alla personalizzazione dell'applicazione e potranno proporre nuove funzionalità.
La parte finale sarà organizzata come una piccola challenge/progetto libero, nella quale i partecipanti potranno scegliere un algoritmo, una simulazione o un problema matematico affrontato durante il corso e realizzarne una versione interattiva o pubblicabile sul web.
In parole semplici: Completiamo il cammino e quindi il ciclo di sviluppo del nostro progetto, rendendolo accessibile online e permettendo a ciascuno di personalizzare la propria creazione. È il momento di mettere la pagina in rete, per mostrare ad amici e genitori il proprio strumento matematico interattivo e funzionante.

Metodologia
Il laboratorio privilegerà un approccio "funzionante → esplorazione → comprensione → modifica".
In molti casi verrà fornito inizialmente un programma funzionante. I partecipanti potranno utilizzarlo e modificarlo per osservare il comportamento del sistema; successivamente il codice verrà analizzato insieme per comprenderne la struttura e gli algoritmi.
Questo approccio permette di lavorare contemporaneamente con ragazzi di livelli diversi: chi è meno esperto può concentrarsi sulla comprensione e sulla modifica del programma, mentre chi possiede maggiori competenze può approfondire gli algoritmi, la matematica sottostante o le prestazioni.
Gli strumenti di IA generativa potranno essere utilizzati come strumenti di supporto alla programmazione, ma il loro utilizzo sarà accompagnato dalla verifica e dalla comprensione del codice prodotto.

Strumenti
Python
Visual Studio Code
NumPy
Matplotlib
Pandas, dove utile
SQLite / SQL
Django
Git / GitHub
L'ambiente Python e le dipendenze verranno predisposti all'inizio del percorso per evitare problemi di configurazione durante gli incontri successivi.
Possibili sviluppi
La sequenza proposta non è completamente rigida. Al termine dei primi incontri potranno essere raccolte le proposte dei partecipanti e, compatibilmente con gli obiettivi del laboratorio, inseriti ulteriori problemi o algoritmi di loro interesse.
Particolare attenzione sarà riservata alla possibilità di proporre livelli di approfondimento differenti, in modo da valorizzare anche i partecipanti con competenze matematiche e informatiche avanzate.

