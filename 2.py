__author__ = 'ujarc'

opened_file = open("CSI.txt", "r")

besedilo = opened_file.read()


rjavi_lasje = "GCCAGTGCCG"
if rjavi_lasje in besedilo:
    print "Rjavi"


kvadraten = "GCCACGG"
if kvadraten in besedilo:
    print "kvadraten"

okrogel = "ACCACAA"
if okrogel in besedilo:
    print "okrogel"

ovalen = "AGGCCTCA"
if ovalen in besedilo:
    print "ovalen"

modra_barva = "TTGTGGTGGC"
if modra_barva in besedilo:
    print "Modra"

zelena = "GGGAGGTGGC"
if zelena in besedilo:
    print "Zelena"

rjava = "AAGTAGTGAC"
if rjava in besedilo:
    print "rjava"

moski = "TGCAGGAACTTC"
if moski in besedilo:
    print "moski"

zenska = "TGAAGGACCTTC"
if zenska in besedilo:
    print "zenska"

belec = "AAAACCTCA"
if belec in besedilo:
    print "belec"

crnec = "CGACTACAG"
if crnec in besedilo:
    print "crnec"

Azijec = "CGCGGGCCG"
if Azijec in besedilo:
    print "Azijec"

