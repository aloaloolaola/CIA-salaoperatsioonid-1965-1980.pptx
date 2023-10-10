soojusmahtuvus, kuumutuskiirus, soojashoiuenergia, jahtumiskiirus = [float(a) for a in input().split(" ")]
#print(soojusmahtuvus, kuumutuskiirus, soojashoiuenergia, jahtumiskiirus)

soojashoiuenergiahulk = 60 * soojashoiuenergia
print(soojashoiuenergiahulk)

jahtumisaeg = (100 - 22) / jahtumiskiirus
kuumutusaeg = (100 - 22) * kuumutuskiirus / 60
#print(jahtumisaeg, kuumutusaeg)
if jahtumisaeg + kuumutusaeg > 60:
    #print("ei jõua jahtuda")
    kuumutusalgus = 3600/(jahtumiskiirus * kuumutuskiirus + 60)
    kuumutusalgustemperatuur = 100 - (3600 * jahtumiskiirus)/(jahtumiskiirus * kuumutuskiirus + 60)
    kuumutusenergia = (100 - kuumutusalgustemperatuur) * soojusmahtuvus
    print(kuumutusenergia)
else:
    #print("jõuab jahtuda")
    kuumutusenergia = (100 - 22) * soojusmahtuvus
    print(kuumutusenergia)