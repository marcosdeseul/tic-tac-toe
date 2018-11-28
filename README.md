# tic-tac-toe

install Python 3.x

# Run game

```sh
python main.py
```


# Run unit tests

```sh
python -m unittest -v test_*.py
```
TDD Recommendation: install [entr](http://entrproject.org/)
```sh
ls **/*.py | entr -c sh -c "python -m unittest -v test_*.py"
```
