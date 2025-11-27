import requests
import json
from datetime import datetime
import os

# Nord Maverick detaljer
SHIP_MMSI = "219034952"
SHIP_IMO = "9877559"

def get_location_name(lat, lon):
    """Approximerer location navn baseret på koordinater"""
    if 30 < lat < 35 and -82 < lon < -78:
        return "Savannah, Georgia, USA"
    elif 50 < lat < 60 and -10 < lon < 10:
        return "Nordsøen"
    elif 25 < lat < 45 and -100 < lon < -70:
        return "Østkysten, USA"
    elif 40 < lat < 50 and -70 < lon < -50:
        return "Atlanterhavet"
    else:
        return "På havet"

def fetch_from_aishub():
    """Hent data fra AISHub (GRATIS API)"""
    # Du skal sætte din AISHub username som GitHub Secret
    username = os.environ.get('AISHUB_USERNAME', '')
    
    if not username:
        print("Ingen AISHub username fundet - bruger demo data")
        return None
    
    url = f"http://data.aishub.net/ws.php?username={username}&format=1&output=json&compress=0&mmsi={SHIP_MMSI}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data and len(data) > 0 and 'data' in data[0] and data[0]['data']:
            vessel = data[0]['data'][0]
            return {
                'latitude': float(vessel.get('LATITUDE', 0)),
                'longitude': float(vessel.get('LONGITUDE', 0)),
                'speed': float(vessel.get('SPEED', 0)) if vessel.get('SPEED') else None,
                'course': float(vessel.get('COURSE', 0)) if vessel.get('COURSE') else None,
                'destination': vessel.get('DESTINATION', 'N/A'),
                'timestamp': vessel.get('TIME', datetime.utcnow().isoformat())
            }
    except Exception as e:
        print(f"AISHub API fejl: {e}")
        return None

def fetch_from_marinetraffic():
    """Hent data fra MarineTraffic (BETALT API)"""
    api_key = os.environ.get('MARINETRAFFIC_API_KEY', '')
    
    if not api_key:
        return None
    
    url = f"https://services.marinetraffic.com/api/exportvessel/v:8/{api_key}/timespan:20/protocol:json/mmsi:{SHIP_MMSI}"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data and len(data) > 0:
            vessel = data[0]
            return {
                'latitude': float(vessel.get('LAT', 0)),
                'longitude': float(vessel.get('LON', 0)),
                'speed': float(vessel.get('SPEED', 0)) if vessel.get('SPEED') else None,
                'course': float(vessel.get('COURSE', 0)) if vessel.get('COURSE') else None,
                'destination': vessel.get('DESTINATION', 'N/A'),
                'timestamp': vessel.get('TIMESTAMP', datetime.utcnow().isoformat())
            }
    except Exception as e:
        print(f"MarineTraffic API fejl: {e}")
        return None

def get_demo_data():
    """Demo data baseret på sidste kendte position"""
    return {
        'latitude': 32.0333,
        'longitude': -80.8833,
        'speed': 0.1,
        'course': 54.8,
        'destination': 'Savannah Anch., USA',
        'timestamp': datetime.utcnow().isoformat()
    }

def main():
    print("Henter Nord Maverick skibsdata...")
    
    # Prøv først AISHub (gratis)
    ship_data = fetch_from_aishub()
    source = "AISHub"
    
    # Hvis det fejler, prøv MarineTraffic
    if not ship_data:
        print("AISHub fejlede, prøver MarineTraffic...")
        ship_data = fetch_from_marinetraffic()
        source = "MarineTraffic"
    
    # Hvis begge fejler, brug demo data
    if not ship_data:
        print("Alle API'er fejlede, bruger demo data")
        ship_data = get_demo_data()
        source = "Demo"
    
    # Tilføj location navn
    ship_data['location'] = get_location_name(
        ship_data['latitude'], 
        ship_data['longitude']
    )
    
    # Tilføj metadata
    output = {
        'ship': {
            'name': 'Nord Maverick',
            'mmsi': SHIP_MMSI,
            'imo': SHIP_IMO,
            'type': 'Chemical/Oil Products Tanker',
            'flag': 'Denmark'
        },
        'position': ship_data,
        'metadata': {
            'updated': datetime.utcnow().isoformat(),
            'source': source
        }
    }
    
    # Gem til JSON fil
    with open('ship-data.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Data gemt! Kilde: {source}")
    print(f"📍 Position: {ship_data['location']}")
    print(f"🌍 Koordinater: {ship_data['latitude']}, {ship_data['longitude']}")

if __name__ == "__main__":
    main()
