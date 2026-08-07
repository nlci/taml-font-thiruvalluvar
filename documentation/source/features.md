---
title: NLCI Tamil - Font Features
fontversion: 0.901
---

The NLCI Tamil fonts have some optional features that may be useful or required for particular uses or languages. This document lists all the available features.

These OpenType features are primarily specified using four-letter tags (e.g. 'cv01'). For more information on how to access OpenType features in specific environments and applications, see [Using Font Features](https://software.sil.org/fonts/features).

This page uses web fonts (WOFF2) to demonstrate font features and should display correctly in all modern browsers. For a more concise example of how to use the NLCI Tamil fonts as a web font see [ThiruValluvar Webfont Example](../web/ThiruValluvar-webfont-example.html). SIL has detailed information, see [Using SIL Fonts on Web Pages](https://software.sil.org/fonts/webfonts).

*If this document is not displaying correctly a PDF version is also provided in the documentation/pdf folder of the release package.*

## Complete feature list

### Languages

The language specific forms are supported by both OpenType and Graphite.

*Unlike other features this support is activated by tagging the span of text as being in a particular language, not by turning on an OpenType feature.*

Unfortunately, the UI needed to access the language-specific behavior is not yet present in many applications.
Therefore, there are pre-built fonts some of the languages.

<span class='affects'>Affects: U+0323 U+1133B U+1133C</span>

Language | 0323 | 1133B | 1133C | Language setting
-------- | ---- | ----- | ----- | -------
Default  | <span class='thiruvalluvar-R normal'>க̣</span> | <span class='thiruvalluvar-R normal'>க𑌻</span> | <span class='thiruvalluvar-R normal'>க𑌼</span> |
Chetti   | <span class='thiruvalluvar-R normal' lang='ctt'>க̣</span> | <span class='thiruvalluvar-R normal' lang='ctt'>க𑌻</span> | <span class='thiruvalluvar-R normal' lang='ctt'>க𑌼</span> | `lang=ctt`
Irula    | <span class='thiruvalluvar-R normal' lang='iru'>க̣</span> | <span class='thiruvalluvar-R normal' lang='iru'>க𑌻</span> | <span class='thiruvalluvar-R normal' lang='iru'>க𑌼</span> | `lang=iru`

### Character variants

#### Nuktas

The character variants are supported by both OpenType and Graphite.

<span class='affects'>Affects: U+0323 U+1133B U+1133C</span>

Feature | 0323 | 1133B | 1133C | Feature setting
------- | ---- | ----- | ----- | -------
Single ring | <span class='thiruvalluvar-R normal'>க̣</span> | <span class='thiruvalluvar-R normal'>க𑌻</span> | <span class='thiruvalluvar-R normal'>க𑌼</span> | `cv01=0`
Double dot  | <span class='thiruvalluvar-R normal' style='font-feature-settings: "cv01" 1'>க̣</span> | <span class='thiruvalluvar-R normal' style='font-feature-settings: "cv01" 1'>க𑌻</span> | <span class='thiruvalluvar-R normal' style='font-feature-settings: "cv01" 1'>க𑌼</span> | `cv01=1`
Single dot  | <span class='thiruvalluvar-R normal' style='font-feature-settings: "cv01" 2'>க̣</span> | <span class='thiruvalluvar-R normal' style='font-feature-settings: "cv01" 2'>க𑌻</span> | <span class='thiruvalluvar-R normal' style='font-feature-settings: "cv01" 2'>க𑌼</span> | `cv01=2`
Double ring | <span class='thiruvalluvar-R normal' style='font-feature-settings: "cv01" 3'>க̣</span> | <span class='thiruvalluvar-R normal' style='font-feature-settings: "cv01" 3'>க𑌻</span> | <span class='thiruvalluvar-R normal' style='font-feature-settings: "cv01" 3'>க𑌼</span> | `cv01=3`

### Stylistic sets

The following stylistic sets are supported in OpenType, but not Graphite.

#### Tamil to Latin Digits <a id="ss19"></a>

<span class='affects'>Affects: U+0BE6 U+0BE7 U+0BE8 U+0BE9 U+0BEA U+0BEB U+0BEC U+0BED U+0BEE U+0BEF</span>

Feature | Sample | Feature setting
------- | ---------------------------- | -------
Default | <span class='thiruvalluvar-R normal'>௦ ௧ ௨ ௩ ௪ ௫ ௬ ௭ ௮ ௯</span> | `ss19=0`
Tamil to Latin Digits | <span class='thiruvalluvar-R normal' style='font-feature-settings: "ss19" 1'>௦ ௧ ௨ ௩ ௪ ௫ ௬ ௭ ௮ ௯</span> | `ss19=1`

#### Latin to Tamil Digits <a id="ss20"></a>

<span class='affects'>Affects: U+0030 U+0031 U+0032 U+0033 U+0034 U+0035 U+0036 U+0037 U+0038 U+0039</span>

Feature | Sample | Feature setting
------- | ---------------------------- | -------
Default | <span class='thiruvalluvar-R normal'>0 1 2 3 4 5 6 7 8 9</span> | `ss20=0`
Latin to Tamil Digits | <span class='thiruvalluvar-R normal' style='font-feature-settings: "ss20" 1'>0 1 2 3 4 5 6 7 8 9</span> | `ss20=1`
