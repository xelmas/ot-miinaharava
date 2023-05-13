## Viikko 3

- Lisätty Board-luokka, joka luo pelikentän ja asettaa miinat.
- Lisätty jokaiselle ruudulle omat Sprite-oliot ja niihin liittyvät grafiikat.
- Testattu, että Board-luokassa pelikentän luominen sekä dimensioiden ja miinojen asetus onnistuu.
- Testattu, että spritejen koordinaatit asetetaan oikein.

## Viikko 4
- Muokattu tiedostojen ja luokkien nimiä, refaktoroitu koodia.
- Board-luokka muutettu Minesweeper-luokaksi, joka vastaa pelilogiikasta.
- Pelilogiikka luotu toimimaan terminaalissa.
- Testattu Minesweeper-luokan reveal-funktion toiminta.
- Luotu käyttöliittymäluokka UI.
- Päävalikkoon luotu neljä eri toimintoa, asetuksiin luotu toiminnallisuus kentän dimensioiden muokkaamiseen.

## Viikko 5
- Pelin graafinen toteutus.
- Lisätty uusi flag-sprite ja kuva.
- Lisätty toiminnallisuus ruutujen liputtamiseen ja liputuksen poistoon
- Lisätty credits-osio menuun, jossa ilmoitettu käytettyjen kuvien tekijä.
- Lisätty options-ikkunaan mahdollisuus muuttaa miinojen määrää pelissä.
- Assets-kansion kuvien kokoa pienennetty kokoon 30x30.
- Lisätty ajanotto (timer).
- Refaktoroitu koodia. Tapahtumakäsittelijät siirretty omiin funktioihin. 
- Luotu oma luokka Board, joka vastaa pelikentästä.
- Lisätty laskuri avattujen ruutujen määrälle.
- Testattu, että Board-luokan liputus ja liputuksen poisto toimii oikein.
- Testattu, että Minesweeper-luokan is_lost(), is_won(), set_time_passed() ja get_time_passed funktiot toimii oikein.
- Luotu sekvenssikaavio pelin aloittamisesta.
- Lisätty teksti kun peli päättyy (voitto tai häviö).

## Viikko 6
- Lisätty sqlite-tietokanta tiedon säilyttämiseen.
- Lisätty docstring-dokumentointi metodeihin ja luokkiin.
- Luotu luokat Result, ResultService, ResultRepository.
- Testattu, että luokat Result, ResultService, ResultRepository toimivat oikein.
- Testattu, että sprite-luokan oliot luodaan oikein.
- Lisätty ohjelman alustustoimenpiteet tietokannalle.
- Päivitetty dokumentit ja arkkitehtuurikuvaukseen lisätty sekvenssikaaviot.
- Luotu alustava käyttöohje.
- Siirretty pelin sovelluslogiikasta vastaavat tiedostot minesweeper.py ja board.py omaan kansioon game.
- Luotu uusin release.

## Viikko 7

### Pelin toiminta
- Muokattu menu-looppia niin, että pelin päättyminen ei sulje ohjelmaa vaan palaa takaisin päävalikkoon.
- Luotu Leaderboard-näkymä pelattujen pelien tilastojen tarkasteluun.
- Lisätty Options-näkymään pelaajan käyttäjänimi, joka on vaihdettavissa. Oletusnimenä "PLAYER".
- Muokattu Custom-levelin syötekentän placeholderit vastaamaan levelin parametrejä (15, 15, 15).
- Lisätty Custom-levelin parametrien syötekenttiin tarkistukset sallituista arvoista. Leveys ja korkeus välillä 5-32 ja miinojen lukumäärä 2-300. Jos ei päde, käytetään oletusarvona lukua 15.
- Lisätty tietokantahaku, joka näyttää vain 10 nopeinta suoritusta nopeusjärjestyksessä.
- Lisätty pelinäkymään alaspäin menevä miinalaskuri, jonka arvo pienenee sitä mukaa kun käyttäjä liputtaa ruutuja, ja vastaavasti kasvaa kun käyttäjä poistaa liputuksen ruudusta. Ei voi mennä kuitenkaan negatiiviseksi.
- Lisätty options-näkymään ohjeistusta käyttäjälle minkä suuruisia ja tyyppisiä syötteitä halutaan.
- Siirretty tuloksen tallennus ja pelinäkymän päivitys UI-luokan hallintaan.
- Luotu luokkaan Board oma metodi koordinaattien ylivuodolle is_over_board() ja korjattu ongelma, että liputtaa pystyi jo avatun ruudun.
- Luotu kustomoitu fontti peli-ikkunan tilastoille (kulunut aika, tehdyt siirrot, miinojen lkm) ja oliko peli voitto/häviö.
- Muokattu Minesweeper-luokan jäljellä olevien miinojen lukumäärälaskurin metodin nimi kuvaavaksi get_game_mines_flagged_info() -> get_unflagged_mines().
- Muokattu UI-luokan tilastojen tarkastelumetodi show_leaderboard() -> leaderboard().

### dokumentaatio
- Päivitetty vaatimusmäärittely.
- Testausdokumentaation luominen.
- Siirretty assets-kansiosta pelin grafiikat omaan images-kansioon ja lisätty font-kansio, joka sisältää kustomoidun font-tiedoston.
- Docstrings-dokumentointi lisätty luokkiin service, repository, spritet.
- Arkkitehtuurikuvauksen päivitys.
- Käyttöohjeen päivitys.

### Testaus
- Testattu että luokka ResultService ja ResultRepository palauttavat 10 parasta tulosta nopeusjärjestyksessä.
- Testattu että sprite-ruudut alustetaan oikein.
- Testattu, että käyttäjälle näkyvä laskuri miinoista ja liputuksista toimii ja  ei voi mennä negatiiviseksi.
- Testattu, että Board-luokan reveal-metodi laskee klikkaukset oikein.
- Testattu, että liputusmetodi ei lisää lippua ruutuun, joka on jo avattu tai ulkopuolella pelikenttää.

