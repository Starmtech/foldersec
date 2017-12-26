#!/usr/bin/python
# -*- coding: utf-8 -*
###################################
#         FolderSec               #
#      langage : Python 2.7       # 
#         date : 18/08/16         #
#          version : 1.0          #
#        auteur : devkort         #
###################################

import hashlib
import os.path
import sys
import time

#fonction checksum
def md5(fnom):
   try:
      hash_md5 = hashlib.md5()
      with open(fnom, 'rw') as f:
         for size in iter(lambda: f.read(4096), b""):
            hash_md5.update(size)
            md5 = hash_md5.hexdigest()
   except :
      pass
   return hash_md5.hexdigest()

#fonction écriture dans le fichier
def fich(cfi):
   dest1 = "/home/devkort/Bureau/test.txt"
   path1 = "/home"
   for dossier, sous_dossiers, fichiers in os.walk(path1):
      for fichier in fichiers:
         print(os.path.join(dossier, fichier))
         test = os.path.join(dossier, fichier)
         num = md5(test)
         if test > 0:
            fichier = open(cfi, "aw")
            fichier.write(test)
            fichier.write(" " )
            fichier.write(num)
            fichier.write('\n')
            fichier.close()


def update(dest):
   os.remove(dest)
   fich(dest)
   print("\n")
   print("****************************************")
   print("* Ancienne base de donnée mise a jours *")
   print("****************************************")
   print("\n")

def check(dest, dest1):
   os.remove(dest1)
   print("\n")
   print("*******************")
   print("* test du fichier *")
   print("*******************")
   print("\n")
   fich(dest1)
   fichier1 = md5(dest)
   fichier2 = md5(dest1)

   if fichier1 != fichier2:
      print("\n")
      print("*********************")
      print("* fichier different *")
      print("*********************")
      print("\n")
   else:
      print("\n")
      print("*********************")
      print("* fichier identique *")
      print("*********************")
      print("\n")


def first(dest):
   fich(dest)
   print("\n")
   print("******************************************")
   print("* fichier exectute pour la premiere fois *")
   print("******************************************")
   print("\n")

def help():
   print("\n")
   print("                    Aide pour l'utilisation du script:")
   print(" foldersec.py --check    permet verifier que le dossier n'a pas était modifié")
   print(" foldersec.py --update   permet de mettre a jours le fichier , a utiliser en cas de changement dans le dossier")
   print(" foldersec.py --help     permet de connaitre les commandes du script et obtenir de l'aide")
   print("\n")



#identification des parametres et execution de la fonction adéquate
arg = "/home/devkort/Bureau/test.txt"
arg1 = "/home/devkort/Bureau/test1.txt"
debut = time.time()
try:
   if len(sys.argv[1])>1:
      if sys.argv[1] == "--update":
         update(arg)
      elif sys.argv[1] == "--check":
         check(arg, arg1)
      elif sys.argv[1] == "--help":
         help()
      else:
        print("Mauvaise commande taper --help pour plus d'information")
except:
   first(arg)
fin = time.time() - debut
print "temps:",fin
