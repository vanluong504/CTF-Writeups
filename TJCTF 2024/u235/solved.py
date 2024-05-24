# #!/usr/bin/env python3
# # Created by Rob 'mubix' Fuller

# # Source of Info: https://www.debjitbiswas.com/elgamal/

# from Crypto.Util.number import inverse
# import sympy
# import random
# from binascii import hexlify, unhexlify

# def shared_secret(g,x,p):
#   # Shared Secret (h)
#   h = pow(g,x,p)
#   return h

# def encrypt(m,r,g,p,h):
#   c1 = pow(g,r,p)
#   # Stolen from https://github.com/dlitz/pycrypto/blob/master/lib/Crypto/PublicKey/ElGamal.py
#   c2 = (m * pow(h, r, p) ) % p
#   return c1,c2

# def decrypt(x,c1,c2,p):
#   s = pow(c1,x,p)
#   print(f"{s = }")
#   dm = (c2 * inverse(s,p)) % p
#   return dm

# if __name__ == "__main__":
#     # input_message = input("Enter message to encrypt: ")
#     # inputbytes = str.encode(input_message)
#     # m = int(hexlify(inputbytes), 16)
#     # p = sympy.randprime(m*2, m*4)
#     # g = sympy.randprime(int(m/2), m)
#     # x = random.randint(int(m/2),m)
#     # r = random.randint(int(m/2),m)
#     a = 7786748143272279885230083929570136234284368297432698839285012280040411676247181


#     p = 1006557409880081094474289244612169962014438359448736358451863306642952626305018944472713415044350968658692727515094769317505054471735110838791544736726202020388502580322012225736985572352552380319748794945735538193408960721596124087699868253292314371848149258400753821283235482032286919292953592804130618071525715007242467231486761719876948089200919616551909129741723066285644069900048285748549425115983478624093780666361561594317530939485059709440056610434868567734465251383281237175743991203641858314025617103200395748758248303534853204951672355724883586907261338189236276352934285483178308600733696423962351624124367
#     g = 3


#     y = 109633685273705994212635627427752760104347665796288426207908639236258338151195384419597401855448428038851291969247638420101634180329054232210725262514345176509331749870202222251687268758966365242471794124189953950331894553786541934189765932313034756250264088792731113013868704324859348031333296677322630400302112959572864792606884684746818699894753630813547185152869482804834096751191249035821524479582011904398010983136910905556008331821755766148756298463424885675847516280712713261253165756058607694454334546341013527380169718650584079714987676147524585348866766645309398768655545078119625734782657911241449320682029
#     M = 154742848158789198511544903912663377789



#     r = 682987144341972776975159150663233436174041938073450239643214850790862774837379616516597174044891000110673499992377432806875467827345036526869173481870146854120351342244448527048876681149282488478260775129376950523166860969024958367901847316768500376455132032336095286959651835627972680794803070083024768977791087595750928136657365368853710110862753161550773513799435469550905379295299172063138050334778787227763185469671337647118671181196476932705028647776734468484933694536789076764203004377043488856711547116449404150090970806825574682270879086814962946670830944429605670179542770266571947675450735517069822808989205
#     s = 636421939579159193614860353226103556240128703795589208046417668185960246995380873810270193611958165207512578610387978590568122284666408643070755932534312811841763290639453615429593350784642150435688932297873543559861119267756988708528059270049515444978534985497473935533285082035520155998023551352816833083753690759295989591483158165455884180426595012187220504349197574068647961679062122550861186039670182859803810899495682370644791419221484827680108244210816242051158300659823386584598526402984379275894072337509930857034489111245372416669214290852979430713652880877926518232604246482949331168777415836276581242325849

#     print("MESSAGE as an int (M) : {}".format(M))
#     print("Prime number (P)      : {}".format(p))
#     print("Generator (G)         : {}".format(g))
#     print("Alice private key (X) : {}".format(a))
#     print("Bob's private key (R) : {}".format(r))

#     h = shared_secret(g,a,p)
#     print("Shared secret (H)     : {}".format(h))

#     c1, c2 = encrypt(M,r,g,p,h)
#     print("Encrypted Message (C1): {}".format(c1))
#     print("Encrypted Message (C2): {}".format(c2))

#     dm = decrypt(a,c1,c2,p)
#     print("Decrypted Integer (dm): {}".format(dm))
#     x = format(dm, 'x')
#     print("Decrypted Hex (x)     : {}".format(x))
#     message = unhexlify(x)
#     print("Decrypted Message     : {}".format(message))



