## FontSpector report

fontspector version: 1.9.0






## Check results




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
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, cherokee, tifinagh, coptic
* U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
* U+0307 COMBINING DOT ABOVE: try adding one of: duployan, syriac, tai-le, tifinagh, coptic, todhri, math, canadian-aboriginal, malayalam, old-permic, hebrew
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: tai-le, cherokee
... and 136 others

Or you can add the above codepoints to one of the subsets supported by the font: cyrillic-ext, latin-ext, latin, vietnamese [code: unreachable-subsetting]
  
  


- ⚠️ **WARN** AkhilNotes-Italic[wght].ttf: The following codepoints supported by the font are not covered by any subsets defined in the font's metadata file, and will never be served. You can solve this by either manually adding additional subset declarations to METADATA.pb, or by editing the glyphset definitions.

* U+02D8 BREVE: try adding one of: canadian-aboriginal, yi
* U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi
* U+02DB OGONEK: try adding one of: yi, canadian-aboriginal
* U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, cherokee, tifinagh, coptic
* U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh
* U+0307 COMBINING DOT ABOVE: try adding one of: duployan, syriac, tai-le, tifinagh, coptic, todhri, math, canadian-aboriginal, malayalam, old-permic, hebrew
* U+030A COMBINING RING ABOVE: try adding one of: duployan, syriac
* U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee
* U+030C COMBINING CARON: try adding one of: tai-le, cherokee
... and 136 others

Or you can add the above codepoints to one of the subsets supported by the font: cyrillic-ext, latin-ext, latin, vietnamese [code: unreachable-subsetting]
  
  

</div>
</details>


</div>
</details>


<details><summary>[8] AkhilNotes[wght].ttf</summary>
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





- ⚠️ **WARN** The most common width is 644 among a set of 18  math glyphs.
The following math glyphs have a different width, though:
width=451: greater, multiply
width=512: divide, minus
width=679: notequal, equal, uni2262
width=730: uni2252, uni2243, congruent
width=731: approxequal
width=605: uni223C
width=574: greaterequal
width=661: plusminus
width=469: logicalnot [code: width-outliers]
  
  

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
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              |
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
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ŋ |                              |
|   The following auxiliary characters are missing from the font: Ŧ |                              |
|   The following auxiliary characters are missing from the font: ŋ |                              |
|   The following auxiliary characters are missing from the font: ŧ |                              | [code: warning-language-shaping]
  
  

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


<details><summary>[8] AkhilNotes-Italic[wght].ttf</summary>
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





- ⚠️ **WARN** The most common width is 719 among a set of 18  math glyphs.
The following math glyphs have a different width, though:
width=587: divide, minus
width=730: uni2243, congruent, uni2252
width=526: greater, multiply
width=605: uni223C
width=736: plusminus
width=754: notequal, equal, uni2262
width=649: greaterequal
width=806: approxequal
width=473: logicalnot [code: width-outliers]
  
  

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
| Auxiliary orthography codepoints:                                 | * da_Latn (Danish)           |
|   The following auxiliary characters are missing from the font: Ǿ |                              |
|   The following auxiliary characters are missing from the font: ǿ |                              |
| Auxiliary orthography codepoints:                                 | * nb_Latn (Norwegian Bokmål) |
|   The following auxiliary characters are missing from the font: Ŋ |                              |
|   The following auxiliary characters are missing from the font: Ŧ |                              |
|   The following auxiliary characters are missing from the font: ŋ |                              |
|   The following auxiliary characters are missing from the font: ŧ |                              |
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
|   The following auxiliary characters are missing from the font: ǯ |                              | [code: warning-language-shaping]
  
  

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






### Summary

| ⚠️ WARN | ℹ️ INFO | ✅ PASS | ⏩ SKIP | 
| ---|---|---|---|
| 18 | 22 | 247 | 95 | 
| 5% | 6% | 65% | 25% | 



