# 🤖 Automatisk Ship Tracking Setup

Systemet er nu sat op til at **automatisk** hente skibsdata hver 15. minut!

## 🚀 Sådan Virker Det:

1. **Python Script** (`fetch-ship-data.py`) henter data fra VesselFinder/AISHub
2. **GitHub Actions** kører scriptet automatisk hver 15. minut
3. Data gemmes i `ship-data.json` 
4. **Hjemmesiden** læser bare JSON filen - simpelt og hurtigt! ⚡

## 📋 Setup Steps (5 minutter):

### 1. Upload Filerne til GitHub

```bash
cd "/Users/sophusandreassen/Desktop/Mr musa ur/OliverShipTracker"
git add .
git commit -m "Add automatic ship tracking"
git push
```

### 2. Tilføj API Key som GitHub Secret (VALGFRIT)

**For Gratis AISHub:**

1. Gå til: https://github.com/sophusand/Olivers-skib/settings/secrets/actions
2. Klik **New repository secret**
3. Name: `AISHUB_USERNAME`
4. Value: Dit AISHub username (f.eks. `sophus`)
5. Klik **Add secret**

**For Betalt MarineTraffic:**

1. Samme som ovenfor, men:
2. Name: `MARINETRAFFIC_API_KEY`
3. Value: Din API key

**UDEN API KEY:** Scriptet bruger automatisk demo data - det virker stadig! 🎯

### 3. Aktiver GitHub Actions

1. Gå til: https://github.com/sophusand/Olivers-skib/actions
2. Hvis der står "Workflows aren't being run", klik **Enable**
3. Klik på "Update Ship Data" workflow
4. Klik **Run workflow** → **Run workflow** (test det!)

### 4. Vent 1 minut

Scriptet vil:
- ✅ Hente skibsdata
- ✅ Gemme `ship-data.json`
- ✅ Commit og push automatisk

### 5. Tjek Hjemmesiden

Gå til: https://sophusand.github.io/Olivers-skib/

Data opdateres nu automatisk hver 15. minut! 🎉

---

## 🔄 Sådan Fungerer Opdateringerne:

- ⏰ **Hver 15. minut**: GitHub Actions kører automatisk
- 🔍 **Henter data**: Fra AISHub eller MarineTraffic
- 💾 **Gemmer til JSON**: `ship-data.json` opdateres
- 🌐 **Hjemmeside opdaterer**: Næste gang nogen besøger siden

## 🎯 Fordele ved Denne Løsning:

✅ **100% Automatisk** - ingen manuel opdatering  
✅ **Sikker** - API keys er skjulte (GitHub Secrets)  
✅ **Hurtig hjemmeside** - læser bare en JSON fil  
✅ **Ingen CORS problemer** - data er hosted på GitHub  
✅ **Gratis** - GitHub Actions er gratis for public repos  
✅ **Pålidelig** - hvis API fejler, bruges demo data  

## 📊 Overvågning:

Se status for opdateringer:
https://github.com/sophusand/Olivers-skib/actions

Hvis noget fejler, får du email fra GitHub!

---

## 🔧 Avancerede Indstillinger:

### Skift Opdaterings Interval

I `.github/workflows/update-ship-data.yml`, find:

```yaml
- cron: '*/15 * * * *'  # Hver 15. minut
```

Skift til:
- `*/5 * * * *` - Hver 5. minut (mere data forbrug)
- `*/30 * * * *` - Hver 30. minut (mindre forbrug)
- `0 * * * *` - Hver time

### Test Lokalt

```bash
cd "/Users/sophusandreassen/Desktop/Mr musa ur/OliverShipTracker"
python3 fetch-ship-data.py
```

Dette genererer `ship-data.json` som du kan inspicere!

---

**Du er klar! 🎉**

Upload filerne til GitHub og systemet kører af sig selv!
