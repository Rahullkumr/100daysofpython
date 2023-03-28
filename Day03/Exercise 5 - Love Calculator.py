'''
    A program that tests the compatibility between two people.

To work out the love score between two people:
    Take both people's names and 
    check for the number of times the letters in the word TRUE occurs. 
    Then check for the number of times the letters in the word LOVE occurs. 
    Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
    "Your score is **x**, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:
    "Your score is **y**, you are alright together."
Otherwise, the message will just be their score. e.g.:
    "Your score is **z**."

e.g.
name1 = "Angela Yu"
name2 = "Jack Bauer"

T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
TotalTRUE = 5

L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
TotalLOVE = 3

Love Score = 53(i.e TotalTRUETotalLOVE)

'''

print("Welcome to the Love Calculator!\n")
print("""
             .;;;, .;;;,                   .;;;, .;;;,
        .;;;,;;;;;,;;;;;,.;;;,       .;;;.,;;;;;,;;;;;,;;;.
       ;;;;oOOoOOoOOoOOoOOo;;;. .,. .;;;oOOoOOoOOoOOoOOo;;;;
   .,,.`oOOo'           `OoOOo,;;;;;,oOOoO'          `oOOo;',,.
  ;;;;oOOo'    ,;;;,       `OoOOo;oOOoO'       ,;;;,   `oOOo;;;;
  `;;OOoO'    ;;;'             `OOO'             `;;;   `OoOO;;'
 ,;;,OOoO     ;;                 "                 ;;    OoOO,;;,
 ;;;;OOoO     `;     ,;;.                          ;'    OoOO;;;;
  ``.;OOoO,    `;    ` ;;    .;;. ;; ;; .;;,      ;'   ,OoOO;,''
    ;;;;OOoO,          ;;    ;  ; `; ;' ;..'         ,OoOO;;;;
     ```.;OOoO,        ;,;;, `;;'  `;'  `;;'       ,OoOO;,'''
        ;;;;OOoO,      '    ',  ,                ,OoOO;;;;
         ```,;OOoO,.          ''              .,OoOO;,'''
             ;;;;OOoO,.                    .,OoOO;;;;
              ````,;OOoO,.              .,OoOO;, '''
                  ;;;;;OOoO,.        .,OoOO;;;;
                   `````,;OOoO,.  .,OoOO;,''''
                        ;;;;;OOoOOoOO;;;;;      
                         `````;;OO;;'''''
                              `;;;;'



""")

helpOrNot = input("If you need help, type 'help' else type any letter\n")
if helpOrNot == "help":
  print("""
    To work out the love score between two people:
      Take both people's names and 
      check for the number of times the letters in the word TRUE occurs. 
      Then check for the number of times the letters in the word LOVE occurs. 
      Then combine these numbers to make a 2 digit number.

    e.g.
      name1 = "Angel Yuan"
      name2 = "Jack Bauer"

      T occurs 0 times
      R occurs 1 time
      U occurs 2 times
      E occurs 2 times
      TotalTRUE = 5

      L occurs 1 time
      O occurs 0 times
      V occurs 0 times
      E occurs 2 times
      TotalLOVE = 3

      Love Score = 53
  
  """)
  name1 = input("\nWhat is your name? \n")
  name2 = input("What is their name? \n")
else:
  name1 = input("\nWhat is your name? \n")
  name2 = input("What is their name? \n")

#Write your code below this line 👇
combined_string = name1 + name2
lowercase_string = combined_string.lower()

# check for the number of times the letters in the word TRUE occurs in both names.
t = lowercase_string.count('t')
r = lowercase_string.count('r')
u = lowercase_string.count('u')
e = lowercase_string.count('e')
true = t + r + u + e

# check for the number of times the letters in the word LOVE occurs.
l = lowercase_string.count('l')
o = lowercase_string.count('o')
v = lowercase_string.count('v')
e = lowercase_string.count('e')
love = l + o + v + e

# combine true_count and love_count to form 2 digit number
truelove = str(true) + str(love)
love_score = int(truelove)

if love_score < 10 or love_score > 90:
  print(
    f"\nYour score is {love_score}, \nyou go together like coke and mentos.")
  print("""

            \\                            ___/________
       ___   )           ,  @              /    \\  \\
    @___, \ /         @__\  /\        @___/      \@/
   /\__,   |         /\_, \/ /       /\__/        |
  / \    / @\       / \   (         / \ /        / \\
_/__|___/___/______/__|____\\_______/__/__________|__\__  
  
  """)
elif love_score < 50 and love_score > 40:
  print(f"\nYour score is {love_score}, \nyou are alright together.")
  print("""
  
 
      O      ~O
     <|\     /|\\
      |   ~o/ | \\o    ~o/    _o
      |\  /|  |\ |\   /|      |\\
     / |  / \ |// >   / \    / > 
  
  """)
else:
  print(f"\nYour score is {love_score}. You can be best partners.")
  print("""

                       .,;;x+nxnnnn,,.
                   .;XXHHMM!!%M??!!?MXMX;,
                  ;!X?XXXXdXXTS!!!?MM!HXMX.
               .<!MH@MM??????M88BB8$$MURMM!;
             .!XMM!!!!MMMMXWWW@@H?????R$U?$Xx
            ;!!??!!!!"';!XX?M$$NWX'<:<'??M!R5!;
           <!!!!'' ;;!!!!!!??T$$$$H!!!!!:':`!M!!;
          <!!!!';XH!!!!!!'!!!!XMRT?!!'<'':.  4H!';
         !'''<';X!!!''  ..  `'"TTM%!':<>.XXh .!' <;;
        !! '<''J!!!'  :Xx ! ..:<!!!!!'' X$$5X'</'!!!!
       <'`'''  ''     !!XxL<!H!!!!!!!''X$$$$X:;<X!!!!'
       ' <''      .X! !!>XX'' '!'uuuid$$$$$5P:?M!>!-'
      '!!''`  .id$d5XL`X%!?XsuJJ$$$$F????XX!`<!'!'';>));<!!!!;;-.
      ':''.<X55$$$$$X!:!!Xd3$$$$$$$$X-x> `!'    .;!!?;;<XXX!!!!!!!:
       .;!XX5$$$$$$$X?!!HX$$$$33X$$$F;,,;!"    :);,,,`''<!!!!!!!!!!!:.
  :sL :!XXXd$$$$$$$$F'!!X53XXX3JJJXSX!XXX    <:JX$$$$$$o.';<<!XX!!X!!!!
 xX$3`!5$$55$$$$$$$5!`!!3$$3333X??SX!XX$!   .XYX$$$$$$$$$h <;<!!?!!!!X!!
'!X3$%<555XX55$$$$$!!:`!?X$3XXt3$3XXL?"?>  'XF""?$$$$$$$P"!!!!);<!!!XXX!h
X.XX3X,?dXXXdd$55$XX!!!.!!XXXdX?<"?X!' ,uuc$$f:h;?$$$$C" :!!XHXX!;!X!!HX!.
fX!X%''<??HX5X5ddXXbi:''`!!X$$X!h; "'  ?3$$$C.`?t$$$$$!``!!?XHHX!!;;t!XH!!
:'''sL'i `X555$5X??X?`    `!X$dXf"    =JUX3$$$$$$$$$$$$r `!?!!!!!!!!!X!!!!
; 'c`$ $b:`XX$$5!!'`       `'??'    .'??$33$$$$$$$$$$$$ :,:,)!':':'!<!)!!!
's $:?k`$L:`!X5!:<!     :          xx)Xx3$3$$$$$$$$$$C ''!!!!XXXXX!!!!!!!!
 4,?h`$ ?$ :!?XXX'     '!<::.     `X$$$$2$$$$$$$$$$$$L. < `!!!!!??!!!!!!!X
.`b'$,$h`$h .!XRXX!.  ' !X5HX!,    `"?T?$$$$$$$$$$$$5d":>` ::`'"!!!!!!!XXH
>`$`$h`$L?$h`'XXXdXX  '-!55$XXXHx:     `'"?5$$$$$5??$bh?)h>~ <!!:.`'!!!!??
! XF)$i$$$$$.<%X$$X!   :XXX$$$$55XX:.   );,(((()idX3u.?(:    ;!!!!!:<<(:<!
X !$X$$$$$$$F!`X$$5!  >X!555$$$$$$XX!:  !X5$J5X$$$$$$$$X':;:;;!!!!!XX;!X!;
$.`33X$$$$$$b!>!X5X .<U5$5$$$$$$$$$$hX: `X$$$$$$$$?????".:;!!;;!XXX!!?;!H!
d! X$$$$$$$5f'L!!?' !JJ$$$$$$5$$$$$$$X! '!X$2??,xndMMMMr'::!!!<!X!?!?X!;?!
X!:?3$$$$$$5fxX`!' <X55$$$$$$$XXX5X5X!!  `?;nHMMMMMMMMMF::;!!!!;;!!;!!XXt;
?U! "X$$$$$X !T'' X5$$$$$5$$$5XXXXX!!''.nMMMMMMMMPP")JWx :;!!X<!;:!!;!XHH1
X!.. <XF",e ecc: <X6X$$5$$$$$55X!!`,xnMMMMMMPP))ndMMMMMM:`:;!XX!!)<!?!!HH5
!!X' .,xdP";$$$;<ST5$55$$$$$$$$5! 4MMMMMP?)ndMMMMMMMMMMMMx :;!XX!!;!!!!XHH
!',xW$$P",??",uu,"$555XX$$5$$??!' `P"(xdMMMMMMMMMMMMMMMMMMh :;!!!!!'!/!?X!
  !$$$$znsd$$$P"` ?XX?XXS9$555?'  :nMMMMMMMMMMMMMMMMMMMMMMMh `;!!!X!:!!!H!
 <H$$$5X$$$$Xud8$$ ?Xd5$$X?T?'',mMM?MMMMMMMMMMMMMMMMMMMMMMMMX ;!:X?!%`!!!!
.!X$$$$$$$5$X$P"',.`?Xd??!" uXbXnmnMMMMMMMMMMMMMMMMMMMMMMMMMM>:<;<!!X!:!!'
!!XX$$$$X$$d$ndd$P" !!?!':MMMMMMMMMMMSMMMMMMMMMMMMMMMMMMMMMMM> `;:!!H!!:!'
!!X$X$$$$$$U$$F",yc <'':MMMMMMMMMM2MMMMMMMMMMMMMMMMMMMMMMMMMM>`;:;;!!!!!;'
!!X$$$$$$$$$$$$P?"" .xMMMMMMMHMCMMMMMMSMMMMMMMMMXMMMMMMMTMMMM'.:;::'''''''
!??$$$$$$$P'`..nnMMxMMMMMMHMMMMMMM?XMMMMMMMSXHMMMMMMNHHUWMMMM :(;;''!!'''
!!!>>>'`..nnMMMMM)MMMMMMhMMMMMMSHMMMMMMSHHMMMMMMM2HXWSMMMMMMM `'''`'
      nHMMMMMMM?dMMMMM!MMMMTXMMMMMSXMMMMMMMMMNTX5XSMMMMMMMMMM
`. .  MMMMMMMP)MMMMMMXMMMMMMMMMSMMMMMMMMMT?!XXHMMMMMTMMMMMMM!
;:  . !MMMMMMXMMMMHMMMMMMMMHSMMMMMMMMM?!XX!M?!XXHWMMMMMMMMMMf
,;.`  `?MMMF(MMMMMMMMMMMHSMMMMMMM?!XX!M?XXHHMMMMMMMMMMMMMMMM
;:.:  . ` ''!?MMMMMMMMHMMMMMP?!X!??XX!!?????!?MMMUMMMMMMMMMP
;.:;  ..`    ~?MMMMMHMMM"())n!SX!!??!!XXHHMHMMMMMMMMMMMXMMM'
;;`.`   . `.   `?T""!)!+MSM!!??!!!!?"?""<'!SMMMMMMM?MMHMMMM
;;,;:`,: .:  .`  -=""'?""````  ..::::)X!!!xn2MMMMMMMMPSTTPT  
  
  """)
