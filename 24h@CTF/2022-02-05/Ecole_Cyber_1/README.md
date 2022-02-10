# 24h@CTF [Desjardins] École Cyber 1 Writeup

## Category

Cryptography

## Description

The challenge provides a [text file](challenge1.txt) with the following content

```
[8mL[28m'É[8mc[28mol[8me[28mcy[8mb[28mer[8m [28mes[8mt[28m u[8mn[28m o[8mr[28mga[8mn[28mis[8mm[28me [8mà[28m b[8mu[28mt [8mn[28mon[8m [28mlu[8mc[28mra[8mt[28mif[8m [28mdo[8mn[28mt [8ml[28ma [8mm[28mis[8ms[28mio[8mn[28m e[8ms[28mt [8md[28me [8md[28mév[8me[28mlo[8mp[28mpe[8mr[28m l[8me[28m t[8ma[28mle[8mn[28mt [8me[28mn [8ms[28méc[8mu[28mri[8mt[28mé [8ma[28mu [8mQ[28mué[8mb[28mec[8m.[28m L[8m'[28méq[8mu[28mip[8me[28m e[8ms[28mt [8mc[28mom[8mp[28mos[8mé[28me [8md[28me [8mp[28mer[8ms[28mon[8mn[28mes[8m [28mpa[8ms[28msi[8mo[28mnn[8mé[28mes[8m [28mpa[8mr[28m l[8me[28m d[8mo[28mma[8mi[28mne[8m [28mde[8m [28mla[8m [28msé[8mc[28mur[8mi[28mté[8m [28met[8m [28mde[8m [28ml'[8mé[28mdu[8mc[28mat[8mi[28mon[8m.[28m N[8mo[28mus[8m [28mai[8mm[28mon[8ms[28m t[8mr[28man[8ms[28mme[8mt[28mtr[8me[28m n[8mo[28mtr[8me[28m p[8ma[28mss[8mi[28mon[8m [28met[8m [28mno[8mu[28ms [8md[28mép[8ml[28moy[8mo[28mns[8m [28mbé[8mn[28mév[8mo[28mle[8mm[28men[8mt[28m b[8me[28mau[8mc[28mou[8mp[28m d[8m'[28mef[8mf[28mor[8mt[28ms [8mp[28mou[8mr[28m a[8mc[28mco[8mm[28mpl[8mi[28mr [8mn[28mot[8mr[28me [8mm[28mis[8ms[28mio[8mn[28m. [8mF[28mLA[8mG[28m{d[8mb[28mab[8md[28m60[8m4[28mf4[8m7[28mb0[8ma[28mcd[8m8[28mfd[8m6[28mf4[8m3[28m63[8m2[28m02[8m3[28ma9[8m6[28m}
```

## Writeup

The text contains many terminal control codes, so we can just try to save the file `challenge1.txt` and print it in a terminal with

`cat challenge1.txt`

The command will print

```
L'colecyber est un organisme  but non lucratif dont la mission est de dvelopper le talent en scurit au Qubec. L'quipe est compose de personnes passionnes par le domaine de la scurit et de l'ducation. Nous aimons transmettre notre passion et nous dployons bnvolement beaucoup d'efforts pour accomplir notre mission. FLAG{dbabd604f47b0acd8fd6f43632023a96}

```

## Flag

`FLAG{dbabd604f47b0acd8fd6f43632023a96}`

-----

If you find errors or you want to contribute to this writeup go to the [GitHub repository](https://github.com/francesco-scar/CTF-writeups/tree/main/24h%40CTF/2022-02-05/Ecole_Cyber_1) or contact me [opening an issue](https://github.com/francesco-scar/CTF-writeups/issues).
