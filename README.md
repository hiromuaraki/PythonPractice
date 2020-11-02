# Pythonの環境構築　使用ツール編
- Homebrew
- pyenv
- Python

# 今からやること
- 「Homebrew」をインストールする
- 「Homebrew」を用いて「pyenv」をインストールする
- 「pyenv」を用いてPythonをインストールする


## Homebrewのインストール

$ `brew -v`

で Homebrew のバージョンが表示されない場合は `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` 
を実行して Homebrew をインストールしてください。


## pyenvのインストール

$ `pyenv -v`

で pyenv のバージョンが表示されない場合は以下のとおり pyenv をインストールしてください。

$ `brew install pyenv`


## pyenvの設定
$ `echo $SHELL`

### 実行結果が `/bin/bash` の場合、以下４つのコマンドを実行してください。

- $ `echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile`
- $ `echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile`
- $ `echo 'eval "$(pyenv init -)"' >> ~/.bash_profile`
- $ `source ~/.bash_profile`

### 実行結果が `/bin/zsh` の場合、以下４つのコマンドを実行してください。

- $ `echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc`
- $ `echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc`
- $ `echo 'eval "$(pyenv init -)"' >> ~/.zshrc`
- $ `source ~/.zshrc`


## Pythonのインストール

では、インストールしたpyenvを用いてPythonをインストールしてみましょう。
pyenvでは複数のバージョンのPythonを使用することができます。ではどのようなバージョンのPythonがインストールできるか確認してみましょう。
以下のコマンドをターミナルで実行してみてください。

$ `pyenv install --list`

現在インストールが可能なPythonのバージョンです。今回は比較的新しい「3.6.5」をインストールしてみましょう。

$ `pyenv install 3.6.5`

次に以下のコマンドを実行してみてください。

$ `pyenv versions`

このコマンドでは、現在インストールされているPythonを一覧で確認することができます。
以下の画像のように、'3.6.5' が表示されていれば、ちゃんとインストールできたことが確認できます。

次にこのコマンドを実行してください。

$ `pyenv global 3.6.5`

これで 3.6.5 のPythonが使えるようになりました！以下のコマンドを実行して確認してみましょう。

$ `python --version`

正しく設定ができていれば、`3.6.5` と表示されたはずです。

これで「3系」のPythonを使えるようになりました！



# スクレイピング使用ツール編
- pip3
- BeautifulSoup
- requests
- lxml


## BeautifulSoupのインストール

下記をインストールしてください。

$ `pip3 install beautifulsoup4`

pip自体をバージョンアップするメッセージが表示された場合は
下記のコマンドでpipコマンドのバージョンをあげることができます。

$ `pip3 install -U pip`


## requestsのインストール

$ `pip3 install requests`


## lxmlのインストール

$ `pip install lxml`


以上で環境構築は完了です、お疲れ様でした🥂









