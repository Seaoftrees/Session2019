# 2019年度 第五回 プログラミング講習会
## 今回の目標
1. 関数が使えるようになる
2. リストが使えるようになる
## おまけ目標
なし

---
# 1.関数が使えるようになる
関数、というと`f(x) = 2x`みたいなものを想像する人が多いは  
これは関数です。そりゃそうだと思うかもしれませんが、この関数は  
> xを代入したら xを二倍にして返す

という関数です。まだそりゃそうだって話ですか。  
では、`g(x) = √x`という関数ならどういう説明になるか。
> xを代入したら、その平方根を求めて返す

という説明です。

## 1.1 標準ライブラリの関数が使えるようになる
実は、Pythonで扱う「関数」もこれと同じようなものです。  
ただ、平方根はそのままでは使えないので、「数学関連の関数使うで！」っていう宣言をしてあげます  
それが`import math`というものです。  
試しに、入力した数の平方根を求めるプログラムを作ってみます。(Githubでは51.pyです)
```py
import math

x = int(input(">> "))

sr = math.sqrt(x)
print(sr)
```
> 解説  
> 1行目に「数学関連の関数使うで！」ってことを宣言します。この`import`系は必ず最初の方に書きます  
> 5行目の`sr = math.sqrt(x)`というところ、これは「mathっていうやつの中のsqrt(x)っていう関数使う」という意味です。  
> そしてその計算結果を`sr`という変数に入れています。

<details>
<summary>え、じゃあsqrt以外もあるの?</summary>
A. あります    
他にも、対数を計算する`math.log(x, base)`だとか、絶対値を計算する`math.fabs(x)`とか色々あります。(詳しく見たい人は[公式](https://docs.python.org/ja/3/library/math.html)見て下さい)
</details>

この、`math.sqrt(x)`こそが、Pythonの関数と言うやつです。だって
> xを代入したら、その平方根を求めて返す

という動作をしているからです。  
そしてこの関数の名前がsqrtという認識で大丈夫です。  

## 1.2 自己定義の関数を作ってみる
自分である関数作りたいときには以下のようにします。  
ここでは`Twice(x) = 2x`という関数を作ってみましょう。  
つまり、関数の名前が「Twice」で、
> xを代入したら、その値を2倍して返す  

という動作をする関数です。(Githubでは52.pyです)  
```py
def Twice(x):
   result = x*2
   return result

n = int(input(">> "))
t = Twice(n)
print(t)
```
このように、`def 名前(引数):`という風に書いてあげます  
> 解説  
> そして:から始まって**インデントの中身**が関数の中身になります。インデントはしっかりしましょう  
`return result`というのは「変数`result`に代入した値を返す」という意味です。  
これがなければ、数字が何も返ってこない関数になっちゃいます。(ただ動作するだけ)   
そして6行目の`t = Twice(n)`というのが「Twiceっていう関数にnを代入する」という動作になっています  

関数の中にいろいろな動作を書き込むことができるので、
> xを代入したら、xを出力する

という関数を作ることもできますし、代入するのがx以外にもyを代入したいなんてこともできます。
```py
def triAve(x, y, z):
   average = (x+y+z)/3
   print("3つの数字の平均は " + float(average))
```
みたいな複雑そうなこともできます。

# 2. リストを使えるようになる
リストってなんやねん。という話から。  
intのリストについてで言うと、「2, 3, 5, 7, 11, 13」という数字(int型のデータ)がいくつか入っているヤツです。  
「じゃあ、intの変数を6つ宣言しとけばええやんけ」と思うかもしれません  
途中から「17を追加したい」とか言われたらどうしましょう。  
Pythonのリストというものは「途中から値を追加する」だとか、「途中である値を削除する」だとか言うことができます。  

上記のものをコードにしてみます。  
あ、`printList(list)`っていう関数は 「listを代入したら中身を出力する」という関数です。 (Githubでは53.pyです)  
```py
def printList(list):
   elements = ""
   for e in list:
      elements += (" " + int(e))
   print(elements)

primes = [2, 3, 5, 7, 11, 13] #これがlistの宣言
printList(primes)

primes.append(17) #最後に17を追加する
printList(primes)
```

つまり、`リストの名前.append(x)`を使ってあげることで追加ができたりします。  
他にも、昇順に並べたいときは 「Python リスト 昇順に並べる」 で検索したり  
リストのある中身(各中身のことを要素といいます)を削除したいときは 「Python リスト 要素の削除」  
などと調べるとでてきます。調べるの大事。  

(これも調べるとでてくることではありますが) 3番目の要素のみ出力したいときは`名前[番目]`を使います  
ここで気をつけなければならないのが「0, 1, 2, ....」とカウントすることです。
上の例でいうと(Githubでは54.py)
```py
primes = [2, 3, 5, 7, 11, 13]
print(primes[2]) #前から3番目の出力
```
となります。  
そして、さっきの`printList`という関数、for文使ってますよね。  
この`for e in list`というもの、「listの中身を前から順番に`e`という変数に代入していく」という動作をしてくれます。  
今何言ってるかわからなくとも、気がつけばこれめちゃくちゃ便利だということがわかります。(へーそんな使い方があるのか。程度でok)  

# さいごに
さて、ここまでで簡易的なプログラミング講習会のチュートリアルが終わります ~~(チュートリアルが大半とか言わないで)~~  
来週から、SlackBOTというものを作っていきます。