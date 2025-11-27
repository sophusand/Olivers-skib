# 🚢 Oliver's Nord Maverick Ship Tracker

En simpel, gratis hjemmeside der viser Oliver's skibsposition i real-time!

## 🌟 Fordele ved Hjemmeside vs. App

| Feature | Hjemmeside | iOS App |
|---------|-----------|---------|
| **Pris** | 🆓 Gratis | 799 kr/år |
| **Setup tid** | ⚡ 5 minutter | 📅 1 uge |
| **Virker på** | 📱💻🖥️ Alt | 📱 Kun iPhone |
| **Vedligehold** | ✅ Intet | 🔄 Forny hver 7. dag |
| **Oliver kan se det** | ✅ Ja, overalt | ❌ Kun på din iPhone |
| **Del med familie** | ✅ Send bare link | ❌ Svært |
| **Widgets** | ❌ Nej | ✅ Ja (med betalt) |

**Anbefaling**: Hjemmeside er perfekt til dette! 🎯

---

## 🚀 Udgiv på GitHub Pages (100% GRATIS)

### Metode 1: Via GitHub Website (Nemmest)

#### Step 1: Opret GitHub Repository

1. Gå til [github.com](https://github.com) og log ind (opret konto hvis ny)
2. Klik **+** → **New repository**
3. Udfyld:
   - **Repository name**: `oliver-ship-tracker`
   - **Description**: "Track Oliver's ship Nord Maverick"
   - **Public** (skal være public for gratis hosting)
   - ✅ Check "Add a README file"
4. Klik **Create repository**

#### Step 2: Upload Hjemmeside

1. I dit nye repo, klik **Add file** → **Upload files**
2. Træk `index.html` fra denne mappe ind i browseren
3. Skriv commit message: "Add ship tracker website"
4. Klik **Commit changes**

#### Step 3: Aktiver GitHub Pages

1. I repo, klik **Settings** (øverst)
2. Scroll ned til **Pages** i venstre menu
3. Under **Source**, vælg:
   - Branch: **main**
   - Folder: **/ (root)**
4. Klik **Save**
5. Vent 1-2 minutter
6. Refresh siden - du får et link!

**Dit website er nu live på**: `https://[ditusername].github.io/oliver-ship-tracker/`

---

### Metode 2: Via Terminal (Hvis du vil bruge Git)

```bash
# Naviger til OliverShipTracker mappen
cd "/Users/sophusandreassen/Desktop/Mr musa ur/OliverShipTracker"

# Initialiser Git repo
git init
git add index.html README.md
git commit -m "Initial commit - Oliver ship tracker"

# Tilføj GitHub remote (erstat USERNAME med dit GitHub username)
git remote add origin https://github.com/USERNAME/oliver-ship-tracker.git

# Push til GitHub
git branch -M main
git push -u origin main
```

Derefter følg Step 3 ovenfor for at aktivere Pages.

---

## 🔧 Tilføj Live Tracking (Valgfrit)

Hjemmesiden virker allerede med demo data! Men for **real-time updates**:

### Option A: AISHub (Gratis - Anbefalet)

1. Opret konto på [aishub.net](https://www.aishub.net)
2. Få din API key (dit username)
3. Opdater `index.html`:

Find denne linje (~135):
```javascript
const response = await fetch(`https://services.marinetraffic.com/api/...`);
```

Erstat med:
```javascript
// GRATIS AISHub API
const USERNAME = 'dit_aishub_username';
const response = await fetch(`http://data.aishub.net/ws.php?username=${USERNAME}&format=1&output=json&compress=0&mmsi=${SHIP_MMSI}`);
```

### Option B: MarineTraffic (Betalt - Bedre data)

1. Tilmeld [marinetraffic.com/en/ais-api-services](https://www.marinetraffic.com/en/ais-api-services)
2. Få API key
3. Erstat API key i linjen (~135) i `index.html`

---

## 📱 Brug Hjemmesiden

### På iPhone (Tilføj til Homescreen)

1. Åbn dit GitHub Pages link i Safari
2. Tryk **Del** knappen (📤)
3. Scroll ned og vælg **"Tilføj til Hjemmeskærm"**
4. Vælg navn: "Oliver's Skib"
5. Tryk **Tilføj**

Nu har du et app-lignende ikon på din homescreen! 📱

### På Mac/Computer

Bare gå til linket i browser - det virker perfekt!

### Del med Familie/Venner

Send bare linket til dem:
`https://[ditusername].github.io/oliver-ship-tracker/`

---

## ✨ Features

✅ **Flot moderne design**  
✅ **Responsivt** (virker på mobil & desktop)  
✅ **Real-time lokal tid** (beregnet fra position)  
✅ **Google Maps integration** (klik for at se på kort)  
✅ **Auto-refresh** hver 5. minut  
✅ **Opdater knap** for manual refresh  
✅ **Fallback til demo data** hvis API fejler  

---

## 🎨 Tilpasning

### Skift Farver

I `index.html`, find CSS gradient (~17-18):
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Prøv andre farver:
- Havblå: `#1e3a8a 0%, #3b82f6 100%`
- Grøn: `#059669 0%, #10b981 100%`
- Solnedgang: `#f59e0b 0%, #ef4444 100%`

### Tilføj Flere Features

Idéer du kan tilføje:
- 🗺️ Embedded kort med skibets rute
- 📊 Graf af hastighed over tid
- 🌡️ Vejrdata for skibets position
- 📸 Billeder af Nord Maverick
- ⚓ Havn destinationer og ankomsttider

---

## 💡 Hvorfor Hjemmeside er Bedre

1. **Oliver kan se det fra skibet** 🚢
   - Han kan åbne linket på sin telefon/tablet
   - Ingen app download nødvendig

2. **Familie kan følge med** 👨‍👩‍👧‍👦
   - Alle kan se hvor han er
   - Ingen installation krævet

3. **Virker på alt** 💻📱
   - iPhone, Android, Mac, Windows
   - Bare åbn link i browser

4. **Nul vedligehold** ✅
   - Ingen 7-dages fornyelse
   - Ingen app updates
   - Virker bare!

5. **100% Gratis** 🆓
   - GitHub Pages er gratis forever
   - Ingen Apple Developer account
   - Ingen hosting costs

---

## 🐛 Troubleshooting

### Hjemmesiden vises ikke efter 10 minutter
→ Tjek at repo er **Public** ikke Private  
→ Gå til Settings → Pages og verificer det er aktiveret

### API returnerer fejl
→ Normal! Siden viser demo data i stedet  
→ For live data, tilføj din egen API key

### Vil have custom domain (f.eks. oliver-ship.dk)
→ Køb domain (~100 kr/år)  
→ I GitHub Settings → Pages → Custom domain

---

## 🎉 Du er Færdig!

Din Nord Maverick tracker er nu live på internettet!

**Næste steps:**
1. ✅ Åbn dit GitHub Pages link
2. 📱 Tilføj til homescreen på iPhone
3. 📧 Send link til Oliver og familie
4. 🌊 Følg Oliver's rejse!

**Link format:**
`https://[ditusername].github.io/oliver-ship-tracker/`

---

**God sejlads til Oliver! ⛵🌊**
