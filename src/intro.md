Qu'est-ce que la cryptographie ?
================================

### Pour vivre heureux vivons cachés

La clef
-------

A quoi bon verrouiller une information sans garder la clef ?<br/>
Cryptage/Decryptage.<br/>
Chiffrer/Dechiffrer.

Avec la meme clef ?<br/>
C'est symetrique.<br/>
_Chiffrement symetrique et symetrique dechiffrement_

Sans donner la clef ?<br/>
C'est asymetrique !<br/>
_Chiffrement asymetrique. Pour le dechiffrement, c'est une autre histoire_

## Rencontre avec le hasard
Le hasard pur en binaire, c'est soit un zero soit un un. <br/>
0 ou 1. a 50/50.<br/>
Ensuite c'est soit 11 soit 10, soit 01 soit 00.
Une chance sur 4.<br/>
Puis 111, 110, 101, 100, ...
Une chance sur 8. _Et cetera_

## L'ordre et le hasard ont un fils : C'est toujours le hasard
C'est la forme la plus pure de la cryptographie. Mathematiquement inviolable. Rend le message indistinguable du hasard.<br/>
Un nombre au hasard 0101110<br/>
Un message a cacher 0011100<br/>
Leurs differences : 0110010 (⊕, xor, [OU exlusif](https://fr.wikipedia.org/wiki/Fonction_OU_exclusif))

## La difference de la difference, c'est la meme.
Prenons notre nombre au hasard 0101110 et notre difference 0110010, et ⊕.<br/>
0101110 ⊕ 0110010 = 0011100<br/>
Notre message de base.<br/>
On peut passer du message au hasard. Puis du hasard au message.<br/>
Chiffrement symetrique : Le chiffrement et le dechiffrement utilisent la meme clef<br/>
_Stream cipher_. [Chiffrement de flux. Chiffrement par flot. Chiffrement en continu.](https://fr.wikipedia.org/wiki/Chiffrement_de_flux)

## Hasard partout
Pour que cette technique de base marche il faut une clef choisie au hasard, et de la meme taille que le message !<br/>
Il faut toujours plus de hasard. Technique du [masque jetable](https://fr.wikipedia.org/wiki/Masque_jetable)<br/>
Si ca se repete trop, c'est du chiffrement de [Cesar] ou [Vigenere], et c'est facile a casser sans la clef.

## Techni-cite
Y'a des constructions plus techniques avec des clef pas trop longue. C'est plus technique mais plus pratique.<br/>
[Stream ciphers](https://fr.wikipedia.org/wiki/Chiffrement_de_flux) ou [Block ciphers](https://en.wikipedia.org/wiki/Block_cipher)<br/>
Un bon [Mode_d'operation](https://fr.wikipedia.org/wiki/Mode_d%27op%C3%A9ration_(cryptographie)), [NaCl crypto_secretbox](https://nacl.cr.yp.to/secretbox.html) par exemple :)
