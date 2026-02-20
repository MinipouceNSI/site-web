1. mkdir ./tpLinux <br>

2. tree <br>

3. cd ./tpLinux <br>
   pwd (pour vérifier où on se trouve) <br>
   touch fic1.txt fic2.txt fichier.md image.jpg exos.md exoos.txt <br>

4. mkdir dosA/ dosA/dosB/ dosA/dosC/ dosD/ <br>
   tree (pour vérifier) <br>

5. mv ./fi* ./dosA/dosB <br>
   tree (pour vérifier) <br>

6. cp fic1.txt ../<br>
   cp fic2.txt ../dosC <br>
   cp fichier.md ../../dosD <br>

7. cd ../../ <br>
   pwd (pour vérifier) <br>
   echo >> ./dosA/fic1.txt "bonjour tout le monde" <br>
   cat ./dosA/fic1.txt (pour vérifier) <br>
   ls -l ./dosA/fic1.txt pour vérifier la taille du fichier (23 dans mon cas) <br>

8. find ./-name *.??? <br>


9. mv ./exoos.txt ./exos.txt<br>

10. cd ../ <br>
touch supprimer.sh <br>
echo ./supprimer.sh >> rm -r ./tpLinux <br>
tree <br>
chmod 777<br>
