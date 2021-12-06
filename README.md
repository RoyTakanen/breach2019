# breach2019
Tarkasta mitkä tiedot sinusta on vuotanut Facebookin vuoden 2019 tietomurrossa.

Sivusto: [breach2019.cf](https://breach2019.cf)

## Valmistelu

Ennen ohjelman käyttöönottoa tarvitset kopion `Finland.txt`-nimisestä tiedostosta, joka löytyy tietovuodosta. Tämä pitää olla omasta takaa. Aseta tiedosto kansioon `data` omalla nimellään. 

## Käyttö

**KIKKAVITONEN:** Asettamalla `DL_URL` ympäristömuuttujan voit ladata ympäristömuuttujan arvosta `Finland.txt`-tiedoston sisällön. Tällöin et tarvitse erillistä `Finland.txt`-tiedostoa `data`-kansioon.

### Kehitysympäristö

Palvelu voidaan käynnistää komennolla `python3 app.py`. Ohjelma lukee tiedoston `data/Finland.txt`. Ilman tiedostoa ohjelma ei käynnisty. Ohjelma käynnistyy porttiin `5000`.

### Tuotanto

Tuotannossa voi käyttää Dockeria. Ohjelmalle on luotu [docker-compose.yml](./docker-compose.yml)-tiedosto, joka käynnistää ohjelman porttiin 8080. 

*Oman `docker-compose.yml`-tiedoston luomisessa huomioitavaa:*

Docker-kontille tulee luoda volume, joka on yhteydessä kontin kansioon `/app/data` ja sisältää `Finland.txt`-tiedoston. Ohjelma löytyy kontin sisällä portista `5000`. 
