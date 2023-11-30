# De genes, genética...

## PID_

Dorcas J. Orengo Ferriz


**Dorcas J. Orengo Ferriz**
Doctora en Biología (Universidad de
Barcelona). Investigadora en el gru-
po de Genética Molecular Evolutiva
del Departamento de Genética de la
Facultad de Biología de la UB. Pro-
fesora del curso de posgrado Filoge-
nias y genealogía de DNA: recons-
trucción y aplicaciones, del Institu-
to de Investigación de la Biodiversi-
dad de la UB (IRBio). Consultora de
la asignatura Biología molecular del
máster de Bioinformática y Bioesta-
dística de la UOC.

```
Ninguna parte de esta publicación, incluido el diseño general y la cubierta, puede ser copiada,
reproducida, almacenada o transmitida de ninguna forma, ni por ningún medio, sea éste eléctrico,químico, mecánico, óptico, grabación, fotocopia, o cualquier otro, sin la previa autorización escrita
de los titulares del copyright.
```

## Índice

- Introducción
- 1. Genética clásica. Leyes de Mendel
- 2. Ligamiento
   - 2.1. Herencia ligada al sexo
   - 2.2. Recombinación y mapas genéticos
   - 2.3. Transposones
- 3. Herramientas estadísticas básicas en el estudio genético
   - 3.1. Cálculo de las proporciones esperadas
   - 3.2. Contraste de hipótesis
- 4. Estudio de pedigríes
- 5. Otros tipos de herencia
- 6. Evolución del concepto de gen



## Introducción

El nacimiento de un bebé es una fuente inagotable de preguntas, sobre todo
en los padres primerizos. ¿Crecerá fuerte y sano? ¿Sabré educarlo? Ahora, ¿por
qué llora?... Pero cuando llegan las visitas, la pregunta estrella es mucho más
simple: ¿Se parece al padre o a la madre? La experiencia nos dice que, aunque
cada individuo es único y diferente, los hijos se parecen a los padres. Y por
ello se emplea un buen rato en observar la carita redonda y sonrosada del bebé
cuyos rasgos aún están por definir, intentando apreciar parecidos de una u
otra familia.

El parecido entre padres e hijos se debe a la transmisión de caracteres hereda-
bles de una generación a la siguiente. Estos caracteres heredables pueden ser
de diversa índole: aspecto físico, características fisiológicas, comportamiento...
Estas características se transmiten a través de los genes. Pero ¿qué es un gen?

El **gen** puede definirse de distintos modos, según el nivel de estudio que este-
mos abordando. Para la comprensión de los conceptos expuestos en este mó-
dulo basta con una definición algo abstracta pero sencilla de gen: "cualquier
factor que determina una característica particular y heredable de un organis-
mo". Al final del módulo, no obstante, abordaremos la definición de gen como
ente físico. Veremos que, en este sentido, la definición de _gen_ ha ido cambian-
do a medida que hemos ido conociendo cómo se estructura la información
genética en el genoma, como explican Gerstein y otros.

La genética estudia los genes, sus patrones de transmisión y cómo las poblacio-
nes cambian su composición genética con el tiempo y el espacio. La genética
es una ciencia relativamente joven. Podemos decir que nació en 1900 cuando
fueron redescubiertos los experimentos publicados por Mendel en 1865. Pero
la humanidad ha utilizado, más o menos conscientemente, los principios bá-
sicos de la genética desde hace miles de años.

```
Referencia bibliográfica
M.￿B.￿Gerstein;￿C.￿Bruce;￿J.
S.￿Rozowsky;￿D.￿Zheng;￿J.
Du;￿J.￿O.￿Korbel;￿O.￿Ema-
nuelsson;￿Z.￿D.￿Zhang;
S.￿Weissman;￿M.￿Zinder
(2007). "What is a gene, post-
ENCODE? History and upda-
ted definition". Genome Re-
search (vol.17, pág. 669-681).
```
El uso de la genética por el hombre se remonta a los orígenes de la agricultura
(hace unos 12.000-15.000 años) y la domesticación de plantas y animales. En
cada especie, el hombre seleccionó entre las variantes disponibles aquellas que
mejor se adaptaban a sus necesidades. Sin saberlo, estaba haciendo uso de la
genética y favoreciendo la perpetuación de una serie de características, y no
otras. En el Talmud, escritos del siglo II que recogen la tradición oral de los
judíos, se encuentra la prohibición de practicar la circuncisión a bebés cuyos
hermanos mayores (o primos hermanos, hijos de hermanas de su madre) hu-
bieran muerto desangrados. Esto indica que eran conscientes de que la apari-
ción de estas hemorragias anómalas (la hemofilia) tenía un origen hereditario

```
La hemofilia
La hemofilia es una enferme-
dad hereditaria ligada al cro-
mosoma X. El enfermo de he-
mofilia carece de un factor de
coagulación de la sangre, lo
que le supone que cualquier
pequeña herida o golpe puede
ocasionar una grave hemorra-
gia externa o interna.
```

que se transmitía por vía materna. Pero el estudio sistemático de la herencia
de caracteres no empieza hasta finales del siglo XIX con los trabajos de Gregor
Mendel, que llevaron a la formulación de las famosas leyes de Mendel.

La herencia mendeliana es el patrón de herencia biológica más simple. Pero
diversos fenómenos como el ligamiento, la interacción génica o la herencia
aditiva pueden complicar mucho los patrones de herencia.


## 1. Genética clásica. Leyes de Mendel

Gregor Mendel (1821-1884) es considerado el padre de la genética debido a
sus experimentos pioneros hibridando plantas de guisantes. Sus experimen-
tos, publicados en alemán en 1865, pasaron inadvertidos hasta 1900 cuando
fueron redescubiertos por Hugo de Vries, Carl Corrents y Erich von Tschermak.
Las observaciones que realizó llevaron posteriormente a la formulación de las
que se conocen como **leyes￿de￿Mendel**.

Figura 5.1. Retrato de Gregor Mendel y lámina de la especie objeto de sus estudios _Pisum
sativum_

Fuente: Wikipedia.

Mendel eligió el guisante, _Pisum sativum_ , como organismo modelo para rea-
lizar sus experimentos porque reunía una serie de características especiales:
presenta variedades con características permanentes que son fácilmente reco-
nocibles; aunque sus flores se autofecundan, los experimentos de fecundación
artificial acostumbran a tener éxito; se cultivan fácilmente, y el periodo de
crecimiento es relativamente corto. A esto debe añadirse la numerosa descen-
dencia que se obtiene a partir de cada planta individual, lo que permite ana-
lizar matemáticamente las proporciones de las distintas características en la
descendencia.

Los organismos modelo utilizados hoy en día en estudios genéticos cumplen
las características que ya buscó Mendel en los guisantes:

- Existencia de variedades observables.
- Fácil mantenimiento.
- Tiempo de generación corto.
- Control sobre los cruzamientos.

```
Referencia bibliográfica
G.￿Mendel (1865). "Versuche
über Pflanzenhybriden". Ver-
handlungen des naturforschen-
den Vereines in Brünn, Bd. IV
für das Jahr 1865. (Abhand-
lungen, 3-47). Brünn.
```

- Numerosa descendencia.

El guisante ha sido abandonado como organismo modelo porque, aunque
Mendel consideró que su desarrollo era relativamente rápido, se trata de una
planta anual. Por ello, Mendel tuvo que invertir ocho años para completar sus
experimentos, algo totalmente impensable hoy en día.

Mendel partió de 34 variedades de guisantes que primero cultivó durante dos
años consecutivos para comprobar que eran variedades puras (la descendencia
era homogénea para las características analizadas). Eligió siete caracteres mor-
fológicos para los que las distintas variedades de guisantes presentaban una
de dos posibles variantes:

- Forma de la semilla (lisa o rugosa).
- Color de la semilla (amarillo o verde).
- Color de las flores (violetas o blancas).
- Forma de la vaina madura (inflada o arrugada).
- Color de la vaina tierna (verde o amarilla).
- Posición de las flores en los tallos (a lo largo del tallo o en su extremo).
- Longitud del tallo (matas altas o matas enanas).

Para cada uno de estos caracteres, realizó experimentos de hibridación cruzada
entre variedades que se diferenciaban en dicho carácter. Los resultados que
obtuvo para cada uno de los siete caracteres que estudió fueron muy similares.
Por ello y para simplificar, nos fijaremos en los resultados que obtuvo sólo en
uno de ellos: la forma de la semilla (tabla 5.1.).

Tabla 5.1. Resultados obtenidos por Mendel al cruzar variedades que diferían en un único carác-
ter del aspecto de la semilla

```
Generación
parental (P)
```
```
1.ª generación filial (F 1 ) 2.ª generación filial (F 2 )
```
```
Lisa × Rugosa Todas lisas 5.474 lisas / 1.850 rugosas
Amarillas × Verdes Todas amarillas 6.022 amarillas / 2.001 verdes
```
Al cruzar dos variedades (generación parental o P) que diferían en un carácter
(por ejemplo, forma de la semilla), vio que los híbridos (o generación filial
F 1 ) presentaban siempre la misma variante de uno de los padres (semilla lisa).

Cuando permitía la autopolinización de la F 1 para obtener la segunda genera-
ción filial o F 2 , obtenía individuos con la variante de los híbridos F 1 (semilla
lisa) y otros individuos en los que reaparecía la variante parental ausente en la
F 1 (semilla rugosa). A la variante presente en la F 1 la llamó **dominante** , y a la

variante parental que reaparecía en la F 2 la llamó **recesiva**. La gran cantidad de
descendientes obtenidos le permitió observar además que en la F 2 la propor-
ción de variantes era aproximadamente de 3 dominante frente a 1 recesiva.


Estos resultados y observaciones se formularon posteriormente en la primera
ley de Mendel.

```
La primera￿ley￿de￿Mendel , o Principio￿de￿segregación , establece que
cada organismo diploide posee dos alelos para un carácter determinado.
Cuando se forman los gametos, estos alelos se separan, yendo cada uno
a un gameto distinto. Asimismo, el concepto de dominancia nos dice que
cuando un organismo tiene dos alelos distintos para un carácter, sólo
se observa el rasgo codificado por uno de ellos, que es el dominante ,
quedando escondido el del otro, que es el recesivo.
```
Mendel continuó sus experimentos durante algunas generaciones más de au-
tofecundación y observó que los individuos con la variante recesiva se com-
portaban siempre como una raza pura, produciendo una descendencia homo-
génea que mostraba dicha variante. En cambio, mientras que algunos indivi-
duos con la variante dominante también parecían una raza pura que producía
descendencia homogénea, otros se parecían a los híbridos de la F 1 , producien-
do una descendencia heterogénea con proporciones 3:1. Estas diferencias en
la descendencia de los híbridos de fenotipo dominante se explican porque en
realidad tienen genotipo distinto.

```
Es muy importante distinguir entre genotipo y fenotipo. El genotipo se
refiere a la información genética presente en un individuo, es decir al
conjunto de alelos que posee. El fenotipo se refiere al aspecto observable
del individuo; este aspecto o conjunto de caracteres que presenta es el
resultado de la interacción entre su genotipo y el ambiente en que se
ha desarrollado.
```
```
Alelo
Alelo es el nombre que recibe
cada una de las posibles va-
riantes de un gen.
```
La figura 5.2. muestra esquemáticamente la explicación de la primera ley de
Mendel y su relación con la meiosis. Los genes se localizan en los cromosomas
y los individuos diploides cuentan con dos copias de cada cromosoma (cro-
mosomas homólogos). Así, cada individuo posee dos alelos para un gen de-
terminado, localizados cada uno sobre un cromosoma homólogo distinto. Si
llamamos _A_ al alelo dominante, y _a_ al recesivo, el genotipo del híbrido de la F 1

es _Aa_ y su fenotipo corresponde al del alelo dominante _A_. Como hemos visto,
los cromosomas homólogos se separan durante la meiosis. Así, cada gameto
sólo contiene una de las dos copias del gen. Durante la fecundación se unen
al azar un gameto de cada progenitor. De ahí las proporciones fenotípicas que
observamos en la F 2 : tres individuos manifiestan la variante dominante ( _A__ )
y un individuo manifiesta la variante recesiva ( _aa_ ), que a su vez responden a
las proporciones genotípicas de 1 AA:2 Aa:1 aa.

```
Ved también
Hemos explicado el comporta-
miento de los cromosomas ho-
mólogos en la meiosis en el ca-
pítulo "Reproducción sexual.
Meiosis"
```
```
Nota
La notación A_ indica que el
individuo es portador de al
menos un alelo dominante A ,
pudiendo ser homocigoto ( AA )
o heterocigoto ( Aa ).
```

```
Figura 5.2. Esquema que explica las observaciones de Mendel resumidas en la primera ley de
Mendel
```
Mendel fue aún más allá y realizó una serie de experimentos de dihibridismo,
en los que consideraba simultáneamente distintos pares de características. Por
ejemplo, cruzó una variedad que producía semillas lisas y amarillas con otra
que las producía rugosas y verdes. Las semillas híbridas fueron todas lisas y
amarillas, tal como esperaba por los resultados obtenidos anteriormente de los
cruces monohíbridos (tabla 5.1.). En la siguiente generación, obtuvo distintos
tipos de semillas: 315 lisas amarillas, 101 rugosas amarillas; 108 lisas verdes y
32 rugosas verdes. Las variantes para los dos caracteres se entremezclan, apa-
reciendo las cuatro combinaciones posibles en unas proporciones cercanas a
9:3:3:1. Estos resultados son la base de la segunda ley de Mendel (figura 5.3.).

```
La segunda￿ley￿de￿Mendel o Principio￿de￿la￿distribución￿indepen-
diente , afirma que los alelos de loci diferentes se separan de forma in-
dependiente.
```
```
Loci
Locus ( loci , en plural) se refiere
al lugar que ocupa un gen de-
terminado en el cromosoma.
Por extensión, también se re-
fiere a dicho gen.
```

```
Figura 5.3. Segunda ley de Mendel
```
```
Nótese que el cruzamiento de este ejemplo genera una Fdistintos pero sólo cuatro fenotipos diferentes, que esperamos encontrar en la siguiente proporción: 9/16 2 , en que los individuos pueden presentar nueve genotipos AB ; 3/16 Ab ;
3/16 aB y 1/16 ab.
```
Hasta aquí se ha considerado que un carácter tiene sólo dos posibles alelos, pe-
ro a menudo un gen tiene alelos múltiples. La herencia de un sistema de alelos
múltiples no difiere de la de un sistema de dos alelos, salvo en que existen más
genotipos y fenotipos posibles. Un sistema de alelos múltiples bien conocido
es el de los grupos sanguíneos AB0. Este sistema cuenta con tres alelos:

- _IA_ , que codifica para el antígeno A.
- _IB_ , que codifica para el antígeno B.
- El alelo _i_ que no codifica para ningún antígeno (0).

El alelo _i_ es recesivo, mientras que los alelos _IA_ y _IB_ son codominantes entre
sí. Podemos, pues, encontrar seis genotipos distintos que determinan cuatro
fenotipos:

- _IAIA_ y _IAi_ grupo sanguineo A.
- _IBIB_ y _IBi_ grupo sanguíneo B.
- _IAIB_ grupo sanguíneo AB.
- _ii_ grupo sanguíneo 0.

```
Aunque en una población pueden existir multitud de alelos distintos
para un gen cualquiera, un individuo sólo cuenta con dos alelos, que
pueden ser iguales ( homocigoto ) o distintos ( heterocigoto ).
```

El patrón de herencia puede ser bastante más complejo que el descrito por
Mendel:

- En ocasiones, un carácter viene determinado por la interacción de diversos
    genes.
- A veces, la manifestación de un carácter está supeditada a determinadas
    condiciones ambientales.

Además, debemos considerar matizaciones y/o ampliaciones para ambas le-
yes de Mendel. Por un lado, no siempre se observa una relación de dominan-
cia/recesividad entre alelos. En algunas ocasiones encontramos **dominancia
incompleta** , observando que el heterocigoto presenta un fenotipo intermedio
al de ambos homocigotos. En otras ocasiones hay **codominancia** , observán-
dose el fenotipo de ambos homocigotos simultáneamente. Por otro lado, no
todas las parejas de loci se heredan independientemente sino que puede exis-
tir **ligamiento**.

El modo de clasificar el tipo de relación de dominancia es un tanto arbitrario,
pudiendo cambiar según el nivel al que estemos observando el fenotipo. Un
ejemplo paradigmático de esto nos lo ofrece la anemia falciforme. La anemia
falciforme es una enfermedad humana grave, determinada por el gen que co-
difica para la hemoglobina, la molécula responsable del transporte de oxígeno

en la sangre. Existen dos alelos _HbA_ y _HbS_ y la tabla 5.2. recoge los fenotipos
que determinan cada uno de los tres genotipos posibles. Si nos fijamos global-
mente en el individuo, veremos que el alelo que determina la anemia falcifor-
me es recesivo. Si centramos nuestra atención en los glóbulos rojos, observa-
remos que los heterocigotos presentan un fenotipo intermedio (dominancia
incompleta). Si descendemos al nivel molecular, veremos que los heterocigo-
tos expresan los dos fenotipos simultáneamente, presentan los dos tipos de
cadenas proteicas (codominancia).

Tabla 5.2. Distintos niveles de observación del fenotipo para el carácter anemia falciforme

```
Genotipo Individuo Glóbulos rojos Hemo-
globina
```
```
HbA HbA Sano Discoidales Forma A
```
```
HbA HbS Sano Sólo se deforman en condiciones de pocooxígeno Formas A y S
```
```
HbS HbS Anemia Deformados en forma de hoz Forma S
```

## 2. Ligamiento

Si sobre un cromosoma se encuentran numerosos genes y si los cromosomas
se transmiten enteros durante la división celular, podemos concluir que di-
chos genes se transmiten conjuntamente, esto es, están ligados. Esta situación
constituye una excepción a la segunda ley de Mendel, que para ser más precisa
debería especificar que son los genes localizados en cromosomas de distintas
parejas los que se transmiten de forma independiente. De todos modos, los
genes de un mismo cromosoma también pueden separarse en la formación de
los gametos debido al fenómeno de recombinación intracromosómica.

Podemos detectar el ligamiento mediante un **cruzamiento￿prueba** , cruzando
un heterocigoto para ambos caracteres con el doble homocigoto recesivo. En
caso de no estar ligados, esperamos encontrar cuatro combinaciones fenotípi-
cas equifrecuentes en la descendencia. En caso de caracteres totalmente liga-
dos, sólo aparecerán dos fenotipos en la descendencia (figura 5.4.).

Figura 5.4. Resultado esperado de un cruzamiento prueba en caso de dos caracteres
independientes o de dos caracteres totalmente ligados

En el caso de genes ligados entre los que hay recombinación con una frecuen-
cia _r_ , encontramos cuatro genotipos en la descendencia, pero estos genotipos
no son equifrecuentes, siendo los más frecuentes los determinados por los ga-
metos no recombinantes (figura 5.5.).

En el caso de un doble heterocigoto, es importante conocer cómo se disponen
los alelos en cada cromosoma o **fase￿de￿los￿alelos** , que definirá el **haplotipo**
del cromosoma o combinación de alelos de cada cromosoma. Cuando los dos
alelos salvajes se encuentran sobre un mismo cromosoma y los mutantes so-
bre el otro, se dice que se encuentran en **fase￿de￿acoplamiento** o **_cis_** ; en caso


contrario se dice que están en **fase￿de￿repulsión** o **_trans_** (figura 5.6.). Depen-
diendo de la fase o haplotipo, la composición de la descendencia será una u
otra, ya que el haplotipo no recombinante se transmite con mayor frecuencia.

```
Figura 5.5. Resultado del cruce prueba para dos genes
ligados con frecuencia de recombinación r entre ellos
```
En el caso de secuenciación de genomas de organismos diploides, a menudo se
secuencia simultáneamente la información portada por ambos cromosomas
homólogos. En el caso de existir diversas posiciones heterocigotas, no es po-
sible saber con certeza qué combinación de variantes es la portada por cada
cromosoma.

```
Figura 5.6. Posibles fases de los alelos de un doble heterocigoto
```
HapMap es un importante proyecto que consiste precisamente en determinar
haplotipos en el genoma humano, es decir, en determinar qué combinaciones
de SNP (acrónimo inglés para _single nucleotide polymorphism_ ) están unidas, y
cómo se distribuyen en distintas poblaciones del mundo. Esta información
ayudará a los investigadores a encontrar asociaciones entre SNP y ciertas en-
fermedades.


Un ejemplo especial de genes ligados lo constituyen los genes ligados al sexo,
que son los que están en los cromosomas sexuales. Las diferencias en esta
pareja de cromosomas hacen que, en la descendencia de determinados cruces,
puedan aparecer unos caracteres en un sexo y no en el otro.

### 2.1. Herencia ligada al sexo

La determinación del sexo (el que un individuo se desarrolle como hembra
o como macho) se consigue por medios diversos según el tipo de organismo
que consideremos. En muchos casos viene mediada por la combinación de un
par de cromosomas: los **cromosomas￿sexuales**. A diferencia del resto de pares
de cromosomas (o **autosomas** ), los cromosomas sexuales no son totalmente
homólogos. En mamíferos y otros organismos, estos cromosomas reciben el
nombre de _cromosomas X_ e _Y_. La combinación XX determina sexo femenino
(♀) y la combinación XY sexo masculino (♂). En otros organismos, como aves
y lepidópteros, los cromosomas sexuales se conocen como Z y W. En este caso,
las hembras son heterogaméticas, presentan los dos cromosomas diferentes
ZW, mientras que los machos son homogaméticos y presentan ZZ.

La herencia de los genes ligados a los cromosomas XY es similar a la de los
genes ligados a los cromosomas ZW, cambiando sólo a qué sexo afecta. Por ello
nos centraremos únicamente en el estudio de los genes ligados al sistema XY.

En general, el cromosoma Y es en gran parte heterocromático, su cromatina
está compactada impidiendo la expresión génica. Además, en comparación
con otros cromosomas contiene pocos genes, algunos específicos del cromo-
soma Y y unos pocos compartidos con el cromosoma X. El cromosoma X con-
tiene un mayor número de genes que el Y.

La herencia de los genes ligados al cromosoma X es un tanto peculiar debido
a que machos y hembras tienen distinto número de copias. Mientras que las
hembras cuentan con dos copias (de origen materno y paterno) los machos
sólo cuentan con una (de origen materno). Por ello, los cruzamientos recípro-
cos muestran resultados distintos (figura 5.7.).

La herencia ligada al cromosoma X fue explicada por primera vez por Thomas
H. Morgan en 1910. Tras descubrir un macho de _D. melanogaster_ con ojos blan-
cos, lo cruzó con hembras de fenotipo salvaje, de ojos rojos. La descendencia
resultó ser homogénea con ojos rojos, indicando que el alelo para ojos blancos
era recesivo. La sorpresa llegó con el recuento de la F 2. Según la herencia men-
deliana esperaba que 1/4 de los individuos, indistintamente machos y hem-
bras, tuvieran los ojos blancos. En cambio, obtuvo una descendencia en que
todas las hembras y la mitad de los machos tenían los ojos rojos y sólo la mitad
de los machos tenían los ojos blancos. Morgan supuso que el gen responsable
del color de los ojos se encontraba en el cromosoma X. Puesto que las hem-

```
Drosophila
Se calcula que en el cromoso-
ma Y de Drosophila sólo hay
entre 10 y 20 genes de copia
única codificadores de proteí-
na, mientras que en el cromo-
soma X hay más de 2.500.
```
```
Cruzamientos recíprocos
Los cruzamientos recíprocos
son pares de cruzamientos en
los que los machos de un cru-
zamiento presentan el fenotipo
de las hembras del otro cruza-
miento y viceversa.
```
```
T. Morgan
T. Morgan recibió el Premio
Nobel en 1933 por sus descu-
brimientos relacionados con el
papel de los cromosomas en la
herencia.
```

bras tienen dos cromosomas X, pueden ser homocigotas o heterocigotas. En
cambio, los machos al no poseer más que un solo cromosoma X se dice que
son **hemicigóticos** y siempre expresan el único alelo que portan.

Morgan predijo que el cruzamiento entre hembras de ojos blancos y machos
de ojos rojos generaría una descendencia en que el fenotipo de la descenden-
cia invertiría su asociación con el sexo: todas las hembras serían de ojos rojos
y todos los machos tendrían ojos blancos. Efectivamente, cuando en las sub-
siguientes generaciones obtuvo hembras con ojos blancos, comprobó experi-
mentalmente que sus predicciones eran correctas.

```
Figura 5.7. Herencia del gen w ( white ) en D. melanogaster
```
```
Esquema de cruzamientos recíprocos entre individuos de dos cepas puras de que el fenotipo de la F 1 es distinto en ambos cruzamientos, y que cuando se cruzan hembras mutantes con machos de tipo Drosophila respecto al color de sus ojos. Nótese
salvaje, el fenotipo de la descendencia invierte su asociación con el sexo.
```
### 2.2. Recombinación y mapas genéticos

```
En general, cuanto más alejados físicamente en el cromosoma se en-
cuentren dos genes, mayor será la frecuencia de recombinación ( r ) entre
ellos y menos ligados estarán.
```
Morgan se dio cuenta que los genes ligados podían separarse y que lo hacían
a frecuencias muy variadas dependiendo de los pares de genes que estuviera
considerando. Partiendo de la teoría cromosómica de la herencia (los genes
se localizan en los cromosomas), Morgan postuló que debía existir un meca-
nismo de intercambio de material cromosómico o entrecruzamiento. Además,
consideró que durante la meiosis los entrecruzamientos se distribuían al azar
sobre el cromosoma.


Estas ideas llevaron a Alfred Sturtevant, un joven estudiante en el laboratorio
de Morgan, a pensar que se podía relacionar directamente las distancias físicas
de los genes sobre el cromosoma con su frecuencia de recombinación. De este
modo, dibujó el primer mapa de ligamiento para seis genes del cromosoma
X de _D. melanogaster_.

En un mapa genético, las distancias entre genes se miden en centimorgans
(cM). Un cM equivale a una recombinación del 1%. Las distancias genéticas
medidas a partir de la recombinación son casi aditivas y sus magnitudes nos
dan pistas de las posiciones relativas de los genes. Imaginemos que tenemos
tres genes ligados A, B y C. Si la distancia entre A y B es de 5 cM y la distancia
entre A y C es de 8 cM, la distancia entre B y C puede ser de 3 cM o de 13 cM.
En el primer caso, el gen B se localiza en una posición intermedia, mientras
que en el segundo caso el gen intermedio es el A (figura 5.8.). Realizando una
serie de cruzamientos dihíbridos para distintos genes podremos ir dibujando
el mapa genético.

```
Figura 5.8 Propiedad aditiva de las distancias de mapa
```
Al construir un mapa genético debe tenerse en cuenta que la recombinación
máxima entre dos genes es del 50%, que es la que observamos entre genes
situados en cromosomas distintos. Genes localizados en un mismo cromoso-
ma separados por más de 50 cM no muestran más ligamiento que genes loca-
lizados en cromosomas distintos. Por otro lado, la recombinación que obser-
vamos entre dos genes distantes es, en realidad, una subestima. Cuanto más
alejados, más probable es que exista recombinación, pudiendo existir dobles
entrecruzamientos. El producto de un doble recombinante no difiere de la
combinación original, lo cual conduce a una subestima de la frecuencia de
recombinación.

```
Referencia bibliográfica
A.￿H.￿Sturtevant (1913).
"The linear arrangement of
six sex-linked factors in Dro-
sophila, as shown by their
mode of association". Journal
of Experimental Zoology (vol.
14, pág. 43-59).
```

Un modo más eficaz de reconstruir un mapa genético consiste en realizar un
cruzamiento prueba de tres puntos. Un único cruzamiento nos proporciona
toda la información para localizar espacialmente tres genes. Además, en un
cruzamiento de este tipo podemos identificar dobles recombinantes entre los
genes más distantes, que sin la información del gen central nos pasarían to-
talmente desapercibidos (figura 5.9.).

Este cruzamiento prueba consiste en utilizar como progenitores a un triple he-
terocigoto y un triple homocigoto recesivo. Aunque el homocigoto pueda ex-
perimentar entrecruzamiento en la meiosis, no apreciaremos recombinación,
puesto que los marcadores usados son idénticos en ambos cromosomas. Ade-
más, como siempre contribuye con un alelo recesivo, el fenotipo que observe-
mos en la descendencia nos indicará directamente el alelo heredado del otro
progenitor. Esto nos permite observar los diferentes tipos de recombinantes
y determinar su frecuencia. En estos cruzamientos podemos obtener ocho fe-
notipos distintos (correspondiendo a ocho genotipos). Los dos fenotipos más
frecuentes nos indican la combinación parental original. Los dos fenotipos
menos frecuentes nos indican los dobles recombinantes y nos proporcionan
la pista de qué gen se localiza en el centro, que será aquel para el cual haya
cambiado el alelo con respecto a los de los otros dos genes. Para calcular la
frecuencia de recombinación entre el gen central y uno de los marginales, se
deberá sumar las clases fenotípicas correspondientes a los recombinantes entre
estos dos genes. Para conocer la frecuencia de recombinación entre los genes
más externos, debemos sumar las frecuencias de recombinación entre el gen
central y cada uno de los marginales.


```
Figura 5.9. Combinaciones alélicas en los gametos de un triple heterocigoto. Entre tres loci ligados podemos observar tres tipos de
entrecruzamientos
```
### 2.3. Transposones

Hasta aquí se ha considerado que la ubicación de los genes en el cromosoma
es constante. Si bien existe recombinación, que permite el intercambio de ma-
terial entre cromosomas homólogos, la posición relativa de este material en
los cromosomas permanece inalterable. Sin embargo, existe un tipo de gen
saltarín que es capaz de cambiar de posición dentro del cromosoma o inclu-
so cambiar de cromosoma, y que a menudo lo hace de un modo replicativo,
expandiendo su número en el genoma. Estos genes son los transposones, ele-
mentos transponibles o TE (del inglés _transposable elements_ ).

Los transposones fueron descubiertos por Barbara McClintock en 1950 cuando
estudiaba la herencia de la coloración de los granos del maíz, _Zea mays_ , y la
composición génica de su cromosoma 9.

```
Referencia bibliográfica
B.￿McClintock (1950). "The
origin and behavior of muta-
ble loci in maize". Proc. Natl.
Acad. Sci. USA (vol. 36, pág.
344-355).
```

La mayoría de los granos tenían una pigmentación completa o eran amarillos.
Unos pocos eran variegados, granos amarillos con manchas irregulares de pig-
mentación. Se pensaba que este patrón respondía a una mutación inestable.
Una mutación en el gen salvaje producía los granos amarillos y la reversión
de la mutación en algunas células era la responsable de los granos jaspeados.

McClintock encontró una línea de maíz en la que el cromosoma 9 se rompía
con mucha frecuencia por el locus _Ds_ ( _Disociation_ ). Además, _Ds_ cambiaba fre-
cuentemente de posición en el cromosoma sin provocar ninguna alteración
visible en el cromosoma. Para que _Ds_ se moviera, era necesaria la presencia
de otro gen no ligado _Ac_ ( _Activator_ ), que también cambiaba frecuentemente
de posición. Vio que cuando _Ds_ cambiaba su posición cerca del locus _C_ (que
determina la pigmentación del grano) desaparecía la acción normal del gen _C_
apareciendo el fenotipo del alelo recesivo _c_ (granos amarillos). Cuando _Ds_ se
movía de nuevo, abandonando esta posición, el fenotipo del alelo _C_ quedaba
totalmente restaurado. Refiriéndose a este ejemplo, McClintck apuntó:

```
"Un caso de transposición de Ds ha sido de particular importancia porque ilustra cómo
pueden surgir nuevos loci mutables asociados con cambios en la expresión génica."
B. McClintock (1950). "The origin and behavior of mutable loci in maize". Proc. Natl.
Acad. Sci. USA (vol. 36, pág. 344-355).
```
Durante años, la comunidad científica pensó que la transposición se restrin-
gía al maíz y no se reconoció la importancia de los transposones hasta la dé-
cada de 1970-80, cuando se demostró su existencia en todos los organismos.
Actualmente sabemos que representan un porcentaje importante de muchos
genomas. Se calcula que el 50% del genoma humano lo constituyen secuen-
cias móviles.

Existen muchos tipos de TE, que se clasifican de diversos modos. Algunos cons-
tan sólo de las secuencias necesarias para su propia transposición, pero otros
codifican además para otros genes:

- Unos son **autónomos** , es decir, no necesitan de ningún otro gen para
    transponerse (por ejemplo, el elemento _Ac_ del maíz).
- Otros son **no￿autónomos** , es decir, necesitan de otros genes para movili-
    zarse (por ejemplo, el elemento _Ds_ del maíz, que precisa de _Ac_ ).

El mecanismo de transposición puede ser conservativo o replicativo:

- En el **conservativo** , el transposón se escinde del cromosoma y se integra
    en una nueva localización.
- En el **replicativo** , el transposón crea una copia que se integrará en un lugar
    nuevo, conservándose la inserción original.

```
B. McClintock
B. McClintock recibió el Pre-
mio Nobel en 1983 por su
descubrimiento de los transpo-
sones.
```

Una característica común a los TE es la presencia de repeticiones directas flan-
queantes de 3-12 pb. Estas secuencias no pertenecen al TE y no se mueven con
él, sino que se originan en el momento de insertarse en un lugar del genoma.
Corresponden a la secuencia original, donde se produce una rotura escalona-
da y posterior inserción del TE con reparación del ADN cortado (figura 5.10.).
Por ello, estas secuencias repetidas son muy variables, aunque su longitud es
constante para cada tipo de TE. Estas repeticiones directas se mantienen una
vez el transposón se escinde, quedando como huellas de su paso en esta po-
sición del genoma. Si estas huellas han sido dejadas dentro o en las proximi-
dades de un gen, pueden alterar la función de éste, incluso una vez que ha
desaparecido el TE.

```
Figura 5.10. Origen de las repeticiones directas que flanquean los TE en el
genoma
```
Los TE eucariotas se clasifican en dos grupos:

- **Retrotransposones** o TE de clase 1.
- **Transposones￿de￿ADN** o TE de clase 2.

Los **retrotransposones** utilizan un intermediario de ARN para movilizarse.
Una transcriptasa inversa pasa el ARN transcrito a ADN que se insertará en un
nuevo lugar. Contienen el gen de la transcriptasa inversa, y en ocasiones otros.
Una vez que el ARNm llega al citoplasma, se traduce la transcriptasa inversa,
que se encarga a continuación de obtener una copia del ARNm a ADN de ca-
dena doble. Este ADN volverá al núcleo donde podrá insertarse en un nuevo
lugar del genoma. Los retrotransposones pueden ser de dos tipos:


- Los que presentan repeticiones terminales largas, o **LTR** (del inglés _long_
    _terminal repeats_ ).
- Los que no las presentan, o **non-LTR**.

Los elementos LINE1 o L1 y Alu son retrotransposones non-LTR presentes en
gran cantidad en el genoma humano. Las secuencias Alu, de unos 300 pb,
están representadas por cerca de un millón de copias en el genoma humano.
Las secuencias L1, de unas 6 kb de longitud, representan aproximadamente el
15% del genoma humano.

Los **transposones￿de￿ADN** autónomos codifican para una transposasa y en
ocasiones para otros genes. La transposasa es necesaria para la escisión y la
inserción del transposón. Los transposones de ADN poseen repeticiones ter-
minales invertidas cortas de 9-40 pb, que son secuencias invertidas y comple-
mentarias la una de la otra. Estas secuencias son reconocidas por la transposa-
sa. Algunos transposones de ADN son el sistema _Ds/Ac_ del maíz y los **elemen-
tos￿** **_P_** de _Drosophila_. Los elementos _P_ parecen estar presentes en todas las po-
blaciones naturales de _D. melanogaster_ , pero su expansión ha debido de tener
lugar en los últimos 50 años, puesto que están ausentes en todas las líneas de
laboratorio originadas a partir de capturas realizadas antes de 1945.

La movilización de los TE puede conllevar la aparición de mutaciones, tal co-
mo hemos visto en el complejo _Ds/Ac_ del maíz. En ocasiones, estas mutaciones
son mucho más graves, como la inserción del retrotransposón L1 dentro del
gen que codifica para el factor de coagulación VIII que provoca la hemofilia,
como explican Kazazian y otros. Así pues, un genoma con un alto porcentaje
de transposones debería ser altamente inestable y sujeto a multitud de muta-
ciones deletéreas. Para evitarlo, la mayoría de los transposones se encuentran
silenciados, permaneciendo inactivos por la acción de diversos mecanismos
como la metilación del ADN, el remodelado de la cromatina o la intervención
de miRNA. Algunos TE pueden codificar siRNA que controlan su propio silen-
ciamiento. Es el caso del siRNA que interfiere con L1, que proviene de la se-
cuencia 5'UTR de L1.

La capacidad de los transposones de transportar con ellos otros genes ha si-
do explotada como herramienta para obtener **organismos￿transgénicos**. En
_Drosophila_ , Spradling y Rubin mostraron que es posible obtener individuos
transgénicos utilizando los elementos _P_. Para ello utilizaron embriones de un
estadio temprano, cuando tan sólo es una célula plurinucleada, en la que los
núcleos que originarán la línea germinal se agrupan en uno de los polos. A
estos embriones se les inyecta una mezcla de dos plásmidos. Un plásmido por-
ta un elemento _P_ defectivo (sin transposasa) donde se ha insertado el gen de
interés. El otro plásmido, el _helper_ ( _ayudante_ , en inglés), contiene el gen de
la transposasa pero carece de las repeticiones invertidas necesarias para inser-
tarse, con lo que se pierde en las siguientes divisiones celulares. El elemento
_P_ puede insertarse en cualquier parte del genoma de los núcleos de la línea
germinal gracias a la transposasa expresada por el _helper_. El individuo adulto

```
Referencia bibliográfica
H.￿H.￿Kazazian;￿C.￿Wong;
H.￿Youssoufian;￿A.￿F.￿Scout;
D.￿G.￿Phillips;￿S.￿E.￿Antona-
rakis (1988). "Haemophilia
A resulting from de novo in-
sertion of L1 sequences re-
presents a novel mechanism
for mutation in man". Nature
(vol. 332, pág. 164-166).
```
```
Ved también
Los siRNA y miRNA y su mo-
do de acción se explican en
el apartado "Interferencia del
ARN" del módulo "Síntesis pro-
teica" de esta asignatura.
```
```
Referencia bibliográfica
A.￿C.￿Spradling;￿G.￿M.￿Ru-
bin (1982). "Transposition of
cloned P elements into Dro-
sophila germ line chromoso-
mes". Science (vol. 218, pág.
341-347).
```

que se obtiene es normal, pero en su descendencia aparecen individuos trans-
génicos, portadores del gen introducido con el elemento _P_. Cada individuo
transgénico muestra el gen insertado en un lugar distinto y éste se hereda de
modo estable y mendeliano.


## 3. Herramientas estadísticas básicas en el estudio genético

Cada patrón de herencia conlleva la observación de proporciones fenotípicas
distintas. Cuando se aborda el estudio de un carácter, se contrastan las pro-
porciones observadas en la descendencia con las esperadas según el modelo
mendeliano (que es el más sencillo). En caso de no ajustarse al modelo, se
plantea una hipótesis nueva, se calculan las proporciones esperadas bajo esta
hipótesis y se contrasta de nuevo. Para este análisis se emplean una serie de
herramientas estadísticas básicas.

En general, utilizamos la estadística en dos momentos:

- Cálculo de las proporciones esperadas.
- Contraste de hipótesis.

### 3.1. Cálculo de las proporciones esperadas

Las proporciones esperadas se calculan aplicando los principios básicos de pro-
babilidad:

- La probabilidad de dos sucesos independientes es el producto de las pro-
    babilidades de estos sucesos.
- La probabilidad de un suceso unión de sucesos excluyentes es la suma de
    las probabilidades de los sucesos individuales.

Así, si consideramos que en un experimento de dihibridismo, los alelos de
cromosomas homólogos tienen la misma probabilidad de formar parte de ga-
metos viables y que todos los gametos tienen la misma probabilidad de inter-
venir en la formación de cigotos viables, podemos calcular las siguientes pro-
babilidades:

```
Un gameto AB en la F 1 P (AB) = P (A) × P (B) = 1/2 × 1/2 = 1/4
```
```
Un cigoto AABB en la F 2 P (AABB) = P (AB) × P (AB) = 1/4 × 1/4 = 1/16
Un individuo A_bb en la F 2 P (A_bb) = P (AAbb) + P (Aabb) + P (aAbb) = 1/16 + 1/16 +
1/16 = 3/16
```
En ocasiones, el cálculo de las proporciones esperadas se complica bastante.
Por ejemplo, al considerar un mayor número de caracteres simultáneamente,
o cuando los distintos gametos no se originan con la misma probabilidad. En
estos casos puede resultar de gran ayuda el uso del **cuadrado￿de￿Punnett**. Para
construirlo, dibujamos una cuadrícula en cuyo borde superior colocamos los

```
Ved también
Podéis ver la figura 5.3. en el
apartado 1 de este módulo.
```

gametos producidos por un progenitor y en el borde izquierdo los gametos
producidos por el otro progenitor. En cada casilla escribiremos la combinación
genotípica resultante de combinar los gametos correspondientes a las entradas
superior e izquierda (figura 5.3.). La probabilidad de obtener un individuo
correspondiente a una casilla determinada es el producto de las probabilidades
de los gametos que lo originan.

### 3.2. Contraste de hipótesis

Las frecuencias que observamos siempre dependen de un muestreo y, en con-
secuencia, están sujetas a un error. Por ello, las frecuencias observadas rara-
mente coinciden exactamente con las esperadas. Para decidir si las desviacio-
nes que observamos pueden ser debidas al muestreo o, por el contrario, son
excesivas y debe buscarse otra explicación plausible, utilizamos la **prueba￿de**

**bondad￿de￿ajuste￿de￿la￿chi-cuadrado￿(χ**^2 **)**.

La fórmula de la χ^2 es:

#### 5.1

```
Los valores que comparamos en una χ^2 siempre han de ser valores ab-
solutos, nunca frecuencias relativas o porcentajes.
```
```
Prueba de bondad de ajuste de la χ^2
Veamos cómo lo aplicaríamos en un ejemplo concreto:
En la tabla 5.1. hemos visto que, tras cruzar guisantes de semillas lisas con guisantes de
semillas rugosas, Mendel obtuvo una F 2 de 7.324 semillas: 5.474 lisas + 1.850 rugosas
(proporción 2.96:1). Según la primera ley de Mendel esperamos una proporción 3:1, es
decir: 5.493 lisas y 1.831 rugosas. Para decidir si las diferencias observadas pueden ser
debidas al azar, aplicamos el test de χ^2 :
χ^2 = (5.474 – 5.493)^2 / 5.493 + (1.850 – 1.831)^2 / 1.831 = 0,0657 + 0,1972 = 0,2628
Para conocer si este valor de χ^2 indica un valor que se ajusta a nuestro modelo, recurrimos
a las tablas de χ^2. En estas tablas encontramos los valores de χ^2 , que marcan los valores
límite de esta distribución para una probabilidad y número de grados de libertad deter-
minados. Siempre que el valor obtenido en el test de χ^2 sea inferior al tabulado, acepta-
remos la hipótesis testada como buena. Un valor de χ^2 superior al tabulado nos llevará
a rechazar la hipótesis.
Los grados de libertad (gl) nos indican el número de modos en que pueden variar libre-
mente las clases observadas. El número de grados de libertad en una prueba de bondad
de ajuste de la χ^2 es uno menos que las clases observadas. En nuestro ejemplo tenemos
dos clases (lisas y rugosas), por lo que, partiendo de un número total de semillas, una vez
sabemos el número de semillas lisas, el número de rugosas ya queda fijado. En general
utilizamos un nivel de significación ε = 0,05. En la tabla de χ^2 , el valor tabulado para
1 gl y ε = 0,05 es de 3,84. Dado que el valor obtenido en la prueba de χ^2 es inferior al
tabulado, aceptamos que nuestra observación se ajusta a los valores esperados según la
hipótesis formulada. Las desviaciones obtenidas entre los valores observados y esperados
pueden explicarse por azar en el muestreo.
```

Debe tenerse en cuenta que, cuando decimos que la descendencia se
ajusta a ciertas frecuencias, se refiere al promedio poblacional, no a un
cruce concreto entre dos individuos. Las frecuencias esperadas siguen
las leyes de la probabilidad y, por tanto, debe considerarse un número
elevado de individuos para no observar desviaciones totalmente aleato-
rias. En organismos con una descendencia considerable, como algunas
plantas o incluso en _Drosophila_ , podríamos contrastar las frecuencias
observadas en un cruce concreto de dos individuos con las frecuencias
esperadas. Sin embargo, no podemos contrastarlas en la descendencia
de una familia humana concreta que, por numerosa que sea, siempre
contará con un número muy limitado de individuos.


## 4. Estudio de pedigríes

La genética humana tiene un gran interés debido a que puede explicar la apa-
rición de multitud de enfermedades. Sin embargo, el estudio de la genética
humana se ve limitado por una serie de circunstancias. Por un lado, el investi-
gador no puede recurrir a cruzamientos controlados que le permitan compro-
bar sus hipótesis. Por otro lado, de cada cruzamiento sólo se obtienen unos
pocos descendientes que no permiten reconocer sin ambigüedad los patrones
de herencia más simples.

Para solventar estas dificultades, los genetistas recurren habitualmente al aná-
lisis de pedigríes. Un **pedigrí** es una representación gráfica de la historia fa-
miliar para un carácter hereditario determinado, expresado en forma de árbol
genealógico (figura 5.11.). En general, la reconstrucción de un pedigrí empie-
za con un individuo que presenta la característica que se desea estudiar, gene-
ralmente una enfermedad, y se le va añadiendo la información de todos los
familiares conocidos.

```
Figura 5.11. Árbol genealógico (parcial) de las casas reales europeas donde se muestra la herencia de la hemofilia
```
En un pedigrí, cada generación se indica con números romanos y cada indi-
viduo dentro de una generación determinada se suele distinguir con números
arábigos. Los hombres se representan por cuadrados y las mujeres por círcu-


los. Los individuos afectados por la característica se indican mediante símbo-
los rellenos (cuadrados o círculos), mientras que los que no la presentan, por
símbolos vacíos. Las líneas que unen los distintos símbolos indican las rela-
ciones entre los individuos: apareamiento (línea horizontal directa) o ascen-
dencia/descendencia (línea vertical).

El estudio de un pedigrí permite averiguar si un carácter determinado es do-
minante o recesivo y si su herencia es autosómica o ligada al sexo. A estas
conclusiones no se llega contrastando frecuencias en la descendencia, sino re-
conociendo patrones asociados con los distintos tipos de herencia. Por ejem-
plo, si un individuo afectado desciende de un padre y una madre no afecta-
dos, la característica debe ser necesariamente recesiva (o, más raramente, ha-
ber aparecido como mutación dominante en uno de los gametos que originó
este individuo).

Para decidir qué tipo de herencia causa el patrón de fenotipos que observamos
en un pedigrí determinado, debemos partir de una hipótesis y rastrear todo
el pedigrí. Según esta hipótesis, asignamos un posible genotipo para cada in-
dividuo y nos cercioramos de que no existe ningún caso incompatible con
ella. Para ello, debemos tener en cuenta que el genotipo de los individuos que
presentan el fenotipo dominante en ocasiones puede ser diverso (homocigo-
to o heterocigoto). Sólo podemos asegurar que el individuo es heterocigoto
cuando desciende de un padre de fenotipo recesivo o tiene un hijo de fenoti-
po recesivo. Por ello, al comprobar nuestra hipótesis debemos asegurarnos de
considerar todos los genotipos posibles para cada individuo. En la genealogía
de la figura 5.11. se muestra la transmisión de la hemofilia, un carácter rece-
sivo ligado al cromosoma X. En el esquema se han marcado como portadoras

( _XAXa_ ) a las mujeres que tuvieron algún hijo hemofílico. Nótese, sin embargo,
que una mujer sana pero heterocigota para la hemofilia puede, por azar, no
pasar el alelo defectuoso a su progenie masculina. Por ello, no podemos con-
firmar el genotipo del resto de mujeres sanas.

Los pedigríes también se utilizan en consejo genético y en medicina forense.
Una pareja con antecedentes familiares para alguna enfermedad hereditaria
puede recurrir a un genetista en busca de consejo genético. El especialista es-
tudia el pedigrí y, conociendo el tipo de herencia del carácter, establece la pro-
babilidad de que un hijo de la pareja pueda padecer la enfermedad. En me-
dicina forense ha sido habitual usar la herencia del grupo sanguíneo AB0 en
pruebas de paternidad, conociendo el grupo sanguíneo de la madre, el del hijo
y el del presunto padre (o padres). Debe destacarse que estas pruebas permiten
descartar un posible padre, pero nunca identificarlo al 100%. En la actualidad
se utiliza una combinación de marcadores moleculares, tipo **microsatélites** o
**SNP** , que permiten una mayor definición del origen genético de un individuo.

```
Ved también
Veremos los marcadores mole-
culares tipo SNP y los microsa-
télites en el capítulo "Marcado-
res genéticos moleculares".
```

## 5. Otros tipos de herencia

Existen otros tipos de herencia biológica menos generales o más complejos,
como la herencia ligada al cromosoma Y, la herencia citoplasmática, la inter-
acción génica, la herencia cuantitativa... Veamos algunos:

- La **herencia￿holándrica** es la que presentan los poquísimos genes ligados
    al cromosoma Y. Estos genes se heredan por línea paterna, sin saltos gene-
    racionales, y son exclusivos de los machos.
- La **herencia￿citoplasmática** hace referencia a todos aquellos genes locali-
    zados en los orgánulos citoplasmáticos (mitocondrias y cloroplastos). En
    principio, estos orgánulos son aportados al cigoto exclusivamente por el
    óvulo. Por tanto, la herencia de estos genes es por línea materna, pero en
    este caso son compartidos por machos y hembras.
- Otro fenómeno que altera las proporciones con respecto a la herencia men-
    deliana es la **impronta￿genética**. Como ya hemos visto, algunos genes
    quedan marcados diferencialmente durante la gametogénesis en machos
    y hembras. Esto lleva a que en la siguiente generación sólo se exprese el
    alelo heredado por uno de los dos sexos.
- La **interacción￿génica** tiene lugar cuando dos o más genes actúan conjun-
    tamente en la expresión de un carácter: el efecto de los alelos del primer
    locus depende de qué combinación alélica presente el segundo locus.
- La **herencia￿cuantitativa** se observa en fenotipos de variación continua,
    muchas veces asociados a caracteres de interés en explotaciones agrope-
    cuarias (tamaño corporal, número de crías por camada, producción de le-
    che, longevidad...). Estos caracteres están modelados por numerosos ge-
    nes y una importante influencia ambiental, y dan origen a una variación
    continua en la población. Aunque la herencia de cada locus individual
    implicado en un carácter de variación continua sigue las leyes de Mendel,
    resulta difícil discernir la aportación de cada locus al fenotipo y para el
    estudio de caracteres cuantitativos debe recurrirse al uso de herramientas
    estadísticas especiales.


## 6. Evolución del concepto de gen

Al principio del módulo apuntamos que la definición de _gen_ puede ser diversa
y más o menos compleja. Por ello, ofrecimos una definición sencilla que nos
ha sido útil hasta aquí: "un gen es cualquier factor que determina una carac-
terística particular y heredable de un organismo". Esta definición, un tanto
abstracta, continúa siendo válida hoy en día. Sin embargo, cuando queremos
especificar qué es un gen con una visión más material, la cosa se complica, de
manera que la definición de _gen_ ha sufrido una profunda evolución a medida
que se conocía mejor la base molecular de la herencia.

Aunque el estudio sistemático de la genética y de los genes se remonta a me-
diados del siglo XIX con los trabajos de Mendel, la palabra _genética_ no fue uti-
lizada hasta 1905 por Bateson, quien también fue el primero en traducir al
inglés los trabajos de Mendel en 1901. Por su parte, el vocablo _gen_ fue utilizado
por primera vez en 1909 por Johannsen, quien lo definía como "las condicio-
nes especiales presentes en los gametos de forma única e independiente y que
especifican muchas características de los organismos".

Con la teoría cromosómica de la herencia, el gen pasa a ocupar una posición
física sobre el cromosoma. Por ello, Morgan y sus colaboradores explican las
observaciones de ligamiento y recombinación por un modelo de "genes orde-
nados linealmente" como las cuentas de un collar.

Cuando se observó el efecto de algunas mutaciones sobre las vías metabólicas
se formuló el principio de "un gen, una enzima", que posteriormente se gene-
ralizó a "un gen, una cadena polipéptidica". Más tarde llegó el conocimiento
del ADN como material genético, el descubrimiento de su estructura peculiar
que asegura su fiel replicación, y el descifrado del código genético. La idea
de gen se identifica con la de ORF, "una secuencia de ADN que codifica para
proteína".

Pero algunos ARN tienen función propia sin traducirse a proteína y, además,
con la secuenciación de los primeros genes se descubrieron los intrones y el
procesamiento del ARN. La idea de gen como ORF excluye a los genes de ARN
y a los intrones. Esto llevó a la definición de _gen_ como "un fragmento de ADN
que se transcribe". De nuevo, el descubrimiento del ayuste alternativo supuso
un reto para la definición de _gen_. Un gen es "una secuencia de ADN que puede
codificar para transcritos alternativos aunque éstos produzcan proteínas dis-
tintas".


Una definición más actual es la de Griffiths y otros, que afirma que "un gen
es una porción de ADN compuesta de una región que se transcribe y de una
región reguladora que hace posible la transcripción".

El proyecto ENCODE ha puesto de manifiesto la gran complejidad que pueden
alcanzar las secuencias codificadoras y reguladoras:

- Muchos intensificadores (regiones reguladoras) se localizan muy alejados
    de la secuencia que se transcribe. Además, un intensificador puede ser
    compartido por diversas unidades de transcripción.
- Existen numerosos genes que se solapan, bien sea compartiendo la misma
    cadena de ADN con otra pauta de lectura, bien utilizando la cadena com-
    plementaria. Es el caso del gen _Adh_ de _D. melanogaster_ , que está incluido en
    un intrón enorme del gen _osp_ y además utiliza la cadena complementaria.
- Existencia de _trans-splicing_ , que es la unión en un ARNm de exones loca-
    lizados en distintos pre-ARNm, y que entra en conflicto con la vieja idea
    de "un gen, un locus".

```
Referencia bibliográfica
A.￿J.￿F.￿Griffiths;￿S.￿R.￿Wess-
ler;￿R.￿C.￿Lewontin;￿S.￿B.
Carroll (2008). Genética (9.ª
ed.). Madrid: McGraw-Hill/
Interamericana de España,
S.A.U.
```
- La gran cantidad de elementos móviles, que también nos enseñan que la
    idea de una localización fija para cada gen no es válida.

Por todo ello, Gerstein y otros han propuesto una nueva definición de _gen_.

```
El gen es una combinación de secuencias genómicas que codifican un
conjunto coherente de productos funcionales potencialmente solapa-
dos.
```
Según esta definición, lo que determina un gen son las secuencias de los pro-
ductos funcionales, no las secuencias transcritas (figura 5.12.). Por ello, los
distintos productos funcionales del mismo tipo (proteína o ARN) que están
codificadas en secuencias de ADN solapadas, se agrupan en un mismo gen. Por
el contrario, aquellos productos funcionales que no comparten secuencias del
ADN aunque procedan de transcritos que comparten el promotor y el inicio
de transcripción, se consideran genes independientes. Así, aunque son impor-
tantes, las regiones reguladoras y las secuencias UTR no se consideran en esta
definición de gen propuesta.

```
Ved también
El Proyecto ENCODE ( ENCy-
clopedia Of DNA Elements ) pre-
tende identificar todos los ele-
mentos funcionales en la se-
cuencia del genoma humano.
Lo vemos en profundidad en
el apartado 5 del módulo "... y
de genomas, genómica" de es-
ta asignatura.
```
```
Referencia bibliográfica
M.￿B.￿Gerstein;￿C.￿Bruce;￿J.
S.￿Rozowsky;￿D.￿Zheng;￿J.
Du;￿J.￿O.￿Korbel;￿O.￿Ema-
nuelsson;￿Z.￿D.￿Zhang;
S.￿Weissman;￿M.￿Zinder
(2007). "What is a gene, post-
ENCODE? History and upda-
ted definition". Genome Re-
search (vol.17, pág. 669-681).
```

Figura 5.12. Ejemplo de una región de ADN con cinco genes según la definición post-ENCODE

Las cajas con letras indican los exones. Las cajas rayadas indican las regiones UTR en los genes de proteína. Los genes I y II comparten la región 5'UTRpero ningún exón. El gen III está formado por un grupo de tres exones (C, D y E) con corte y empalme alternativo, en el que cada exón es compartido
por distintas proteínas. El gen IV, a pesar de estar solapado al gen III, no comparte ningún exón (están en cadenas complementarias). El gen V tiene elexón X, que se solapa con el exón A del gen I, y el exón Y, que se solapa con el exón E del gen III. No obstante, como es un gen de ARN, mientras que los
genes I y III son de proteína, representa un gen distinto.


