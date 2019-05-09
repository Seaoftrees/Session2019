# 2019年度 第1回 プログラミング講習会
## 今回の目標
1. Bash on Ubuntuのインストール
2. Bash on UbuntuのセットアップとPythonのインストール
3. [Visual Studio Code](https://azure.microsoft.com/ja-jp/products/visual-studio-code/)のインストール
   * 別に他のヤツ使っても構わんよ? ([Atom](https://atom.io/)とか[PyCharm](https://www.jetbrains.com/pycharm/)とか)
4. Visual Studio Code(以下VS Code) の設定
   * VS Code の拡張機能で「Python」とか言うのを入れる
5. この講義で使うフォルダーの作成
6. Python3 (以下Python)で「Hello, World!」を出力する

## おまけ目標
 * Pythonを用いて電卓代わりに計算してみる
   * 欲を言うと+, -, *, /, //, %がわかるレベルに

## 諸注意
この講義はOSがWindows10(Japanese)であるということを前提に行っています。  
他OS(Windows7, MaxOS, Linux, Sorarisとか)使ってる人はGoogle先生と根性で何とかしてください

---
## 1. Bash on Ubuntuのインストール
### 1.1 Ubuntuのインストール
左下のスタートボタンから「Microsoft Store」を調べて起動する  
右上の検索欄に「Ubuntu」と入れて検索する  
アプリのうち「Ubuntu」と書いてあるものをインストール (※Ubuntu 18.04LTSやUbuntu16.04LTSではないので注意)  

### 1.2 Windows Subsystem for Linux (WSL)の有効化
左下のスタートボタンを押して、歯車マークをクリック  
「アプリ」の項目をクリックし、「アプリと機能」の項目の一番下までスクロールする  
下から三番目の「関連項目」の「プログラムと機能」をクリック  
コントロールパネルが開くので、左側の「Windowsの機能の有効化または無効化」をクリック  
Windowsの機能ウィンドウの中の「Windows Subsystem for Linux」の項目を見つけチェックを入れる  
「OK」を押すと勝手になんかやってくれるので、それが終わり次第再起動

## 2. Bash on UbuntuのセットアップとPythonのインストール
### 2.1 Bash on Ubuntuのセットアップ
再起動が終わったら、左下のスタートボタンを押して「Ubuntu」と調べて起動する  
> Installing, this may take a few minutes...

と出るのでしばらく待ってあげる
>Please create a default UNIX user account. The username does not need to match your Windows username.  
For more information visit: https://aka.ms/wslusers  
Enter new UNIX username: 

と出てくるので、Bash on Ubutnuで使いたいユーザー名を入れる  
(好きなものでok, 短いと表示が簡潔でいいかもしれない)
>Enter new UNIX password: 

と出てくるので好きなパスワードを入力。**絶対に忘れないこと!**  
なお、パスワードを入力しても画面は反応しないが仕様なので問題ない  
(後ろから除かれても大丈夫なようにこういう仕組みになっている。Linuxは大体こんなもの)
> Retype new UNIX password:

と出てくるので、同じパスワードを入力(確認用)
>sea@DESKTOP-BC0RMNS:~$ 

と出てきたら成功。(seaは私のユーザー名、DESKTOP-BC0RMNSは私のデバイス名なので異なって入れ大丈夫)  

### 2.2 Ubuntuの更新
Bash on Ubuntu(以下bash)上で、以下のようにコマンドを実行  ($ は入力しなくてよい)  
`$ sudo apt update`  
すると以下のような表示が出てくるのでパスワードを入力する  
> [sudo] password for ユーザー名:

再度いうが、パスワードを入力しても画面は反応しないが仕様なので問題ない  
sudoというコマンドはWindowsでいう管理者権限なのでこういう入力がある  
(※実際はroot権限で実行し、Linuxでのrootはwindowsでの管理者権限より圧倒的に強いので注意)  
  
なんかいろいろ出てくるけどほっといてok  
再度入力できるようになったら以下のコマンドを実行  
`$ sudo apt upgrade`  
なんかいろいろ出てくるけどほっといてok  
ただし以下のメッセージが出たら「y」を入力してEnterを押す
> Do you want to continue? [Y/n]

これは「Diskを消費するけどいい?」って丁寧に訪ねてくれているもの  
たかだか数十MB程度なので最近のパソコンは問題ない  
再度入力できるようになったら以下のコマンドを実行  
`$ sudo apt autoremove`  
これはいらないアプリパッケージなどを削除するもの  
同様に以下のメッセージが出てきたら「y」を入力してEnterを押す  
>Do you want to continue? [Y/n]

## 2.3 Pythonのインストール
以下のコマンドを実行する。以上  
`$ sudo apt install python`    
同様に以下のメッセージが表示されたら「y」を入力してEnterを押す
>After this operation, 16.8 MB of additional disk space will be used.  
Do you want to continue? [Y/n]

再度コマンドが入力できるようになった後、以下のコマンドが実行できればインストール成功  
`$ python3 --version`  
↓出力↓
> Python 3.6.5  


## 3. VS Codeのインストール
[VSCodeの公式ページ](https://azure.microsoft.com/ja-jp/products/visual-studio-code/)からインストーラをダウンロードしてインストール  
このとき、PATHを通しておくみたいなところにチェックを入れると楽かもしれません

# 4. VS Code の設定
左側のアイコンに四角いマーク(虫マークの下)を押して以下の拡張機能をインストール
- Python  
- Japanese Language Pack for Visual Studio Code  
  
英語がいい人は下のやつ入れなくて良い  
他にほしいものや独自の設定が有る人は勝手に入れたり設定したりしてok

# 5. この講義で使うフォルダーの作成
以下の手順でフォルダーを作ります  
> 5.1 Windowsのエクスプローラを開いて `C:\Users\ユーザー名` を開く  
> 5.2 右クリックで「新規作成(X)」→「フォルダー(F)」と進み`session`という名前のフォルダーを作成する  

これからこの「C:\Users\ユーザー名\session」というフォルダを使用して講座を進めます  
こんなややこしい場所に作った理由は「コマンドプロンプトを使いやすくするため」です  
いちいち開くのがめんどくさい人は、デスクトップにショートカットを作ってください  
  
最後に以下の作業をしておいてください
> 5.3 エクスプローラ上部の「表示」タブをクリックし、右寄りにある「ファイル名拡張子」のチェックボックスにチェックを入れる(※Win10の場合)

# 6. Python3で「Hello, World!」を出力する
コマンドプロンプトを起動して `python` と打ちます  
そして以下を入力します(`>>>`は入力しなくていい)  
```python:helloworld.py
>>> print("Hello, World!")
```
出力結果が以下の通りになったら成功です
> Hello, World!

終了するときは以下のように入力します
```python:exit.py
>>> exit()
```

# おまけ
この欄で 和、差、積、商、余り なども計算できます  
実際にやってみましょう
## 和
和は `+` という文字で「足し算するよ！」という意味として使います ~~(今更)~~  
こういう記号のことを「 **演算子** (四則演算子)」といいます  
~~テストには出るかもしれませんが、この名前を憶えても実用性は微妙です~~  
実際にやってみます

```python:sum.py
>>> 2+3
```
結果
> 5

---
## 差
差は`-`という演算子を使います。負の数でもいけます
```python:subtraction.py
>>> 5-2
```
結果
> 3

---
## 積
積は`*`という演算子を使います。「アスタリスク」と読みます
```python:multi.py
>>> 3*7
```
結果
> 21

---
## 商
商は`/`という演算子を使います。  
(※Python以外のたいていの言語は、整数同士の割り算だと、答えも整数しか返ってこないので注意してください。 5/2 をすると 2 になるみたいな感じで)
```python:div1.py
>>> 5/2
```
結果
> 2.5
  
余談ですが、たいていの他言語みたいに整数の範囲だけで割り算したい場合は`//`という演算子を使います。
```python:div2.py
>>> 5//2
```
結果
> 2

---
## 余り
割ったあまりが欲しい場合は`%`という演算子を使います。これ割と使います(個人的感想)。
```python:mod.py
>>> 19%5
```
結果
> 4

# お疲れ様です
第一回の講義はここまでです。  
Google先生で「python math」とかでggると平方根とか対数とかいろいろ計算できます。  
これでPythonは立派な計算機です(?)