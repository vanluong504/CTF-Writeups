# # FLAG = b"crypto{???????????????????????????????????}"

# from Crypto.Util.number import *

# n = 95341235345618011251857577682324351171197688101180707030749869409235726634345899397258784261937590128088284421816891826202978052640992678267974129629670862991769812330793126662251062120518795878693122854189330426777286315442926939843468730196970939951374889986320771714519309125434348512571864406646232154103
# e = 3
# c = 63476139027102349822147098087901756023488558030079225358836870725611623045683759473454129221778690683914555720975250395929721681009556415292257804239149809875424000027362678341633901036035522299395660255954384685936351041718040558055860508481512479599089561391846007771856837130233678763953257086620228436828


# def pad100(msg):
#     return msg + b'\x00' * (100 - len(msg))

# flag = b"crypto{" + b"\x00" * len("???????????????????????????????????") + b"}"
# print(len(flag))
# flag = pad100(flag)

# m = bytes_to_long(flag)
# print(m)

# P.<x> = PolynomialRing(Zmod(n))
# f = ((m + (2 **(8 * 58)) * x) ** 3 - c)//(2 ** (8 * 58 * e))

# f = f.monic()

# print(b"crypto{" + long_to_bytes( int(f.small_roots(epsilon = 1 / 20)[0]) ) + b"}")


n = 27772857409875257529415990911214211975844307184430241451899407838750503024323367895540981606586709985980003435082116995888017731426634845808624796292507989171497629109450825818587383112280639037484593490692935998202437639626747133650990603333094513531505209954273004473567193235535061942991750932725808679249964667090723480397916715320876867803719301313440005075056481203859010490836599717523664197112053206745235908610484907715210436413015546671034478367679465233737115549451849810421017181842615880836253875862101545582922437858358265964489786463923280312860843031914516061327752183283528015684588796400861331354873
e = 16
ct = 11303174761894431146735697569489134747234975144162172162401674567273034831391936916397234068346115459134602443963604063679379285919302225719050193590179240191429612072131629779948379821039610415099784351073443218911356328815458050694493726951231241096695626477586428880220528001269746547018741237131741255022371957489462380305100634600499204435763201371188769446054925748151987175656677342779043435047048130599123081581036362712208692748034620245590448762406543804069935873123161582756799517226666835316588896306926659321054276507714414876684738121421124177324568084533020088172040422767194971217814466953837590498718

PR.<x> = PolynomialRing(Zmod(n))

f = x ^ 16 - ct

f = f.roots()
for x in f:
    print(bytes.fromhex(hex(x[0])[2:]))