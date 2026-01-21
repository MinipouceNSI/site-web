### Le langage HTML

1. HTML

HyperText Markup *Langage de balises hypertexte*

un fichier `.html` est un fichier de texte (comme le markdown par exemple). On ouvre un fichier de 2 façons:
-le développeur => avec un éditeur de code (ex: VisualStudioCode)
- l'utilisateur => avec un navigateur (ex: firefox)

le plus souvent les balises html sont en couple (ouvrante/fermante) mais il existe aussi des balises *orpheline*:
- `<MaBalise></MaBalise>`
- `<Mabalise>`

la structure minimale d'une page web est:

```html
<!DOCTYPE html>
<html>
<head></head>
<body></body>
</html>
```

Le site de référence pour les langages du WEB des développeurs de Mozilla.
[https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements)

Quelques balises à connaître:
- <body></body> 
- <head></head> contient ce qui n'est pas visible sur la page
- `<hl></hl>`permet de faire de titres sur la page
- `<p></p>`permet de faire un paragraphe
- `<a href=""></a>` permet d'accrocher ;e curseur pour cliquer vers un lien
- `<img src="">` pour insérer une image
- `<br>` pour casser la ligne
- `<ul></ul>` pour réakser une liste sans ordre
- `<ol></ul>` pour réaliser une liste ordonnée
- `<li></li>` pour insérer des items dans une liste


les balises ouvrantes peuvent contenir des attributs définis sur le site de référence ou l'attribut `clas=""`:<br>
`<maBalise attribut=""></maBalise>`

----------------
Pour donner le chemin relatif vers un fichier, on utilise:
- `,/` pour chercher dans le dossier courant
- `,./` pour chercher dans le dossier du dessus


2. Le CSS
Cascading Style Sheet *feuille de style en cascade*
[https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties)

Pour définir du style, il faut un sélecteur (element HTML ou class), des accolades, une propriété, une valeur.

```css
selecteur{
    propriete:valeur;
}

```

On peut écrire le CSS:
-dans le fichier html entre les balises `<style></style>`
-dans un fichier dédié avec l'extension `.css` ; il faut ajouter une balise orpheline `<link rel="stylesheet" href="">`

Il existe plus de 500 propriétés et encore davantage de valeurs possible, mais souvent, les valeurs sont :
- des couleurs (un nom, un code comme rgb)
- des tailles : plusieurs unités sont possibles
    - `px` pour pixels
    - `em` relatif a la taille de la police
    - `%` relatif a la taille du contenant

Remarque : Quand le sélecteur css est un élément HTML (par exemple `p`) alors les propriétés s'appliquent à tous les éléments du même type.
Pour différencier des éléments de même nature, on peut utiliser l'attribut `class` ou `id`.
Dans ce cas, le sélecteur est le nom de la classe précédé d'un `.` ou le nom de l'identifiant précédé d'un `#`.