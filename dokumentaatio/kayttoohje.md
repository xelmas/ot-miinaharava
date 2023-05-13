# Käyttöohje

Lataa sovelluksen viimeisimmän releasen lähdekoodi.

### Konfigurointi

Tulosten tallennukseen käytettävän tiedoston nimeä voi muokata hakemiston .env-tiedostossa. Tiedosto luodaan automaattisesti data-hakemistoon, jos sitä ei vielä ole. Tiedosto on muotoa: \
```DB_FILENAME=database.sqlite```

### Sovelluksen käynnistäminen

1. Lataamisen jälkeen siirry juuri luotuun hakemistoon ja asenna riippuvuudet komennolla ```poetry install```
2. Suorita vaadittavat alustustoimenpiteet komennolla ```poetry run invoke build```
3. Käynnistä sovellus komennolla ```poetry run invoke start```

### Päävalikko (Main Menu)

Sovellus avautuu päävalikkonäkymään:

![Kuva päävalikosta](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/kayttoohje_main_menu.png)

Käyttäjä voi valita haluamansa toiminnon klikkaamalla hiiren vasenta painiketta.

### Pelin pelaaminen (Play)

![Kuva peli-ikkunasta](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/kayttoohje_playing_clean.png)

Sovellus avaa uuden ikkunan, jossa on miinaharavapeli. Peliä pelataan siten, että hiiren vasemmalla klikatessa ruutu avautuu ja oikealla klikatessa ruutu liputetaan. Jo liputettua tai avattua ruutua ei voi liputtaa.

![Kuva peli-ikkunasta liput](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/kayttoohje_playing.png)

Peli-ikkunassa näkyy oikealla allekkain kulunut aika, siirtojen lukumäärä ja jäljellä olevien miinojen lukumäärä, joka vähenee sitä mukaa kun ruutuja liputetaan.

![Kuva pelin päättymisestä voitto](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/kayttoohje_game_end_won.png)

![Kuva pelin päättymisestä häviö](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/kayttoohje_game_end_lost.png)

Pelin päättyessä näytetään kaikkien miinojen sijainti ja näytetään käyttäjälle peliruudun alareunassa oliko peli voitto vai häviö.

### Asetusten muuttaminen (Options)

![Kuva asetuksista](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/kayttoohje_options.png)

Sovellus avaa pudotusvalikon, jossa on vaihtoehtoina valittavina vaikeustasoina Beginner, Intermediate, Expert tai Custom. Käyttäjänimen voi muuttaa syöttämällä haluttu nimi (oltava 3-10 merkkiä) ja painamalla Enter-näppäintä.

![Kuva Custom-vaihtoehdon valinnasta](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/kayttoohje_options_custom.png)

Mikäli käyttäjä valitsee pudotusvalikosta vaihtoehdon Custom, näytölle ilmestyy kentät, joihin voidaan syöttää halutut parametrit pelin leveydelle, korkeudelle ja miinojen lukumäärälle. Pelin korkeuden ja leveyden on oltava väliltä 5-32 ja miinojen lukumäärän väliltä 2-300. Valinta vahvistetaan painamalla Enter-näppäintä (huom. tehtävä jokaisen parametrin kohdalla erikseen). 

Jos syötetyt arvot eivät vastaa annettuja ehtoja, käytetään oletusarvoina lukua 15 kaikilla parametreilla.

### Tilastojen tarkastelu (Leaderboard)

Sovellus näyttää pelattujen voittojen tilastot.

![Kuva tilastosta](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/kayttoohje_leaderboard.png)

Tilastonäkymässä näkyy tuloksittain pelaajan nimi, pelattu vaikeustaso, peliin kulunut aika sekunteina ja käytetyt siirrot. Pelattu vaikeustaso on annettu muodossa w, h, m, missä 
  - w on pelin leveys 
  - h on pelin korkeus 
  - m on miinojen lukumäärä.

### Sovelluksen sulkeminen (Quit)

Ohjelman suoritus lopetetaan.
