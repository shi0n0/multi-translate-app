## マルチ翻訳アプリ


# 概要

GPTAPIを使用したマルチ翻訳アプリです。  
自然言語処理での翻訳なので機械翻訳的なニュアンスではなく、自然な文として生成することが可能になると思います。  


# 機能(予定)

- 言語Aから言語nへの自然言語処理翻訳 - (完了)  
- 翻訳結果の言語Aへの逆翻訳 - (機能自体は実装完了、あとは少しの調整)
- 要望の追加、再翻訳  
- 翻訳形式の選択(カジュアル、形式的、説明 etc...)  
- 一度に複数の言語への翻訳、翻訳結果の表示 - (コストがかかりすぎるので却下)  
- デプロイ - (完了)  

# 開発理由

最近話題にもなってきたGPTAPIを使用してみたかったのが一つ。  
そして、GPTの優れている点を考えた時にやはり自然言語処理が思いついたので、普段から不便に思っていた機械翻訳の欠点をGPTなら補えるのではと考えたのがもう一つです。 
この二つの理由を解決するために開発するに至りました。  


# 現状の機械翻訳の問題

現状有力な機械翻訳はおそらくGoogle翻訳とDeepLだと思います。ですが、これらの翻訳はそれぞれ大きな欠点があります。  

- Google翻訳は形式的な翻訳はできますが、応用が効きませんし口語訳はできません。  
- DeepLは口語訳は得意ですが、形式的な翻訳には向きません。  

そして、どちらも共通して言えるのが、日本語からの翻訳だとニュアンスの違う翻訳結果が発生してしまうということです。おそらく日本語には独特の言葉は言い回し、例えなどを多用する傾向にあるので機械的な翻訳だとそれを汲み取れないのだと思います。  

そこで、GPTの登場です。  
GPTは自然言語処理によって様々な言語にも対応し、カジュアルから形式的な文章、単語まで全てに対応しています。実際使ってみればわかるのですが、おそらく他の翻訳とは比べ物にならないくらい自然で優秀です。

# 開発コメント枠

- GPTAPIについて無知のまま進めてたので利用料について学びました。  
現時点(5/12)で1$行ってないくらい、無料分全18$。なかなかきついです。  
何かでマネタイズできるなら別ですけど広告なんてどうやってつけたらいいのかわからないし、そもそもデプロイもまだなのでそこからのお話になりそうです。
デプロイ経験もなく、実際借り物で作っているこのアプリをデプロイしていいのかさえ曖昧。色々模索してみます...

- (5/14)  
Renderでデプロイしました！でもなぜかCSSが反映されなくて若干使いにくい仕様になっています。どうにか治したい...  
公開したはいいもののAPIの使用料が18$を超えたらお金かかってしまうので公開停止します。

- (5/15)  
どうやってもCSS反映されなかった(Whitenoisは試してない)のでHTMLにstyleで埋め込みました。ワンページWEBアプリだからいいよね？いいよ！やったー！

- (5/16)  
逆翻訳を実装しようとしてviewsに処理を書いたけどボタンを押してもな何も反応しない...  
なぜなのか分からないし一旦翻訳関数だけ残して翻訳関数の実行関数はリセットした。次やるときに実行関数を書いていこうと思う。

- (5/19)  
更新し忘れてたけど、一応逆翻訳の機能は実装できた。単純に自分がViewsの書き方をわかっていなかったせいであって、実装自体はそこまで難しいものではなかった。(更新したのは昨日の5/18)  
ただ、今ある翻訳アプリみたいに翻訳元と翻訳後の位置が入れ替わるとかはまだできていないので徐々にそういった細かいところまで実装したい。特に位置の入れ替えは最優先でやる。    

- (5/20)  
Deployブランチを作成しました。  
理由は、Renderでの環境変数の設定方法と開発環境の環境変数の設定方法が違うためです。今まではgithubにpushするためにデプロイ用のコードに書き換えて、開発時は開発用のコードに書き換えてという処理をしていたのですが、開発環境のブランチとデプロイ用のブランチを分けることでよりわかりやすくなります。  
開発時のコードにしてそのままpushしてしまってRenderが動かないということや、pushすべきでないものまでpushしてしまって訳わからなくなるってことが多々あったので...  
これからは開発環境で成功したものをmainにpushして、deployブランチにデプロイ用のコードに編集してpushするようにします。  
何気にブランチを複数活用するって経験が初めてだったりするのでちょっと進歩した気分。  

- (5/27)  
デザインを見やすくして、コピーボタンを新たに設置、プロンプトを変更しました  
背景色を若干暗くして、翻訳フォームが浮いて見えるようにし、影をつけました。あと可読性を加味してNoto Sans JPにフォントを変更しました。  
なんとなくレスポンシブをした方がいいかなと思って翻訳フォームも可変サイズになりました。  
コピーボタンはJavascriptで実装しています。コピーするとアラートがなる仕様。  
コピーボタンとアラートを閉じる位置がほぼ変わらないのでそこまでめんどくさくはならないと思います。  
プロンプトは日本語→英語への変換は日本語に、英語→日本語への変換は英語にすることでより自然な表現ができると感じました。  
mainにpushして、deployにpushしてというやり方ではなく、developにpushしてプルリクでマージした方が良いと考えたので、リネームを実施しました。  
↑
と考えたのですが、プルリクを送るとそのブランチは使えなくなるようなので(リモートの方が先というエラーが出た)、原点回帰してmainに統一しようと思います。  

 - (5/28~5/29)  
 文章校正機能を追加します。  
 当初翻訳機能のみのつもりでしたが、同じような作り方で別の機能を搭載できるのでGPTAPIを使って色々な機能を体験できるツールに企画を変更しようと思います。  
 そのために、base.htmlを作ってこれから作るhtmlにextendsしました。  
 レイアウトは元の文章→生成された文章なので、翻訳から流用する形にしようと思います。未だ中途半端にしか作れていないのでこれから続きを開発していきます。

 - (6/3)  
 Tailwindを実装しました。  
 使い始めで何もわかっていないですがなんとなく若干レスポンシブに対応しました。(翻訳の方だけ)  
 矢印の方向とかの問題があるのでまだ完全にはできていないのですが、そこは難しい処理じゃないと思うので深く考えていません。  
 本当に手探りなので、中々慣れるのに時間がかかりそうです。  

- (6/4)  
 文章校正の方にもtailwind対応しました。  
 tokenなどの関係で長い文章は対応できなかったり難解なものは取り扱えず処理できないようです。  
 使用token数やmodelをグレードアップすればできるにはできますが、金銭的な問題や管理ができなくなるので現状維持のままでいきたいと考えていますが、もし現状より良い策があったら都度ここに追記します。  

 - (6/5)  
 余計な必要のない記述を簡略化しました(コメントアウトなど)
 ある程度開発が終わっているので、このプロジェクトをもう少し深く続けるか次の開発に進むか迷っています。  
 自分的にはこのままこのプロジェクトを大きくして柱にするのもありかなと思いつつ、他の開発にも進まなければ数がないので見栄え的に良くないと思っています。  
 せっかくtailwindとかも触り始めているので、モチベーション的にも新しいのがいいのかな...  
 <br>

 - (6/8)  
 一応サービスではあるのでトップページみたいなものを作ろうと思いトップページ用の開発をしています。  
 機能としては説明とサービスへの導線なので、HTMlとCSS,一部javascriptで事足りるかなと。そのため、そこまで時間はかからないと思います。  
 <br>

- (6/11)  
 左上タイトルをAI Toolsで固定して、クリックでトップページに遷移するようにしました。  
 トップページは各アプリ(現時点では二つしかない)に飛べるようにナビゲーションページにします。更に、githubや作者Twitterなどを仮でヘッダーに表示しています。  
 何を追加して何を消すかなどは決まっていないので後々開発していく上で考えていこうと思います。  
 <br>

- (6/13)  
 Talk(会話)ページを作成しました。  
 LINEみたいなチャット形式、もしくは他の形式を想定しています。自分が何かを発すると返答を考えてくれる仕組みです。  
 まだ実装段階ではなく準備をしただけなのでもしかしたら何か問題が発生するかもしれませんが、その時はまた方針転換しようと思います。  
 プロンプトを設定してAPIを叩いてレスポンスを表示するという形の都合上、会話のような前後の文章を記憶する処理というのはもしかしたらChatGPTを使用しないとできないのかな...と考えている最中です。  
 <br>

- (6/15)  
 トップページを若干改変しました。レスポンシブに何も対応していないことに気づき、簡易的ではありますが、大幅に崩れるということは無くなったはず。 
 あと、もしかしたら近いうちにこのアプリが何かしら外の目に触れる機会があるかもしれないので綺麗に整備しないといけなくなりました。  
 別のアプリの可能性もあるし、そもそも外の目に触れることが確定しているわけではないんですけど。
<br>

- (6/18)  
 ボタンのレスポンシブ対応をしました。今まではスマホサイズでも上下ではなく右左で表示されていました。  
 修正後はPCでは右左、スマホでは上下になっています。   
 正直逆翻訳を逆矢印で表現するのはわかりにくいと思ってきたので他のマークを検討中です。  

- New!(6/22)  
 時間がなくてなかなか進めないですが、文章から生成することが可能になりました。  
 ですが、なぜか文章をプロンプトとして生成すると返答がおかしくなってしまうのでそこを解決しないといけなくなりました。  
 プロンプトを読み込んでいるのは確実で、Q.これは何語ですか？:寿限無 と質問すると日本語って返ってくるので、何が原因でおかしい返答が返ってきているのかは不明です。  
 解決次第まだすぐ更新しようと思います。

# 開発した感想
(5/15)  
簡単でもどれだけ悪くてもいいからアプリを開発することが大事だと身に沁みて感じました。本当に誇張なく。  
自分の今年の目標は小さくてもいいからアプリをたくさん作る！です。whetherAppはまあ例外として、こちらはその第一歩として歩んだアプリです。まだ完成はしていないですが...