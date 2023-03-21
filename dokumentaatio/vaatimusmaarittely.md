# Vaatimusmaäärittely

## Sovelluksen tarkoitus

Sovellus on yksinpelattava miinaharava, jonka vaikeustason voi käyttäjä itse kustomoida. Käyttäjä voittaa pelin, mikäli onnistuu merkkaamaan kaikki piilossa olevat miinat. Käyttäjä häviää pelin, mikäli osuu miinaan.

## Toiminnallisuudet

### Ennen kirjautumista

- Käyttäjä voi luoda uuden tunnuksen sovellukseen
    - Tunnuksen on oltava uniikki ja vähintään 3 merkin pituinen
- Käyttäjä voi kirjautua sisään sovellukseen
    - Kirjautuminen onnistuu, mikäli syötetty käyttäjätunnus ja salasana ovat oikeat
    - Jos tunnus tai salasana on väärä, sovellus ilmoittaa virheestä

### Kirjautumisen jälkeen

- Käyttäjä näkee tilaston omista pelatuista peleistä (siirrot, kulunut aika)
- Käyttäjä voi aloittaa uuden pelin valitsemallaan vaikeustasolla (haluttu leveys x korkeus, miinojen määrä)
    - leveys, korkeus ja miinojen määrä on oltava positiivisia nollaa suurempia lukuja
- Käyttäjä voi kirjautua ulos sovelluksesta

### Pelaaminen

- Vaikeustaso määräytyy käyttäjän valitseman pelikentän leveyden, korkeuden ja miinojen lukumäärän mukaan
- Kun uusi peli aloitetaan, aloitetaan myös ajanotto ja avattujen ruutujen (siirtojen) laskeminen
- Käyttäjä voi merkata/poistaa merkityn miinan painamalla hiiren oikeaa painiketta
    - siirtojen lukumäärä ei kasva
- Käyttäjä voi avata ruudun painamalla hiiren vasenta painiketta
    - siirtojen lukumäärä kasvaa
- Mikäli avattu ruutu on miina, peli päättyy
    - ajanotto lopetetaan

## Jatkokehitysideat
- Pelattujen pelien järjestys ajan mukaan pienimmästä suurimpaan
- Pelattujen pelien poistaminen listalta