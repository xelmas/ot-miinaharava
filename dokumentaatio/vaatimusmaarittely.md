# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovellus on yksinpelattava miinaharava, jonka vaikeustason voi käyttäjä itse kustomoida tai valita oletustasoista. Käyttäjä voittaa pelin, mikäli onnistuu avaamaan kaikki ruudut, joissa ei ole miinaa. Käyttäjä häviää pelin, mikäli avaa ruudun, jossa on miina.

## Toiminnallisuudet

### Päävalikko
- Käyttäjälle näkyy neljä eri toimintoa: Play (pelaaminen), Options (asetukset), Leaderboard (tilasto), Quit (lopetus).

### Pelaaminen
- Vaikeustaso määräytyy käyttäjän valitseman pelikentän leveyden, korkeuden ja miinojen lukumäärän mukaan.
- Kun uusi peli aloitetaan, aloitetaan myös ajanotto ja avattujen ruutujen (siirtojen) laskeminen.
- Käyttäjälle näkyy laskuri, joka kertoo kuinka monta miinaa pelissä vielä on. Laskurin arvo pienenee kun käyttäjä liputtaa ruutuja. Laskuri ei kuitenkaan voi mennä negatiiviseksi, eikä se ota kantaa sisältääkö käyttäjän merkkaama ruutu todella miinaa.
- Käyttäjä voi merkata miinan sisältävän ruudun liputtamalla sen painamalla hiiren oikeaa painiketta. Käyttäjä voi myös poistaa liputuksen klikkaamalla liputettua ruutua uudestaan hiiren oikealla painikkeella.
    - Siirtojen lukumäärä ei kasva.
    - Jäljellä olevien miinojen lukumäärä vähenee yhdellä.
- Käyttäjä voi avata ruudun painamalla hiiren vasenta painiketta.
    - Siirtojen lukumäärä kasvaa yhdellä.
- Mikäli avattu ruutu on miina, peli päättyy.
    - Ajanotto lopetetaan.
- Kun peli päättyy, ilmoitetaan käyttäjälle oliko peli voitto vai häviö ja palataan takaisin päävalikkoon. Jos peli päättyi voittoon, tallennetaan tulos tietokantaan.

### Asetukset
- Käyttäjä voi valita neljästä eri vaihtoehdosta vaikeustason: Beginner, Intermediate, Expert tai Custom.
- Jos käyttäjä valitsee Custom, pyydetään käyttäjää syöttämään pelikentän leveys, korkeus ja miinojen lukumäärä.
    - Vaikeustason leveys tai korkeus ei voi olla suurempi kuin 32, mutta oltava vähintään 5.
    - Miinoja on oltava vähintään 2 ja maksimissaan 300. Jos miinoja on yhtä paljon kuin ruutuja, käytetään oletusarvoa 15.
- Käyttäjä voi antaa käyttäjänimen, joka tallennetaan tietokantaan pelituloksen yhteydessä, kun peli päättyy voittoon. Oletusnimenä "PLAYER".

### Tilasto
- Käyttäjälle näytetään max 10 parasta tulosta aikajärjestyksessä nopeimmasta hitaimpaan.
- Jos peli päättyy voittoon, tulos tallennetaan tietokantaan. Tietokantaan tallennetaan asetuksissa valitut tiedot: pelaajan nimi, pelin leveys, korkeus ja miinojen lukumäärä. Pelistä tallennetaan lisäksi peliin kulunut aika sekunteina ja kuinka monta siirtoa eli klikkausta käyttäjä käytti ruutujen avaamiseen.

### Lopetus
- Sulkee ohjelman.

## Jatkokehitysideat
- Pelattujen pelien poistaminen listalta.
- Mahdollisuus luoda käyttäjätunnus ja kirjautua sisään.
- Äänitehosteiden lisääminen.
- Pelitulosten näyttäminen vaikeustasoittain.
- Menun ulkoasun muokkaus.
