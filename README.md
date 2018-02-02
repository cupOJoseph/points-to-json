# points-to-json
Turn a list of points into a json objectwrite it to a file

Example:

In example.txt
```
(1,11)
(2,22)
```
Run `$ python3 example.txt`

A new file, example.txt.json, will be created but not formated nicely.
```javascript
{
	"perimeter": [{
		"x": 1.0,
		"y": 11.0
	},
  	{
		"x": 2.0,
		"y": 22.0
	}]
}
```
