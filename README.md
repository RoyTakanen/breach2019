# breach2019
Tarkasta mitkä tiedot sinusta on vuotanut Facebookin vuoden 2019 tietomurrossa.

## Demo

[https://breach2019.kaikkitietokoneista.net/](https://breach2019.kaikkitietokoneista.net/)

## Valmistelu

Ennen ohjelman käyttöönottoa joudut siirtämään tiedot MongoDB-tietokantaan. Tarvitset myös tiedoston nimeltä `Finland.txt`. Tämä pitää olla omasta takaa. Aseta ensiksi yhdistystiedot tiedostoon `db_generate.py`. Seuraavaksi ajamalla komennon `python3 db_generate.py` aloitat tietojen tallentamisen tietokantaan. 

## Käyttö

Tarvitset käyttämistä varten MongoDB-tietokannan, jonka yhdistystiedot sinun tulee asettaa `app.py`:ssä. Palvelu voidaan käynnistää komennolla `python3 app.py`. Suosittelen ajamaan ohjelmaa kuitenkin pm2:lla. Komento tähän on `pm2 start app.py --name breach2019 --interpreter python3`. 
