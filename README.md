# Colourettu

This is a small collection of colour functions in Python, that can be used
to determine the (relative) lumansity of a colour and the contrast
between two colours.

## Installation

~~~
pip install colourettu
~~~

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
>>> colourettu.luminance(c4)
~~~

## Contrast

Contrast the difference in (precieved) brightness between colours.
Values vary between 1:1 (a given colour on itself) and 21:1 (white on black).

To compute contrast, two colours are required.

~~~python
>>> colourettu.contrast("#FFF", "#FFF")	# white on white
1.0
>>> colourettu.contrast(c1, "#000")	# black on white
20.999999999999996
>>> colourettu.contrast(c4, c5)
4.363552233203198
~~~

`contrast` can also be called on an already existing colour, but a second
colour needs to be provided:

~~~python
>>> c4.contrast(c5)
4.363552233203198
~~~

### Use of Contrast

For Basic readability, the ANSI standard is a contrast of 3:1 between the text
and it's background. The W3C proposes this as a minimum acceissibilty standard
for regular text under 18pt and bold text under 14pt. This is referred to as the
*A* standard. The W3C defines a higher *AA* standard with a mimimum contrast of
4.5:1. This is approximately equivalent to 20/40 vision, and is common for
those over 80. The W3C define an even higher *AAA* standard with a 7:1 minimum
contrast. This would be equivalent to 20/80 vision. Generally, it is assumed
that those with vision beyond this would access the web with the use of
assistive technologies.

If needed, these constants are stored in the library.

~~~python
>>> colourettu.A_contrast
3.0
>>> colourettu.AA_contrast
4.5
>>> colourettu.AAA_contrast
7.0
~~~

Also mentioned (and confirmed by personal experience), if the contrast is *too*
great, this can also cause readability problems when reading longer passages,
but I have been (yet) unable to find any quantitative research to this effect.
