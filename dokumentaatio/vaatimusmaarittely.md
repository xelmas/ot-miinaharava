# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on yksinpelattava miinaharava, jonka vaikeustason voi käyttäjä itse kustomoida tai valita oletustasoista. Käyttäjä voittaa pelin, mikäli onnistuu avaamaan kaikki ruudut, joissa ei ole miinaa. Käyttäjä häviää pelin, mikäli osuu miinaan.

## Toiminnallisuudet

### Päävalikko
- Käyttäjälle näkyy neljä eri toimintoa: play (pelaaminen), options (asetukset), leaderboard (tilasto), quit (lopetus). (Tehty)

### Pelaaminen
- Vaikeustaso määräytyy käyttäjän valitseman pelikentän leveyden, korkeuden ja miinojen lukumäärän mukaan (Tehty)
- Kun uusi peli aloitetaan, aloitetaan myös ajanotto ja avattujen ruutujen (siirtojen) laskeminen
- Käyttäjä voi merkata/poistaa merkityn miinan painamalla hiiren oikeaa painiketta (Tehty)
    - Siirtojen lukumäärä ei kasva
- Käyttäjä voi avata ruudun painamalla hiiren vasenta painiketta (Tehty)
    - Siirtojen lukumäärä kasvaa
- Mikäli avattu ruutu on miina, peli päättyy  (Tehty)
    - Ajanotto lopetetaan

### Asetukset
- Käyttäjä voi valita neljästä eri vaihtoehdosta vaikeustason: Beginner, Intermediate, Expert tai Custom. (Tehty)
- Jos käyttäjä valitsee Custom, pyydetään käyttäjää syöttämään pelikentän leveys, korkeus ja miinojen lukumäärä. (Tehty)

### Tilasto
- Käyttäjä voi tarkastella pelattujen pelien tilastoja

### Lopetus
- Sulkee ohjelman. (Tehty)

## Jatkokehitysideat
- Pelattujen pelien järjestys ajan mukaan pienimmästä suurimpaan
- Pelattujen pelien poistaminen listalta
- Mahdollisuus luoda käyttäjätunnus ja kirjautua sisään
