import os

html_template = """<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Appunti Polimi</title>
    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav>
        <a href="index.html" class="logo">Salvo's Blog</a>
        <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="about.html">Chi Sono Io</a></li>
            <li><a href="appunti.html" class="active">Appunti Polimi</a></li>
            <li><a href="gpx.html">Tracce GPX</a></li>
        </ul>
    </nav>

    <section class="hero" style="padding-bottom: 2rem;">
        <h1>{title}</h1>
        <p>{subtitle}</p>
    </section>

    <div class="container" style="max-width: 800px;">
        <div class="note-card" style="margin-bottom: 30px;">
            <h2><i class="fas fa-info-circle"></i> Descrizione degli Appunti</h2>
            <p>{desc}</p>
        </div>

        <div class="note-card" style="margin-bottom: 30px; border-color: rgba(99, 102, 241, 0.4);">
            <h2><i class="fas fa-lightbulb" style="color: #f1c40f;"></i> I miei consigli per l'esame</h2>
            <ul style="color: var(--text-muted); line-height: 1.8;">
                {tips}
            </ul>
        </div>

        <div style="text-align: center; margin-top: 40px;">
            <a href="INSERISCI_QUI_IL_LINK_DI_DRIVE" target="_blank" class="btn" style="font-size: 1.2rem; padding: 15px 30px; background: #0F9D58; box-shadow: 0 4px 15px rgba(15, 157, 88, 0.4);">
                <i class="fab fa-google-drive"></i> Scarica da Google Drive
            </a>
            <p style="color: var(--text-muted); margin-top: 15px; font-size: 0.9rem;">
                Il file è in formato PDF. Cliccando sul pulsante si aprirà in una nuova scheda.
            </p>
        </div>

        <div style="text-align: center; margin-top: 50px;">
            <a href="appunti.html" style="color: var(--text-muted); text-decoration: none; font-weight: 600; font-size: 1.1rem;">
                <i class="fas fa-arrow-left"></i> Torna a tutti gli appunti
            </a>
        </div>
    </div>
</body>
</html>
"""

subjects = [
    {
        "file": "geometria.html",
        "title": "Geometria e Algebra Lineare",
        "subtitle": "Spazi vettoriali, matrici e astrazione: le basi per l'ingegneria.",
        "desc": "Appunti completi sulle matrici, sistemi lineari, spazi vettoriali, applicazioni lineari, autovalori e autovettori. Include anche la parte di geometria analitica.",
        "tips": "<li>Saper calcolare un determinante o invertire una matrice ad occhi chiusi è vitale.</li><li>Fai molti esercizi pratici per capire cosa significa geometricamente la teoria.</li>"
    },
    {
        "file": "informatica.html",
        "title": "Fondamenti di Informatica",
        "subtitle": "Il primo approccio alla programmazione in C.",
        "desc": "Spiegazioni dettagliate su variabili, cicli, funzioni, puntatori e strutture dati dinamiche (liste, alberi) in C. Codici di esempio commentati riga per riga.",
        "tips": "<li>I puntatori sono l'argomento in cui tutti si bloccano: disegna la memoria su carta!</li><li>Prova sempre il codice al computer, non studiarlo solo sui libri.</li>"
    },
    {
        "file": "fisica1.html",
        "title": "Fisica 1",
        "subtitle": "Cinematica, Dinamica e Termodinamica.",
        "desc": "Formulari completi e risoluzione passo passo dei tipici problemi di meccanica del punto, del corpo rigido e principi della termodinamica.",
        "tips": "<li>Fai diagrammi di corpo libero ordinati e grandi.</li><li>Controlla sempre le equazioni dimensionali alla fine dell'esercizio!</li>"
    },
    {
        "file": "elettrotecnica.html",
        "title": "Elettrotecnica",
        "subtitle": "Domina correnti, tensioni e circuiti.",
        "desc": "Risoluzione di reti elettriche in regime stazionario (Kirchhoff, Thevenin, Norton) e in regime sinusoidale (fasori, potenze).",
        "tips": "<li>Attenzione ai segni! Un segno sbagliato fa sballare tutta la rete.</li><li>I fasori ti salvano la vita nel regime sinusoidale, ripassa i numeri complessi.</li>"
    },
    {
        "file": "economia.html",
        "title": "Economia e Organizzazione Aziendale",
        "subtitle": "Usciamo dalle equazioni per entrare nel mondo aziendale.",
        "desc": "Appunti teorici e pratici su bilancio, partita doppia, analisi dei costi e teoria dell'impresa.",
        "tips": "<li>Usa le mappe concettuali per memorizzare i concetti di gestione.</li><li>Le scritture di bilancio vanno capite con la logica del 'dare' e 'avere'.</li>"
    },
    {
        "file": "analisi2.html",
        "title": "Analisi Matematica 2",
        "subtitle": "Dal piano allo spazio: integrali doppi e curve.",
        "desc": "Sviluppo di funzioni a più variabili, gradienti, integrali multipli, flussi e campi vettoriali.",
        "tips": "<li>Le coordinate polari e sferiche vanno capite alla perfezione.</li><li>Disegna sempre i domini di integrazione prima di impostare gli integrali!</li>"
    },
    {
        "file": "automatica.html",
        "title": "Fondamenti di Automatica",
        "subtitle": "Il cuore dell'Ingegneria dell'Automazione.",
        "desc": "Modelli matematici, Laplace, funzioni di trasferimento, diagrammi di Bode e sintesi di controllori PID.",
        "tips": "<li>Impara a tracciare i diagrammi di Bode velocemente a mano.</li><li>La stabilità (criterio di Nyquist) deve essere compresa intuitivamente.</li>"
    },
    {
        "file": "fisicatecnica.html",
        "title": "Fisica Tecnica e Macchine",
        "subtitle": "Calore, fluidi e macchine industriali.",
        "desc": "Termodinamica applicata, scambio termico (conduzione, convezione, irraggiamento) e studio cicli termodinamici.",
        "tips": "<li>Fai molta attenzione alle convenzioni dei segni per calore e lavoro.</li><li>Impara a leggere i diagrammi termodinamici.</li>"
    },
    {
        "file": "modellistica.html",
        "title": "Modellistica dei Sistemi Meccanici",
        "subtitle": "Dalla cinematica alle equazioni di Lagrange.",
        "desc": "Equazioni differenziali del moto, dinamica di sistemi multicorpo e vibrazioni meccaniche.",
        "tips": "<li>Il metodo di Lagrange semplifica tutto se imposti bene le coordinate generalizzate.</li><li>Fai attenzione ai segni di energia potenziale e cinetica.</li>"
    },
    {
        "file": "elettronica.html",
        "title": "Fondamenti di Elettronica",
        "subtitle": "Diodi, Transistor e Op-Amp.",
        "desc": "Componenti a semiconduttore, circuiti logici e calcolo guadagno di amplificatori operazionali ideali e reali.",
        "tips": "<li>Per gli op-amp ideali, il 'corto circuito virtuale' risolve il 90% degli esercizi.</li><li>Nei transistor ipotizza la regione di lavoro e poi verifica!</li>"
    },
    {
        "file": "reti.html",
        "title": "Reti di Telecomunicazione",
        "subtitle": "Come comunicano i computer.",
        "desc": "Modello ISO/OSI, TCP/IP, algoritmi di instradamento (Routing) e protocolli.",
        "tips": "<li>Impara i vari livelli ISO/OSI come le tue tasche.</li><li>Il calcolo delle subnet richiede molto esercizio.</li>"
    },
    {
        "file": "sistemi.html",
        "title": "Sistemi Informatici",
        "subtitle": "Il ponte tra l'hardware e il software.",
        "desc": "Gestione della CPU, memoria virtuale, concorrenza, semafori nei Sistemi Operativi e Database.",
        "tips": "<li>I deadlock si capiscono provando a rompere mentalmente l'algoritmo.</li><li>Fai schemi a blocchi per la memoria virtuale.</li>"
    }
]

out_dir = r"d:\antigravity\sityi a caso"

for s in subjects:
    content = html_template.format(
        title=s['title'],
        subtitle=s['subtitle'],
        desc=s['desc'],
        tips=s['tips']
    )
    with open(os.path.join(out_dir, s['file']), "w", encoding="utf-8") as f:
        f.write(content)
