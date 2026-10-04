import os
import glob

directory = r"d:\antigravity\sityi a caso"
files = [f for f in glob.glob(os.path.join(directory, "*.html")) if os.path.basename(f) not in ['index.html', 'about.html', 'appunti.html', 'gpx.html']]

back_btn_top = """
        <!-- TASTO INDIETRO TOP -->
        <div style="margin-bottom: 25px;">
            <a href="appunti.html" style="color: var(--text-muted); text-decoration: none; font-weight: 600; font-size: 1rem; transition: color 0.3s;" onmouseover="this.style.color='#fff'" onmouseout="this.style.color='var(--text-muted)'">
                <i class="fas fa-arrow-left"></i> Torna indietro ad Appunti
            </a>
        </div>"""

for file_path in files:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
    
    if "TASTO INDIETRO TOP" not in content:
        # Inserisci il bottone in alto
        content = content.replace('<div class="container" style="max-width: 800px;">', '<div class="container" style="max-width: 800px;">' + back_btn_top)
        
        # Trasforma anche il link che c'era in fondo in un vero e proprio bottone visibile
        content = content.replace('style="color: var(--text-muted); text-decoration: none; font-weight: 600; font-size: 1.1rem;"', 'class="btn" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); box-shadow: none;"')
        
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

print("Aggiornamento completato.")
