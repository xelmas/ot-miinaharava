# Käyttöohje

Lataa sovelluksen viimeisimmän releasen lähdekoodi.

### Sovelluksen käynnistäminen

1. Lataamisen jälkeen siirry juuri luotuun hakemistoon ja asenna riippuvuudet komennolla ```poetry install```
2. Suorita vaadittavat alustustoimenpiteet komennolla ```poetry run invoke build```
3. Käynnistä sovellus komennolla ```poetry run invoke start```

### Päävalikko (Main Menu)

Sovellus avautuu päävalikkonäkymään:

![Kuva päävalikosta](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/kayttoohje_main_menu.png)

Käyttäjä voi valita haluamansa toiminnon klikkaamalla hiiren oikeaa painiketta.

### Pelin pelaaminen(Play)

![Kuva peli-ikkunasta](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/kayttoohje_playing.png)

Sovellus avaa uuden ikkunan, jossa on miinaharavapeli. Peliä pelataan siten, että hiiren oikealla klikatessa ruutu avautuu ja vasemmalla klikatessa ruutu liputetaan. Jo liputettua tai avattua ruutua ei voi liputtaa.

![Kuva pelin päättymisestä](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/kayttoohje_game_end.png)

Pelin päättyessä näytetään kaikkien miinojen sijainti ja näytetään käyttäjälle peliruudun alareunassa oliko peli voitto vai häviö.

### Asetusten muuttaminen (Options)

![Kuva asetuksista](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/kayttoohje_options.png)

Sovellus avaa pudotusvalikon, jossa on vaihtoehtoina valittavina vaikeustasoina Beginner, Intermediate, Expert tai Custom. Mikäli käyttäjä valitsee vaihtoehdon Custom, näytölle ilmestyy kentät, joihin käyttäjä voi syöttää haluamansa parametrit pelin leveydelle, korkeudelle ja miinojen lukumäärälle.

![Kuva Custom-vaihtoehdon valinnasta](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/kayttoohje_options_custom.png)

Syötteeksi hyväksytään vain positiivisia nollaa suurempia kokonaislukuja, jonka jälkeen käyttäjä vahvistaa syötteen painamalla Enter-näppäintä.

### Tilastojen tarkastelu (Leaderboard)

Sovellus näyttää pelattujen voittojen tilastot

### Sovelluksen sulkeminen (Quit)

Ohjelman suoritus lopetetaan.
