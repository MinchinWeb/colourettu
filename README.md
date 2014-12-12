# Colourettu

## Note on Spelling

I have used the Canadian/British spelling of *colour* through this
and the code, however, if you use the American spelling (i.e. without
the *u*), the code should still work. That said, this only applies
to the internals of the library, `Colourettu` will always have the *u*
in it.

~~~python
>>> colouretta.colour == colouretta.color
True
~~~

## Colour Class

Colours are created by calling the `colour` class. Colour values
can be provided via 3 or 6 digit hex notation, or providing a
list or a tuple or the Red, Green, and Blue values (as intergers).

~~~python
import colourettu

c1 = colourettu.colour()	# defaults to #FFF
c2 = colourettu.colour("#eee")	# equivlant to #EEEEEE
c3 = colourettu.colour("#456bda")
c4 = colourettu.colour([3, 56, 129])
c5 = colourettu.colour((63, 199, 233))
~~~

The value of each channel can be pulled out:

~~~python
>>> c4.red()
3
>>> c4.green()
56
>>> c4.blue()
129
~~~

You can also get the colour back as either a hex value, or a rgb tuple:

~~~python
>>> c2.hex()
'#EEEEEE'
>>> c2.rgb()
(238, 238, 238)
~~~

## (Relative) Luminance

Luminance is a meansure of how 'bright' a colour is. Values are normalized
so that the Luminance of White is 1 and the Luminance of Black is 0. That is
to say:

~~~python
>>> colourettu.luminance("#FFF")	# white
0.9999999999999999
>>> colourettu.luminance("#000")	# black
0.0
~~~

`luminance` can also be called on an already existing colour:

~~~python
>>> c3.luminance()
0.2641668488934239
~~~
