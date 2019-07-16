# 2019年度 6回 プログラミング講習会
## やってみること
1. slack鯖とBOTトークンの作成
2. 簡単なslackBOTの作成
3. 独自のものを作ってみる
## おまけ目標
上記の3.を頑張るんやで

---
# 1.slack鯖とBOTトークンの作成
[Python3系でSlack Botの作成〜基礎的な対話を実装する](https://qiita.com/croissant1028/items/8d6334b76576762df349)  
[Pythonを使ったSlackBot作成方法](https://qiita.com/kunitaya/items/690028e33ba5c666f3e2)  
を参考に作っていきます。  

[slackのワークスペースの作成](https://slack.com/create)に飛んで、メールアドレス(自分のものなら何でもいい)を入力し、ワークスペースを作成します。  

`Check your email! We've sent a 6-digit confirmation code to 入力したメアド. It will expire shortly, so enter it soon.`と表示されるので、メアドに送られてくる桁の数字を入力してあげます。  

すると`What's the name of your company or team?`と出てくるので、好きなslack鯖の名前を入力してあげます。  

次に`What’s a project your team is working on?`と出てくるので、好きなプロジェクト名を入れてあげます。  

最後に`Who else is working on this project?`と出てきます。招待してあげたい友人のメアドを入力すると招待することができます。もちろん後から追加することも可能です。  
(もし、この段階で誰も追加しない場合は下にある`Skip for now`を押してあげます)  

以上で、作成完了です。表示される`See Your Channel in Slack`という緑のボタンを押すと作ったSlackに入れます。

# 2. 簡単なSlackBOTの作成
上記のサイトに加え、[PythonのslackbotライブラリでSlackボットを作る](https://qiita.com/sukesuke/items/1ac92251def87357fdf6) も参考に作っていきます。  

## 2.1 APIトークンの発行
[ココ](https://api.slack.com/)にアクセスし、`Start Building`をクリック  

`Create a Slack App`というのが出てきます。`App Name`のところにBOTの名前を、  `Development Slack Workspace`のところで、先ほど作ったワークスペースを選択します  
これらができれば`Create App`を押します  

次に`Add features and functionality`項目の中の`Permissions`を押します

少し下にスクロールして`Scopes`というところの`Select Permission Scopes
`というところで、`Administrator the workspace`を選択し、`Save Changes`で保存します。  
(※本来は必要最低限の権限を付与します。さもなくば乗っ取られたりした場合に、悪い奴が何でもできることになります)

戻るボタンを押すか、左側の`Basic Infomation`から先ほどの画面に戻り、Permissionsの下にできた`Install your app to your workspace`を押して`Install App to Workspace`ボタンを押します  

すると`Install`のボタンが現れるのでそれを押します。  

次に左側の`Bot Users`を押します。  
そこで`Add a BotUser`を押し、Display nameに表示したい名前(Botの名前)、  
Default Usernameに初期の名前(Display nameと同じで大丈夫です)、  
`Always Show My Bot as Online`の項目を有効にします  
終われば下の`Add User Bot`を押します

すると上側に`You’ve changed the permission scopes your app uses. Please reinstall your app for these changes to take effect (and if your app is listed in the Slack App Directory, you’ll need to resubmit it as well).`というのが出てくるので reinstall your appのリンクを押して、`Reinstall App`ボタンを押し、その後出てくる`Install`を押します。  

最後に、左メニューの`OAuth & Permissions`の項目を押し、`Bot User OAuth Access Token`と書いてある場所の下にある「xox」から始まる謎の文字列をコピーします。  
(※これがbotをつなぐコードみたいなものです。他人にパクられないように気を付けてください！)

## 2.2 pipのインストール
コマンドプロンプトを起動して`pip3 install slackbot`を打って実行します  
後は待つだけ。

## 2.3 ファイルの準備
```
slackbot
    ├ run.py
    ├ slackbot_settings.py
    ├ plugins
        ├ __init__.py
        └ my_mention.py
```
こんな感じでディレクトリ構造を作ります。Githubからslackbot.zipで
ダウンロードできるようにしておきます。  

初期設定は[Pythonを使ったSlackBotの作成方法](https://qiita.com/kunitaya/items/690028e33ba5c666f3e2)