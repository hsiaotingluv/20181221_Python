Python 3.8.2 (v3.8.2:7b3ab5921f, Feb 24 2020, 17:52:18) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = []
for x in range(10):
    for y in range(10):
        if x%2 == 0:
            if y%2 != 0:
                list1.append((x, y))
                
SyntaxError: multiple statements found while compiling a single statement
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
>>> c
KeyboardInterrupt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
>>> for count in range(6, 1, -1):
	print(count, end = " ")

	
6 5 4 3 2 
>>> 
>>> ordvalue = ord("asd")
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    ordvalue = ord("asd")
TypeError: ord() expected a character, but string of length 3 found
>>> ord('z')
122
>>> ord('a')
97
>>> 122-97
25
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py
Enter a one-word, lowercase message: hello world
Enter the distance value: 19001
䪡䪞䪥䪥䪨䩙䪰䪨䪫䪥䪝
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py
Enter a one-word, lowercase message: hello world
Enter the distance value: 9
qnuux)x{um
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py
Enter the code text: qnuux)x{um
Enter the distance value: 9
hello world
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py
Enter the code text: 䪡䪞䪥䪥䪨䩙䪰䪨䪫䪥䪝
Enter the distance value: 19001
hello world
>>> ord('䪡')
19105
>>> chr('1038409183')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    chr('1038409183')
TypeError: an integer is required (got type str)
>>> chr(1038409183)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    chr(1038409183)
ValueError: chr() arg not in range(0x110000)
>>> chr(110000)
'\U0001adb0'
>>> ord('的')
30340
>>> ord('婷')
23159
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py
Enter a one-word, lowercase message: 我是小婷
Enter the distance value: 1029
昖樴怔幼
>>> 
= RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py
Enter the code text: 昖樴怔幼
Enter the distance value: 1029
我是小婷
>>> 'encrypt e decrypt d'.split()
['encrypt', 'e', 'decrypt', 'd']
>>> a = "abcdt"
>>> a.find(3)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.find(3)
TypeError: must be str, not int
>>> a.find("a")
0
>>> a.find("t")
4
>>> a[2]
'c'
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Key #25: HVWGGWGGAMMGSQFSHHASGGOUSS.
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Key #0: GUVF VF ZL FRPERG ZRFFNTR.
Key #1: FTUE UE YK EQODQF YQEEMSQ.
Key #2: ESTD TD XJ DPNCPE XPDDLRP.
Key #3: DRSC SC WI COMBOD WOCCKQO.
Key #4: CQRB RB VH BNLANC VNBBJPN.
Key #5: BPQA QA UG AMKZMB UMAAIOM.
Key #6: AOPZ PZ TF ZLJYLA TLZZHNL.
Key #7: ZNOY OY SE YKIXKZ SKYYGMK.
Key #8: YMNX NX RD XJHWJY RJXXFLJ.
Key #9: XLMW MW QC WIGVIX QIWWEKI.
Key #10: WKLV LV PB VHFUHW PHVVDJH.
Key #11: VJKU KU OA UGETGV OGUUCIG.
Key #12: UIJT JT NZ TFDSFU NFTTBHF.
Key #13: THIS IS MY SECRET MESSAGE.
Key #14: SGHR HR LX RDBQDS LDRRZFD.
Key #15: RFGQ GQ KW QCAPCR KCQQYEC.
Key #16: QEFP FP JV PBZOBQ JBPPXDB.
Key #17: PDEO EO IU OAYNAP IAOOWCA.
Key #18: OCDN DN HT NZXMZO HZNNVBZ.
Key #19: NBCM CM GS MYWLYN GYMMUAY.
Key #20: MABL BL FR LXVKXM FXLLTZX.
Key #21: LZAK AK EQ KWUJWL EWKKSYW.
Key #22: KYZJ ZJ DP JVTIVK DVJJRXV.
Key #23: JXYI YI CO IUSHUJ CUIIQWU.
Key #24: IWXH XH BN HTRGTI BTHHPVT.
Key #25: HVWG WG AM GSQFSH ASGGOUS.
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Key #0: qnuux)x{um
Key #1: qnuux)x{um
Key #2: qnuux)x{um
Key #3: qnuux)x{um
Key #4: qnuux)x{um
Key #5: qnuux)x{um
Key #6: qnuux)x{um
Key #7: qnuux)x{um
Key #8: qnuux)x{um
Key #9: qnuux)x{um
Key #10: qnuux)x{um
Key #11: qnuux)x{um
Key #12: qnuux)x{um
Key #13: qnuux)x{um
Key #14: qnuux)x{um
Key #15: qnuux)x{um
Key #16: qnuux)x{um
Key #17: qnuux)x{um
Key #18: qnuux)x{um
Key #19: qnuux)x{um
Key #20: qnuux)x{um
Key #21: qnuux)x{um
Key #22: qnuux)x{um
Key #23: qnuux)x{um
Key #24: qnuux)x{um
Key #25: qnuux)x{um
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200418 (file).py", line 65, in <module>
    text = read.file()
NameError: name 'read' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the distance value: 9
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200418 (file).py", line 69, in <module>
    ordvalue = ord(ch)
NameError: name 'ch' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the distance value: 9
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200418 (file).py", line 69, in <module>
    ordvalue = ord(ch)
TypeError: ord() expected a character, but string of length 13 found
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the distance value: 9
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200418 (file).py", line 69, in <module>
    ordvalue = ord(char)
TypeError: ord() expected a character, but string of length 13 found
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter a one-word, lowercase message: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the distance value: 9
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200418 (file).py", line 80, in <module>
    codee += chr(cipherValue)
NameError: name 'codee' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the distance value: 9
Qnuux)x{um*V)wjvn)r|)q|rjx}rwpJ{n)x~)}qn{nHWrln)}x)vnn})x~7
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the distance value: 9








Qnuux)x{um*V)wjvn)r|)q|rjx}rwpJ{n)x~)}qn{nHWrln)}x)vnn})x~7
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the distance value: 9
Qnuux)x{um*
V)wjvn)r|)q|rjx}rwp
J{n)x~)}qn{nH
Wrln)}x)vnn})x~7

>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the distance value: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to decrypt: Qnuux)x{um*
V)wjvn)r|)q|rjx}rwp
J{n)x~)}qn{nH
Wrln)}x)vnn})x~7
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200418 (file).py", line 96, in <module>
    cipherValue = ordvalue - distance
NameError: name 'distance' is not defined
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to decrypt: Qnuux)x{um*
V)wjvn)r|)q|rjx}rwp
J{n)x~)}qn{nH
Wrln)}x)vnn})x~7
Pmttw(wztl)
Olssv'~vysk(
Nkrru&}uxrj'
Mjqqt%|twqi&
Lipps${svph%
Khoor#zruog$
Jgnnq"yqtnf#
Ifmmp!xpsme"
Hello world!

Gdkknvnqkc 	
Fcjjmumpjb
Ebiiltloia
Dahhksknh`
C`ggjrjmg_
B_ffiqilf^
A^eehphke]
@]ddgogjd\
?\ccfnfic[
>[bbemehbZ
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200418 (file).py", line 100, in <module>
    translated += chr(cipherValue)
ValueError: chr() arg not in range(0x110000)
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to decrypt: GUVF VF ZL FRPERG ZRFFNTR.
FTUEUEYKEQODQFYQEEMSQ-
ESTDTDXJDPNCPEXPDDLRP,
DRSCSCWICOMBODWOCCKQO+
CQRBRBVHBNLANCVNBBJPN*
BPQAQAUGAMK@MBUMAAIOM)
AOP@P@TF@LJ?LATL@@HNL(
@NO?O?SE?KI>K@SK??GMK'
?MN>N>RD>JH=J?RJ>>FLJ&
>LM=M=QC=IG<I>QI==EKI%
=KL<L<PB<HF;H=PH<<DJH$
<JK;K;OA;GE:G<OG;;CIG#
;IJ:J:N@:FD9F;NF::BHF"
:HI9I9M?9EC8E:ME99AGE!
9GH8H8L>8DB7D9LD88@FD 
8FG7G7K=7CA6C8KC77?EC
7EF6F6J<6B@5B7JB66>DB
6DE5E5I;5A?4A6IA55=CA
5CD4D4H:4@>3@5H@44<B@
4BC3C3G93?=2?4G?33;A?
3AB2B2F82><1>3F>22:@>
2@A1A1E71=;0=2E=119?=
1?@0
@0
D6
0<:/<1
D<008><
0>?/	?/	C5	/;9.;0	C;//7=;
/=>.>.B4.:8-:/B:..6<:
.<=-=-A3-97,9.A9--5;9
-;<,<,@2,86+8-@8,,4:8
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to decrypt: GUVF VF ZL FRPERG ZRFFNTR.
ftueueykeqodqfyqeemsq-
estdtdxjdpncpexpddlrp,
drscscwicombodwocckqo+
cqrbrbvhbnlancvnbbjpn*
bpqaqaugamk`mbumaaiom)
aop`p`tf`lj_latl``hnl(
`no_o_se_ki^k`sk__gmk'
_mn^n^rd^jh]j_rj^^flj&
^lm]m]qc]ig\i^qi]]eki%
]kl\l\pb\hf[h]ph\\djh$
\jk[k[oa[geZg\og[[cig#
[ijZjZn`ZfdYf[nfZZbhf"
ZhiYiYm_YecXeZmeYYage!
YghXhXl^XdbWdYldXX`fd 
XfgWgWk]WcaVcXkcWW_ec
WefVfVj\Vb`UbWjbVV^db
VdeUeUi[Ua_TaViaUU]ca
UcdTdThZT`^S`Uh`TT\b`
TbcScSgYS_]R_Tg_SS[a_
SabRbRfXR^\Q^Sf^RRZ`^
R`aQaQeWQ][P]Re]QQY_]
Q_`P
`P
dV
P\ZO\Q
d\PPX^\
P^_O	_O	cU	O[YN[P	c[OOW][
O]^N^NbTNZXMZObZNNV\Z
N\]M]MaSMYWLYNaYMMU[Y
M[\L\L`RLXVKXM`XLLTZX
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to decrypt: Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.
kvbia`thfuvailwslh`hua+ibajlyahpuafp`hi`byk-
juah`_sgetu`hkvrkg_gt`*ha`ikx`got`eo_gh_axj,
it`g_^rfdst_gjuqjf^fs_)g`_hjw_fns_dn^fg^`wi+
hs_f^]qecrs^fitpie]er^(f_^giv^emr^cm]ef]_vh*
gr^e]\pdbqr]ehsohd\dq]'e^]fhu]dlq]bl\de\^ug)
fq]d\[ocapq\dgrngc[cp\&d]\egt\ckp\ak[cd[]tf(
ep\c[Znb`op[cfqmfbZbo[%c\[dfs[bjo[`jZbcZ\se'
do[bZYma_noZbepleaYanZ$b[ZcerZainZ_iYabY[rd&
cnZaYXl`^mnYadokd`X`mY#aZYbdqY`hmY^hX`aXZqc%
bmY`XWk_]lmX`cnjc_W_lX"`YXacpX_glX]gW_`WYpb$
alX_WVj^\klW_bmib^V^kW!_XW`boW^fkW\fV^_VXoa#
`kW^VUi][jkV^alha]U]jV ^WV_anV]ejV[eU]^UWn`"
_jV]UTh\ZijU]`kg`\T\iU]VU^`mU\diUZdT\]TVm_!
^iU\TSg[YhiT\_jf_[S[hT\UT]_lT[chTYcS[\SUl^ 
]hT[SRfZXghS[^ie^ZRZgS[TS\^kSZbgSXbRZ[RTk]
\gSZRQeYWfgRZ]hd]YQYfRZSR[]jRYafRWaQYZQSj\
[fRYQPdXVefQY\gc\XPXeQYRQZ\iQX`eQV`PXYPRi[
ZeQXPOcWUdePX[fb[WOWdPXQPY[hPW_dPU_OWXOQhZ
YdPWONbVTcdOWZeaZVNVcOWPOXZgOV^cOT^NVWNPgY
XcOVNMaUSbcNVYd`YUMUbNVONWYfNU]bNS]MUVMOfX
WbNUML`TRabMUXc_XTLTaMUNMVXeMT\aMR\LTULNeW
VaMTLK
_SQ
`aL
TW
b^WSKS`L
TML
UWdLS[`LQ
[K
STKMdV
U`LSKJ	^RP	_`K	SV	a]VRJR_K	SLK	TVcKRZ_KP	ZJ	RSJLcU
T_KRJI]QO^_JRU`\UQIQ^JRKJSUbJQY^JOYIQRIKbT
S^JQIH\PN]^IQT_[TPHP]IQJIRTaIPX]INXHPQHJaS
R]IPHG[OM\]HPS^ZSOGO\HPIHQS`HOW\HMWGOPGI`R
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to decrypt: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to decrypt: Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.
kvbia`thfuvailwslh`hua+ibajlyahpuafp`hi`byk-
juah`_sgetu`hkvrkg_gt`*ha`ikx`got`eo_gh_axj,
it`g_^rfdst_gjuqjf^fs_)g`_hjw_fns_dn^fg^`wi+
hs_f^]qecrs^fitpie]er^(f_^giv^emr^cm]ef]_vh*
gr^e]\pdbqr]ehsohd\dq]'e^]fhu]dlq]bl\de\^ug)
fq]d\[ocapq\dgrngc[cp\&d]\egt\ckp\ak[cd[]tf(
ep\c[Znb`op[cfqmfbZbo[%c\[dfs[bjo[`jZbcZ\se'
do[bZYma_noZbepleaYanZ$b[ZcerZainZ_iYabY[rd&
cnZaYXl`^mnYadokd`X`mY#aZYbdqY`hmY^hX`aXZqc%
bmY`XWk_]lmX`cnjc_W_lX"`YXacpX_glX]gW_`WYpb$
alX_WVj^\klW_bmib^V^kW!_XW`boW^fkW\fV^_VXoa#
`kW^VUi][jkV^alha]U]jV ^WV_anV]ejV[eU]^UWn`"
_jV]UTh\ZijU]`kg`\T\iU]VU^`mU\diUZdT\]TVm_!
^iU\TSg[YhiT\_jf_[S[hT\UT]_lT[chTYcS[\SUl^ 
]hT[SRfZXghS[^ie^ZRZgS[TS\^kSZbgSXbRZ[RTk]
\gSZRQeYWfgRZ]hd]YQYfRZSR[]jRYafRWaQYZQSj\
[fRYQPdXVefQY\gc\XPXeQYRQZ\iQX`eQV`PXYPRi[
ZeQXPOcWUdePX[fb[WOWdPXQPY[hPW_dPU_OWXOQhZ
YdPWONbVTcdOWZeaZVNVcOWPOXZgOV^cOT^NVWNPgY
XcOVNMaUSbcNVYd`YUMUbNVONWYfNU]bNS]MUVMOfX
WbNUML`TRabMUXc_XTLTaMUNMVXeMT\aMR\LTULNeW
VaMTLK
_SQ
`aL
TW
b^WSKS`L
TML
UWdLS[`LQ
[K
STKMdV
U`LSKJ	^RP	_`K	SV	a]VRJR_K	SLK	TVcKRZ_KP	ZJ	RSJLcU
T_KRJI]QO^_JRU`\UQIQ^JRKJSUbJQY^JOYIQRIKbT
S^JQIH\PN]^IQT_[TPHP]IQJIRTaIPX]INXHPQHJaS
R]IPHG[OM\]HPS^ZSOGO\HPIHQS`HOW\HMWGOPGI`R
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to decrypt: Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.
1 mxdkcb!vjh!wxc!kn!yunjbjwc-!kdc!ln{cjrwch!rb!jkbd{m/
2 nyeldc"wki"xyd"lo"zvokckxd."led"mo|dksxdi"sc"klce|n0
3 ozfmed#xlj#yze#mp#{wpldlye/#mfe#np}eltyej#td#lmdf}o1
4 p{gnfe$ymk$z{f$nq$|xqmemzf0$ngf$oq~fmuzfk$ue$mneg~p2
5 q|hogf%znl%{|g%or%}yrnfn{g1%ohg%prgnv{gl%vf%nofhq3
6 r}iphg&{om&|}h&ps&~zsogo|h2&pih&qshow|hm&wg&opgir4
7 s~jqih'|pn'}~i'qt'{tphp}i3'qji'rtipx}in'xh'pqhjs5
8 tkrji(}qo(~j(ru(|uqiq~j4(rkj(sujqy~jo(yi(qrikt6
9 ulskj)~rp)k)sv)}vrjrk5)slk)tvkrzkp)zj)rsjlu7
10 vmtlk*sq*l*tw*~wsksl6*tml*uwls{lq*{k*stkmv8
11 wnuml+tr+m+ux+xtltm7+unm+vxmt|mr+|l+tulnw9
12 xovnm,us,n,vy,yumun8,von,wynu}ns,}m,uvmox:
13 ypwon-vt-o-wz-zvnvo9-wpo-xzov~ot-~n-vwnpy;
14 zqxpo.wu.p.x{.{wowp:.xqp.y{pwpu.o.wxoqz<
15 {ryqp/xv/q/y|/|xpxq;/yrq/z|qxqv/p/xypr{=
16 |szrq0yw0r0z}0}yqyr<0zsr0{}ryrw0q0yzqs|>
17 }t{sr1zx1s1{~1~zrzs=1{ts1|~szsx1r1z{rt}?
18 ~u|ts2{y2t2|2{s{t>2|ut2}t{ty2s2{|su~@
19 v}ut3|z3u3}3|t|u?3}vu3~u|uz3t3|}tvA
20 w~vu4}{4v4~4}u}v@4~wv4v}v{4u4}~uwB
21 xwv5~|5w55~v~wA5xw5w~w|5v5~vxC
22 yxw6}6x66wxB6yx6xx}6w6wyD
23 zyx7~7y77xyC7zy7yy~7x7xzE
24 {zy88z88yzD8{z8zz8y8y{F
25 |{z99{99z{E9|{9{{9z9z|G
26 }|{::|::{|F:}|:||:{:{}H
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.
vmtlk*sq*l*tw*~wsksl6*tml*uwls{lq*{k*stkmv8

Enter the code to decrypt: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: hello world
rovvy*y|vn

Enter the code to decrypt: rovvy*y|vn
qnuux)x{um
pmttw(wztl
olssv'~vysk
nkrru&}uxrj
mjqqt%|twqi
lipps${svph
khoor#zruog
jgnnq"yqtnf
ifmmp!xpsme
hello world
gdkknvnqkc
fcjjmumpjb
ebiiltloia
dahhksknh`
c`ggjrjmg_
b_ffiqilf^
a^eehphke]
`]ddgogjd\
_\ccfnfic[
^[bbemehbZ
]ZaadldgaY
\Y``ckcf`X
[X__bjbe_W
ZW^^aiad^V
YV]]`h`c]U
XU\\_g_b\T
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: hello world
rovvy*y|vn

Enter the code to decrypt: rovvy*y|vn
qnuux)x{um
pmttw(wztl
olssv'~vysk
nkrru&}uxrj
mjqqt%|twqi
lipps${svph
khoor#zruog
jgnnq"yqtnf
ifmmp!xpsme
hello world
gdkknvnqkc
fcjjmumpjb
ebiiltloia
dahhksknh`
c`ggjrjmg_
b_ffiqilf^
a^eehphke]
`]ddgogjd\
_\ccfnfic[
^[bbemehbZ
]ZaadldgaY
\Y``ckcf`X
[X__bjbe_W
ZW^^aiad^V
YV]]`h`c]U
XU\\_g_b\T
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: hello world
rovvy*y|vn

Enter the code to decrypt: rovvy*y|vn
qnuux)x{um
pmttw(wztl
olssv'~vysk
nkrru&}uxrj
mjqqt%|twqi
lipps${svph
khoor#zruog
jgnnq"yqtnf
ifmmp!xpsme
hello world
gdkknvnqkc
fcjjmumpjb
ebiiltloia
dahhksknh`
c`ggjrjmg_
b_ffiqilf^
a^eehphke]
`]ddgogjd\
_\ccfnfic[
^[bbemehbZ
]ZaadldgaY
\Y``ckcf`X
[X__bjbe_W
ZW^^aiad^V
YV]]`h`c]U
XU\\_g_b\T
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: my name is hsiaoting
w*xkwo*s}*r}sky~sxq

Enter the code to decrypt: w*xkwo*s}*r}sky~sxq
v)wjvn)r|)q|rjx}rwp
u(vium(q{(p{qiw|qvo
t'uhtl'pz'ozphv{pun
s&tgsk&oy&nyoguzotm
r~%sfrj%nx%mxnftynsl
q}$reqi$mw$lwmesxmrk
p|#qdph#lv#kvldrwlqj
o{"pcog"ku"jukcqvkpi
nz!obnf!jt!itjbpujoh
my name is hsiaoting
lxm`ldhrgrh`nshmf
kwl_kcgqfqg_mrgle
jvk^jbfpepf^lqfkd
iuj]iaeodoe]kpejc
hti\h`dncnd\jodib
gsh[g_cmbmc[incha
frgZf^blalbZhmbg`
eqfYe]ak`kaYglaf_
dpeXd\`j_j`Xfk`e^
codWc[_i^i_Wej_d]
bncVbZ^h]h^Vdi^c\
ambUaY]g\g]Uch]b[
`laT`X\f[f\Tbg\aZ
_k`S_W[eZe[Saf[`Y
^j_R^VZdYdZR`eZ_X
]i^Q]UYcXcYQ_dY^W
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: hello
rovvy

Enter the code to decrypt: Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.
Kvbia`thfuvailwslh`hua+ibajlyahpuafp`hi`byk-
Juah`_sgetu`hkvrkg_gt`*ha`ikx`got`eo_gh_axj,
It`g_^rfdst_gjuqjf^fs_)g`_hjw_fns_dn^fg^`wi+
Hs_f^]qecrs^fitpie]er^(f_^giv^emr^cm]ef]_vh*
Gr^e]\pdbqr]ehsohd\dq]'e^]fhu]dlq]bl\de\^ug)
Fq]d\[ocapq\dgrngc[cp\&d]\egt\ckp\ak[cd[]tf(
Ep\c[Znb`op[cfqmfbZbo[%c\[dfs[bjo[`jZbcZ\se'
Do[bZYma_noZbepleaYanZ$b[ZcerZainZ_iYabY[rd&
CnZaYXl`^mnYadokd`X`mY#aZYbdqY`hmY^hX`aXZqc%
BmY`XWk_]lmX`cnjc_W_lX"`YXacpX_glX]gW_`WYpb$
AlX_WVj^\klW_bmib^V^kW!_XW`boW^fkW\fV^_VXoa#
@kW^VUi][jkV^alha]U]jV ^WV_anV]ejV[eU]^UWn`"
?jV]UTh\ZijU]`kg`\T\iU]VU^`mU\diUZdT\]TVm_!
>iU\TSg[YhiT\_jf_[S[hT\UT]_lT[chTYcS[\SUl^ 
=hT[SRfZXghS[^ie^ZRZgS[TS\^kSZbgSXbRZ[RTk]
<gSZRQeYWfgRZ]hd]YQYfRZSR[]jRYafRWaQYZQSj\
;fRYQPdXVefQY\gc\XPXeQYRQZ\iQX`eQV`PXYPRi[
:eQXPOcWUdePX[fb[WOWdPXQPY[hPW_dPU_OWXOQhZ
9dPWONbVTcdOWZeaZVNVcOWPOXZgOV^cOT^NVWNPgY
8cOVNMaUSbcNVYd`YUMUbNVONWYfNU]bNS]MUVMOfX
7bNUML`TRabMUXc_XTLTaMUNMVXeMT\aMR\LTULNeW
6aMTLK
_SQ
`aL
TW
b^WSKS`L
TML
UWdLS[`LQ
[K
STKMdV
5`LSKJ	^RP	_`K	SV	a]VRJR_K	SLK	TVcKRZ_KP	ZJ	RSJLcU
4_KRJI]QO^_JRU`\UQIQ^JRKJSUbJQY^JOYIQRIKbT
3^JQIH\PN]^IQT_[TPHP]IQJIRTaIPX]INXHPQHJaS
2]IPHG[OM\]HPS^ZSOGO\HPIHQS`HOW\HMWGOPGI`R
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: hello
rovvy

Enter the code to decrypt: Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.
1 Kvbia`thfuvailwslh`hua+ibajlyahpuafp`hi`byk-
2 Juah`_sgetu`hkvrkg_gt`*ha`ikx`got`eo_gh_axj,
3 It`g_^rfdst_gjuqjf^fs_)g`_hjw_fns_dn^fg^`wi+
4 Hs_f^]qecrs^fitpie]er^(f_^giv^emr^cm]ef]_vh*
5 Gr^e]\pdbqr]ehsohd\dq]'e^]fhu]dlq]bl\de\^ug)
6 Fq]d\[ocapq\dgrngc[cp\&d]\egt\ckp\ak[cd[]tf(
7 Ep\c[Znb`op[cfqmfbZbo[%c\[dfs[bjo[`jZbcZ\se'
8 Do[bZYma_noZbepleaYanZ$b[ZcerZainZ_iYabY[rd&
9 CnZaYXl`^mnYadokd`X`mY#aZYbdqY`hmY^hX`aXZqc%
10 BmY`XWk_]lmX`cnjc_W_lX"`YXacpX_glX]gW_`WYpb$
11 AlX_WVj^\klW_bmib^V^kW!_XW`boW^fkW\fV^_VXoa#
12 @kW^VUi][jkV^alha]U]jV ^WV_anV]ejV[eU]^UWn`"
13 ?jV]UTh\ZijU]`kg`\T\iU]VU^`mU\diUZdT\]TVm_!
14 >iU\TSg[YhiT\_jf_[S[hT\UT]_lT[chTYcS[\SUl^ 
15 =hT[SRfZXghS[^ie^ZRZgS[TS\^kSZbgSXbRZ[RTk]
16 <gSZRQeYWfgRZ]hd]YQYfRZSR[]jRYafRWaQYZQSj\
17 ;fRYQPdXVefQY\gc\XPXeQYRQZ\iQX`eQV`PXYPRi[
18 :eQXPOcWUdePX[fb[WOWdPXQPY[hPW_dPU_OWXOQhZ
19 9dPWONbVTcdOWZeaZVNVcOWPOXZgOV^cOT^NVWNPgY
20 8cOVNMaUSbcNVYd`YUMUbNVONWYfNU]bNS]MUVMOfX
21 7bNUML`TRabMUXc_XTLTaMUNMVXeMT\aMR\LTULNeW
22 6aMTLK
_SQ
`aL
TW
b^WSKS`L
TML
UWdLS[`LQ
[K
STKMdV
23 5`LSKJ	^RP	_`K	SV	a]VRJR_K	SLK	TVcKRZ_KP	ZJ	RSJLcU
24 4_KRJI]QO^_JRU`\UQIQ^JRKJSUbJQY^JOYIQRIKbT
25 3^JQIH\PN]^IQT_[TPHP]IQJIRTaIPX]INXHPQHJaS
26 2]IPHG[OM\]HPS^ZSOGO\HPIHQS`HOW\HMWGOPGI`R
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: hello
rovvy

Enter the code to decrypt: Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.
1 vbiax¹thf¹uva¹il¹wslhxhua­¹iba¹jlyahpuaf¹px¹hixbyk«
2 uahvw¸sge¸tuv¸hk¸vrkgwgtv¬¸hav¸ikxvgotve¸ow¸ghwaxjª
3 ttguv·rfd·stu·gj·uqjfvfsu«·gtu·hjwufnsud·nv·fgvtwi©
4 ssftu¶qec¶rst¶fi¶tpieuertª¶fst¶givtemrtc¶mu¶efusvh¨
5 rrestµpdbµqrsµehµsohdtdqs©µersµfhusdlqsbµltµdetrug§
6 qqdrs´oca´pqr´dg´rngcscpr¨´dqr´egtrckpra´ks´cdsqtf¦
7 ppcqr³nbl³opq³cf³qmfbrboq§³cpq³dfsqbjoql³jr³bcrpse¥
8 oobpq²mak²nop²be²pleaqanp¦²bop²cerpainpk²iq²abqord¤
9 nnaop±lhj±mno±ad±okdhphmo¥±ano±bdqohhmoj±hp±hapnqc£
10 mmfno°kgi°lmn°fc°njcgogln¤°fmn°acpngglni°go°gfompb¢
11 llemn¯jfh¯klm¯eb¯mibfnfkm£¯elm¯dbomffkmh¯fn¯fenloa¡
12 kkdlm®ieg®jkl®da®lhaemejl¢®dkl®canleejlg®em®edmknb 
13 jjckl­hdf­ijk­c`­kg`dldik¡­cjk­b`mkddikf­dl­dcljma
14 ciibjk¬gce¬hij¬b_¬jf_ckchj ¬bij¬a_ljcchje¬ck¬cbkil`
15 hhaij«fbd«ghi«a^«ie^bjbgi«ahi«`^kibbgid«bj«bajhk_
16 ~gg`hiªeacªfghª`]ªhd]aiafhª`ghª_]jhaafhcªaiªa`igj^
17 }ff_gh©d`b©efg©_\©gc\`h`eg©_fg©^\ig`Xegb©Xh©`_hfi]
18 |ee^fg¨c_a¨def¨^[¨fb[_g_df¨^ef¨][hf_Wdfa¨Wg¨_^geh\
19 {dd]ef§b^`§cde§]Z§eaZ^f^ce§]de§\Zge^Vce`§Vf§^]fdg[
20 zcc\de¦a]_¦bcd¦\Y¦dRY]e]bd¦\cd¦[Yfd]Ubd_¦Ue¦]\ecfZ
21 çybb[cd¥P\^¥abc¥[X¥cQX\d\ac¥[bc¥ZXec\Tac^¥Td¥\[dbeY
22 xaaZbc¤O[]¤Nab¤ZW¤bPW[c[Nb¤Zab¤YWdb[SNb]¤Sc¤[ZcadX
23 wL`Yab£NZ\£MLa£YV£aOVZbZMa£Y`a£XVcaZRMa\£Rb£ZYb`cW
Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200418 (file).py", line 117, in <module>
    print(distance, translated)
KeyboardInterrupt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: hello
klmnopqrstuvwxyzcdefghijkl

Enter the code to decrypt: Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.
Kvbia`thfuvailwslh`hua+ibajlyahpuafp`hi`byk-
Juah`_sgetu`hkvrkg_gt`*ha`ikx`got`eo_gh_axj,
It`g_^rfdst_gjuqjf^fs_)g`_hjw_fns_dn^fg^`wi+
Hs_f^]qecrs^fitpie]er^(f_^giv^emr^cm]ef]_vh*
Gr^e]\pdbqr]ehsohd\dq]'e^]fhu]dlq]bl\de\^ug)
Fq]d\[ocapq\dgrngc[cp\&d]\egt\ckp\ak[cd[]tf(
Ep\c[Znb`op[cfqmfbZbo[%c\[dfs[bjo[`jZbcZ\se'
Do[bZYma_noZbepleaYanZ$b[ZcerZainZ_iYabY[rd&
CnZaYXl`^mnYadokd`X`mY#aZYbdqY`hmY^hX`aXZqc%
BmY`XWk_]lmX`cnjc_W_lX"`YXacpX_glX]gW_`WYpb$
AlX_WVj^\klW_bmib^V^kW!_XW`boW^fkW\fV^_VXoa#
@kW^VUi][jkV^alha]U]jV ^WV_anV]ejV[eU]^UWn`"
?jV]UTh\ZijU]`kg`\T\iU]VU^`mU\diUZdT\]TVm_!
>iU\TSg[YhiT\_jf_[S[hT\UT]_lT[chTYcS[\SUl^ 
=hT[SRfZXghS[^ie^ZRZgS[TS\^kSZbgSXbRZ[RTk]
<gSZRQeYWfgRZ]hd]YQYfRZSR[]jRYafRWaQYZQSj\
;fRYQPdXVefQY\gc\XPXeQYRQZ\iQX`eQV`PXYPRi[
:eQXPOcWUdePX[fb[WOWdPXQPY[hPW_dPU_OWXOQhZ
9dPWONbVTcdOWZeaZVNVcOWPOXZgOV^cOT^NVWNPgY
8cOVNMaUSbcNVYd`YUMUbNVONWYfNU]bNS]MUVMOfX
7bNUML`TRabMUXc_XTLTaMUNMVXeMT\aMR\LTULNeW
6aMTLK
_SQ
`aL
TW
b^WSKS`L
TML
UWdLS[`LQ
[K
STKMdV
5`LSKJ	^RP	_`K	SV	a]VRJR_K	SLK	TVcKRZ_KP	ZJ	RSJLcU
4_KRJI]QO^_JRU`\UQIQ^JRKJSUbJQY^JOYIQRIKbT
3^JQIH\PN]^IQT_[TPHP]IQJIRTaIPX]INXHPQHJaS
2]IPHG[OM\]HPS^ZSOGO\HPIHQS`HOW\HMWGOPGI`R
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: Lwcjba uig vwb jm xtmiaivb
klmnopqrstuvwxyzcdefghijkl

Enter the code to decrypt: Lwcjba uig vwb jm xtmiaivb
1 Kvbia`thfuvailwslh`hua
2 Juah`_sgetu`hkvrkg_gt`
3 It`g_^rfdst_gjuqjf^fs_
4 Hs_f^]qecrs^fitpie]er^
5 Gr^e]\pdbqr]ehsohd\dq]
6 Fq]d\[ocapq\dgrngc[cp\
7 Ep\c[Znb`op[cfqmfbZbo[
8 Do[bZYma_noZbepleaYanZ
9 CnZaYXl`^mnYadokd`X`mY
10 BmY`XWk_]lmX`cnjc_W_lX
11 AlX_WVj^\klW_bmib^V^kW
12 @kW^VUi][jkV^alha]U]jV
13 ?jV]UTh\ZijU]`kg`\T\iU
14 >iU\TSg[YhiT\_jf_[S[hT
15 =hT[SRfZXghS[^ie^ZRZgS
16 <gSZRQeYWfgRZ]hd]YQYfR
17 ;fRYQPdXVefQY\gc\XPXeQ
18 :eQXPOcWUdePX[fb[WOWdP
19 9dPWONbVTcdOWZeaZVNVcO
20 8cOVNMaUSbcNVYd`YUMUbN
21 7bNUML`TRabMUXc_XTLTaM
22 6aMTLK
_SQ
`aL
TW
b^WSKS`L
23 5`LSKJ	^RP	_`K	SV	a]VRJR_K
24 4_KRJI]QO^_JRU`\UQIQ^J
25 3^JQIH\PN]^IQT_[TPHP]I
26 2]IPHG[OM\]HPS^ZSOGO\H
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.
klmnopqrstuvwxyzcdefghijkl

Enter the code to decrypt: Lwcjba uig vwb jm xtmiaivb, jcb kmzbiqvbg qa ijaczl.
1 vbiax¹thf¹uva¹il¹wslhxhua­¹iba¹jlyahpuaf¹px¹hixbyk«
2 uahvw¸sge¸tuv¸hk¸vrkgwgtv¬¸hav¸ikxvgotve¸ow¸ghwaxjª
3 ttguv·rfd·stu·gj·uqjfvfsu«·gtu·hjwufnsud·nv·fgvtwi©
4 ssftu¶qec¶rst¶fi¶tpieuertª¶fst¶givtemrtc¶mu¶efusvh¨
5 rrestµpdbµqrsµehµsohdtdqs©µersµfhusdlqsbµltµdetrug§
6 qqdrs´oca´pqr´dg´rngcscpr¨´dqr´egtrckpra´ks´cdsqtf¦
7 ppcqr³nbl³opq³cf³qmfbrboq§³cpq³dfsqbjoql³jr³bcrpse¥
8 oobpq²mak²nop²be²pleaqanp¦²bop²cerpainpk²iq²abqord¤
9 nnaop±lhj±mno±ad±okdhphmo¥±ano±bdqohhmoj±hp±hapnqc£
10 mmfno°kgi°lmn°fc°njcgogln¤°fmn°acpngglni°go°gfompb¢
11 llemn¯jfh¯klm¯eb¯mibfnfkm£¯elm¯dbomffkmh¯fn¯fenloa¡
12 kkdlm®ieg®jkl®da®lhaemejl¢®dkl®canleejlg®em®edmknb 
13 jjckl­hdf­ijk­c`­kg`dldik¡­cjk­b`mkddikf­dl­dcljma
14 iibjk¬gce¬hij¬b_¬jf_ckchj ¬bij¬a_ljcchje¬ck¬cbkil`
15 hhaij«fbd«ghi«a^«ie^bjbgi«ahi«`^kibbgid«bj«bajhk_
16Traceback (most recent call last):
  File "/Users/hsiaotingluv/Desktop/python/20200418 (file).py", line 116, in <module>
    print(distance, translated)
KeyboardInterrupt
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: hello hsiao ting
klmnopqrstuvwxyzcdefghijkl

Enter the code to decrypt: klmnopqrstuvwxyzcdefghijkl
1 jklmnopqrstuvwxybcdefghijk
2 ijklmnopqrstuvwxabcdefghij
3 hijklmnopqrstuvwtabcdefghi
4 ghijklmnopqrstuvsrabcdefgh
5 fghijklmnopqrsturqpabcdefg
6 efghijklmnopqrstqponabcdef
7 defghijklmnopqrsponmlabcde
8 cdefghijklmnopqronmlkjabcd
9 bcdefghijklmnopqnmlkjihabc
10 abcdefghijklmnopmlkjihgfab
11 dabcdefghijklmnolkjihgfeda
12 cbabcdefghijklmnkjihgfedcb
13 ba`abcdefghijklmjihgfedcba
14 a`_^abcdefghijklihgfedcba`
15 `_^]\abcdefghijkhgfedcba`_
16 _^]\[Zabcdefghijgfedcba`_^
17 ^]\[ZYXabcdefghifedcba`_^]
18 ]\[ZYXWVabcdefghedcba`_^]\
19 \[ZYXWVUTabcdefgdcba`_^]\[
20 [ZYXWVUTSRabcdefcba`_^]\[Z
21 ZYXWVUTSRQPabcdeba`_^]\[ZY
22 YXWVUTSRQPONabcda`_^]\[ZYX
23 XWVUTSRQPONMLabc`_^]\[ZYXW
24 WVUTSRQPONMLKJab_^]\[ZYXWV
25 VUTSRQPONMLKJIHa^]\[ZYXWVU
26 UTSRQPONMLKJIHGF]\[ZYXWVUT
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: klmnopqrstuvwxyzcdefghijkl
klmnopqrstuvwxyzcdefghijkl

Enter the code to decrypt: klmnopqrstuvwxyzcdefghijkl
1 lmnopqrstuvwxyzcdefghijklm
2 mnopqrstuvwxyzcdefghijklmn
3 nopqrstuvwxyzcdefghijklmno
4 opqrstuvwxyzcdefghijklmnop
5 pqrstuvwxyzcdefghijklmnopq
6 qrstuvwxyzcdefghijklmnopqr
7 rstuvwxyzcdefghijklmnopqrs
8 stuvwxyzcdefghijklmnopqrst
9 tuvwxyzcdefghijklmnopqrstu
10 uvwxyzcdefghijklmnopqrstuv
11 vwxyzcdefghijklmnopqrstuvw
12 wxyzcdefghijklmnopqrstuvwx
13 xyzcdefghijklmnopqrstuvwxy
14 yzcdefghijklmnopqrstuvwxyz
15 zcdefghijklmnopqrstuvwxyzc
16 cdefghijklmnopqrstuvwxyzcd
17 defghijklmnopqrstuvwxyzcde
18 efghijklmnopqrstuvwxyzcdef
19 fghijklmnopqrstuvwxyzcdefg
20 ghijklmnopqrstuvwxyzcdefgh
21 hijklmnopqrstuvwxyzcdefghi
22 ijklmnopqrstuvwxyzcdefghij
23 jklmnopqrstuvwxyzcdefghijk
24 klmnopqrstuvwxyzcdefghijkl
25 lmnopqrstuvwxyz{defghijklm
26 mnopqrstuvwxyz{|efghijklmn
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: hello hsiao ting
rovvy*resky*fsxq

Enter the code to decrypt: rovvy*resky*fsxq
1 spwwz+sftlz+gtyr
2 tqxxc,tgumc,huzs
3 uryyd-uhvnd-ivct
4 vszze.viwoe.jwdu
5 wtccf/wjxpf/kxev
6 xuddg0xkyqg0lyfw
7 yveeh1ylzrh1mzgx
8 zwffi2zmcsi2nchy
9 cxggj3cndtj3odiz
10 dyhhk4doeuk4pejc
11 eziil5epfvl5qfkd
12 fcjjm6fqgwm6rgle
13 gdkkn7grhxn7shmf
14 hello8hsiyo8ting
15 ifmmp9itjzp9ujoh
16 jgnnq:jukcq:vkpi
17 khoor;kvldr;wlqj
18 lipps<lwmes<xmrk
19 mjqqt=mxnft=ynsl
20 nkrru>nyogu>zotm
21 olssv?ozphv?cpun
22 pmttw@pcqiw@dqvo
23 qnuuxAqdrjxAerwp
24 rovvyBreskyBfsxq
25 spwwzCsftlzCgtyr
26 tqxx{Dtgum{Dhuzs
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: hellohsiaoting
rovvyreskyfsxq

Enter the code to decrypt: rovvyreskyfsxq
1 spwwzsftlzgtyr
2 tqxxctgumchuzs
3 uryyduhvndivct
4 vszzeviwoejwdu
5 wtccfwjxpfkxev
6 xuddgxkyqglyfw
7 yveehylzrhmzgx
8 zwffizmcsinchy
9 cxggjcndtjodiz
10 dyhhkdoeukpejc
11 eziilepfvlqfkd
12 fcjjmfqgwmrgle
13 gdkkngrhxnshmf
14 hellohsiyoting
15 ifmmpitjzpujoh
16 jgnnqjukcqvkpi
17 khoorkvldrwlqj
18 lippslwmesxmrk
19 mjqqtmxnftynsl
20 nkrrunyoguzotm
21 olssvozphvcpun
22 pmttwpcqiwdqvo
23 qnuuxqdrjxerwp
24 rovvyreskyfsxq
25 spwwzsftlzgtyr
26 tqxx{tgum{huzs
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: hello hsiao ting
rovvy*resky*fsxq

Enter the code to decrypt: rovvy*resky*fsxq
1 qnuux¯qdrjx¯erwp
2 pmttw®pcqiw®dqvo
3 olssv­obphv­cpun
4 nkrru¬naogu¬botm
5 mjqqt«mpnft«ansl
6 lippsªlomesªnmrk
7 khoor©knldr©mlqj
8 jgnnq¨jmkcq¨lkpi
9 ifmmp§iljbp§kjoh
10 hello¦hkiao¦jing
11 gdkkn¥gjhdn¥ihmf
12 fcjjm¤figcm¤hgle
13 ebiil£ehfbl£gfkd
14 dahhk¢dgeak¢fejc
15 c\ggj¡cfd`j¡edib
16 b[ffi bec_i dcha
17 aZeehadb^hcbgX
18 VYddgVca]gbafW
19 UXccfUbT\faTeV
20 TWbbeTaS[e`SdU
21 SVaadS`RZd_RcT
22 RUNNcR_QYc^QbS
23 QTMMbQ^PXb]PaR
24 PSLLaP]OWa\OJQ
25 ORKKHO\NVH[NIP
26 NQJJGN[MUGZMHO
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: hellohsiaoting
rovvyreskyfsxq

Enter the code to decrypt: rovvyreskyfsxq
1 qnuuxqdrjxerwp
2 pmttwpcqiwdqvo
3 olssvobphvcpun
4 nkrrunaogubotm
5 mjqqtmpnftansl
6 lippslomesnmrk
7 khoorknldrmlqj
8 jgnnqjmkcqlkpi
9 ifmmpiljbpkjoh
10 hellohkiaojing
11 gdkkngjhdnihmf
12 fcjjmfigcmhgle
13 ebiilehfblgfkd
14 dahhkdgeakfejc
15 c\ggjcfd`jedib
16 b[ffibec_idcha
17 aZeehadb^hcbgX
18 VYddgVca]gbafW
19 UXccfUbT\faTeV
20 TWbbeTaS[e`SdU
21 SVaadS`RZd_RcT
22 RUNNcR_QYc^QbS
23 QTMMbQ^PXb]PaR
24 PSLLaP]OWa\OJQ
25 ORKKHO\NVH[NIP
26 NQJJGN[MUGZMHO
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: hellohsiaoting
rovvyreskyfsxq

Enter the code to decrypt: rovvyreskyfsxq
1 qnuuxqdrjxerwp
2 pmttwpcqiwdqvo
3 olssvobphvcpun
4 nkrrunaogubotm
5 mjqqtmznftansl
6 lippslymeszmrk
7 khoorkxldrylqj
8 jgnnqjwkcqxkpi
9 ifmmpivjbpwjoh
10 hellohuiaoving
11 gdkkngthznuhmf
12 fcjjmfsgymtgle
13 ebiilerfxlsfkd
14 dahhkdqewkrejc
15 czggjcpdvjqdib
16 byffibocuipcha
17 axeehanbthobgz
18 zwddgzmasgnafy
19 yvccfylzrfmzex
20 xubbexkyqelydw
21 wtaadwjxpdkxcv
22 vszzcviwocjwbu
23 uryybuhvnbivat
24 tqxxatgumahuzs
25 spwwzsftlzgtyr
26 rovvyreskyfsxq
>>> 
=========== RESTART: /Users/hsiaotingluv/Desktop/python/20200418 (file).py ===========
Enter the code to encrypt: hellohsiaoting
rovvyrcskydsxq

Enter the code to decrypt: rovvyrcskydsxq
1 qnuuxqbrjxcrwp
2 pmttwpaqiwbqvo
3 olssvotphvapun
4 nkrrunsogurotm
5 mjqqtmrnftqnsl
6 lippslqmespmrk
7 khoorkpldrolqj
8 jgnnqjokcqnkpi
9 ifmmpinjbpmjoh
10 hellohmiaoling
11 gdkknglhdnkhmf
12 fcjjmfkgcmjgle
13 ebiilejfblifkd
14 dahhkdieakhejc
15 c\ggjchd`jgdib
16 b[ffibgc_ifcha
17 aZeehafb^hebgX
18 VYddgVea]gdafW
19 UXccfUdT\fcTeV
20 TWbbeTcS[ebSdU
21 SVaadSbRZdaRcT
22 RUNNcRaQYc`QbS
23 QTMMbQ`PXb_PaR
24 PSLLaP_OWa^OJQ
25 ORKKHO^NVH]NIP
26 NQJJGN]MUG\MHO
>>> 