
===========================Este es el juego de Cartas 3 y 2==========================

Consta de dos jugadores a los cuales se le reparten 5 cartas(a cada jugador). Un jugador ganará un punto cuando logre tener a mano 3 cartas con el mismo valor numérico y 2 cartas con otro valor numerico(mismos). Ejemplo: tres cartas con el #6 y dos cartas con el #11. El juego terminará hasta que no queden mas cartas en el mazo, y ganará el jugador con mayor puntos acumulados.

Al momento de ejecutar el juego lo primero que se presentara seran las reglas y condiciones para la victoria. Luego se mostrara el titulo del juego y se procedera a ingresar los nombres de los jugadores. A continuacion se iniciara la partida con el turno del primer jugador. Se mostrara el nombre del jugador y las cartas de este, debajo se presentan el mazo de cartas con la cantidad de cartas restantes, la pila de cartas donde se iran tirando las cartas que los jugadores desechen. Mas a bajo se presentara un menu de opciones para los jugadores, del cual se debera escoger una estas escribiendo el numero de la opcion(1 o 2), luego se presentaran unas preguntas a las que se debera responder escribiendo la letra S, la letra N o el numero de una de las cartas que posee el jugador de turno dependiendo de la pregunta mostrada. Se mostrara un mensaje en caso de que uno de los jugadores logre una combinacion de 3 cartas del mismo valor numerico y dos de otra(se le otorgara un punto).

Lo descrito anteriormente se repetira hasta que ya no queden cartas suficientes para repartir, al final se mostrara un mensaje con el nombre del jugador que ha ganado que sera el que halla acumulado mayor cantidad de puntos.

La version de Python utilizada en el desarrollo de este juego es la 3.7

Se requieren las librerias **time**, **os** y **random**.

-De libreria time utilizo la funcion **sleep** para colocar un intervalo de tiempo entre la ejecucion de dos instrucciones.

-En el caso de la libreria os, es usada para poder limpiar la pantalla en consola(con **system('cls')**).  

-De la libreria random hago uso de la funcion **sample** para organizar las cartas del Deck de manera aleatoria.  