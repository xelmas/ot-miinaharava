# Käyttöohje

Lataa sovelluksen viimeisimmän releasen lähdekoodi.

### Sovelluksen käynnistäminen

1. Lataamisen jälkeen siirry juuri luotuun hakemistoon ja asenna riippuvuudet komennolla ```poetry install```
2. Suorita vaadittavat alustustoimenpiteet komennolla ```poetry run invoke build```
3. Käynnistä sovellus komennolla ```poetry run invoke start```

### Päävalikko (Main Menu)

Sovellus avautuu päävalikkonäkymään:

![Kuva päävalikosta]()

Käyttäjä voi valita haluamansa toiminnon klikkaamalla hiiren oikeaa painiketta.

### Pelin pelaaminen(Play)

![Kuva peli-ikkunasta]()

Sovellus avaa uuden ikkunan, jossa on miinaharavapeli. Peliä pelataan siten, että hiiren oikealla klikatessa ruutu avautuu ja vasemmalla klikatessa ruutu liputetaan. Jo liputettua tai avattua ruutua ei voi liputtaa. Pelin päättyessä näytetään kaikkien miinojen sijainti ja näytetään käyttäjälle peliruudun alareunassa oliko peli voitto vai häviö.

![Kuva pelin päättymisestä]()

### Asetusten muuttaminen (Options)

![Kuva asetuksista]()
![Kuva Custom-vaihtoehdon valinnasta]()

Sovellus avaa pudotusvalikon, jossa on vaihtoehtoina valittavina vaikeustasoina Beginner, Intermediate, Expert tai Custom. Mikäli käyttäjä valitsee vaihtoehdon Custom, näytölle ilmestyy kentät, joihin käyttäjä voi syöttää haluamansa parametrit pelin leveydelle, korkeudelle ja miinojen lukumääräälle.

### Tilastojen tarkastelu (Leaderboard)

Sovellus näyttää pelattujen voittojen tilastot

### Sovelluksen sulkeminen (Quit)

Ohjelman suoritus lopetetaan.
