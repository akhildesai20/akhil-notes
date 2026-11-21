## FontSpector report

fontspector version: 1.9.0






## Check results




<details><summary>[10] AkhilNotes-Italic[wght].ttf</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. (contour_count)</summary>
    <div>


> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be constructured in a handful of ways. This means a glyph's contour count will only differ slightly amongst different fonts, e.g a 'g' could either be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs to a display family.
> 
> This check currently does not cover variable fonts because there's plenty of alternative ways of constructing glyphs with multiple outlines for each feature in a VarFont. The expected contour count data for this check is currently optimized for the typical construction of glyphs in static fonts.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are
     inferred from the typical amounts of contours observed in a
     large collection of reference font families. The divergences
     listed below may simply indicate a significantly different
     design on some of your glyphs. On the other hand, some of these
     may flag actual bugs in the font such as glyphs mapped to an
     incorrect codepoint. Please consider reviewing the design and
     codepoint assignment of these to make sure they are correct.


    The following glyphs do not have the recommended number of contours:
* approxequal (U+2248): found 3, expected one of: [2, 6]
* colon (U+003A): found 4, expected one of: [2, 6]
* ellipsis (U+2026): found 6, expected one of: [3, 7]
* exclam (U+0021): found 3, expected one of: [2, 6]
* period (U+002E): found 2, expected one of: [1, 5]
* quotedblleft (U+201C): found 4, expected one of: [2, 6]
* quotedblright (U+201D): found 4, expected one of: [2, 6]
* semicolon (U+003B): found 4, expected one of: [2, 6]
* quotedbl (U+0022): found 4, expected one of: [2, 6]
... and 53 others [code: contour-count]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. (interpolation_issues)</summary>
    <div>


> When creating a variable font, the designer must make sure that corresponding paths have the same start points across masters, as well as that corresponding component shapes are placed in the same order within a glyph across masters. If this is not done, the glyph will not interpolate correctly.
> 
> Here we check for the presence of potential interpolation errors using the interpolatable crate.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3930]





- ⚠️ **WARN** Interpolation issue in D: Wrong start point: contour 2 should start at 7 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in D: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in colon: Wrong start point: contour 1 should start at 18 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in colon: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in colon: Wrong start point: contour 3 should start at 18 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in colon: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in comma: Wrong start point: contour 1 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ellipsis: Wrong start point: contour 1 should start at 49 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ellipsis: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ellipsis: Wrong start point: contour 3 should start at 49 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ellipsis: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ellipsis: Wrong start point: contour 5 should start at 47 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ellipsis: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in exclam: Wrong start point: contour 1 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in exclam: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in period: Wrong start point: contour 1 should start at 18 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in period: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in question: Wrong start point: contour 2 should start at 41 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotedblleft: Wrong start point: contour 1 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotedblleft: Wrong start point: contour 3 should start at 23 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotedblright: Wrong start point: contour 1 should start at 26 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotedblright: Wrong start point: contour 3 should start at 26 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quoteleft: Wrong start point: contour 1 should start at 20 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quoteright: Wrong start point: contour 1 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in registered: Wrong start point: contour 5 should start at 12 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in registered: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in semicolon: Wrong start point: contour 1 should start at 10 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in semicolon: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in semicolon: Wrong start point: contour 3 should start at 13 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in semicolon: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in sterling: Wrong start point: contour 1 should start at 16 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotedbl: Wrong start point: contour 1 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotedbl: Wrong start point: contour 3 should start at 23 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotesingle: Wrong start point: contour 1 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in periodcentered: Wrong start point: contour 1 should start at 18 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in periodcentered: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Aacute: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Adieresis: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Adieresis: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Adieresis: Wrong start point: contour 5 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Adieresis: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Ccedilla: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Eacute: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Edieresis: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Edieresis: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Edieresis: Wrong start point: contour 4 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Edieresis: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Iacute: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Idieresis: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Idieresis: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Idieresis: Wrong start point: contour 4 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Idieresis: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Oacute: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Odieresis: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Odieresis: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Odieresis: Wrong start point: contour 5 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Odieresis: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Uacute: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Udieresis: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Udieresis: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Udieresis: Wrong start point: contour 4 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Udieresis: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Yacute: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in aacute: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in adieresis: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in adieresis: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in adieresis: Wrong start point: contour 5 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in adieresis: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ccedilla: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in eacute: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in edieresis: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in edieresis: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in edieresis: Wrong start point: contour 4 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in edieresis: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in iacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in idieresis: Wrong start point: contour 2 should start at 17 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in idieresis: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in idieresis: Wrong start point: contour 4 should start at 17 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in idieresis: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in oacute: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in odieresis: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in odieresis: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in odieresis: Wrong start point: contour 5 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in odieresis: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in divide: Wrong start point: contour 2 should start at 18 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in divide: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in divide: Wrong start point: contour 4 should start at 18 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in divide: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uacute: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in udieresis: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in udieresis: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in udieresis: Wrong start point: contour 5 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in udieresis: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in yacute: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ydieresis: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ydieresis: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ydieresis: Wrong start point: contour 5 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ydieresis: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Aogonek: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in aogonek: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Cacute: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in cacute: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Cdotaccent: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Cdotaccent: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in cdotaccent: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in cdotaccent: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Dcaron: Wrong start point: contour 2 should start at 7 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Dcaron: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Edotaccent: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Edotaccent: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in edotaccent: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in edotaccent: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Eogonek: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in eogonek: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Gdotaccent: Wrong start point: contour 4 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Gdotaccent: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in gdotaccent: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in gdotaccent: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Gcommaaccent: Wrong start point: contour 4 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in gcommaaccent: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Iogonek: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in iogonek: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Idotaccent: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Idotaccent: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Kcommaaccent: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in kcommaaccent: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Lacute: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in lacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Lcommaaccent: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in lcommaaccent: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Nacute: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in nacute: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Ncommaaccent: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ncommaaccent: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Ohungarumlaut: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Ohungarumlaut: Wrong start point: contour 5 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ohungarumlaut: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ohungarumlaut: Wrong start point: contour 5 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Racute: Wrong start point: contour 5 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in racute: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0156: Wrong start point: contour 5 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0157: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Sacute: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in sacute: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Scedilla: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in scedilla: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0162: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0163: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Uhungarumlaut: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Uhungarumlaut: Wrong start point: contour 4 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uhungarumlaut: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uhungarumlaut: Wrong start point: contour 5 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Uogonek: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uogonek: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Ydieresis: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Ydieresis: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Ydieresis: Wrong start point: contour 4 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Ydieresis: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Zacute: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in zacute: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Zdotaccent: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Zdotaccent: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in zdotaccent: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in zdotaccent: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni01EA: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni01EB: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni01F4: Wrong start point: contour 4 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni01F5: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0226: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0226: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0227: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0227: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0228: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0229: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni022E: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni022E: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni022F: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni022F: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E02: Wrong start point: contour 5 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E02: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E03: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E03: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E0A: Wrong start point: contour 2 should start at 7 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E0A: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E0A: Wrong start point: contour 4 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E0A: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E0B: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E0B: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E10: Wrong start point: contour 2 should start at 7 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E10: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E10: Wrong start point: contour 4 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E11: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E1E: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E1E: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E1F: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E1F: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E22: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E22: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E23: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E23: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E26: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E26: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E26: Wrong start point: contour 5 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E26: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E27: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E27: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E28: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E29: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E30: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E31: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E3E: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E3F: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E40: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E40: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E41: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E41: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E44: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E44: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E45: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E45: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E54: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E55: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E56: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E56: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E57: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E57: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E58: Wrong start point: contour 5 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E58: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E59: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E59: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E60: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E60: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E61: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E61: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E6A: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E6A: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E6B: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E6B: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Wacute: Wrong start point: contour 2 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in wacute: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Wdieresis: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Wdieresis: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Wdieresis: Wrong start point: contour 4 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Wdieresis: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in wdieresis: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in wdieresis: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in wdieresis: Wrong start point: contour 5 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in wdieresis: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E86: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E86: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E87: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E87: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8A: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8A: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8B: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8B: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8C: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8C: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8C: Wrong start point: contour 4 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8C: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8D: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8D: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8D: Wrong start point: contour 4 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8D: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8E: Wrong start point: contour 2 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8E: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8F: Wrong start point: contour 3 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8F: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E97: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E97: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in minute: Wrong start point: contour 1 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in second: Wrong start point: contour 1 should start at 26 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in second: Wrong start point: contour 3 should start at 26 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni2219: Wrong start point: contour 1 should start at 17 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni2219: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni2236: Wrong start point: contour 1 should start at 18 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni2236: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni2236: Wrong start point: contour 3 should start at 18 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni2236: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni22C5: Wrong start point: contour 1 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni22C5: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 1 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 3 should start at 17 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 5 should start at 15 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 7 should start at 18 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 7 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 9 should start at 18 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 9 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 11 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 11 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 13 should start at 18 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 13 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 15 should start at 20 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 15 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 17 should start at 15 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 17 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 19 should start at 17 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 19 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Eth: Wrong start point: contour 2 should start at 7 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Eth: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Dcroat: Wrong start point: contour 2 should start at 7 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Dcroat: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in exclamdown: Wrong start point: contour 1 should start at 19 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in exclamdown: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in questiondown: Wrong start point: contour 2 should start at 41 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotesinglbase: Wrong start point: contour 1 should start at 20 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotedblbase: Wrong start point: contour 1 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in periodcentered.loclCAT: Wrong start point: contour 1 should start at 17 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in periodcentered.loclCAT: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in periodcentered.loclCAT.case: Wrong start point: contour 1 should start at 18 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in periodcentered.loclCAT.case: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in _Dsmall: Wrong start point: contour 2 should start at 7 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in D.circled: Wrong start point: contour 4 should start at 7 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in D_d: Wrong start point: contour 2 should start at 7 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in D_d: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. (mandatory_avar_table)</summary>
    <div>


> Most variable fonts should include an avar table to correctly define axes progression rates.
> 
> For example, a weight axis from 0% to 100% doesn't map directly to 100 to 1000, because a 10% progression from 0% may be too much to define the 200, while 90% may be too little to define the 900.
> 
> If the progression rates of axes is linear, this check can be ignored. Fontmake will also skip adding an avar table if the progression rates are linear. However, it is still recommended that designers visually proof each instance is at the expected weight, width etc.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3100]





- ⚠️ **WARN** The font does not include an avar table.  If the progression rates of axes is linear and no user-mapping is expected, this is fine, and this check can be ignored or excluded. [code: missing-avar]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. (math_signs_width)</summary>
    <div>


> #,         It is a common practice to have math signs sharing the same width         (preferably the same width as tabular figures accross the entire font family).
> 
> This probably comes from the will to avoid additional tabular math signs knowing that their design can easily share the same width.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3832]





- ⚠️ **WARN** The most common width is 730 among a set of 18  math glyphs.
The following math glyphs have a different width, though:
width=587: minus, divide
width=719: less, plus, lessequal
width=526: greater, multiply
width=806: approxequal
width=736: plusminus
width=754: uni2262, equal, notequal
width=649: greaterequal
width=473: logicalnot
width=605: uni223C [code: width-outliers]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure font has overlaps bit set correctly. (overlaps_bit)</summary>
    <div>


> Fonts whose glyphs contain overlapping paths should have the overlaps bit set correctly to avoid rendering errors. (See for example https://github.com/google/fonts/issues/11120)
> 
> This should normally be done by the font compiler, but some compilers do not correctly set the bit.




Original proposal: [https://github.com/googlefonts/gftools/pulls/965]





- ⚠️ **WARN** The following glyphs have overlaps but the overlaps bit is not set:
* uni01CD (U+01CD)
* uni1E54 (U+1E54)
* Otilde (U+00D5)
* d (U+0064)
* Ecircumflex (U+00CA)
* at (U+0040)
* ycircumflex (U+0177)
* uni0109 (U+0109)
* racute (U+0155)
... and 382 others [code: no-overlaps-bit]
  
  


- ⚠️ **WARN** The following glyphs do not have overlaps but the overlaps bit is set:
* acute (U+00B4)
* hungarumlaut (U+02DD)
* dotaccentcomb (U+0307)
* guilsinglright (U+203A)
* ogonekcomb (U+0328)
* rightBlackSmallTriangle (U+25B8)
* circumflex (U+02C6)
* brokenbar (U+00A6)
* ogonek (U+02DB)
... and 53 others [code: overlaps-bit-set]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>


> This check uses a heuristic to determine which GF glyphsets a font supports. Then it checks the font for correct shaping behaviour for all languages in those glyphsets.




Original proposal: [https://github.com/googlefonts/fontbakery/issues/4147]





- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages                    |
|-------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                 | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: ʻ |                              |
| Auxiliary orthography codepoints:                                 | * ca_Latn (Catalan)          |
|   The following auxiliary characters are missing from the font: Ŀ |                              |
|   The following auxiliary characters are missing from the font: ŀ |                              |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǥ |                              |
|   The following auxiliary characters are missing from the font: Ŋ |                              |
|   The following auxiliary characters are missing from the font: Ŧ |                              |
|   The following auxiliary characters are missing from the font: Ʒ |                              |
|   The following auxiliary characters are missing from the font: Ǯ |                              |
|   The following auxiliary characters are missing from the font: ǥ |                              |
|   The following auxiliary characters are missing from the font: ŋ |                              |
|   The following auxiliary characters are missing from the font: ŧ |                              |
|   The following auxiliary characters are missing from the font: ʒ |                              |
|   The following auxiliary characters are missing from the font: ǯ |                              |
| Auxiliary orthography codepoints:                                 | * nl_Latn (Dutch)            |
|   The following auxiliary characters are missing from the font: Ĳ |                              |
|   The following auxiliary characters are missing from the font: ĳ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ŋ |                              |
|   The following auxiliary characters are missing from the font: Ŧ |                              |
|   The following auxiliary characters are missing from the font: ŋ |                              |
|   The following auxiliary characters are missing from the font: ŧ |                              |
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph (outline_direction)</summary>
    <div>


> In TrueType fonts, the outermost contour of a glyph should be oriented clockwise, while the inner contours should be oriented counter-clockwise. Getting the path direction wrong can lead to rendering issues in some software.




Original proposal: [https://github.com/fonttools/fontbakery/issues/2056]





- ⚠️ **WARN** The following glyphs have a counter-clockwise outer contour:

* .notdef has a counter-clockwise outer contour
* zero (U+0030) has a counter-clockwise outer contour
* one (U+0031) has a counter-clockwise outer contour
* two (U+0032) has a counter-clockwise outer contour
* three (U+0033) has a counter-clockwise outer contour
* four (U+0034) has a counter-clockwise outer contour
* five (U+0035) has a counter-clockwise outer contour
* six (U+0036) has a counter-clockwise outer contour
* seven (U+0037) has a counter-clockwise outer contour
... and 1522 others [code: ccw-outer-contour]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments (overlapping_path_segments)</summary>
    <div>


> Some rasterizers encounter difficulties when rendering glyphs with overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points. When two segments share the same coordinates, they are considered overlapping.




Original proposal: [https://github.com/google/fonts/issues/7594#issuecomment-2401909084]





- ⚠️ **WARN** The following glyphs have overlapping path segments:

* .notdef: Line(Line { p0: (11.0, -105.0), p1: (12.0, -108.0) }) has the same coordinates as a previous segment.
* .notdef: Line(Line { p0: (12.0, -108.0), p1: (16.0, -111.0) }) has the same coordinates as a previous segment.
* .notdef: Line(Line { p0: (16.0, -111.0), p1: (20.0, -112.0) }) has the same coordinates as a previous segment.
* .notdef: Line(Line { p0: (11.0, -100.0), p1: (11.0, -105.0) }) has the same coordinates as a previous segment.
* paragraph (U+00B6): Line(Line { p0: (266.0, 699.0), p1: (261.0, 696.0) }) has the same coordinates as a previous segment.
* paragraph (U+00B6): Line(Line { p0: (261.0, 696.0), p1: (257.0, 693.0) }) has the same coordinates as a previous segment.
* paragraph (U+00B6): Line(Line { p0: (257.0, 693.0), p1: (255.0, 688.0) }) has the same coordinates as a previous segment.
* paragraph (U+00B6): Line(Line { p0: (270.0, 700.0), p1: (266.0, 699.0) }) has the same coordinates as a previous segment.
* whiteSmallSquare (U+25AB): Line(Line { p0: (34.0, 222.0), p1: (34.0, 217.0) }) has the same coordinates as a previous segment.
... and 3 others [code: overlapping-path-segments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>


> Microsoft keeps a list of font vendors and their respective contact info. This list is updated regularly and is indexed by a 4-char "Vendor ID" which is stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some applications may display the type designer / type foundry contact info on some dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in that list or if it has some of the default values used by the most common font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs. If you registered recently, you're safe to ignore warnings emitted by this check, since your ID will soon be included in one of our upcoming releases.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3943, https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** OS/2 VendorID value 'AKHL' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check font follows the Google Fonts vertical metric schema (googlefonts/vertical_metrics)</summary>
    <div>


> This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be   between 120% and 200% of UPM * Warning if sum is over 150% of UPM
> 
> The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
> 
> Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics




Original proposal: [https://github.com/fonttools/fontbakery/pull/3762 and https://github.com/fonttools/fontbakery/pull/3921]





- ⚠️ **WARN** We recommend the absolute sum of the hhea metrics should be between 1.2-1.5x of the font's upm. This font has 1.506x (1506) [code: bad-hhea-range]
  
  

</div>
</details>


</div>
</details>


<details><summary>[1] </summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. (googlefonts/metadata/unreachable_subsetting)</summary>
    <div>


> This check ensures that all encoded glyphs in the font are covered by a subset declared in the METADATA.pb. Google Fonts splits the font into a set of subset fonts based on the contents of the `subsets` field and the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions will not be served in the subsetted fonts, and so will be unreachable to the end user.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4097 and https://github.com/fonttools/fontbakery/pull/4273]





- ⚠️ **WARN** AkhilNotes[wght].ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: canadian-aboriginal, yi
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: canadian-aboriginal, yi
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, math, cherokee
* U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
* U+0307 COMBINING DOT ABOVE: try adding one of: tai-le, tifinagh, hebrew, old-permic, malayalam, math, todhri, canadian-aboriginal, duployan, coptic, syriac
* U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage
* U+030C COMBINING CARON: try adding one of: cherokee, tai-le
... and 136 others

Or you can add the above codepoints to one of the subsets supported by the font: cyrillic-ext, latin-ext, latin, vietnamese [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** AkhilNotes-Italic[wght].ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: canadian-aboriginal, yi
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: canadian-aboriginal, yi
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: coptic, tifinagh, math, cherokee
* U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic
* U+0307 COMBINING DOT ABOVE: try adding one of: tai-le, tifinagh, hebrew, old-permic, malayalam, math, todhri, canadian-aboriginal, duployan, coptic, syriac
* U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage
* U+030C COMBINING CARON: try adding one of: cherokee, tai-le
... and 136 others

Or you can add the above codepoints to one of the subsets supported by the font: cyrillic-ext, latin-ext, latin, vietnamese [code: unreachable-subsetting]
  
  

</div>
</details>


</div>
</details>


<details><summary>[10] AkhilNotes[wght].ttf</summary>
<div>


<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. (contour_count)</summary>
    <div>


> Visually QAing thousands of glyphs by hand is tiring. Most glyphs can only be constructured in a handful of ways. This means a glyph's contour count will only differ slightly amongst different fonts, e.g a 'g' could either be 2 or 3 contours, depending on whether its double story or single story.
> 
> However, a quotedbl should have 2 contours, unless the font belongs to a display family.
> 
> This check currently does not cover variable fonts because there's plenty of alternative ways of constructing glyphs with multiple outlines for each feature in a VarFont. The expected contour count data for this check is currently optimized for the typical construction of glyphs in static fonts.




Original proposal: [https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are
     inferred from the typical amounts of contours observed in a
     large collection of reference font families. The divergences
     listed below may simply indicate a significantly different
     design on some of your glyphs. On the other hand, some of these
     may flag actual bugs in the font such as glyphs mapped to an
     incorrect codepoint. Please consider reviewing the design and
     codepoint assignment of these to make sure they are correct.


    The following glyphs do not have the recommended number of contours:
* approxequal (U+2248): found 3, expected one of: [2, 6]
* colon (U+003A): found 4, expected one of: [2, 6]
* ellipsis (U+2026): found 6, expected one of: [3, 7]
* exclam (U+0021): found 3, expected one of: [2, 6]
* period (U+002E): found 2, expected one of: [1, 5]
* quotedblleft (U+201C): found 4, expected one of: [2, 6]
* quotedblright (U+201D): found 4, expected one of: [2, 6]
* semicolon (U+003B): found 4, expected one of: [2, 6]
* quotedbl (U+0022): found 4, expected one of: [2, 6]
... and 53 others [code: contour-count]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Detect any interpolation issues in the font. (interpolation_issues)</summary>
    <div>


> When creating a variable font, the designer must make sure that corresponding paths have the same start points across masters, as well as that corresponding component shapes are placed in the same order within a glyph across masters. If this is not done, the glyph will not interpolate correctly.
> 
> Here we check for the presence of potential interpolation errors using the interpolatable crate.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3930]





- ⚠️ **WARN** Interpolation issue in D: Wrong start point: contour 2 should start at 7 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in colon: Wrong start point: contour 1 should start at 18 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in colon: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in colon: Wrong start point: contour 3 should start at 18 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in colon: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in comma: Wrong start point: contour 1 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ellipsis: Wrong start point: contour 1 should start at 49 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ellipsis: Wrong start point: contour 3 should start at 49 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ellipsis: Wrong start point: contour 5 should start at 47 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in exclam: Wrong start point: contour 1 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in exclam: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in period: Wrong start point: contour 1 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in period: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in question: Wrong start point: contour 2 should start at 41 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotedblleft: Wrong start point: contour 1 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotedblleft: Wrong start point: contour 3 should start at 20 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotedblright: Wrong start point: contour 1 should start at 23 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotedblright: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quoteleft: Wrong start point: contour 1 should start at 20 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quoteright: Wrong start point: contour 1 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in registered: Wrong start point: contour 5 should start at 12 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in registered: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in semicolon: Wrong start point: contour 1 should start at 8 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in semicolon: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in semicolon: Wrong start point: contour 3 should start at 13 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in semicolon: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in sterling: Wrong start point: contour 1 should start at 16 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotedbl: Wrong start point: contour 1 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotedbl: Wrong start point: contour 3 should start at 20 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotesingle: Wrong start point: contour 1 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in periodcentered: Wrong start point: contour 1 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in periodcentered: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Aacute: Wrong start point: contour 3 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Adieresis: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Adieresis: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Adieresis: Wrong start point: contour 5 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Adieresis: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Ccedilla: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Eacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Edieresis: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Edieresis: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Edieresis: Wrong start point: contour 4 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Edieresis: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Iacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Idieresis: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Idieresis: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Idieresis: Wrong start point: contour 4 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Idieresis: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Oacute: Wrong start point: contour 3 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Odieresis: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Odieresis: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Odieresis: Wrong start point: contour 5 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Odieresis: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Uacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Udieresis: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Udieresis: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Udieresis: Wrong start point: contour 4 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Udieresis: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Yacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in aacute: Wrong start point: contour 3 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in adieresis: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in adieresis: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in adieresis: Wrong start point: contour 5 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in adieresis: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ccedilla: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in eacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in edieresis: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in edieresis: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in edieresis: Wrong start point: contour 4 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in edieresis: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in iacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in idieresis: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in idieresis: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in idieresis: Wrong start point: contour 4 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in idieresis: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in oacute: Wrong start point: contour 3 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in odieresis: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in odieresis: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in odieresis: Wrong start point: contour 5 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in odieresis: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in divide: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in divide: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in divide: Wrong start point: contour 4 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in divide: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uacute: Wrong start point: contour 3 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in udieresis: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in udieresis: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in udieresis: Wrong start point: contour 5 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in udieresis: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in yacute: Wrong start point: contour 3 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ydieresis: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ydieresis: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ydieresis: Wrong start point: contour 5 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ydieresis: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Aogonek: Wrong start point: contour 3 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in aogonek: Wrong start point: contour 3 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Cacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in cacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Cdotaccent: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Cdotaccent: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in cdotaccent: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in cdotaccent: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Dcaron: Wrong start point: contour 2 should start at 7 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Edotaccent: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Edotaccent: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in edotaccent: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in edotaccent: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Eogonek: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in eogonek: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Gdotaccent: Wrong start point: contour 4 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Gdotaccent: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in gdotaccent: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in gdotaccent: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Gcommaaccent: Wrong start point: contour 4 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in gcommaaccent: Wrong start point: contour 3 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Iogonek: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in iogonek: Wrong start point: contour 3 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Idotaccent: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Idotaccent: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Kcommaaccent: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in kcommaaccent: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Lacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in lacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Lcommaaccent: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in lcommaaccent: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Nacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in nacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Ncommaaccent: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ncommaaccent: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Ohungarumlaut: Wrong start point: contour 3 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Ohungarumlaut: Wrong start point: contour 5 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ohungarumlaut: Wrong start point: contour 3 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in ohungarumlaut: Wrong start point: contour 5 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Racute: Wrong start point: contour 5 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in racute: Wrong start point: contour 3 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0156: Wrong start point: contour 5 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0157: Wrong start point: contour 3 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Sacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in sacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Scedilla: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in scedilla: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0162: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0163: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Uhungarumlaut: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Uhungarumlaut: Wrong start point: contour 4 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uhungarumlaut: Wrong start point: contour 3 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uhungarumlaut: Wrong start point: contour 5 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Uogonek: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uogonek: Wrong start point: contour 3 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Ydieresis: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Ydieresis: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Ydieresis: Wrong start point: contour 4 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Ydieresis: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Zacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in zacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Zdotaccent: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Zdotaccent: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in zdotaccent: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in zdotaccent: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni01EA: Wrong start point: contour 3 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni01EB: Wrong start point: contour 3 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni01F4: Wrong start point: contour 4 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni01F5: Wrong start point: contour 3 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0226: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0226: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0227: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0227: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0228: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni0229: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni022E: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni022E: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni022F: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni022F: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E02: Wrong start point: contour 5 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E02: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E03: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E03: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E0A: Wrong start point: contour 2 should start at 7 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E0A: Wrong start point: contour 4 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E0A: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E0B: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E0B: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E10: Wrong start point: contour 2 should start at 7 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E10: Wrong start point: contour 4 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E11: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E1E: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E1E: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E1F: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E1F: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E22: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E22: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E23: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E23: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E26: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E26: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E26: Wrong start point: contour 5 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E26: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E27: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E27: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E28: Wrong start point: contour 3 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E29: Wrong start point: contour 2 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E30: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E31: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E3E: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E3F: Wrong start point: contour 3 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E40: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E40: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E41: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E41: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E44: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E44: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E45: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E45: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E54: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E55: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E56: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E56: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E57: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E57: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E58: Wrong start point: contour 5 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E58: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E59: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E59: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E60: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E60: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E61: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E61: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E6A: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E6A: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E6B: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E6B: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Wacute: Wrong start point: contour 2 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in wacute: Wrong start point: contour 3 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Wdieresis: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Wdieresis: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Wdieresis: Wrong start point: contour 4 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Wdieresis: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in wdieresis: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in wdieresis: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in wdieresis: Wrong start point: contour 5 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in wdieresis: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E86: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E86: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E87: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E87: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8A: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8A: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8B: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8B: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8C: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8C: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8C: Wrong start point: contour 4 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8C: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8D: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8D: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8D: Wrong start point: contour 4 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8D: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8E: Wrong start point: contour 2 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8E: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8F: Wrong start point: contour 3 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E8F: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E97: Contour 2 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni1E97: Contour 4 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in minute: Wrong start point: contour 1 should start at 24 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in second: Wrong start point: contour 1 should start at 23 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in second: Wrong start point: contour 3 should start at 25 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni2219: Wrong start point: contour 1 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni2219: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni2236: Wrong start point: contour 1 should start at 18 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni2236: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni2236: Wrong start point: contour 3 should start at 18 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni2236: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni22C5: Wrong start point: contour 1 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in uni22C5: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 1 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 3 should start at 15 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 3 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 5 should start at 17 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 5 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 7 should start at 17 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 7 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 9 should start at 15 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 9 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 11 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 11 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 13 should start at 15 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 13 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 15 should start at 15 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 15 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 17 should start at 15 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 17 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Wrong start point: contour 19 should start at 13 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in dottedcircle: Contour 19 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Eth: Wrong start point: contour 2 should start at 7 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in Dcroat: Wrong start point: contour 2 should start at 7 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in exclamdown: Wrong start point: contour 1 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in exclamdown: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in questiondown: Wrong start point: contour 2 should start at 41 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotesinglbase: Wrong start point: contour 1 should start at 20 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotedblbase: Wrong start point: contour 1 should start at 22 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in quotedblbase: Wrong start point: contour 3 should start at 20 in wght=900 (and contour should be reversed) [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in periodcentered.loclCAT: Wrong start point: contour 1 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in periodcentered.loclCAT: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in periodcentered.loclCAT.case: Wrong start point: contour 1 should start at 14 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in periodcentered.loclCAT.case: Contour 1 becomes underweight in wght=900 compared to default [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in _Dsmall: Wrong start point: contour 2 should start at 7 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in D.circled: Wrong start point: contour 4 should start at 7 in wght=900 [code: interpolation-issue]
  
  


- ⚠️ **WARN** Interpolation issue in D_d: Wrong start point: contour 2 should start at 7 in wght=900 [code: interpolation-issue]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure variable fonts include an avar table. (mandatory_avar_table)</summary>
    <div>


> Most variable fonts should include an avar table to correctly define axes progression rates.
> 
> For example, a weight axis from 0% to 100% doesn't map directly to 100 to 1000, because a 10% progression from 0% may be too much to define the 200, while 90% may be too little to define the 900.
> 
> If the progression rates of axes is linear, this check can be ignored. Fontmake will also skip adding an avar table if the progression rates are linear. However, it is still recommended that designers visually proof each instance is at the expected weight, width etc.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3100]





- ⚠️ **WARN** The font does not include an avar table.  If the progression rates of axes is linear and no user-mapping is expected, this is fine, and this check can be ignored or excluded. [code: missing-avar]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. (math_signs_width)</summary>
    <div>


> #,         It is a common practice to have math signs sharing the same width         (preferably the same width as tabular figures accross the entire font family).
> 
> This probably comes from the will to avoid additional tabular math signs knowing that their design can easily share the same width.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3832]





- ⚠️ **WARN** The most common width is 679 among a set of 18  math glyphs.
The following math glyphs have a different width, though:
width=605: uni223C
width=512: divide, minus
width=730: uni2252, uni2243, congruent
width=469: logicalnot
width=731: approxequal
width=644: plus, lessequal, less
width=661: plusminus
width=451: multiply, greater
width=574: greaterequal [code: width-outliers]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Ensure font has overlaps bit set correctly. (overlaps_bit)</summary>
    <div>


> Fonts whose glyphs contain overlapping paths should have the overlaps bit set correctly to avoid rendering errors. (See for example https://github.com/google/fonts/issues/11120)
> 
> This should normally be done by the font compiler, but some compilers do not correctly set the bit.




Original proposal: [https://github.com/googlefonts/gftools/pulls/965]





- ⚠️ **WARN** The following glyphs have overlaps but the overlaps bit is not set:
* iacute (U+00ED)
* uni014F (U+014F)
* uni012D (U+012D)
* uring (U+016F)
* Aogonek (U+0104)
* increment (U+2206)
* Yacute (U+00DD)
* ecircumflex (U+00EA)
* ydieresis (U+00FF)
... and 384 others [code: no-overlaps-bit]
  
  


- ⚠️ **WARN** The following glyphs do not have overlaps but the overlaps bit is set:
* longs (U+017F)
* dotaccent (U+02D9)
* Scommaaccent (U+0218)
* caroncomb.alt
* circumflex (U+02C6)
* caroncomb (U+030C)
* upBlackSmallTriangle (U+25B4)
* circumflexcomb_gravecomb
* idotbelow (U+1ECB)
... and 53 others [code: overlaps-bit-set]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Shapes languages in all GF glyphsets. (googlefonts/glyphsets/shape_languages)</summary>
    <div>


> This check uses a heuristic to determine which GF glyphsets a font supports. Then it checks the font for correct shaping behaviour for all languages in those glyphsets.




Original proposal: [https://github.com/googlefonts/fontbakery/issues/4147]





- ⚠️ **WARN** Warning language shaping:

| Message                                                           | Languages                    |
|-------------------------------------------------------------------|------------------------------|
| Auxiliary orthography codepoints:                                 | * nl_Latn (Dutch)            |
|   The following auxiliary characters are missing from the font: Ĳ |                              |
|   The following auxiliary characters are missing from the font: ĳ |                              |
| Auxiliary orthography codepoints:                                 | * fi_Latn (Finnish)          |
|   The following auxiliary characters are missing from the font: Ǥ |                              |
|   The following auxiliary characters are missing from the font: Ŋ |                              |
|   The following auxiliary characters are missing from the font: Ŧ |                              |
|   The following auxiliary characters are missing from the font: Ʒ |                              |
|   The following auxiliary characters are missing from the font: Ǯ |                              |
|   The following auxiliary characters are missing from the font: ǥ |                              |
|   The following auxiliary characters are missing from the font: ŋ |                              |
|   The following auxiliary characters are missing from the font: ŧ |                              |
|   The following auxiliary characters are missing from the font: ʒ |                              |
|   The following auxiliary characters are missing from the font: ǯ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ŋ |                              |
|   The following auxiliary characters are missing from the font: Ŧ |                              |
|   The following auxiliary characters are missing from the font: ŋ |                              |
|   The following auxiliary characters are missing from the font: ŧ |                              |
| Auxiliary orthography codepoints:                                 | * ca_Latn (Catalan)          |
|   The following auxiliary characters are missing from the font: Ŀ |                              |
|   The following auxiliary characters are missing from the font: ŀ |                              |
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              |
| Auxiliary orthography codepoints:                                 | * en_Latn (English)          |
|   The following auxiliary characters are missing from the font: ʻ |                              | [code: warning-language-shaping]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check the direction of the outermost contour in each glyph (outline_direction)</summary>
    <div>


> In TrueType fonts, the outermost contour of a glyph should be oriented clockwise, while the inner contours should be oriented counter-clockwise. Getting the path direction wrong can lead to rendering issues in some software.




Original proposal: [https://github.com/fonttools/fontbakery/issues/2056]





- ⚠️ **WARN** The following glyphs have a counter-clockwise outer contour:

* .notdef has a counter-clockwise outer contour
* zero (U+0030) has a counter-clockwise outer contour
* one (U+0031) has a counter-clockwise outer contour
* two (U+0032) has a counter-clockwise outer contour
* three (U+0033) has a counter-clockwise outer contour
* four (U+0034) has a counter-clockwise outer contour
* five (U+0035) has a counter-clockwise outer contour
* six (U+0036) has a counter-clockwise outer contour
* seven (U+0037) has a counter-clockwise outer contour
... and 1529 others [code: ccw-outer-contour]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments (overlapping_path_segments)</summary>
    <div>


> Some rasterizers encounter difficulties when rendering glyphs with overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points. When two segments share the same coordinates, they are considered overlapping.




Original proposal: [https://github.com/google/fonts/issues/7594#issuecomment-2401909084]





- ⚠️ **WARN** The following glyphs have overlapping path segments:

* .notdef: Line(Line { p0: (39.0, -105.0), p1: (42.0, -108.0) }) has the same coordinates as a previous segment.
* .notdef: Line(Line { p0: (42.0, -108.0), p1: (45.0, -111.0) }) has the same coordinates as a previous segment.
* .notdef: Line(Line { p0: (45.0, -111.0), p1: (50.0, -112.0) }) has the same coordinates as a previous segment.
* .notdef: Line(Line { p0: (38.0, -100.0), p1: (39.0, -105.0) }) has the same coordinates as a previous segment.
* paragraph (U+00B6): Line(Line { p0: (217.0, 699.0), p1: (214.0, 696.0) }) has the same coordinates as a previous segment.
* paragraph (U+00B6): Line(Line { p0: (214.0, 696.0), p1: (211.0, 693.0) }) has the same coordinates as a previous segment.
* paragraph (U+00B6): Line(Line { p0: (211.0, 693.0), p1: (210.0, 688.0) }) has the same coordinates as a previous segment.
* paragraph (U+00B6): Line(Line { p0: (222.0, 700.0), p1: (217.0, 699.0) }) has the same coordinates as a previous segment.
* whiteSmallSquare (U+25AB): Line(Line { p0: (34.0, 222.0), p1: (35.0, 217.0) }) has the same coordinates as a previous segment.
... and 3 others [code: overlapping-path-segments]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. (googlefonts/vendor_id)</summary>
    <div>


> Microsoft keeps a list of font vendors and their respective contact info. This list is updated regularly and is indexed by a 4-char "Vendor ID" which is stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some applications may display the type designer / type foundry contact info on some dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in that list or if it has some of the default values used by the most common font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs. If you registered recently, you're safe to ignore warnings emitted by this check, since your ID will soon be included in one of our upcoming releases.




Original proposal: [https://github.com/fonttools/fontbakery/issues/3943, https://github.com/fonttools/fontbakery/issues/4829]





- ⚠️ **WARN** OS/2 VendorID value 'AKHL' is not yet recognized.
If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at https://www.microsoft.com/typography/links/vendorlist.aspx
 [code: unknown]
  
  

</div>
</details>





<details>
    <summary>⚠️ <b>WARN</b> Check font follows the Google Fonts vertical metric schema (googlefonts/vertical_metrics)</summary>
    <div>


> This check generally enforces Google Fonts’ vertical metrics specifications. In particular: * lineGap must be 0 * Sum of hhea ascender + abs(descender) + linegap must be   between 120% and 200% of UPM * Warning if sum is over 150% of UPM
> 
> The threshold levels 150% (WARN) and 200% (FAIL) are somewhat arbitrarily chosen and may hint at a glaring mistake in the metrics calculations or UPM settings.
> 
> Our documentation includes further information: https://github.com/googlefonts/gf-docs/tree/main/VerticalMetrics




Original proposal: [https://github.com/fonttools/fontbakery/pull/3762 and https://github.com/fonttools/fontbakery/pull/3921]





- ⚠️ **WARN** We recommend the absolute sum of the hhea metrics should be between 1.2-1.5x of the font's upm. This font has 1.506x (1506) [code: bad-hhea-range]
  
  

</div>
</details>


</div>
</details>






### Summary

| ⚠️ WARN | ℹ️ INFO | ✅ PASS | ⏩ SKIP | 
| ---|---|---|---|
| 649 | 22 | 243 | 95 | 
| 64% | 2% | 24% | 9% | 



