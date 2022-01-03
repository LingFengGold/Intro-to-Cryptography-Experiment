

# Lab 01 (2 hrs): Programming Basics

### Program 1: Type Hint, String, Bytes, Hex, Base64

In this program, you are required to learn basic concepts of Python 3.

Type hints is a feature to specify the type of a variable, which is useful for write correct codes. In all lab assignments, you are **required** to write Python 3 code with type hints feature. Recall that you are required to use **at least** Python 3.10, otherwise you might suffer from issues brings by type hints as PEP 563 has not become the default option until Python 3.10.

Your programs does the following:

- Read a byte array from the console input, where the byte array is expressed as a hex string (`str`). The console input is:

  ```txt
  deadbeef
  ```

- Decode the hex string as the byte array (`bytes`)

- Print each byte in the byte array as a decimal integer, with a space as the separator, i.e.:

  ```python
  def output_bytes(in_bytes:bytes):
      for ch in in_bytes:
          print(ch, end=' ')
      print()
  ```
  
- Print each byte in the byte array as a hexadecimal integer, with a space as the separator

- Encode the byte array as a Base64 string(`str`), and output the string

- Read another byte array from the console input, where the byte array is expressed as a hex string (`str`). The console input is:

  ```txt
  6465616462656566
  ```

- Decode the hex string as the byte array (`bytes`)

- As the decoded byte array **happens to be** a UTF-8 (or, ASCII) encoded bytes, decode the byte array to the text string(`str`):

  ```python
  def decode_utf8(in_bytes:bytes)->str:
      return in_bytes.decode('utf-8')
  ```

- Print the decoded text string

In your `readme.pdf` file, apart from the general information, it should include:

- A figure representing the relationship between all the variables in your program with type `bytes` and `str`. Example here:

  ![](Lab01-Fig-1.png)

  The figure above is corresponding to the following code.
  
  ```python
  first_hex:str = input()
  first_bytes:bytes = bytes.fromhex(first_hex)
  ```

# Lab 02 (4 hrs): Classical Cryptography

## Part 1 (3 hrs): 

### Program 1: Vigenère cipher (on alphabet string)

In this program, you are required to implement the Vigenère cipher algorithm from scratch, to encrypt and decrypt for alphabet string. The encrypt and decrypt method should be pure functions, i.e. without side effects.

Your program does the following:

- Read an alphabet string from the console input, where the string is only consisting of 26 uppercase letters (A-Z). The first string represents the plaintext.
- Read the second alphabet string. It is ensured that the length of second alphabet string is the same with the first string. The second string represents the key.
- Encrypt the plaintext with the key.
- Print the ciphertext alphabet string.
- Decrypt the ciphertext with the key.

#### Example Input & Output

Input:

```txt
ABCDEFG
ABCDEFG
```

Output:

```txt
ACEGIKM
ABCDEFG
```

### Program 2: Columnar transposition (on alphabet string)

http://rumkin.com/tools/cipher/coltrans.php

A columnar transposition, also known as a row-column transpose, is a very simple cipher to perform by hand. First, you write your message in columns.  Then, you just rearrange the columns.  For example.  I have the message, `Which wristwatches are swiss wristwatches`.  You convert everything to upper case and write it without spaces.  When you write it down, make sure to put it into columns and number them.  Let's use five columns.

|               | Unencoded     | Rearranged    |
| ------------- | ------------- | ------------- |
| **Column #:** | **4 2 5 3 1** | **1 2 3 4 5** |
|               | W H I C H     | H H C W I     |
|               | W R I S T     | T R S W I     |
|               | W A T C H     | H A C W T     |
|               | E S A R E     | E S R E A     |
|               | S W I S S     | S W S S I     |
|               | W R I S T     | T R S W I     |
|               | W A T C H     | H A C W T     |
|               | E S           | S E           |

Now, you just read the columns down in the order that you number them. Above, you will see the key is `4 2 5 3 1`, which means you write down the last column first, then the second, then the fourth, the first, and finally the middle.  When you are all done, you will get `HTHESTHHRASWRASCSCRSSCWWWESWWEIITAIIT`. 

Your program does the following:

- Read an integer from the console, representing the column count. In the example above, the count is `5`.
- Read the encryption key, i.e. the order of columns, separated by space. In the example above, the key is `4 2 5 3 1`.
- Read the plaintext string in one line. In the example above, the plaintext is `WHICHWRISTWATCHESARESWISSWRISTWATCHES`.
- Perform the columnar transposition.
- Print the ciphertext string. In the example above, the ciphertext is `HTHESTHHRASWRASCSCRSSCWWWESWWEIITAIIT`.

#### Example Input & Output

Input:

```txt
5
4 2 5 3 1
WHICHWRISTWATCHESARESWISSWRISTWATCHES
```

Output:

```txt
HTHESTHHRASWRASCSCRSSCWWWESWWEIITAIIT
```

## Part 2 (1 hrs):

### Program 3: Vigenère cipher (on bytes)

In this program, you are required to extend the Vigenère cipher (on alphabet string) to bytes, in order to encrypt arbitrary data on the computer.

Your program does the following:

- Read a hex string from the console input. The first string represents the plaintext bytes as a hex string. Remember that you need to decode the hex string into bytes.
- Read a hex string from the console input. The second string represents the encryption key bytes as a hex string.
- Encrypt the plaintext with the key.
- Print the ciphertext bytes as a hex string.
- Print the ciphertext bytes as a Base64 string.

From now on, the alphabet string is deprecated. Cryptography methods, such as encryption and decryption, operates on bytes.

#### Example Input & Output

Input:

```txt
abcd
abcd
```

Output:

```txt
569a
Vpo=
```


# Lab 03 (4 hrs): Symmetric Encryption

## Part 1 (1 hrs):

### Program 1: 3DES

In this program, you are required to implement the 3DES algorithm using the provided encrypt and decrypt function of DES. The encrypt and decrypt method of 3DES should also be pure functions, i.e. without side effects.

Your program does the following:

- Read a hex string from the console input. The string represents the plaintext bytes as a hex string.

- Read a hex string from the console input. The string represents the first key bytes as a hex string.

- Read a hex string from the console input. The string represents the second key bytes as a hex string.

- Read a hex string from the console input. The string represents the third key bytes as a hex string.

- Encrypt the plaintext with the three keys.

- Print the ciphertext bytes as a hex string.

- Decrypt the ciphertext with the three keys.

- Print the plaintext bytes after decryption as a hex string.

#### Example Input & Output

Input:

```txt
8787878787878787
133457799bbcdff1
0e329232ea6d0d73
133457799bbcdff1
```

Output:

```txt
e98a0b8e59b3eeb7
8787878787878787
```


## Part 2 (3 hrs):

### Program 2: AES

**Modes of operations** allow you to encrypt more data than the block size of your symmetric block cipher. Example: `CBC`.

In this program, you are required to demonstrate the `AES-256-CBC` algorithm **with a third-party crypto library**, `pycryptodome`. Recall that you must provide a corresponding `requirements.txt` file if any third party libraries are involved in the code.

Your program does the following:

- Read a text string from the console input.
- Encode the text string with `utf-8` encoding, as the plaintext bytes.
- Pad the plaintext bytes with `pkcs7` algorithm.
- Print the padded bytes as a hex string.
- Read a Base64 string from the console input. The string represents the key bytes as a Base64 string. If the length of key bytes is not expected, abort the program with a Python code `raise Exception('key length mismatch')`
- Read a Base64 string from the console input. The string represents the IV bytes as a Base64 string. If the length of IV bytes is not expected, abort the program with a Python code `raise Exception('IV length mismatch')`
- Encrypt the padded plaintext bytes with the key and IV.
- Print the ciphertext bytes as a Base64 string.
- Decrypt the ciphertext bytes with the key and IV.
- Unpad the decrypted plaintext bytes with `pkcs7` algorithm.
- Print the unpadded bytes as a hex string.
- Decode the unpadded bytes with `utf-8` encoding, and print the decoded text string.

#### Example Input & Output

Input:

```txt
I don't like deadbeef. 你呢？
1UO7ZnmwcT7KtScS2hAZV+aZ1Gk95HPK1EqcXT6rqoU=
6GXIzJ0GD/76WkTtgmaDYQ==
```

Output:

```txt
4920646f6e2774206c696b652064656164626565662e20e4bda0e591a2efbc9f10101010101010101010101010101010
c0LWy2BUg949eMO+G8NgxUzKVNNFys8EzavYFhP0Tc/mZM/UVVe4E3b34cEyu1Ze
not identical
4920646f6e2774206c696b652064656164626565662e20e4bda0e591a2efbc9f
I don't like deadbeef. 你呢？
```

Note: the first line of the example input is consisting of the following 26 characters:

| I    |      | d    | o    | n    | '    | t    |      | l    | i    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| k    | e    |      | d    | e    | a    | d    | b    | e    | e    |
| f    | .    |      | 你   | 呢   | ？   |      |      |      |      |


# Lab 04 (4 hrs): Public Key Encryption

## Part 1 (2 hrs):

### Program 1: Textbook RSA (on group)

Note: **group** as in group theory. You are not allowed to finish your work in group.

In this part, you are required to implement the textbook RSA algorithm from scratch. It contains the following three procedures, KeyGen, Encrypt, and Decrypt.

- KeyGen
  - Return the private key $(N,d)$ and the corresponding public key $(N,e)$. The prime number $p$ and $q$ should be approximately 512 bits and therefore the RSA modulus number $N$ should be approximately 1024 bits. Note that finding an encryption exponent $e$ might be time-consuming.
- Encrypt
  - Given a plaintext message $m \in \mathbb{Z}_N$ and a public key $(N,e)$, return the encrypted message $c$.
- Decrypt
  - Given a ciphertext message $c \in \mathbb{Z}_N$ and a private key $(N,d)$, return the decrypted message $m^\prime$.

Your program does the following:

- Generate a textbook RSA key pair. You may use the **Miller-Rabin Test** algorithm to determine whether an integer is prime. Print the private key and the public key as multiple decimal strings.
- Read a decimal string representing a plaintext message $m$. Raise an exception if $m$ is invalid.
- Encrypt the message $m$. Print the encrypted message $c$ as a decimal string.
- Decrypt the encrypted message $c$. Print the decrypted message $m^\prime$ as a decimal string.
- If you think the textbook RSA algorithm is secure, print `secure`. Print `insecure` otherwise.

Note that in this program, you may only include third-party codes or libraries for:

- **Miller-Rabin Test**
- **Extended Euclidean Algorithm** 

Recall that including any third-party codes without claiming is considered as lack of academic integrity, and results in failing this course.

#### Example Input & Output

Input:

```txt
34862844108815430278935886114814204661242105806196134451262421197958661737288465541172280522822644267285105893266043422314800759306377373320298160258654603531159702663926160107285223145666239673833817786345065431976764139550904726039902450456522584204556470321705267433321819673919640632299889369457498214445
```

Output:

```txt
Private key:
N: 72480887416135972061737686062889407161759160887103574047817069443537714713215543172947835307344891172810092267953794611202591069661157992794959838750479208506005687981686025809332691431473809292764988868581099330149458758861391108410825625141738698507086062910615219209815042032904395035912581683751821198857
d: 32680572261276319950892386078453159129961789301515586779730994965995850002546722461272347997633819895532355760655076469284315213156424132333399966484423792583164625536594707257030835906698882316535262007407891728303620471604461013849133230965147690242465484589704113381685121927918786879123393719930911981301
Public key:
N: 72480887416135972061737686062889407161759160887103574047817069443537714713215543172947835307344891172810092267953794611202591069661157992794959838750479208506005687981686025809332691431473809292764988868581099330149458758861391108410825625141738698507086062910615219209815042032904395035912581683751821198857
e: 33917284234023552492304328018336609591997179645740843023623954792230653601864281593260663435095146463818240660159742130550887732511002455913550343095875105353898810744096024635824071115264943251609500722062745618030825015239681817073644641294390347390699708726562812289026328860966096616801710266920990047581
Ciphertext:
c: 15537860445392860627791921113547942268433746816211127779088849816425871267717435366808469771763672942339306019626033112604790279521256018388004503987281369444308463737059894900987688503037651823759352061264031327006538524035092808762774686406194114456168335939404457164139055755834030978327226465998086412320
Plaintext:
m': 34862844108815430278935886114814204661242105806196134451262421197958661737288465541172280522822644267285105893266043422314800759306377373320298160258654603531159702663926160107285223145666239673833817786345065431976764139550904726039902450456522584204556470321705267433321819673919640632299889369457498214445
insecure
```

## Part 2 (2 hrs):

### Program 2: ElGamal (on group)

In this part, you are required to implement the ElGamal algorithm from scratch. It contains the following three procedures, KeyGen, Encrypt, and Decrypt.

- KeyGen
  - Return the private key $(p,\alpha,a)$ and the corresponding public key $(p,\alpha,\beta)$. The prime number $p$ should be approximately 512 bits. Note that finding a primitive root $\alpha$ in $\mathbb{F}_p$ might be time-consuming.
- Encrypt
  - Given a plaintext message $m \in \mathbb{F}_p$ and a public key $(p,\alpha,\beta)$, return the encrypted message $(r,t)$ and the secret key $k$.
- Decrypt
  - Given a ciphertext message $(r,t)$ and a private key $(p,\alpha,a)$, return the decrypted message $m^\prime$.

Your program does the following:

- Generate a private key and the corresponding public key. You may use the **Miller-Rabin Test** algorithm to determine whether an integer is prime. Print the private key and the public key as multiple decimal strings.
- Read a decimal string representing a plaintext message $m$. Raise an exception if $m$ is invalid.
- Encrypt the message $m$. Print the encrypted message $(r,t)$ as multiple decimal strings.
- Decrypt the encrypted message $(r,t)$. Print the decrypted message $m^\prime$ as a decimal string.

Note that in this program, you may only include third-party codes or libraries for:

- **Miller-Rabin Test**
- finding a primitive root modulo prime p

Note: you are not allowed to use **Extended Euclidean Algorithm** in this program.

#### Example Input & Output

Input:

```
4137696876930090267522398697653550193405311689664069574322834683213199126531348263326633721504049779673544721298253021191958429503842792929508773630980912
```

Output:

```txt
Private Key:
p: 11483166658585481347156601461652228747628274304826764495442296421425015253161813634115028572768478982068325434874240950329795338367115426954714853905429627
alpha: 9312361210673900259563710385567927129060681135208816314239276128613236057152973946513124497622387244317947113336161405537229616593187205949777328006346729
a: 3101984266868748920462287182124446696068493916489350126886947863612185839382696504960710290519388739925364867918988436503372297381505951416202859274461749
Public Key:
p: 11483166658585481347156601461652228747628274304826764495442296421425015253161813634115028572768478982068325434874240950329795338367115426954714853905429627
alpha: 9312361210673900259563710385567927129060681135208816314239276128613236057152973946513124497622387244317947113336161405537229616593187205949777328006346729
beta: 1159968293290431483618624548862401630355209517151486248093696597103338439113317368321706438200804727461211332263913961450514008706205896803328741922554539
Ciphertext:
r: 4270390275647605104323112550114089020700231211424317817144932009272298324070546918004125267551309710095448806447104314957099856583975262276729327418983805
t: 3221108136460372613636905604674169025183939828688657275543956232356097903511339858673306464341986911484482234789310340929730245929110146334280736926494309
Plaintext:
m': 4137696876930090267522398697653550193405311689664069574322834683213199126531348263326633721504049779673544721298253021191958429503842792929508773630980912
```

# Lab 05 (2 hrs): Key Exchange

### Program 1: Diffie–Hellman key exchange (on group)

In this part, you are required to implement the Diffie–Hellman key exchange algorithm in $\mathbb{Z}_p$ from scratch. (Hint: review the procedure of ElGamal algorithm). As the Setup procedure is the same as ElGamal algorithm, it is assumed that the public parameters of $p$ and $\alpha$ are both set to constants in this part.

```txt
p: 11483166658585481347156601461652228747628274304826764495442296421425015253161813634115028572768478982068325434874240950329795338367115426954714853905429627
alpha: 9312361210673900259563710385567927129060681135208816314239276128613236057152973946513124497622387244317947113336161405537229616593187205949777328006346729
```

In this program, two parties, Alice and Bob, want to get a symmetric key for future symmetric encryption via Diffie–Hellman key exchange, and hope that adversaries learn nothing about the shared symmetric key. In this program, it is assumed that only Honest-but-Curious adversaries exist.

Your program will output the following items:

- All the transmission data on the communicate channel (in correct order, if necessary), e.g. `Alice to Bob: blah blah blah`.
- The symmetric key that Alice gets, that is the result of Diffie–Hellman key exchange.
- The symmetric key that Bob gets, that is the result of Diffie–Hellman key exchange.

**Example Output**

```txt
Alice to Bob: 8940959903919892646369383076988236263414149283589789417534093823879702643730138301746710316972043367005133179322397075568692734123174632487566957931486431
Bob to Alice: 4384683352873557635562368964248068727038294529254597987180258684651520296204501642442796366842225710992904070529210926322430373646688781391733323295711438
Result (Alice view): 11340178546045069617516325240966622435238310460224925781433563012664618800006804703149537436309299281476260328893892580363729101975655852342449233799172983
Result (Bob view): 11340178546045069617516325240966622435238310460224925781433563012664618800006804703149537436309299281476260328893892580363729101975655852342449233799172983
```

# Lab 06 (4 hrs): Signature

## Part 1 (2 hrs):

### Program 1: Textbook RSA (on group)

In this part, you are required to implement the textbook RSA algorithm for signing from scratch. The signing procedure is quite similar with encryption, but you should not be confused with them. It contains the following three procedures, KeyGen, Encrypt, and Decrypt.

- KeyGen
  - Same as Lab 04.
- Sign
  - Given a plaintext message $m \in \mathbb{Z}_N$ and a private key $(N,d)$, return the signature $s$.
- Verify
  - Given a plaintext message $m \in \mathbb{Z}_N$, the signature $s$, and a public key $(N,e)$, check whether the signature is valid or not.

Your program does the following:

- Generate a textbook RSA key pair. Print the private key and the public key as multiple decimal strings.
- Read a decimal string representing a plaintext message $m$. Raise an exception if $m$ is invalid.
- Sign the message $m$. Print the signature $s$ as a decimal string.
- Verify the signature $s$ of message $m$. Print `valid` if the signature is valid. Print `invalid` otherwise.
- Randomly pick a number as a faked message $m^\prime$, and verify the signature $s$ of message $m^\prime$. Print `valid` if the signature is valid. Print `invalid` otherwise.
- Randomly pick a number as a faked signature $s^\prime$, and verify the signature $s^\prime$ of message $m$. Print `valid` if the signature is valid. Print `invalid` otherwise.

Note that in this program, you may only include third-party codes or libraries for:

- **Miller-Rabin Test**
- **Extended Euclidean Algorithm**

**Example Input & Output**

Input:

```txt
34862844108815430278935886114814204661242105806196134451262421197958661737288465541172280522822644267285105893266043422314800759306377373320298160258654603531159702663926160107285223145666239673833817786345065431976764139550904726039902450456522584204556470321705267433321819673919640632299889369457498214445
```

Output:

```txt
Private key:
N: 60578014255102269896133371904627262317416253087521326961353447386111108220456127698087451094233400895389904195033258942460533045725424252051031082346623918833115880605331217845541371778050413570487118811797680786863916249631173243202415281126677535724142072672389239932425514746354116788337452709735978693441
d: 29794267204372868920195293823377577521348286669753768926422253485197790892996900859124258444603569195973796199037022534122349660497314477050901363975617785986341374781520104383687018770714375371190852092718547427166813248293087229107819441125188332290624176181241072609675470769160255268721140521999754996495
Public key:
N: 60578014255102269896133371904627262317416253087521326961353447386111108220456127698087451094233400895389904195033258942460533045725424252051031082346623918833115880605331217845541371778050413570487118811797680786863916249631173243202415281126677535724142072672389239932425514746354116788337452709735978693441
e: 50236051684532724158959956908047535011547027752807918443381101532977239879805272363541815186678432878182913685573432227040470122555922161989827750747871310928207045877463632837569381571438481188390948780929921154288163100313907723263741344747325268803766335694293737307011671572842257344517928948772977494407
Signature:
s: 34580775293086014798734721087900779255336448150833662767477345836086991760074172833491041507919156367652845778336488884879942244053190133044473935740553882083350076369679814132582396981838752038660178872674779525999874634128284351865411689078895902069902392417208340043916976695929474980926586642060201969134
Verify s of m:
valid
m' (faked): 50450048059881262533055051783615244680711671489653790401184574597060270328158473249590629579575748444416670136818805407617798193709438157542915258506987898524296742253334657876701634724978818355153836962043088167025161694157068501323069379606742460252729290661161539614496733300584141680283224222741900536312
Verify s of m':
invalid
s' (faked): 28243222593155363957786267188064169499833133908722962853038127116797113724411953085666999176421008597106689088871876968450636497620934133534312574374692406966037865626499421933604018821681836276566498093397822394074799560633387005572367768063152314140663154660143389779133176949492679329809464448869998812303
Verify s' of m:
invalid
```

## Part 2 (2 hrs):

### Program 2: ElGamal (on group)

In this part, you are required to implement the ElGamal algorithm for signing from scratch. It contains the following three procedures, KeyGen, Encrypt, and Decrypt.

- KeyGen
  - Same as Lab 04.
- Sign
  - Given a plaintext message $m \in \mathbb{F}_p$ and a private key $(p,\alpha,a)$, return the signature $(r,s)$.
- Verify
  - Given a plaintext message $m \in \mathbb{F}_p$, the signature $(r,s)$, and a public key $(p,\alpha,\beta)$, check whether the signature is valid or not.

Your program does the following:

- Generate a private key and the corresponding public key. Print the private key and the public key as multiple decimal strings.
- Read a decimal string representing a plaintext message $m$. Raise an exception if $m$ is invalid.
- Sign the message $m$. Print the signature $(r,s)$ as multiple decimal string.
- Verify the signature $(r,s)$ of message $m$. Print `valid` if the signature is valid. Print `invalid` otherwise.
- Randomly pick a number as a faked message $m^\prime$, and verify the signature $(r,s)$ of message $m^\prime$. Print `valid` if the signature is valid. Print `invalid` otherwise.
- Randomly pick numbers as a faked signature $(r^\prime,s^\prime)$, and verify the signature $(r^\prime,s^\prime)$ of message $m$. Print `valid` if the signature is valid. Print `invalid` otherwise.

Note that in this program, you may only include third-party codes or libraries for:

- **Miller-Rabin Test**
- finding a primitive root modulo prime p
- **Extended Euclidean Algorithm**

**Example Input & Output**

Input

```txt
4137696876930090267522398697653550193405311689664069574322834683213199126531348263326633721504049779673544721298253021191958429503842792929508773630980912
```

Output

```txt
Private Key:
p: 7623676177142273666176960941160763267715363061271226168423102803703307888568083070768414734233175022763592082166829461334117317633004076503299319393933531
alpha: 4852157426089893935411617364720859800493089641146556442371879299424783880014557103402720169349703681228223731146566716914079006206076028164786870639438634
a: 3378999248556716821986051126236329620786292051032565251155929677736759564488623249788309621451301313648501424873153999478194379023701985528788334198300666
Public Key:
p: 7623676177142273666176960941160763267715363061271226168423102803703307888568083070768414734233175022763592082166829461334117317633004076503299319393933531
alpha: 4852157426089893935411617364720859800493089641146556442371879299424783880014557103402720169349703681228223731146566716914079006206076028164786870639438634
beta: 900191922914835354062391486383477573543038624757518577920766087560733127924139275266000620349618745988286788581537670898557439116232221539792308522703996
Signature:
r: 6319172751757190059617527527206702628329370565289520380207782237638117089626184819108054497002450108714662052571938062244969670733303628072961698241980976
s: 4487722435787272797267428160768266252523442175017409508193970626399238483647311021229856082277095824456827558298764078442861955288380137538351154715433474
Verify (r,s) of m:
valid
m' (faked): 3794592956927179165727339787771495164761281462584199354337653233001069555811671313157589195265413704693831537814309912166154940955900923275208659567603551
Verify (r,s) of m':
invalid
r' (faked): 3159232051056019432416597255218241709553275595410987553313618304348446526218613835913933078438390905736100418385914557962667666159701449384865696308181869
s' (faked): 6724747854387400941199482927499544178640823360059844483666200355270210965256010155751083409193280897361331961705674904878262224584821396243969282511950802
Verify (r',s') of m:
invalid
```



# Lab 07 (4 hrs): Hash

## Part 1 (2 hrs):

### Program 1: Regular hash algorithms

In this program, you are required to invoke the `md5` and `sha256` algorithms that are implemented in `hashlib` build-in library. Your program does the following:

- Read the input byte array as a hex string.
- Output the md5 digest of the input, as a hex string.
- Output the md5 digest of the input, as a Base64 string.
- Output the sha256 digest of the input, as a hex string.
- Output the sha256 digest of the input, as a Base64 string..

**Example Input 1**

```txt
d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70
```

**Example Output 1**

```txt
MD5 digest of the input:
79054025255fb1a26e4bc422aef54eb4
eQVAJSVfsaJuS8QirvVOtA==

SHA256 digest of the input:
8d12236e5c4ed9f4e790db4d868fd5c399df267e18ff65c1107c328228cffc98
jRIjblxO2fTnkNtNho/Vw5nfJn4Y/2XBEHwygijP/Jg=
```
**Example Input 1**

```txt
d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70
```

**Example Output 2**

```txt
MD5 digest of the input:
79054025255fb1a26e4bc422aef54eb4
eQVAJSVfsaJuS8QirvVOtA==

SHA256 digest of the input:
b9fef2a8fc93b05e7701e97196fda6c4fbeea25ff8e64fdfee7015eca8fa617d
uf7yqPyTsF53Aelxlv2mxPvuol/45k/f7nAV7Kj6YX0=
```


### Program 2: HMAC

In this program, you are required to invoke the `scrypt` algorithms that are implemented in `hashlib` build-in library. Your program does the following:

- Read the plaintext password as a text string
- Encode the password into byte array, with `utf-8` encoding
- Read the salt byte array as a hex string
- Invoke the `scrypt` method with parameters $n=4$, $r=8$, $p=16$
- Output the result byte array as a hex string

**Example Input**

```txt
Thi$ i$ my passw0rd!
477d15cb740ca1da08f6d851361b3c80
```

**Example Output**

```txt
fd5963b9e6905d36ca8d00e3a740a3ab7a40b3d60237b6f2ed3025eee770f2d71bc95ba3e98265bea4308250d02f0e10bb78e710d9f0ef7ae9a4fa52a0818d27
```

## Part 2 (2 hrs):

### Program 3: Password store and verification

In this part, you are provided with a Python program file, simulating an authentication server. You should implement the unfinished parts, so that adversaries that cracked into the database will not get the user's plaintext password.

**Warning:** the Chinese translation of word `login`(or `log in`, `log on`) is `登录`(or `登入`). If you misspelled the word as `登陆` in any submission files, you will lose **all** the credits in this part.

# Lab 08 (8 hrs): Group Project

Note: group as in group of people.

## Option 1 (solo project): DIGEST authentication in real scene (sdu_net)

Re-implement an sdu_net client for the digest authentication of SRUN3000. The source code of a demo client [sdunetd](github.com/SadPencil/sdunetd) is provided.

SDU-Jinan (wireless network only): http://202.194.15.87/
SDU-Qingdao (both wired and wireless network): http://101.76.193.1/

## Option 2 (solo project): implement AES from scratch

Implement the standard `AES-128-CBC` algorithm **from scratch**. You are not allowed to use any third-party libraries or crypto modules.

## Option 3 (group project of 2 students): hs-airdrop

Read the source code and write a documentation about how the Handshake Airdrop works. A valid ssh key pair is provided for claiming the airdrop.

The program and the encrypted data are as follows:

https://github.com/handshake-org/hs-airdrop

https://github.com/handshake-org/hs-tree-data

An ssh key pair is already attached with this document.

## Option 4 (group project of 2 students): Ethereum and smart contract demonstration

Get the official Ethereum client, and run a **private** network with your own genesis file. Then, write a smart contract with the Solidity language, and deploy the contract into the private network. The smart contract is to construct a simple decentralized lottery platform, where the only trusted party is the random seed generator, who uploads the random seed. The contract should be written from scratch, but you may re-use any source code that exists on the Internet, as long as you specify the source. Demonstrate how to interact with the contract.

## Option 5 (group project of 2 students): simple zero-knowledge proof demonstration

Get [xJsnark](https://github.com/akosba/xjsnark), a high-level zk-SNARKs framework. Select and run at least three examples (*circuits*) that comes with xJsnark, and answer the following questions:

- What the circuit does
- Which variables are visible to the prover, and which are not
- A situation that is suitable for applying the circuit

Finally, write your own circuit for demonstration, and answer the above questions, too. You may re-use any source code that exists on the Internet or comes with xJsnark, as long as you specify the source. 
