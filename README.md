# python-rison

Python version of the rison encoder/decoder originally taken from http://mjtemplate.org/examples/rison.html

## Usage

```python
import rison

print rison.dumps({'foo': 'bar'})  # '(foo:bar)'

print rison.loads('(foo:bar)')  # {'foo': 'bar'}
```

## Tests

```
pip install nose
nosetests tests/*.py
```
