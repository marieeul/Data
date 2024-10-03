# Nanoteknologi
Inneholder koder jeg har gjort for øvinger og proskjekter i noen av fagene jeg har hatt. All koding jeg har gjort er ikke inkludert. 

## Nanotools
Notebooks for behandling av data fra ulike elektron mikroskop som FIB, SEM og TEM.
Lærer å bruke hyperspy pakken. Hadde faget i 3 klasse, høsten 2021.

## Bionano
Beregnet radius og diffusjonskonstanter på nano- og mikropartikler høsten 2021.

På mikropartiklene ble det brukt particle tracking i ImageJ fra en video tatt med lysmikroskop for å se hvor mye partiklene flytta på seg mellom bildene. Distansen partikklene hadde flytta på seg ble lagret som CSV filer. Deretter ble python brukt til å beregne diffusjonskonstantenene og radiusene for partiklene. Det ble så laget histogram for å presantere resultatene. Histogramer for diffusjonskonstant og radius for prøve A er vist her.

Diffusjonskonstanten for nanopartiklene ble funnet ved hjelp av absorbsjonsforskjell i farge. Partiklene var blå og ble pumpet gjennom en mikrokanal sammen med vann. Differanse i fargeintensiteten fra start til slutt kan brukes til å estimere diffusjonskonstanten for partikklene. Bilde av curvefittingen til dataene våre er vist.

## Livssyklusanalyse
Mine øvinger gjort i TEP4223 høsten 2023 i 5 klasse.

Kort emnebeskrivelse: Faget gir en innføring i rammeverket for livsløpsanalyser (life cycle assesment). 
Livsløpsanalyser brukes for å analysere hvor i løpet til et produkt miljøbelastningene er størst og hvilke miljøbelastinger ulike produkter gir. 
Det brukes for å forsikre seg om at miljøtiltak har en samlet effekt og at man ikke bare flytter utslipp fra bruks fasen til tilvirkningsfasen av et produkt eller bare endrer på hvilke miljøbelastninger produktet gir. 
Emnet skal gjøre studenten i stand til å: - Gjennomføre en moderat kompleks LCA under veiledning. 
Lenke til emnebeskrivelse: https://www.ntnu.no/studier/emner/TEP4223/2023#tab=omEmnet

Øvingene er gjort i Jupyter Notebooks. En liten andel av koden var gitt av foreleser. Øvingene blir mer komplekse etterhvert.

Kode delen av eksamensbesvarelsen min er også lastet opp. 
Oppgaven var å gjøre en livssyklusanalyse for å sammenligne en diselbuss med en elektriskbuss for å kunne gi en anbefaling til et bystyre om hva man burde kjøpe inn basert på miljbelastningen til de to alternativene. 
Relevant data var gitt i excel tabeller som så måtte leses og lagres i pandas matriser. 
Data om matrial og energi bruk for de to bussene var gitt og utslippene knyttet til en standard mengde av matrialene/energiene brukt. 
Matrisene ble så slått sammen og fremstilt på en gunstig måte før matriser for utslipp og belastning for hver busstype ble regnet ut.
 
