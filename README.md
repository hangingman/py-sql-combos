# py-sql-combos

## require

- antlr4
- python3
- pip3
- tk-dev

```
// 必要なライブラリ追加
$ sudo apt-get install antlr4
$ sudo apt-get install tk-dev

$ pyenv install 3.6.8
$ pyenv global 3.6.8

$ pip install -r requirements.txt

// GUIの起動
$ python3 py-sql-combos/main.py

// antlrの文法ファイル更新
$ antlr4 -Dlanguage=Python3 MySqlLexer.g4 MySqlParser.g4
```
