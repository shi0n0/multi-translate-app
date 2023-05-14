## マルチ翻訳アプリ


# 概要

GPTAPIを使用したマルチ翻訳アプリです。  
自然言語処理での翻訳なので機械翻訳的なニュアンスではなく、自然な文として生成することが可能になると思います。  


# 機能(予定)

- 言語Aから言語nへの自然言語処理翻訳 - (完了)  
- 翻訳結果の言語Aへの逆翻訳  
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

- New!(5/14)  
Renderでデプロイしました！でもなぜかCSSが反映されなくて若干使いにくい仕様になっています。どうにか治したい...  
公開したはいいもののAPIの使用料が18$を超えたらお金かかってしまうので公開停止します。


# 開発した感想