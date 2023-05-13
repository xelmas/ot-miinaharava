# Testausdokumentaatio

Ohjelman toiminta on testattu unittestin automatisoiduilla yksikkö- ja integraatiotesteillä sekä manuaalisesti järjestelmätason testeillä.

## Yksikkö- ja integraatiotestaus

### Minesweeper-luokka

Luokka Minesweeper on testattu testiluokalla [TestMinesweeper](https://github.com/xelmas/ot-miinaharava/blob/main/src/tests/minesweeper_test.py).

### Board-luokka

Luokka Board on testattu testiluokalla [TestBoard](https://github.com/xelmas/ot-miinaharava/blob/main/src/tests/board_test.py). 

### Sprite-luokat

Sprite-luokan oliot ovat testattu omilla [testiluokillaan](https://github.com/xelmas/ot-miinaharava/blob/main/src/tests/sprites_test.py)
TestAdjacent, TestEmpty, TestFlag, TestMine ja TestUnrevealed.

### Service-luokka

Luokka ResultService on testattu testiluokalla [TestResultService](https://github.com/xelmas/ot-miinaharava/blob/main/src/tests/result_service_test.py). ResultService alustetaan injektoimalla sille riippuvuudeksi FakeResultRepository-luokan olio, joka tallentaa tietoa muistiin.

### Repositorio-luokka

ResultRepository-luokka on testattu testiluokalla [TestResultRepository](https://github.com/xelmas/ot-miinaharava/blob/main/src/tests/result_repository_test.py). Käytetyn testitietokannan nimi on konfiguroitu .env.test-tiedostoon.

### Testikattavuus

Sovelluksen testien haarautumiskattavuus on 99 %.

![Kuva testikattavuudesta](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kuvat/coverage-report.png)

Testaamatta on jäänyt config.py tiedostosta virhetilanne, joka aiheutuu jos konfiguraatiotiedostoa ei löydy.

## Järjestelmätestaus

Järjestelmätestaus on tehty manuaalisesti.

### Asentaminen

Sovelluksen asentaminen on testattu toimivaksi Linux-ympäristössä [käyttöohjetta](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/kayttoohje.md) noudattamalla.

### Toiminnallisuudet

Pelin toiminta on testattu niin, että kaikki [vaatimusmäärittelyssä](https://github.com/xelmas/ot-miinaharava/blob/main/dokumentaatio/vaatimusmaarittely.md) mainitut kohdat ovat käyty läpi. Kaikkiin syötekenttiin on yritetty syöttää myös virheellisiä arvoja, kuten merkkijonoja ja tyhjiä.

## Sovellukseen jääneet virhetilanteet

Ohjelman suoritus kaatuu, mikäli se yritetään käynnistää ilman, että SQLite tietokantaa on ensin alustettu. Eli käyttöohjeen mukaista ```poetry run invoke build``` komentoa ei ole suoritettu ensin.
