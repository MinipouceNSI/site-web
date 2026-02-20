1. mkdir ./tpLinux

2. tree

3. cd ./tpLinux 
   pwd (pour vérifier où on se trouve)
   touch fic1.txt fic2.txt fichier.md image.jpg exos.md exoos.txt

4. mkdir dosA/ dosA/dosB/ dosA/dosC/ dosD/
   tree (pour vérifier)

5. mv ./fi* ./dosA/dosB
   tree (pour vérifier)

6. cp fic1.txt ../
   cp fic2.txt ../dosC
   cp fichier.md ../../dosD

7. cd ../../
   pwd (pour vérifier)
   echo >> ./dosA/fic1.txt "bonjour tout le monde"
   cat ./dosA/fic1.txt (pour vérifier)
   ls -l ./dosA/fic1.txt pour vérifier la taille du fichier (23 dans mon cas)

8. find ./-name *.???


9. mv ./exoos.txt ./exos.txt

10. cd ../
touch supprimer.sh
echo ./supprimer.sh >> rm -r ./tpLinux
tree
chmod 777
