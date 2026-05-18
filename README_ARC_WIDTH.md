# Lanko Analizės (Arc Width) Modulis

Šis modulis (`arc_width_module.py`) yra skirtas interaktyviai impedanso spektroskopijos (EIS) Nyquist grafikų analizei. Jis leidžia vartotojams patogiai, naudojant stačiakampio žymėjimą pele, pasirinkti dominančius impedanso lankus ir automatiškai išskaičiuoti lygiavertės grandinės parametrus (R, CPE elementus) bei tikrojo modelio talpą.

## Pagrindinės Funkcijos

*   **Interaktyvus Žymėjimas:** Dešiniuoju pelės mygtuku (arba kairiuoju, priklausomai nuo Matplotlib konfigūracijos) apibrėžkite stačiakampį aplink dominantį Nyquist lanką.
*   **Apskritimo Aproksimacija (Least Squares Fit):** Modulis automatiškai pritaiko mažiausių kvadratų metodą (Least Squares) ir aproksimuoja pasirinktą lanką tobulu apskritimu.
*   **Fizikinių Parametrų Išgavimas:** 
    *   Išskaičiuojama varža **R** (tarp lanko kirtimosi su X ašimi taškų).
    *   Apskaičiuojamas slopinimo koeficientas **n** (CPE elemento).
    *   Apskaičiuojamas **Q** (CPE admintansas).
    *   Suskaičiuojama ekvivalentinė talpa **C_eq** pagal parametrų maksimumo dažnį.
*   **Rezultatų Fiksavimas:** Leidžia „užfiksuoti“ išanalizuotus lankus (naudojant mygtuką arba `S` klavišą), išsaugant grafinius markerius ekrane ir išvedant statistiką į tekstinį langą tolimesnei analizei.
*   **Kelių Temperatūrų Palaikymas:** Galima analizuoti pavienes temperatūras arba visas aktyvias („Visi pažymėti“) temperatūras vienu metu, kiekvienam duomenų rinkiniui priskiriant atskirą lanko aproksimaciją.

## Kaip Naudoti

1. Paleiskite CeraMIS programą.
2. Užkraukite tyrimų duomenis (pvz., `.json` projektą).
3. Eikite į „Interaktyvi EIS“ (ar pan. priklausomai nuo sąsajos) ir atidarykite Lanko Analizės langą.
4. Grafike pele apibrėžkite lanką. Ekrane bus išvesta pradinė parametrų informacija.
5. Spauskite **„Užfiksuoti pažymėtą lanką“** (arba `S` klavišą), kad įrašytumėte matavimą ir eitumėte prie kito lanko tyrinėjimo.

## Techninė Informacija

*   Naudoja `matplotlib` bibliotekos `RectangleSelector` interaktyviam žymėjimui.
*   Palaiko pilną integraciją su `Tkinter` (naudoja `FigureCanvasTkAgg`).
*   Aproksimacijoms naudojamas `numpy.linalg.lstsq` algoritmas greitam algebriniam apskritimo lygties sprendimui ($A \mathbf{c} = B$).
