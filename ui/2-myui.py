#! /usr/bin/env python3

from PyQt5 import QtWidgets, QtGui, QtCore
from ui import Ui_Dialog
import sys

data='''

<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale=1">
<link rel="profile" href="https://gmpg.org/xfn/11">
<link rel="pingback" href="https://clay-atlas.com/xmlrpc.php">
<meta name='robots' content='index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' />
<link rel="alternate" href="https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/" hreflang="zh" />
<link rel="alternate" href="https://clay-atlas.com/us/blog/2019/09/17/python-english-tutorial-pyqt5-label-lineedit-pushbutton/" hreflang="en" />

<meta name="google-site-verification" content="vjlQUFO0r6TN0RINgqDRwzQpZ_oOk0JeCJAaRcrL3fQ" />
<meta name="yandex-verification" content="9296aed640301d0e" />

<title>[PyQt5] 基本教學(2) QLabel, QLineEdit, QPushButton - Clay-Technology World</title>
<meta name="description" content="今天將會紀錄該如何使用 Python 撰寫 PyQt5 中的 QLabel、QLineEdit、QPushButton 等等的元件，並使用 clicked.connect() 來撰寫我們按鈕的事件。若會這些功能，基本上已經可以寫出一些相當陽春的程式了。" />
<link rel="canonical" href="https://clay-atlas.com/blog/2019/08/27/pyqt5-基本教學-2-qlabel-qlineedit-qpushbutton/" />
<meta property="og:locale" content="zh_TW" />
<meta property="og:locale:alternate" content="en_US" />
<meta property="og:type" content="article" />
<meta property="og:title" content="[PyQt5] 基本教學(2) QLabel, QLineEdit, QPushButton - Clay-Technology World" />
<meta property="og:description" content="今天將會紀錄該如何使用 Python 撰寫 PyQt5 中的 QLabel、QLineEdit、QPushButton 等等的元件，並使用 clicked.connect() 來撰寫我們按鈕的事件。若會這些功能，基本上已經可以寫出一些相當陽春的程式了。" />
<meta property="og:url" content="https://clay-atlas.com/blog/2019/08/27/pyqt5-基本教學-2-qlabel-qlineedit-qpushbutton/" />
<meta property="og:site_name" content="Clay-Technology World" />
<meta property="article:published_time" content="2019-08-27T09:14:36+00:00" />
<meta property="article:modified_time" content="2021-04-08T13:06:31+00:00" />
<meta property="og:image" content="https://clay-atlas.com/wp-content/uploads/2020/09/Python_PyQt5.png" />
<meta property="og:image:width" content="768" />
<meta property="og:image:height" content="801" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:label1" content="Written by" />
<meta name="twitter:data1" content="Clay" />
<meta name="twitter:label2" content="Est. reading time" />
<meta name="twitter:data2" content="4 分鐘" />
<script type="application/ld+json" class="yoast-schema-graph">{"@context":"https://schema.org","@graph":[{"@type":"WebSite","@id":"https://clay-atlas.com/#website","url":"https://clay-atlas.com/","name":"Clay-Technology World","description":"Hope every day is better than yesterday","publisher":{"@id":"https://clay-atlas.com/#/schema/person/c8bfcc3ce56147efc88cdd6f7733a766"},"potentialAction":[{"@type":"SearchAction","target":{"@type":"EntryPoint","urlTemplate":"https://clay-atlas.com/?s={search_term_string}"},"query-input":"required name=search_term_string"}],"inLanguage":"zh-TW"},{"@type":"ImageObject","@id":"https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/#primaryimage","inLanguage":"zh-TW","url":"https://i1.wp.com/clay-atlas.com/wp-content/uploads/2020/09/Python_PyQt5.png?fit=768%2C801&ssl=1","contentUrl":"https://i1.wp.com/clay-atlas.com/wp-content/uploads/2020/09/Python_PyQt5.png?fit=768%2C801&ssl=1","width":768,"height":801,"caption":"PyQt5 is a Python framework for developing interfaces"},{"@type":"WebPage","@id":"https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/#webpage","url":"https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/","name":"[PyQt5] \u57fa\u672c\u6559\u5b78(2) QLabel, QLineEdit, QPushButton - Clay-Technology World","isPartOf":{"@id":"https://clay-atlas.com/#website"},"primaryImageOfPage":{"@id":"https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/#primaryimage"},"datePublished":"2019-08-27T09:14:36+00:00","dateModified":"2021-04-08T13:06:31+00:00","description":"\u4eca\u5929\u5c07\u6703\u7d00\u9304\u8a72\u5982\u4f55\u4f7f\u7528 Python \u64b0\u5beb PyQt5 \u4e2d\u7684 QLabel\u3001QLineEdit\u3001QPushButton \u7b49\u7b49\u7684\u5143\u4ef6\uff0c\u4e26\u4f7f\u7528 clicked.connect() \u4f86\u64b0\u5beb\u6211\u5011\u6309\u9215\u7684\u4e8b\u4ef6\u3002\u82e5\u6703\u9019\u4e9b\u529f\u80fd\uff0c\u57fa\u672c\u4e0a\u5df2\u7d93\u53ef\u4ee5\u5beb\u51fa\u4e00\u4e9b\u76f8\u7576\u967d\u6625\u7684\u7a0b\u5f0f\u4e86\u3002","breadcrumb":{"@id":"https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/#breadcrumb"},"inLanguage":"zh-TW","potentialAction":[{"@type":"ReadAction","target":["https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/"]}]},{"@type":"BreadcrumbList","@id":"https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/#breadcrumb","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":"https://clay-atlas.com/"},{"@type":"ListItem","position":2,"name":"[PyQt5] \u57fa\u672c\u6559\u5b78(2) QLabel, QLineEdit, QPushButton"}]},{"@type":"Article","@id":"https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/#article","isPartOf":{"@id":"https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/#webpage"},"author":{"@id":"https://clay-atlas.com/#/schema/person/c8bfcc3ce56147efc88cdd6f7733a766"},"headline":"[PyQt5] \u57fa\u672c\u6559\u5b78(2) QLabel, QLineEdit, QPushButton","datePublished":"2019-08-27T09:14:36+00:00","dateModified":"2021-04-08T13:06:31+00:00","mainEntityOfPage":{"@id":"https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/#webpage"},"wordCount":450,"commentCount":2,"publisher":{"@id":"https://clay-atlas.com/#/schema/person/c8bfcc3ce56147efc88cdd6f7733a766"},"image":{"@id":"https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/#primaryimage"},"thumbnailUrl":"https://i1.wp.com/clay-atlas.com/wp-content/uploads/2020/09/Python_PyQt5.png?fit=768%2C801&ssl=1","keywords":["PyQt5","Python"],"articleSection":["PyQt5","Python"],"inLanguage":"zh-TW","potentialAction":[{"@type":"CommentAction","name":"Comment","target":["https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/#respond"]}]},{"@type":["Person","Organization"],"@id":"https://clay-atlas.com/#/schema/person/c8bfcc3ce56147efc88cdd6f7733a766","name":"Clay","image":{"@type":"ImageObject","@id":"https://clay-atlas.com/#personlogo","inLanguage":"zh-TW","url":"https://secure.gravatar.com/avatar/fb7c6baee50bb79acc3afb91e8e5a545?s=96&d=retro&r=g","contentUrl":"https://secure.gravatar.com/avatar/fb7c6baee50bb79acc3afb91e8e5a545?s=96&d=retro&r=g","caption":"Clay"},"logo":{"@id":"https://clay-atlas.com/#personlogo"},"sameAs":["https://clay-atlas.com","ccs96307"],"url":"https://clay-atlas.com/blog/author/ccs96307/"}]}</script>

<link rel='dns-prefetch' href='//secure.gravatar.com' />
<link rel='dns-prefetch' href='//www.googletagmanager.com' />
<link rel='dns-prefetch' href='//s.w.org' />
<link rel='dns-prefetch' href='//i0.wp.com' />
<link rel='dns-prefetch' href='//i1.wp.com' />
<link rel='dns-prefetch' href='//i2.wp.com' />
<link rel='dns-prefetch' href='//c0.wp.com' />
<link rel='dns-prefetch' href='//jetpack.wordpress.com' />
<link rel='dns-prefetch' href='//s0.wp.com' />
<link rel='dns-prefetch' href='//s1.wp.com' />
<link rel='dns-prefetch' href='//s2.wp.com' />
<link rel='dns-prefetch' href='//public-api.wordpress.com' />
<link rel='dns-prefetch' href='//0.gravatar.com' />
<link rel='dns-prefetch' href='//1.gravatar.com' />
<link rel='dns-prefetch' href='//2.gravatar.com' />
<link rel='dns-prefetch' href='//widgets.wp.com' />
<link rel='dns-prefetch' href='//pagead2.googlesyndication.com' />
<link rel="alternate" type="application/rss+xml" title="訂閱《Clay-Technology World》&raquo; 資訊提供" href="https://clay-atlas.com/feed/" />
<link rel="alternate" type="application/rss+xml" title="訂閱《Clay-Technology World》&raquo; 留言的資訊提供" href="https://clay-atlas.com/comments/feed/" />
<link rel="alternate" type="application/rss+xml" title="訂閱《Clay-Technology World 》&raquo;〈[PyQt5] 基本教學(2) QLabel, QLineEdit, QPushButton〉留言的資訊提供" href="https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/feed/" />
<script type="text/javascript">
			window._wpemojiSettings = {"baseUrl":"https:\/\/s.w.org\/images\/core\/emoji\/13.1.0\/72x72\/","ext":".png","svgUrl":"https:\/\/s.w.org\/images\/core\/emoji\/13.1.0\/svg\/","svgExt":".svg","source":{"concatemoji":"https:\/\/clay-atlas.com\/wp-includes\/js\/wp-emoji-release.min.js?ver=5.8.1"}};
			!function(e,a,t){var n,r,o,i=a.createElement("canvas"),p=i.getContext&&i.getContext("2d");function s(e,t){var a=String.fromCharCode;p.clearRect(0,0,i.width,i.height),p.fillText(a.apply(this,e),0,0);e=i.toDataURL();return p.clearRect(0,0,i.width,i.height),p.fillText(a.apply(this,t),0,0),e===i.toDataURL()}function c(e){var t=a.createElement("script");t.src=e,t.defer=t.type="text/javascript",a.getElementsByTagName("head")[0].appendChild(t)}for(o=Array("flag","emoji"),t.supports={everything:!0,everythingExceptFlag:!0},r=0;r<o.length;r++)t.supports[o[r]]=function(e){if(!p||!p.fillText)return!1;switch(p.textBaseline="top",p.font="600 32px Arial",e){case"flag":return s([127987,65039,8205,9895,65039],[127987,65039,8203,9895,65039])?!1:!s([55356,56826,55356,56819],[55356,56826,8203,55356,56819])&&!s([55356,57332,56128,56423,56128,56418,56128,56421,56128,56430,56128,56423,56128,56447],[55356,57332,8203,56128,56423,8203,56128,56418,8203,56128,56421,8203,56128,56430,8203,56128,56423,8203,56128,56447]);case"emoji":return!s([10084,65039,8205,55357,56613],[10084,65039,8203,55357,56613])}return!1}(o[r]),t.supports.everything=t.supports.everything&&t.supports[o[r]],"flag"!==o[r]&&(t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&t.supports[o[r]]);t.supports.everythingExceptFlag=t.supports.everythingExceptFlag&&!t.supports.flag,t.DOMReady=!1,t.readyCallback=function(){t.DOMReady=!0},t.supports.everything||(n=function(){t.readyCallback()},a.addEventListener?(a.addEventListener("DOMContentLoaded",n,!1),e.addEventListener("load",n,!1)):(e.attachEvent("onload",n),a.attachEvent("onreadystatechange",function(){"complete"===a.readyState&&t.readyCallback()})),(n=t.source||{}).concatemoji?c(n.concatemoji):n.wpemoji&&n.twemoji&&(c(n.twemoji),c(n.wpemoji)))}(window,document,window._wpemojiSettings);
		</script>
<style type="text/css">
img.wp-smiley,
img.emoji {
	display: inline !important;
	border: none !important;
	box-shadow: none !important;
	height: 1em !important;
	width: 1em !important;
	margin: 0 .07em !important;
	vertical-align: -0.1em !important;
	background: none !important;
	padding: 0 !important;
}
</style>
<link rel='stylesheet' id='wp-block-library-css' href='https://c0.wp.com/c/5.8.1/wp-includes/css/dist/block-library/style.min.css' type='text/css' media='all' />
<style id='wp-block-library-inline-css' type='text/css'>
.has-text-align-justify{text-align:justify;}
</style>
<link rel='stylesheet' id='mediaelement-css' href='https://c0.wp.com/c/5.8.1/wp-includes/js/mediaelement/mediaelementplayer-legacy.min.css' type='text/css' media='all' />
<link rel='stylesheet' id='wp-mediaelement-css' href='https://c0.wp.com/c/5.8.1/wp-includes/js/mediaelement/wp-mediaelement.min.css' type='text/css' media='all' />
<link rel='stylesheet' id='email-subscribers-css' href='https://clay-atlas.com/wp-content/plugins/email-subscribers/lite/public/css/email-subscribers-public.css?ver=4.8.0' type='text/css' media='all' />
<link rel='stylesheet' id='neve-style-css' href='https://clay-atlas.com/wp-content/themes/neve/assets/css/style-legacy.min.css?ver=3.0.3' type='text/css' media='all' />
<style id='neve-style-inline-css' type='text/css'>
.header-menu-sidebar-inner li.menu-item-nav-search { display: none; }
		[data-row-id] .row { display: flex !important; align-items: center; flex-wrap: unset;}
		@media (max-width: 960px) { .footer--row .row { flex-direction: column; } }
.nv-meta-list li.meta:not(:last-child):after { content:"/" }
 .container{ max-width: 748px; } .has-neve-button-color-color{ color: var(--nv-primary-accent)!important; } .has-neve-button-color-background-color{ background-color: var(--nv-primary-accent)!important; } .single-post-container .alignfull > [class*="__inner-container"], .single-post-container .alignwide > [class*="__inner-container"]{ max-width:718px } .button.button-primary, button, input[type=button], .btn, input[type="submit"], /* Buttons in navigation */ ul[id^="nv-primary-navigation"] li.button.button-primary > a, .menu li.button.button-primary > a, .wp-block-button.is-style-primary .wp-block-button__link, .wc-block-grid .wp-block-button .wp-block-button__link, form input[type="submit"], form button[type="submit"]{ background-color: var(--nv-primary-accent);color: #ffffff;border-radius:3px 3px 3px 3px;border:none;border-width:1px 1px 1px 1px; } .button.button-primary:hover, ul[id^="nv-primary-navigation"] li.button.button-primary > a:hover, .menu li.button.button-primary > a:hover, .wp-block-button.is-style-primary .wp-block-button__link:hover, .wc-block-grid .wp-block-button .wp-block-button__link:hover, form input[type="submit"]:hover, form button[type="submit"]:hover{ background-color: var(--nv-primary-accent);color: #ffffff; } .button.button-secondary:not(.secondary-default), .wp-block-button.is-style-secondary .wp-block-button__link{ background-color: var(--nv-primary-accent);color: #ffffff;border-radius:3px 3px 3px 3px;border:none;border-width:1px 1px 1px 1px; } .button.button-secondary.secondary-default{ background-color: var(--nv-primary-accent);color: #ffffff;border-radius:3px 3px 3px 3px;border:none;border-width:1px 1px 1px 1px; } .button.button-secondary:not(.secondary-default):hover, .wp-block-button.is-style-secondary .wp-block-button__link:hover{ background-color: var(--nv-primary-accent);color: #ffffff; } .button.button-secondary.secondary-default:hover{ background-color: var(--nv-primary-accent);color: #ffffff; } body, .site-title{ font-size: 15px; line-height: 1.6em; letter-spacing: 0px; font-weight: 400; text-transform: none; font-family: Arial, Helvetica, sans-serif, var(--nv-fallback-ff); } form input:read-write, form textarea, form select, form select option, form.wp-block-search input.wp-block-search__input, .widget select{ color: var(--nv-text-color); font-family: Arial, Helvetica, sans-serif, var(--nv-fallback-ff); } form.search-form input:read-write{ padding-right:45px !important; font-family: Arial, Helvetica, sans-serif, var(--nv-fallback-ff); } .header-main-inner,.header-main-inner a:not(.button),.header-main-inner .navbar-toggle{ color: var(--nv-site-bg); } .header-main-inner .nv-icon svg,.header-main-inner .nv-contact-list svg{ fill: var(--nv-site-bg); } .header-main-inner .icon-bar{ background-color: var(--nv-site-bg); } .hfg_header .header-main-inner .nav-ul .sub-menu{ background-color: #000000; } .hfg_header .header-main-inner{ background-color: #000000; } .header-menu-sidebar .header-menu-sidebar-bg,.header-menu-sidebar .header-menu-sidebar-bg a:not(.button),.header-menu-sidebar .header-menu-sidebar-bg .navbar-toggle{ color: var(--nv-text-color); } .header-menu-sidebar .header-menu-sidebar-bg .nv-icon svg,.header-menu-sidebar .header-menu-sidebar-bg .nv-contact-list svg{ fill: var(--nv-text-color); } .header-menu-sidebar .header-menu-sidebar-bg .icon-bar{ background-color: var(--nv-text-color); } .hfg_header .header-menu-sidebar .header-menu-sidebar-bg .nav-ul .sub-menu{ background-color: var(--nv-site-bg); } .hfg_header .header-menu-sidebar .header-menu-sidebar-bg{ background-color: var(--nv-site-bg); } .header-menu-sidebar{ width: 360px; } .builder-item--logo .site-logo img{ max-width: 120px; } .builder-item--logo .site-logo{ padding:10px 0px 10px 0px; } .builder-item--logo{ margin:0px 0px 0px 0px; } .builder-item--nav-icon .navbar-toggle{ padding:10px 15px 10px 15px; } .builder-item--nav-icon{ margin:0px 0px 0px 0px; } .builder-item--primary-menu .nav-menu-primary > .nav-ul li:not(.woocommerce-mini-cart-item) > a,.builder-item--primary-menu .nav-menu-primary > .nav-ul .has-caret > a,.builder-item--primary-menu .nav-menu-primary > .nav-ul .neve-mm-heading span,.builder-item--primary-menu .nav-menu-primary > .nav-ul .has-caret{ color: #939393; } .builder-item--primary-menu .nav-menu-primary > .nav-ul li:not(.woocommerce-mini-cart-item) > a:after,.builder-item--primary-menu .nav-menu-primary > .nav-ul li > .has-caret > a:after{ background-color: #0b95ff; } .builder-item--primary-menu .nav-menu-primary > .nav-ul li:not(.woocommerce-mini-cart-item):hover > a,.builder-item--primary-menu .nav-menu-primary > .nav-ul li:hover > .has-caret > a,.builder-item--primary-menu .nav-menu-primary > .nav-ul li:hover > .has-caret{ color: #0b95ff; } .builder-item--primary-menu .nav-menu-primary > .nav-ul li:hover > .has-caret svg{ fill: #0b95ff; } .builder-item--primary-menu .nav-menu-primary > .nav-ul li.current-menu-item > a,.builder-item--primary-menu .nav-menu-primary > .nav-ul li.current_page_item > a,.builder-item--primary-menu .nav-menu-primary > .nav-ul li.current_page_item > .has-caret > a{ color: #4e6fff; } .builder-item--primary-menu .nav-menu-primary > .nav-ul li.current-menu-item > .has-caret svg{ fill: #4e6fff; } .builder-item--primary-menu .nav-ul > li:not(:last-of-type){ margin-right:20px; } .builder-item--primary-menu .style-full-height .nav-ul li:not(.menu-item-nav-search):not(.menu-item-nav-cart):hover > a:after{ width: calc(100% + 20px); } .builder-item--primary-menu .nav-ul li a, .builder-item--primary-menu .neve-mm-heading span{ min-height: 25px; } .builder-item--primary-menu{ font-size: 1em; line-height: 1.6em; letter-spacing: 0px; font-weight: 500; text-transform: none;padding:0px 0px 0px 0px;margin:0px 0px 0px 0px; } .builder-item--primary-menu svg{ width: 1em;height: 1em; } .builder-item--header_search_responsive a.nv-search.nv-icon > svg{ width: 15px;height: 15px; } .builder-item--header_search_responsive input[type=submit],.builder-item--header_search_responsive .nv-search-icon-wrap{ width: 14px; } .builder-item--header_search_responsive .nv-nav-search .search-form input[type=search]{ height: 40px; font-size: 14px;padding-right:50px;border-width:1px 1px 1px 1px;border-radius:1px 1px 1px 1px; } .builder-item--header_search_responsive .nv-search-icon-wrap .nv-icon svg{ width: 14px;height: 14px; } .builder-item--header_search_responsive .close-responsive-search svg{ width: 14px;height: 14px; } .builder-item--header_search_responsive{ padding:0px 10px 0px 10px;margin:0px 0px 0px 0px; } .footer-top-inner{ background-color: #000000; } .footer-top-inner,.footer-top-inner a:not(.button),.footer-top-inner .navbar-toggle{ color: #ffffff; } .footer-top-inner .nv-icon svg,.footer-top-inner .nv-contact-list svg{ fill: #ffffff; } .footer-top-inner .icon-bar{ background-color: #ffffff; } .footer-top-inner .nav-ul .sub-menu{ background-color: #000000; } .footer-bottom-inner{ background-color: #000000; } .footer-bottom-inner,.footer-bottom-inner a:not(.button),.footer-bottom-inner .navbar-toggle{ color: #ffffff; } .footer-bottom-inner .nv-icon svg,.footer-bottom-inner .nv-contact-list svg{ fill: #ffffff; } .footer-bottom-inner .icon-bar{ background-color: #ffffff; } .footer-bottom-inner .nav-ul .sub-menu{ background-color: #000000; } .builder-item--footer-one-widgets{ padding:0px 0px 0px 0px;margin:0px 0px 0px 0px; } .builder-item--footer_copyright, .builder-item--footer_copyright *{ color: #000000; } .builder-item--footer_copyright{ font-size: 1em; line-height: 1.6em; letter-spacing: 0px; font-weight: 500; text-transform: none;padding:0px 0px 0px 0px;margin:0px 0px 0px 0px; } .builder-item--footer_copyright svg{ width: 1em;height: 1em; } @media(min-width: 576px){ .container{ max-width: 992px; } .single-post-container .alignfull > [class*="__inner-container"], .single-post-container .alignwide > [class*="__inner-container"]{ max-width:962px } body, .site-title{ font-size: 16px; line-height: 1.6em; letter-spacing: 0px; } .header-menu-sidebar{ width: 360px; } .builder-item--logo .site-logo img{ max-width: 120px; } .builder-item--logo .site-logo{ padding:10px 0px 10px 0px; } .builder-item--logo{ margin:0px 0px 0px 0px; } .builder-item--nav-icon .navbar-toggle{ padding:10px 15px 10px 15px; } .builder-item--nav-icon{ margin:0px 0px 0px 0px; } .builder-item--primary-menu .nav-ul > li:not(:last-of-type){ margin-right:20px; } .builder-item--primary-menu .style-full-height .nav-ul li:not(.menu-item-nav-search):not(.menu-item-nav-cart):hover > a:after{ width: calc(100% + 20px); } .builder-item--primary-menu .nav-ul li a, .builder-item--primary-menu .neve-mm-heading span{ min-height: 25px; } .builder-item--primary-menu{ font-size: 1em; line-height: 1.6em; letter-spacing: 0px;padding:0px 0px 0px 0px;margin:0px 0px 0px 0px; } .builder-item--primary-menu svg{ width: 1em;height: 1em; } .builder-item--header_search_responsive input[type=submit],.builder-item--header_search_responsive .nv-search-icon-wrap{ width: 14px; } .builder-item--header_search_responsive .nv-nav-search .search-form input[type=search]{ height: 40px; font-size: 14px;padding-right:50px;border-width:1px 1px 1px 1px;border-radius:1px 1px 1px 1px; } .builder-item--header_search_responsive .nv-search-icon-wrap .nv-icon svg{ width: 14px;height: 14px; } .builder-item--header_search_responsive .close-responsive-search svg{ width: 14px;height: 14px; } .builder-item--header_search_responsive{ padding:0px 10px 0px 10px;margin:0px 0px 0px 0px; } .builder-item--footer-one-widgets{ padding:0px 0px 0px 0px;margin:0px 0px 0px 0px; } .builder-item--footer_copyright{ font-size: 1em; line-height: 1.6em; letter-spacing: 0px;padding:0px 0px 0px 0px;margin:0px 0px 0px 0px; } .builder-item--footer_copyright svg{ width: 1em;height: 1em; } }@media(min-width: 960px){ .container{ max-width: 1289px; } body:not(.single):not(.archive):not(.blog):not(.search) .neve-main > .container .col, body.post-type-archive-course .neve-main > .container .col, body.post-type-archive-llms_membership .neve-main > .container .col{ max-width: 70%; } body:not(.single):not(.archive):not(.blog):not(.search) .nv-sidebar-wrap, body.post-type-archive-course .nv-sidebar-wrap, body.post-type-archive-llms_membership .nv-sidebar-wrap{ max-width: 30%; } .neve-main > .archive-container .nv-index-posts.col{ max-width: 70%; } .neve-main > .archive-container .nv-sidebar-wrap{ max-width: 30%; } .neve-main > .single-post-container .nv-single-post-wrap.col{ max-width: 70%; } .single-post-container .alignfull > [class*="__inner-container"], .single-post-container .alignwide > [class*="__inner-container"]{ max-width:872px } .container-fluid.single-post-container .alignfull > [class*="__inner-container"], .container-fluid.single-post-container .alignwide > [class*="__inner-container"]{ max-width:calc(70% + 15px) } .neve-main > .single-post-container .nv-sidebar-wrap{ max-width: 30%; } body, .site-title{ font-size: 18px; line-height: 1.6em; letter-spacing: 0px; } .header-menu-sidebar{ width: 360px; } .builder-item--logo .site-logo img{ max-width: 150px; } .builder-item--logo .site-logo{ padding:10px 0px 10px 0px; } .builder-item--logo{ margin:0px 0px 0px 0px; } .builder-item--nav-icon .navbar-toggle{ padding:10px 15px 10px 15px; } .builder-item--nav-icon{ margin:0px 0px 0px 0px; } .builder-item--primary-menu .nav-ul > li:not(:last-of-type){ margin-right:20px; } .builder-item--primary-menu .style-full-height .nav-ul li:not(.menu-item-nav-search):not(.menu-item-nav-cart) > a:after{ left:-10px;right:-10px } .builder-item--primary-menu .style-full-height .nav-ul li:not(.menu-item-nav-search):not(.menu-item-nav-cart):hover > a:after{ width: calc(100% + 20px); } .builder-item--primary-menu .nav-ul li a, .builder-item--primary-menu .neve-mm-heading span{ min-height: 25px; } .builder-item--primary-menu{ font-size: 1em; line-height: 1.6em; letter-spacing: 0px;padding:0px 0px 0px 0px;margin:0px 0px 0px 0px; } .builder-item--primary-menu svg{ width: 1em;height: 1em; } .builder-item--header_search_responsive input[type=submit],.builder-item--header_search_responsive .nv-search-icon-wrap{ width: 14px; } .builder-item--header_search_responsive .nv-nav-search .search-form input[type=search]{ height: 40px; font-size: 14px;padding-right:50px;border-width:1px 1px 1px 1px;border-radius:1px 1px 1px 1px; } .builder-item--header_search_responsive .nv-search-icon-wrap .nv-icon svg{ width: 14px;height: 14px; } .builder-item--header_search_responsive .close-responsive-search svg{ width: 14px;height: 14px; } .builder-item--header_search_responsive{ padding:0px 10px 0px 10px;margin:0px 0px 0px 0px; } .builder-item--footer-one-widgets{ padding:0px 0px 0px 0px;margin:0px 0px 0px 0px; } .builder-item--footer_copyright{ font-size: 1em; line-height: 1.6em; letter-spacing: 0px;padding:0px 0px 0px 0px;margin:0px 0px 0px 0px; } .builder-item--footer_copyright svg{ width: 1em;height: 1em; } }:root{--nv-primary-accent:#0366d6;--nv-secondary-accent:#0e509a;--nv-site-bg:#ffffff;--nv-light-bg:#ededed;--nv-dark-bg:#14171c;--nv-text-color:#393939;--nv-text-dark-bg:#ffffff;--nv-c-1:#77b978;--nv-c-2:#f37262;--nv-fallback-ff:Arial, Helvetica, sans-serif;}
</style>
<link rel='stylesheet' id='wp-featherlight-css' href='https://clay-atlas.com/wp-content/plugins/wp-featherlight/css/wp-featherlight.min.css?ver=1.3.4' type='text/css' media='all' />
<link rel='stylesheet' id='social-logos-css' href='https://c0.wp.com/p/jetpack/10.1/_inc/social-logos/social-logos.min.css' type='text/css' media='all' />
<link rel='stylesheet' id='jetpack_css-css' href='https://c0.wp.com/p/jetpack/10.1/css/jetpack.css' type='text/css' media='all' />
<script type='text/javascript' id='jetpack_related-posts-js-extra'>
/* <![CDATA[ */
var related_posts_js_options = {"post_heading":"h4"};
/* ]]> */
</script>
<script type='text/javascript' src='https://c0.wp.com/p/jetpack/10.1/_inc/build/related-posts/related-posts.min.js' id='jetpack_related-posts-js'></script>
<script type='text/javascript' src='https://c0.wp.com/c/5.8.1/wp-includes/js/jquery/jquery.min.js' id='jquery-core-js'></script>
<script type='text/javascript' src='https://c0.wp.com/c/5.8.1/wp-includes/js/jquery/jquery-migrate.min.js' id='jquery-migrate-js'></script>
<script type='text/javascript' id='email-subscribers-js-extra'>
/* <![CDATA[ */
var es_data = {"messages":{"es_empty_email_notice":"Please enter email address","es_rate_limit_notice":"You need to wait for sometime before subscribing again","es_single_optin_success_message":"Successfully Subscribed.","es_email_exists_notice":"Email Address already exists!","es_unexpected_error_notice":"Oops.. Unexpected error occurred.","es_invalid_email_notice":"Invalid email address","es_try_later_notice":"Please try after some time"},"es_ajax_url":"https:\/\/clay-atlas.com\/wp-admin\/admin-ajax.php"};
/* ]]> */
</script>
<script type='text/javascript' src='https://clay-atlas.com/wp-content/plugins/email-subscribers/lite/public/js/email-subscribers-public.js?ver=4.8.0' id='email-subscribers-js'></script>
<script type='text/javascript' src='https://www.googletagmanager.com/gtag/js?id=UA-144743596-1' id='google_gtagjs-js' async></script>
<script type='text/javascript' id='google_gtagjs-js-after'>
window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}
gtag('set', 'linker', {"domains":["clay-atlas.com"]} );
gtag("js", new Date());
gtag("set", "developer_id.dZTNiMT", true);
gtag("config", "UA-144743596-1", {"anonymize_ip":true});
</script>
<link rel="https://api.w.org/" href="https://clay-atlas.com/wp-json/" /><link rel="alternate" type="application/json" href="https://clay-atlas.com/wp-json/wp/v2/posts/422" /><link rel="EditURI" type="application/rsd+xml" title="RSD" href="https://clay-atlas.com/xmlrpc.php?rsd" />
<link rel="wlwmanifest" type="application/wlwmanifest+xml" href="https://clay-atlas.com/wp-includes/wlwmanifest.xml" />
<meta name="generator" content="WordPress 5.8.1" />
<link rel='shortlink' href='https://wp.me/pba1NM-6O' />
<link rel="alternate" type="application/json+oembed" href="https://clay-atlas.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fclay-atlas.com%2Fblog%2F2019%2F08%2F27%2Fpyqt5-%25e5%259f%25ba%25e6%259c%25ac%25e6%2595%2599%25e5%25ad%25b8-2-qlabel-qlineedit-qpushbutton%2F" />
<link rel="alternate" type="text/xml+oembed" href="https://clay-atlas.com/wp-json/oembed/1.0/embed?url=https%3A%2F%2Fclay-atlas.com%2Fblog%2F2019%2F08%2F27%2Fpyqt5-%25e5%259f%25ba%25e6%259c%25ac%25e6%2595%2599%25e5%25ad%25b8-2-qlabel-qlineedit-qpushbutton%2F&#038;format=xml" />
<meta name="generator" content="Site Kit by Google 1.40.0" /><style type='text/css'>img#wpstats{display:none}</style>
<style type="text/css">
				/* If html does not have either class, do not show lazy loaded images. */
				html:not( .jetpack-lazy-images-js-enabled ):not( .js ) .jetpack-lazy-image {
					display: none;
				}
			</style>
<script>
				document.documentElement.classList.add(
					'jetpack-lazy-images-js-enabled'
				);
			</script>
<script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script><script>(adsbygoogle = window.adsbygoogle || []).push({"google_ad_client":"ca-pub-5018964120096873","enable_page_level_ads":true,"tag_partner":"site_kit"});</script><link rel="icon" href="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2021/03/cropped-c-b-final.png?fit=32%2C32&#038;ssl=1" sizes="32x32" />
<link rel="icon" href="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2021/03/cropped-c-b-final.png?fit=192%2C192&#038;ssl=1" sizes="192x192" />
<link rel="apple-touch-icon" href="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2021/03/cropped-c-b-final.png?fit=180%2C180&#038;ssl=1" />
<meta name="msapplication-TileImage" content="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2021/03/cropped-c-b-final.png?fit=270%2C270&#038;ssl=1" />
<style type="text/css" id="wp-custom-css">
			/* Featured image alignment center */
.nv-post-thumbnail-wrap img {
		width: 400px;
    display: auto !important;
  	margin-left: auto !important;
  	margin-right: auto !important;
}

.nv-thumb-wrap img {
	  display:  !important;
		margin: center;
  	margin-left: center !important;
  	margin-right: center !important;
}

.nv-thumb-wrap img, .nv-post-thumbnail-wrap img {
    display: block !important;
  	margin-left: auto !important;
  	margin-right: auto !important;
}

/* Image border */
.imgBorder {
  border-radius: 8px;
  border: 1px solid #ddd;
	text-align: center;
}

.wp-block-image {
    text-align: center;
}


/* shortcode */
code {
	border-color: rgb(220,220,220);
	border-radius: 7px;
	background: rgb(245,245,245);

	padding: 1.8px;
	padding-left: 5px;
	padding-right: 5px;
}

.wp-block-code {
  border-color: rgb(220,220,220);
	border-width: 2px;
	background: rgb(245,245,245);
}


/* custom html css style */
.ccode {
	display: block;
	overflow-x: auto;
	white-space: pre;
}


/* tag cloud */
.tagcloud a { 
	display: inline-block;
  margin: 2px 2px;
  padding: 1px 8px;
	
	color: black;
	
	border-color: grey;
	border-width: 1px;
	border-style: solid;
  border-radius: 12px;
}


.wp-block-table {
	text-align: center;
}
		</style>
</head>
<body class="post-template-default single single-post postid-422 single-format-standard wp-custom-logo wp-featherlight-captions  nv-sidebar-right menu_sidebar_slide_left" id="neve_body">
<div class="wrapper">
<header class="header" role="banner" next-page-hide>
<a class="neve-skip-link show-on-focus" href="#content" tabindex="0">
Skip to content </a>
<div id="header-grid" class="hfg_header site-header">
<nav class="header--row header-main hide-on-mobile hide-on-tablet layout-full-contained nv-navbar header--row" data-row-id="main" data-show-on="desktop">
<div class="header--row-inner header-main-inner">
<div class="container">
<div class="row row--wrapper" data-section="hfg_header_layout_main">
<div class="builder-item hfg-item-first col-4 desktop-left"><div class="item--inner builder-item--logo" data-section="title_tagline" data-item-id="logo">
<div class="site-logo">
<a class="brand" href="https://clay-atlas.com/" title="Clay-Technology World" aria-label="Clay-Technology World"><div class="title-with-logo"><img width="350" height="350" src="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2021/03/cropped-output.png?fit=350%2C350&amp;ssl=1" class="skip-lazy" alt="" loading="lazy" srcset="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2021/03/cropped-output.png?w=350&amp;ssl=1 350w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2021/03/cropped-output.png?resize=300%2C300&amp;ssl=1 300w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2021/03/cropped-output.png?resize=150%2C150&amp;ssl=1 150w" sizes="(max-width: 350px) 100vw, 350px" /><div class="nv-title-tagline-wrap"><p class="site-title">Clay-Technology World</p><small>Hope every day is better than yesterday</small></div></div></a></div>
</div>
</div><div class="builder-item has-nav hfg-item-last col-8 desktop-right hfg-is-group"><div class="item--inner builder-item--primary-menu has_menu" data-section="header_menu_primary" data-item-id="primary-menu">
<div class="nv-nav-wrap">
<div role="navigation" class="style-border-bottom nav-menu-primary" aria-label="Primary Menu">
<ul id="nv-primary-navigation-main" class="primary-menu-ul nav-ul"><li id="menu-item-806" class="menu-item menu-item-type-post_type menu-item-object-page menu-item-806"><a href="https://clay-atlas.com/clays-blog-about-me/">About Me</a></li>
<li id="menu-item-5774" class="pll-parent-menu-item menu-item menu-item-type-custom menu-item-object-custom current-menu-parent menu-item-has-children menu-item-5774"><a href="#pll_switcher"><span class="menu-item-title-wrap"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAMAAABBPP0LAAAAVFBMVEUAILQAGrEAEazhAAD5AADwAACBot+5ued2mNv6aWv7X1/5UVHoAACWltz5+fz+/v5ahNPyRkv5QkL5OTn2MTH3Kir1JiZOe87rOkb1Hh70FRXyDQ3JFHMOAAAAU0lEQVR4AQXBgQ3CMBAAMV8+Iuy/LKhUgB0kRchDfksRbU59R1Xd14If51QNK3Ndc6im7Hg63DVhr/kct2pSr8WRahIWUk1i2XrHo7tYbB8IL/AHd28PeH6kKkoAAAAASUVORK5CYII=" alt="中文 (台灣)" width="16" height="11" style="width: 16px; height: 11px;" /><span style="margin-left:0.3em;">中文 (台灣)</span></span><div class="caret-wrap 2" tabindex="0"><span class="caret"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path d="M207.029 381.476L12.686 187.132c-9.373-9.373-9.373-24.569 0-33.941l22.667-22.667c9.357-9.357 24.522-9.375 33.901-.04L224 284.505l154.745-154.021c9.379-9.335 24.544-9.317 33.901.04l22.667 22.667c9.373 9.373 9.373 24.569 0 33.941L240.971 381.476c-9.373 9.372-24.569 9.372-33.942 0z" /></svg></span></div></a>
<ul class="sub-menu">
<li id="menu-item-5774-zh" class="lang-item lang-item-29 lang-item-zh current-lang lang-item-first menu-item menu-item-type-custom menu-item-object-custom menu-item-5774-zh"><a href="https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/" hreflang="zh-TW" lang="zh-TW"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAMAAABBPP0LAAAAVFBMVEUAILQAGrEAEazhAAD5AADwAACBot+5ued2mNv6aWv7X1/5UVHoAACWltz5+fz+/v5ahNPyRkv5QkL5OTn2MTH3Kir1JiZOe87rOkb1Hh70FRXyDQ3JFHMOAAAAU0lEQVR4AQXBgQ3CMBAAMV8+Iuy/LKhUgB0kRchDfksRbU59R1Xd14If51QNK3Ndc6im7Hg63DVhr/kct2pSr8WRahIWUk1i2XrHo7tYbB8IL/AHd28PeH6kKkoAAAAASUVORK5CYII=" alt="中文 (台灣)" width="16" height="11" style="width: 16px; height: 11px;" /><span style="margin-left:0.3em;">中文 (台灣)</span></a></li>
<li id="menu-item-5774-us" class="lang-item lang-item-36 lang-item-us menu-item menu-item-type-custom menu-item-object-custom menu-item-5774-us"><a href="https://clay-atlas.com/us/blog/2019/09/17/python-english-tutorial-pyqt5-label-lineedit-pushbutton/" hreflang="en-US" lang="en-US"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAMAAABBPP0LAAAAmVBMVEViZsViZMJiYrf9gnL8eWrlYkjgYkjZYkj8/PujwPybvPz4+PetraBEgfo+fvo3efkydfkqcvj8Y2T8UlL8Q0P8MzP9k4Hz8/Lu7u4DdPj9/VrKysI9fPoDc/EAZ7z7IiLHYkjp6ekCcOTk5OIASbfY/v21takAJrT5Dg6sYkjc3Nn94t2RkYD+y8KeYkjs/v7l5fz0dF22YkjWvcOLAAAAgElEQVR4AR2KNULFQBgGZ5J13KGGKvc/Cw1uPe62eb9+Jr1EUBFHSgxxjP2Eca6AfUSfVlUfBvm1Ui1bqafctqMndNkXpb01h5TLx4b6TIXgwOCHfjv+/Pz+5vPRw7txGWT2h6yO0/GaYltIp5PT1dEpLNPL/SdWjYjAAZtvRPgHJX4Xio+DSrkAAAAASUVORK5CYII=" alt="English" width="16" height="11" style="width: 16px; height: 11px;" /><span style="margin-left:0.3em;">English</span></a></li>
</ul>
</li>
</ul> </div>
</div>
</div>
<div class="item--inner builder-item--header_search_responsive" data-section="header_search_responsive" data-item-id="header_search_responsive">
<div class="nv-search-icon-component">
<div [class]="visible ? 'menu-item-nav-search active canvas' : 'menu-item-nav-search canvas'" class="menu-item-nav-search canvas" tabindex="0">
<a aria-label="Search" href="#" class="nv-icon nv-search">
<svg width="15" height="15" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg"><path d="M1216 832q0-185-131.5-316.5t-316.5-131.5-316.5 131.5-131.5 316.5 131.5 316.5 316.5 131.5 316.5-131.5 131.5-316.5zm512 832q0 52-38 90t-90 38q-54 0-90-38l-343-342q-179 124-399 124-143 0-273.5-55.5t-225-150-150-225-55.5-273.5 55.5-273.5 150-225 225-150 273.5-55.5 273.5 55.5 225 150 150 225 55.5 273.5q0 220-124 399l343 343q37 37 37 90z" /></svg>
</a> <div class="nv-nav-search" aria-label="search">
<div class="form-wrap container responsive-search">
<form role="search" method="get" class="search-form" action="https://clay-atlas.com/">
<label>
<span class="screen-reader-text">Search for...</span>
</label>
<input type="search" class="search-field" placeholder="Search for..." value="" name="s" />
<button type="submit" class="search-submit" aria-label="Search">
<span class="nv-search-icon-wrap">
<div class="nv-icon nv-search">
<svg width="15" height="15" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg"><path d="M1216 832q0-185-131.5-316.5t-316.5-131.5-316.5 131.5-131.5 316.5 131.5 316.5 316.5 131.5 316.5-131.5 131.5-316.5zm512 832q0 52-38 90t-90 38q-54 0-90-38l-343-342q-179 124-399 124-143 0-273.5-55.5t-225-150-150-225-55.5-273.5 55.5-273.5 150-225 225-150 273.5-55.5 273.5 55.5 225 150 150 225 55.5 273.5q0 220-124 399l343 343q37 37 37 90z" /></svg>
</div> </span>
</button>
</form>
</div>
<div class="close-container container responsive-search">
<button tabindex="0" class="close-responsive-search">
<svg width="50" height="50" viewBox="0 0 20 20" fill="#555555"><path d="M14.95 6.46L11.41 10l3.54 3.54l-1.41 1.41L10 11.42l-3.53 3.53l-1.42-1.42L8.58 10L5.05 6.47l1.42-1.42L10 8.58l3.54-3.53z" /><rect /></svg>
</button>
</div>
</div>
</div>
</div>
</div>
</div> </div>
</div>
</div>
</nav>
<nav class="header--row header-main hide-on-desktop layout-full-contained nv-navbar header--row" data-row-id="main" data-show-on="mobile">
<div class="header--row-inner header-main-inner">
<div class="container">
<div class="row row--wrapper" data-section="hfg_header_layout_main">
<div class="builder-item hfg-item-first col-8 tablet-left mobile-left"><div class="item--inner builder-item--logo" data-section="title_tagline" data-item-id="logo">
<div class="site-logo">
<a class="brand" href="https://clay-atlas.com/" title="Clay-Technology World" aria-label="Clay-Technology World"><div class="title-with-logo"><img width="350" height="350" src="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2021/03/cropped-output.png?fit=350%2C350&amp;ssl=1" class="skip-lazy" alt="" loading="lazy" srcset="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2021/03/cropped-output.png?w=350&amp;ssl=1 350w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2021/03/cropped-output.png?resize=300%2C300&amp;ssl=1 300w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2021/03/cropped-output.png?resize=150%2C150&amp;ssl=1 150w" sizes="(max-width: 350px) 100vw, 350px" /><div class="nv-title-tagline-wrap"><p class="site-title">Clay-Technology World</p><small>Hope every day is better than yesterday</small></div></div></a></div>
</div>
</div><div class="builder-item hfg-item-last col-4 tablet-right mobile-right"><div class="item--inner builder-item--nav-icon" data-section="header_menu_icon" data-item-id="nav-icon">
<div class="menu-mobile-toggle item-button navbar-toggle-wrapper">
<button type="button" class="navbar-toggle" aria-label="
			Navigation Menu			">
<span class="bars">
<span class="icon-bar"></span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
</span>
<span class="screen-reader-text">Navigation Menu</span>
</button>
</div> 
</div>
</div> </div>
</div>
</div>
</nav>
<div id="header-menu-sidebar" class="header-menu-sidebar menu-sidebar-panel slide_left">
<div id="header-menu-sidebar-bg" class="header-menu-sidebar-bg">
<div class="close-sidebar-panel navbar-toggle-wrapper">
<button type="button" class="navbar-toggle active" aria-label="
				Navigation Menu				">
<span class="bars">
<span class="icon-bar"></span>
<span class="icon-bar"></span>
<span class="icon-bar"></span>
</span>
<span class="screen-reader-text">
Navigation Menu </span>
</button>
</div>
<div id="header-menu-sidebar-inner" class="header-menu-sidebar-inner ">
<div class="builder-item has-nav hfg-item-last hfg-item-first col-12 desktop-right tablet-left mobile-left"><div class="item--inner builder-item--primary-menu has_menu" data-section="header_menu_primary" data-item-id="primary-menu">
<div class="nv-nav-wrap">
<div role="navigation" class="style-border-bottom nav-menu-primary" aria-label="Primary Menu">
<ul id="nv-primary-navigation-sidebar" class="primary-menu-ul nav-ul"><li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-806"><a href="https://clay-atlas.com/clays-blog-about-me/">About Me</a></li>
<li class="pll-parent-menu-item menu-item menu-item-type-custom menu-item-object-custom current-menu-parent menu-item-has-children menu-item-5774"><a href="#pll_switcher"><span class="menu-item-title-wrap"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAMAAABBPP0LAAAAVFBMVEUAILQAGrEAEazhAAD5AADwAACBot+5ued2mNv6aWv7X1/5UVHoAACWltz5+fz+/v5ahNPyRkv5QkL5OTn2MTH3Kir1JiZOe87rOkb1Hh70FRXyDQ3JFHMOAAAAU0lEQVR4AQXBgQ3CMBAAMV8+Iuy/LKhUgB0kRchDfksRbU59R1Xd14If51QNK3Ndc6im7Hg63DVhr/kct2pSr8WRahIWUk1i2XrHo7tYbB8IL/AHd28PeH6kKkoAAAAASUVORK5CYII=" alt="中文 (台灣)" width="16" height="11" style="width: 16px; height: 11px;" /><span style="margin-left:0.3em;">中文 (台灣)</span></span><div class="caret-wrap 2" tabindex="0"><span class="caret"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path d="M207.029 381.476L12.686 187.132c-9.373-9.373-9.373-24.569 0-33.941l22.667-22.667c9.357-9.357 24.522-9.375 33.901-.04L224 284.505l154.745-154.021c9.379-9.335 24.544-9.317 33.901.04l22.667 22.667c9.373 9.373 9.373 24.569 0 33.941L240.971 381.476c-9.373 9.372-24.569 9.372-33.942 0z" /></svg></span></div></a>
<ul class="sub-menu">
<li class="lang-item lang-item-29 lang-item-zh current-lang lang-item-first menu-item menu-item-type-custom menu-item-object-custom menu-item-5774-zh"><a href="https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/" hreflang="zh-TW" lang="zh-TW"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAMAAABBPP0LAAAAVFBMVEUAILQAGrEAEazhAAD5AADwAACBot+5ued2mNv6aWv7X1/5UVHoAACWltz5+fz+/v5ahNPyRkv5QkL5OTn2MTH3Kir1JiZOe87rOkb1Hh70FRXyDQ3JFHMOAAAAU0lEQVR4AQXBgQ3CMBAAMV8+Iuy/LKhUgB0kRchDfksRbU59R1Xd14If51QNK3Ndc6im7Hg63DVhr/kct2pSr8WRahIWUk1i2XrHo7tYbB8IL/AHd28PeH6kKkoAAAAASUVORK5CYII=" alt="中文 (台灣)" width="16" height="11" style="width: 16px; height: 11px;" /><span style="margin-left:0.3em;">中文 (台灣)</span></a></li>
<li class="lang-item lang-item-36 lang-item-us menu-item menu-item-type-custom menu-item-object-custom menu-item-5774-us"><a href="https://clay-atlas.com/us/blog/2019/09/17/python-english-tutorial-pyqt5-label-lineedit-pushbutton/" hreflang="en-US" lang="en-US"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAMAAABBPP0LAAAAmVBMVEViZsViZMJiYrf9gnL8eWrlYkjgYkjZYkj8/PujwPybvPz4+PetraBEgfo+fvo3efkydfkqcvj8Y2T8UlL8Q0P8MzP9k4Hz8/Lu7u4DdPj9/VrKysI9fPoDc/EAZ7z7IiLHYkjp6ekCcOTk5OIASbfY/v21takAJrT5Dg6sYkjc3Nn94t2RkYD+y8KeYkjs/v7l5fz0dF22YkjWvcOLAAAAgElEQVR4AR2KNULFQBgGZ5J13KGGKvc/Cw1uPe62eb9+Jr1EUBFHSgxxjP2Eca6AfUSfVlUfBvm1Ui1bqafctqMndNkXpb01h5TLx4b6TIXgwOCHfjv+/Pz+5vPRw7txGWT2h6yO0/GaYltIp5PT1dEpLNPL/SdWjYjAAZtvRPgHJX4Xio+DSrkAAAAASUVORK5CYII=" alt="English" width="16" height="11" style="width: 16px; height: 11px;" /><span style="margin-left:0.3em;">English</span></a></li>
</ul>
</li>
</ul> </div>
</div>
</div>
</div> </div>
</div>
</div>
<div class="header-menu-sidebar-overlay"></div>
</div>
</header>
<main id="content" class="neve-main" role="main">
<div class="container single-post-container">
<div class="row">
<article id="post-422" class="nv-single-post-wrap col post-422 post type-post status-publish format-standard has-post-thumbnail hentry category-pyqt5 category-python tag-pyqt5 tag-python">
<div class="entry-header"><div class="nv-title-meta-wrap "><h1 class="title entry-title">[PyQt5] 基本教學(2) QLabel, QLineEdit, QPushButton</h1><ul class="nv-meta-list"><li class="meta author vcard"><img class="photo" alt="Clay" src="https://secure.gravatar.com/avatar/fb7c6baee50bb79acc3afb91e8e5a545?s=20&#038;d=retro&#038;r=g" />&nbsp;<span class="author-name fn"><a href="https://clay-atlas.com/blog/author/ccs96307/" title="Posts by Clay" rel="author">Clay</a></span></li><li class="meta date posted-on"><time class="entry-date published" datetime="2019-08-27T09:14:36+00:00" content="2019-08-27">2019-08-27</time><time class="updated" datetime="2021-04-08T13:06:31+00:00">2021-04-08</time></li><li class="meta comments"><a href="https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/#comments">2 Comments</a></li><li class="meta category"><a href="https://clay-atlas.com/blog/category/python/pyqt5/" rel="category tag">PyQt5</a>, <a href="https://clay-atlas.com/blog/category/python/" rel="category tag">Python</a></li></ul></div></div><div class="nv-thumb-wrap"><img width="768" height="620" src="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2020/09/Python_PyQt5.png?resize=768%2C620&amp;ssl=1" class="skip-lazy wp-post-image" alt loading="lazy" srcset="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2020/09/Python_PyQt5.png?zoom=2&amp;resize=768%2C620&amp;ssl=1 1536w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2020/09/Python_PyQt5.png?zoom=3&amp;resize=768%2C620&amp;ssl=1 2304w" sizes="(max-width: 768px) 100vw, 768px"><noscript><img width="768" height="620" src="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2020/09/Python_PyQt5.png?resize=768%2C620&amp;ssl=1" class="skip-lazy wp-post-image" alt="" loading="lazy" srcset="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2020/09/Python_PyQt5.png?zoom=2&amp;resize=768%2C620&amp;ssl=1 1536w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2020/09/Python_PyQt5.png?zoom=3&amp;resize=768%2C620&amp;ssl=1 2304w" sizes="(max-width: 768px) 100vw, 768px" /></noscript></div><div class="nv-content-wrap entry-content">
<p>今天，我想要將我嘗試 PyQt5 裡頭 Label、LineEdit、PushButton 的經驗記錄下來。順帶一題，目前維止都還是倚靠 Qt Designer 來拉出界面。</p>
<p>也許總有一天必須自己撰寫界面原始碼（畢竟 Qt Designer 裡頭的元件其實並不完整，當然也或許只是我沒找到），希望能持續堅持學習到那天！</p>
<span id="more-422"></span>
<p>一如既往，如果你想參閱官方指南，也許你可以參考： <a href="https://www.riverbankcomputing.com/static/Docs/PyQt5/index.html?highlight=qicon">https://www.riverbankcomputing.com/static/Docs/PyQt5/index.html?highlight=qicon</a></p>
<hr class="wp-block-separator has-text-color has-background has-very-dark-gray-background-color has-very-dark-gray-color is-style-wide" />
<h2 class="has-text-align-center">QLabel</h2>
<p>Label 可說是我們最常使用的元件之一，上次的心得筆記也是使用這個元件來印出『Hello World!』。</p>
<p>這次我們更進一步，使用程式碼設定大小、位置、文字 ...... 等等的屬性。</p>

<div style="background: #f8f8f8; overflow:auto; width:auto; border:solid gray; border-width:.1em .1em .1em .8em; padding:.2em .5em;">
<pre class="ccode" style="margin: 0; line-height: 125%; font-size:15px;"><span></span><span style="color: #008000; font-weight: bold">from</span> <span style="color: #0000FF; font-weight: bold">PyQt5</span> <span style="color: #008000; font-weight: bold">import</span> <span class="n">QtWidgets</span><span class="p">,</span> <span class="n">QtGui</span><span class="p">,</span> <span class="n">QtCore</span>
<span style="color: #008000; font-weight: bold">from</span> <span style="color: #0000FF; font-weight: bold">UI.Label</span> <span style="color: #008000; font-weight: bold">import</span> <span class="n">Ui_MainWindow</span>
<span style="color: #008000; font-weight: bold">import</span> <span style="color: #0000FF; font-weight: bold">sys</span>


<span style="color: #008000; font-weight: bold">class</span> <span style="color: #0000FF; font-weight: bold">MainWindow</span><span class="p">(</span><span class="n">QtWidgets</span><span style="color: #666666">.</span><span class="n">QMainWindow</span><span class="p">):</span>
    <span style="color: #008000; font-weight: bold">def</span> <span style="color: #0000FF">__init__</span><span class="p">(</span><span style="color: #008000">self</span><span class="p">):</span>
        <span style="color: #008000">super</span><span class="p">(</span><span class="n">MainWindow</span><span class="p">,</span> <span style="color: #008000">self</span><span class="p">)</span><span style="color: #666666">.</span><span style="color: #0000FF">__init__</span><span class="p">()</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span> <span style="color: #666666">=</span> <span class="n">Ui_MainWindow</span><span class="p">()</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span><span style="color: #666666">.</span><span class="n">setupUi</span><span class="p">(</span><span style="color: #008000">self</span><span class="p">)</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span><span style="color: #666666">.</span><span class="n">label</span><span style="color: #666666">.</span><span class="n">setFont</span><span class="p">(</span><span class="n">QtGui</span><span style="color: #666666">.</span><span class="n">QFont</span><span class="p">(</span><span style="color: #BA2121">&#39;Arial&#39;</span><span class="p">,</span> <span style="color: #666666">50</span><span class="p">))</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span><span style="color: #666666">.</span><span class="n">label</span><span style="color: #666666">.</span><span class="n">setGeometry</span><span class="p">(</span><span class="n">QtCore</span><span style="color: #666666">.</span><span class="n">QRect</span><span class="p">(</span><span style="color: #666666">10</span><span class="p">,</span> <span style="color: #666666">10</span><span class="p">,</span> <span style="color: #666666">600</span><span class="p">,</span> <span style="color: #666666">200</span><span class="p">))</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span><span style="color: #666666">.</span><span class="n">label</span><span style="color: #666666">.</span><span class="n">setText</span><span class="p">(</span><span style="color: #BA2121">&#39;Hello World!&#39;</span><span class="p">)</span>


<span style="color: #008000; font-weight: bold">if</span> <span style="color: #19177C">__name__</span> <span style="color: #666666">==</span> <span style="color: #BA2121">&#39;__main__&#39;</span><span class="p">:</span>
    <span class="n">app</span> <span style="color: #666666">=</span> <span class="n">QtWidgets</span><span style="color: #666666">.</span><span class="n">QApplication</span><span class="p">([])</span>
    <span class="n">window</span> <span style="color: #666666">=</span> <span class="n">MainWindow</span><span class="p">()</span>
    <span class="n">window</span><span style="color: #666666">.</span><span class="n">show</span><span class="p">()</span>
    <span class="n">sys</span><span style="color: #666666">.</span><span class="n">exit</span><span class="p">(</span><span class="n">app</span><span style="color: #666666">.</span><span class="n">exec_</span><span class="p">())</span>
</pre></div>
<textarea readonly id="93264191" style="position:absolute;left:-9999px">from PyQt5 import QtWidgets, QtGui, QtCore
from UI.Label import Ui_MainWindow
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setFont(QtGui.QFont('Arial', 50))
        self.ui.label.setGeometry(QtCore.QRect(10, 10, 600, 200))
        self.ui.label.setText('Hello World!')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())</textarea>
<button type="button" onclick="copyEvent('93264191')" style="float: right">COPY</button>
<script>
function copyEvent(id) {
  let textarea;
  let result;

  try {
    textarea = document.createElement('textarea');
    textarea.setAttribute('readonly', true);
    textarea.setAttribute('contenteditable', true);
    textarea.style.position = 'fixed'; // prevent scroll from jumping to the bottom when focus is set.
    textarea.value = document.getElementById(id).textContent;

    document.body.appendChild(textarea);

    textarea.focus();
    textarea.select();

    const range = document.createRange();
    range.selectNodeContents(textarea);

    const sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);

    textarea.setSelectionRange(0, textarea.value.length);
    result = document.execCommand('copy');
  } catch (err) {
    console.error(err);
    result = null;
  } finally {
    document.body.removeChild(textarea);
  }

  // manual copy fallback using prompt
  if (!result) {
    const isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;
    const copyHotkey = isMac ? '⌘C' : 'CTRL+C';
    result = prompt(`Press ${copyHotkey}`, string); // eslint-disable-line no-alert
    if (!result) {
      return false;
    }
  }
  return true;
}
</script>
<p><br>Output:</p>
<figure class="wp-block-image"><a href="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-10.png?ssl=1"><img loading="lazy" width="805" height="643" src="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-10.png?resize=805%2C643&#038;ssl=1" alt class="wp-image-423 jetpack-lazy-image" data-recalc-dims="1" data-lazy-srcset="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-10.png?w=805&amp;ssl=1 805w, https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-10.png?resize=300%2C240&amp;ssl=1 300w, https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-10.png?resize=768%2C613&amp;ssl=1 768w" data-lazy-sizes="(max-width: 805px) 100vw, 805px" data-lazy-src="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-10.png?resize=805%2C643&amp;is-pending-load=1#038;ssl=1" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"><noscript><img loading="lazy" width="805" height="643" src="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-10.png?resize=805%2C643&#038;ssl=1" alt="" class="wp-image-423" srcset="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-10.png?w=805&amp;ssl=1 805w, https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-10.png?resize=300%2C240&amp;ssl=1 300w, https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-10.png?resize=768%2C613&amp;ssl=1 768w" sizes="(max-width: 805px) 100vw, 805px" data-recalc-dims="1" /></noscript></a></figure>
<hr class="wp-block-separator has-text-color has-background has-very-dark-gray-background-color has-very-dark-gray-color is-style-wide" />

<div style="background: #f8f8f8; overflow:auto; width:auto; border:solid gray; border-width:.1em .1em .1em .8em; padding:.2em .5em;">
<pre class="ccode" style="margin: 0; line-height: 125%; font-size:15px;"><span></span><span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span><span style="color: #666666">.</span><span class="n">label</span><span style="color: #666666">.</span><span class="n">setFont</span><span class="p">(</span><span class="n">QtGui</span><span style="color: #666666">.</span><span class="n">QFont</span><span class="p">(</span><span style="color: #BA2121">&#39;Arial&#39;</span><span class="p">,</span> <span style="color: #666666">50</span><span class="p">))</span>
</pre></div>
<textarea readonly id="59723157" style="position:absolute;left:-9999px">self.ui.label.setFont(QtGui.QFont('Arial', 50))</textarea>
<button type="button" onclick="copyEvent('59723157')" style="float: right">COPY</button>
<script>
function copyEvent(id) {
  let textarea;
  let result;

  try {
    textarea = document.createElement('textarea');
    textarea.setAttribute('readonly', true);
    textarea.setAttribute('contenteditable', true);
    textarea.style.position = 'fixed'; // prevent scroll from jumping to the bottom when focus is set.
    textarea.value = document.getElementById(id).textContent;

    document.body.appendChild(textarea);

    textarea.focus();
    textarea.select();

    const range = document.createRange();
    range.selectNodeContents(textarea);

    const sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);

    textarea.setSelectionRange(0, textarea.value.length);
    result = document.execCommand('copy');
  } catch (err) {
    console.error(err);
    result = null;
  } finally {
    document.body.removeChild(textarea);
  }

  // manual copy fallback using prompt
  if (!result) {
    const isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;
    const copyHotkey = isMac ? '⌘C' : 'CTRL+C';
    result = prompt(`Press ${copyHotkey}`, string); // eslint-disable-line no-alert
    if (!result) {
      return false;
    }
  }
  return true;
}
</script>
<p> <br>這行程式是用於設定字體、大小:</p>
<p><br></p>
<hr class="wp-block-separator has-text-color has-background has-very-dark-gray-background-color has-very-dark-gray-color is-style-wide" />

<div style="background: #f8f8f8; overflow:auto; width:auto; border:solid gray; border-width:.1em .1em .1em .8em; padding:.2em .5em;">
<pre class="ccode" style="margin: 0; line-height: 125%; font-size:15px;"><span></span><span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span><span style="color: #666666">.</span><span class="n">label</span><span style="color: #666666">.</span><span class="n">setGeometry</span><span class="p">(</span><span class="n">QtCore</span><span style="color: #666666">.</span><span class="n">QRect</span><span class="p">(</span><span style="color: #666666">10</span><span class="p">,</span> <span style="color: #666666">10</span><span class="p">,</span> <span style="color: #666666">600</span><span class="p">,</span> <span style="color: #666666">200</span><span class="p">))</span>
</pre></div>
<textarea readonly id="49744916" style="position:absolute;left:-9999px">self.ui.label.setGeometry(QtCore.QRect(10, 10, 600, 200))</textarea>
<button type="button" onclick="copyEvent('49744916')" style="float: right">COPY</button>
<script>
function copyEvent(id) {
  let textarea;
  let result;

  try {
    textarea = document.createElement('textarea');
    textarea.setAttribute('readonly', true);
    textarea.setAttribute('contenteditable', true);
    textarea.style.position = 'fixed'; // prevent scroll from jumping to the bottom when focus is set.
    textarea.value = document.getElementById(id).textContent;

    document.body.appendChild(textarea);

    textarea.focus();
    textarea.select();

    const range = document.createRange();
    range.selectNodeContents(textarea);

    const sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);

    textarea.setSelectionRange(0, textarea.value.length);
    result = document.execCommand('copy');
  } catch (err) {
    console.error(err);
    result = null;
  } finally {
    document.body.removeChild(textarea);
  }

  // manual copy fallback using prompt
  if (!result) {
    const isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;
    const copyHotkey = isMac ? '⌘C' : 'CTRL+C';
    result = prompt(`Press ${copyHotkey}`, string); // eslint-disable-line no-alert
    if (!result) {
      return false;
    }
  }
  return true;
}
</script>
<p><br>這行程式的意思是： <code>QRect(x, y, 水平長度, 縱向長度)</code></p>
<p>記得，(x, y) 座標原點是位於左上角哦！</p>
<hr class="wp-block-separator is-style-wide" />

<div style="background: #f8f8f8; overflow:auto; width:auto; border:solid gray; border-width:.1em .1em .1em .8em; padding:.2em .5em;">
<pre class="ccode" style="margin: 0; line-height: 125%; font-size:15px;"><span></span><span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span><span style="color: #666666">.</span><span class="n">label</span><span style="color: #666666">.</span><span class="n">setText</span><span class="p">(</span><span style="color: #BA2121">&#39;Hello World!&#39;</span><span class="p">)</span>
</pre></div>
<textarea readonly id="04625252" style="position:absolute;left:-9999px">self.ui.label.setText('Hello World!')</textarea>
<button type="button" onclick="copyEvent('04625252')" style="float: right">COPY</button>
<script>
function copyEvent(id) {
  let textarea;
  let result;

  try {
    textarea = document.createElement('textarea');
    textarea.setAttribute('readonly', true);
    textarea.setAttribute('contenteditable', true);
    textarea.style.position = 'fixed'; // prevent scroll from jumping to the bottom when focus is set.
    textarea.value = document.getElementById(id).textContent;

    document.body.appendChild(textarea);

    textarea.focus();
    textarea.select();

    const range = document.createRange();
    range.selectNodeContents(textarea);

    const sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);

    textarea.setSelectionRange(0, textarea.value.length);
    result = document.execCommand('copy');
  } catch (err) {
    console.error(err);
    result = null;
  } finally {
    document.body.removeChild(textarea);
  }

  // manual copy fallback using prompt
  if (!result) {
    const isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;
    const copyHotkey = isMac ? '⌘C' : 'CTRL+C';
    result = prompt(`Press ${copyHotkey}`, string); // eslint-disable-line no-alert
    if (!result) {
      return false;
    }
  }
  return true;
}
</script>
<p><br>這行程式就很明顯了：這是設定我們要印出的文字：</p>
<hr class="wp-block-separator has-text-color has-background has-very-dark-gray-background-color has-very-dark-gray-color is-style-wide" />
<h2 class="has-text-align-center">QLineEdit</h2>
<p>這裡介紹一下，LineEdit 是一種『可供使用者輸入文字的欄位』。最常見的想必就是網站上輸入帳號密碼的那種欄位吧，我們顯示出來看看。</p>
<figure class="wp-block-image"><a href="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-11.png?ssl=1"><img loading="lazy" width="799" height="633" src="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-11.png?resize=799%2C633&#038;ssl=1" alt class="wp-image-424 jetpack-lazy-image" data-recalc-dims="1" data-lazy-srcset="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-11.png?w=799&amp;ssl=1 799w, https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-11.png?resize=300%2C238&amp;ssl=1 300w, https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-11.png?resize=768%2C608&amp;ssl=1 768w" data-lazy-sizes="(max-width: 799px) 100vw, 799px" data-lazy-src="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-11.png?resize=799%2C633&amp;is-pending-load=1#038;ssl=1" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"><noscript><img loading="lazy" width="799" height="633" src="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-11.png?resize=799%2C633&#038;ssl=1" alt="" class="wp-image-424" srcset="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-11.png?w=799&amp;ssl=1 799w, https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-11.png?resize=300%2C238&amp;ssl=1 300w, https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-11.png?resize=768%2C608&amp;ssl=1 768w" sizes="(max-width: 799px) 100vw, 799px" data-recalc-dims="1" /></noscript></a></figure>
<p>沒錯！就是中間顯示著『Welcome!』的那個欄位，那就是 LineEdit 這種元件的模樣。</p>
<p>基本上，我們可以調用程式針對其屬性做出各式各樣的調整，比如說遮蔽顯示文字（可用於輸入密碼）、限制使用者可輸入的文字上限、輸入事先設定的預設文字、提整文字顏色 ...... 等等，其實我們都可以隨心所欲地做到。</p>
<p>大家不妨試試看還有哪些功能可以使用，想必一定會有收穫的。</p>
<p>接下來介紹今天的最後一項元件，也會順便完成一個簡單的範例程式。</p>
<hr class="wp-block-separator has-text-color has-background has-very-dark-gray-background-color has-very-dark-gray-color is-style-wide" />
<h2 class="has-text-align-center">QPushButton</h2>
<p>PushButton 其實就是我們最常見的『按鈕』。如同剛才的圖例所示：</p>
<figure class="wp-block-image"><a href="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-12.png?ssl=1"><img loading="lazy" width="799" height="633" src="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-12.png?resize=799%2C633&#038;ssl=1" alt class="wp-image-425 jetpack-lazy-image" data-recalc-dims="1" data-lazy-srcset="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-12.png?w=799&amp;ssl=1 799w, https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-12.png?resize=300%2C238&amp;ssl=1 300w, https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-12.png?resize=768%2C608&amp;ssl=1 768w" data-lazy-sizes="(max-width: 799px) 100vw, 799px" data-lazy-src="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-12.png?resize=799%2C633&amp;is-pending-load=1#038;ssl=1" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"><noscript><img loading="lazy" width="799" height="633" src="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-12.png?resize=799%2C633&#038;ssl=1" alt="" class="wp-image-425" srcset="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-12.png?w=799&amp;ssl=1 799w, https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-12.png?resize=300%2C238&amp;ssl=1 300w, https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-12.png?resize=768%2C608&amp;ssl=1 768w" sizes="(max-width: 799px) 100vw, 799px" data-recalc-dims="1" /></noscript></a></figure>
<p>顯示著 Display 的那個按鈕就是我們的 PushButton，在這裡紀錄一下我如何完成這個界面。</p>
<figure class="wp-block-image"><a href="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-13.png?fit=840%2C473&amp;ssl=1"><img loading="lazy" width="1920" height="1080" src="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-13.png?fit=840%2C473&amp;ssl=1" alt class="wp-image-426 jetpack-lazy-image" data-lazy-srcset="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-13.png?w=1920&amp;ssl=1 1920w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-13.png?resize=300%2C169&amp;ssl=1 300w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-13.png?resize=768%2C432&amp;ssl=1 768w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-13.png?resize=1024%2C576&amp;ssl=1 1024w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-13.png?resize=1200%2C675&amp;ssl=1 1200w" data-lazy-sizes="(max-width: 1200px) 100vw, 1200px" data-lazy-src="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-13.png?fit=840%2C473&amp;ssl=1&amp;is-pending-load=1" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"><noscript><img loading="lazy" width="1920" height="1080" src="https://i2.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-13.png?fit=840%2C473&amp;ssl=1" alt="" class="wp-image-426" srcset="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-13.png?w=1920&amp;ssl=1 1920w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-13.png?resize=300%2C169&amp;ssl=1 300w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-13.png?resize=768%2C432&amp;ssl=1 768w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-13.png?resize=1024%2C576&amp;ssl=1 1024w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-13.png?resize=1200%2C675&amp;ssl=1 1200w" sizes="(max-width: 1200px) 100vw, 1200px" /></noscript></a></figure>
<p>沒錯！就是直接使用 Designer 來拉出這三個元件！</p>
<p>由左而右分別是： Label, LineEdit, PushButton 這三種元件。</p>
<p>我們看看生成的檔案（已被 PyUIC 轉檔）：</p>

<div style="background: #f8f8f8; overflow:auto; width:auto; border:solid gray; border-width:.1em .1em .1em .8em; padding:.2em .5em;">
<pre class="ccode" style="margin: 0; line-height: 125%; font-size:15px;"><span></span><span style="color: #408080; font-style: italic"># -*- coding: utf-8 -*-</span>

<span style="color: #408080; font-style: italic"># Form implementation generated from reading ui file &#39;LineEdit.ui&#39;</span>
<span style="color: #408080; font-style: italic">#</span>
<span style="color: #408080; font-style: italic"># Created by: PyQt5 UI code generator 5.11.3</span>
<span style="color: #408080; font-style: italic">#</span>
<span style="color: #408080; font-style: italic"># WARNING! All changes made in this file will be lost!</span>

<span style="color: #008000; font-weight: bold">from</span> <span style="color: #0000FF; font-weight: bold">PyQt5</span> <span style="color: #008000; font-weight: bold">import</span> <span class="n">QtCore</span><span class="p">,</span> <span class="n">QtGui</span><span class="p">,</span> <span class="n">QtWidgets</span>

<span style="color: #008000; font-weight: bold">class</span> <span style="color: #0000FF; font-weight: bold">Ui_MainWindow</span><span class="p">(</span><span style="color: #008000">object</span><span class="p">):</span>
    <span style="color: #008000; font-weight: bold">def</span> <span style="color: #0000FF">setupUi</span><span class="p">(</span><span style="color: #008000">self</span><span class="p">,</span> <span class="n">MainWindow</span><span class="p">):</span>
        <span class="n">MainWindow</span><span style="color: #666666">.</span><span class="n">setObjectName</span><span class="p">(</span><span style="color: #BA2121">&quot;MainWindow&quot;</span><span class="p">)</span>
        <span class="n">MainWindow</span><span style="color: #666666">.</span><span class="n">resize</span><span class="p">(</span><span style="color: #666666">800</span><span class="p">,</span> <span style="color: #666666">600</span><span class="p">)</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">centralwidget</span> <span style="color: #666666">=</span> <span class="n">QtWidgets</span><span style="color: #666666">.</span><span class="n">QWidget</span><span class="p">(</span><span class="n">MainWindow</span><span class="p">)</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">centralwidget</span><span style="color: #666666">.</span><span class="n">setObjectName</span><span class="p">(</span><span style="color: #BA2121">&quot;centralwidget&quot;</span><span class="p">)</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">lineEdit</span> <span style="color: #666666">=</span> <span class="n">QtWidgets</span><span style="color: #666666">.</span><span class="n">QLineEdit</span><span class="p">(</span><span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">centralwidget</span><span class="p">)</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">lineEdit</span><span style="color: #666666">.</span><span class="n">setGeometry</span><span class="p">(</span><span class="n">QtCore</span><span style="color: #666666">.</span><span class="n">QRect</span><span class="p">(</span><span style="color: #666666">150</span><span class="p">,</span> <span style="color: #666666">100</span><span class="p">,</span> <span style="color: #666666">191</span><span class="p">,</span> <span style="color: #666666">51</span><span class="p">))</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">lineEdit</span><span style="color: #666666">.</span><span class="n">setObjectName</span><span class="p">(</span><span style="color: #BA2121">&quot;lineEdit&quot;</span><span class="p">)</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">label</span> <span style="color: #666666">=</span> <span class="n">QtWidgets</span><span style="color: #666666">.</span><span class="n">QLabel</span><span class="p">(</span><span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">centralwidget</span><span class="p">)</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">label</span><span style="color: #666666">.</span><span class="n">setGeometry</span><span class="p">(</span><span class="n">QtCore</span><span style="color: #666666">.</span><span class="n">QRect</span><span class="p">(</span><span style="color: #666666">0</span><span class="p">,</span> <span style="color: #666666">100</span><span class="p">,</span> <span style="color: #666666">131</span><span class="p">,</span> <span style="color: #666666">51</span><span class="p">))</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">label</span><span style="color: #666666">.</span><span class="n">setObjectName</span><span class="p">(</span><span style="color: #BA2121">&quot;label&quot;</span><span class="p">)</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">pushButton</span> <span style="color: #666666">=</span> <span class="n">QtWidgets</span><span style="color: #666666">.</span><span class="n">QPushButton</span><span class="p">(</span><span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">centralwidget</span><span class="p">)</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">pushButton</span><span style="color: #666666">.</span><span class="n">setGeometry</span><span class="p">(</span><span class="n">QtCore</span><span style="color: #666666">.</span><span class="n">QRect</span><span class="p">(</span><span style="color: #666666">390</span><span class="p">,</span> <span style="color: #666666">100</span><span class="p">,</span> <span style="color: #666666">131</span><span class="p">,</span> <span style="color: #666666">51</span><span class="p">))</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">pushButton</span><span style="color: #666666">.</span><span class="n">setObjectName</span><span class="p">(</span><span style="color: #BA2121">&quot;pushButton&quot;</span><span class="p">)</span>
        <span class="n">MainWindow</span><span style="color: #666666">.</span><span class="n">setCentralWidget</span><span class="p">(</span><span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">centralwidget</span><span class="p">)</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">menubar</span> <span style="color: #666666">=</span> <span class="n">QtWidgets</span><span style="color: #666666">.</span><span class="n">QMenuBar</span><span class="p">(</span><span class="n">MainWindow</span><span class="p">)</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">menubar</span><span style="color: #666666">.</span><span class="n">setGeometry</span><span class="p">(</span><span class="n">QtCore</span><span style="color: #666666">.</span><span class="n">QRect</span><span class="p">(</span><span style="color: #666666">0</span><span class="p">,</span> <span style="color: #666666">0</span><span class="p">,</span> <span style="color: #666666">800</span><span class="p">,</span> <span style="color: #666666">25</span><span class="p">))</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">menubar</span><span style="color: #666666">.</span><span class="n">setObjectName</span><span class="p">(</span><span style="color: #BA2121">&quot;menubar&quot;</span><span class="p">)</span>
        <span class="n">MainWindow</span><span style="color: #666666">.</span><span class="n">setMenuBar</span><span class="p">(</span><span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">menubar</span><span class="p">)</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">statusbar</span> <span style="color: #666666">=</span> <span class="n">QtWidgets</span><span style="color: #666666">.</span><span class="n">QStatusBar</span><span class="p">(</span><span class="n">MainWindow</span><span class="p">)</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">statusbar</span><span style="color: #666666">.</span><span class="n">setObjectName</span><span class="p">(</span><span style="color: #BA2121">&quot;statusbar&quot;</span><span class="p">)</span>
        <span class="n">MainWindow</span><span style="color: #666666">.</span><span class="n">setStatusBar</span><span class="p">(</span><span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">statusbar</span><span class="p">)</span>

        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">retranslateUi</span><span class="p">(</span><span class="n">MainWindow</span><span class="p">)</span>
        <span class="n">QtCore</span><span style="color: #666666">.</span><span class="n">QMetaObject</span><span style="color: #666666">.</span><span class="n">connectSlotsByName</span><span class="p">(</span><span class="n">MainWindow</span><span class="p">)</span>

    <span style="color: #008000; font-weight: bold">def</span> <span style="color: #0000FF">retranslateUi</span><span class="p">(</span><span style="color: #008000">self</span><span class="p">,</span> <span class="n">MainWindow</span><span class="p">):</span>
        <span class="n">_translate</span> <span style="color: #666666">=</span> <span class="n">QtCore</span><span style="color: #666666">.</span><span class="n">QCoreApplication</span><span style="color: #666666">.</span><span class="n">translate</span>
        <span class="n">MainWindow</span><span style="color: #666666">.</span><span class="n">setWindowTitle</span><span class="p">(</span><span class="n">_translate</span><span class="p">(</span><span style="color: #BA2121">&quot;MainWindow&quot;</span><span class="p">,</span> <span style="color: #BA2121">&quot;MainWindow&quot;</span><span class="p">))</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">label</span><span style="color: #666666">.</span><span class="n">setText</span><span class="p">(</span><span class="n">_translate</span><span class="p">(</span><span style="color: #BA2121">&quot;MainWindow&quot;</span><span class="p">,</span> <span style="color: #BA2121">&quot;TextLabel&quot;</span><span class="p">))</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">pushButton</span><span style="color: #666666">.</span><span class="n">setText</span><span class="p">(</span><span class="n">_translate</span><span class="p">(</span><span style="color: #BA2121">&quot;MainWindow&quot;</span><span class="p">,</span> <span style="color: #BA2121">&quot;PushButton&quot;</span><span class="p">))</span>
</pre></div>
<textarea readonly id="59944440" style="position:absolute;left:-9999px"># -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LineEdit.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 100, 191, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 100, 131, 51))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(390, 100, 131, 51))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))</textarea>
<button type="button" onclick="copyEvent('59944440')" style="float: right">COPY</button>
<script>
function copyEvent(id) {
  let textarea;
  let result;

  try {
    textarea = document.createElement('textarea');
    textarea.setAttribute('readonly', true);
    textarea.setAttribute('contenteditable', true);
    textarea.style.position = 'fixed'; // prevent scroll from jumping to the bottom when focus is set.
    textarea.value = document.getElementById(id).textContent;

    document.body.appendChild(textarea);

    textarea.focus();
    textarea.select();

    const range = document.createRange();
    range.selectNodeContents(textarea);

    const sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);

    textarea.setSelectionRange(0, textarea.value.length);
    result = document.execCommand('copy');
  } catch (err) {
    console.error(err);
    result = null;
  } finally {
    document.body.removeChild(textarea);
  }

  // manual copy fallback using prompt
  if (!result) {
    const isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;
    const copyHotkey = isMac ? '⌘C' : 'CTRL+C';
    result = prompt(`Press ${copyHotkey}`, string); // eslint-disable-line no-alert
    if (!result) {
      return false;
    }
  }
  return true;
}
</script>
<p><br>若是我們仔細看產生的檔案，會發現 Label, LineEdit, PushButton 已經被定義了。</p>
<p>至此，簡單的界面已經被完成了，剩下的就是我們撰寫程式邏輯的部份：</p>

<div style="background: #f8f8f8; overflow:auto; width:auto; border:solid gray; border-width:.1em .1em .1em .8em; padding:.2em .5em;">
<pre class="ccode" style="margin: 0; line-height: 125%; font-size:15px;"><span></span><span style="color: #408080; font-style: italic"># -*- coding: utf-8 -*-</span>
<span style="color: #008000; font-weight: bold">from</span> <span style="color: #0000FF; font-weight: bold">PyQt5</span> <span style="color: #008000; font-weight: bold">import</span> <span class="n">QtWidgets</span><span class="p">,</span> <span class="n">QtGui</span><span class="p">,</span> <span class="n">QtCore</span>
<span style="color: #008000; font-weight: bold">from</span> <span style="color: #0000FF; font-weight: bold">LineEdit</span> <span style="color: #008000; font-weight: bold">import</span> <span class="n">Ui_MainWindow</span>
<span style="color: #008000; font-weight: bold">import</span> <span style="color: #0000FF; font-weight: bold">sys</span>


<span style="color: #008000; font-weight: bold">class</span> <span style="color: #0000FF; font-weight: bold">MainWindow</span><span class="p">(</span><span class="n">QtWidgets</span><span style="color: #666666">.</span><span class="n">QMainWindow</span><span class="p">):</span>
    <span style="color: #008000; font-weight: bold">def</span> <span style="color: #0000FF">__init__</span><span class="p">(</span><span style="color: #008000">self</span><span class="p">):</span>
        <span style="color: #008000">super</span><span class="p">(</span><span class="n">MainWindow</span><span class="p">,</span> <span style="color: #008000">self</span><span class="p">)</span><span style="color: #666666">.</span><span style="color: #0000FF">__init__</span><span class="p">()</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span> <span style="color: #666666">=</span> <span class="n">Ui_MainWindow</span><span class="p">()</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span><span style="color: #666666">.</span><span class="n">setupUi</span><span class="p">(</span><span style="color: #008000">self</span><span class="p">)</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span><span style="color: #666666">.</span><span class="n">label</span><span style="color: #666666">.</span><span class="n">setFont</span><span class="p">(</span><span class="n">QtGui</span><span style="color: #666666">.</span><span class="n">QFont</span><span class="p">(</span><span style="color: #BA2121">&#39;Arial&#39;</span><span class="p">,</span> <span style="color: #666666">10</span><span class="p">))</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span><span style="color: #666666">.</span><span class="n">label</span><span style="color: #666666">.</span><span class="n">setText</span><span class="p">(</span><span style="color: #BA2121">&#39;Nothing&#39;</span><span class="p">)</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span><span style="color: #666666">.</span><span class="n">lineEdit</span><span style="color: #666666">.</span><span class="n">setText</span><span class="p">(</span><span style="color: #BA2121">&#39;Welcome!&#39;</span><span class="p">)</span>

        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span><span style="color: #666666">.</span><span class="n">pushButton</span><span style="color: #666666">.</span><span class="n">setText</span><span class="p">(</span><span style="color: #BA2121">&#39;Display&#39;</span><span class="p">)</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span><span style="color: #666666">.</span><span class="n">pushButton</span><span style="color: #666666">.</span><span class="n">clicked</span><span style="color: #666666">.</span><span class="n">connect</span><span class="p">(</span><span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">buttonClicked</span><span class="p">)</span>

    <span style="color: #008000; font-weight: bold">def</span> <span style="color: #0000FF">buttonClicked</span><span class="p">(</span><span style="color: #008000">self</span><span class="p">):</span>
        <span class="n">text</span> <span style="color: #666666">=</span> <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span><span style="color: #666666">.</span><span class="n">lineEdit</span><span style="color: #666666">.</span><span class="n">text</span><span class="p">()</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span><span style="color: #666666">.</span><span class="n">label</span><span style="color: #666666">.</span><span class="n">setText</span><span class="p">(</span><span class="n">text</span><span class="p">)</span>
        <span style="color: #008000">self</span><span style="color: #666666">.</span><span class="n">ui</span><span style="color: #666666">.</span><span class="n">lineEdit</span><span style="color: #666666">.</span><span class="n">clear</span><span class="p">()</span>


<span style="color: #008000; font-weight: bold">if</span> <span style="color: #19177C">__name__</span> <span style="color: #666666">==</span> <span style="color: #BA2121">&#39;__main__&#39;</span><span class="p">:</span>
    <span class="n">app</span> <span style="color: #666666">=</span> <span class="n">QtWidgets</span><span style="color: #666666">.</span><span class="n">QApplication</span><span class="p">([])</span>
    <span class="n">window</span> <span style="color: #666666">=</span> <span class="n">MainWindow</span><span class="p">()</span>
    <span class="n">window</span><span style="color: #666666">.</span><span class="n">show</span><span class="p">()</span>
    <span class="n">sys</span><span style="color: #666666">.</span><span class="n">exit</span><span class="p">(</span><span class="n">app</span><span style="color: #666666">.</span><span class="n">exec_</span><span class="p">())</span>
</pre></div>
<textarea readonly id="56062068" style="position:absolute;left:-9999px"># -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtGui, QtCore
from LineEdit import Ui_MainWindow
import sys


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setFont(QtGui.QFont('Arial', 10))
        self.ui.label.setText('Nothing')
        self.ui.lineEdit.setText('Welcome!')

        self.ui.pushButton.setText('Display')
        self.ui.pushButton.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        text = self.ui.lineEdit.text()
        self.ui.label.setText(text)
        self.ui.lineEdit.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())</textarea>
<button type="button" onclick="copyEvent('56062068')" style="float: right">COPY</button>
<script>
function copyEvent(id) {
  let textarea;
  let result;

  try {
    textarea = document.createElement('textarea');
    textarea.setAttribute('readonly', true);
    textarea.setAttribute('contenteditable', true);
    textarea.style.position = 'fixed'; // prevent scroll from jumping to the bottom when focus is set.
    textarea.value = document.getElementById(id).textContent;

    document.body.appendChild(textarea);

    textarea.focus();
    textarea.select();

    const range = document.createRange();
    range.selectNodeContents(textarea);

    const sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);

    textarea.setSelectionRange(0, textarea.value.length);
    result = document.execCommand('copy');
  } catch (err) {
    console.error(err);
    result = null;
  } finally {
    document.body.removeChild(textarea);
  }

  // manual copy fallback using prompt
  if (!result) {
    const isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;
    const copyHotkey = isMac ? '⌘C' : 'CTRL+C';
    result = prompt(`Press ${copyHotkey}`, string); // eslint-disable-line no-alert
    if (!result) {
      return false;
    }
  }
  return true;
}
</script>
<p><br>我們可以看到，我事先將 Label, LineEdit, PushButton 都設定好了顯示的文字。</p>
<p>然後最重要的是，我寫了一個按鈕按下去的事件，使用 <code>clicked.connect('你想要觸發的函式')</code> 可以完成這個指令。</p>
<p>在 <code>buttonClicked()</code> 這個函式裡頭，我將 LineEdit 裡我們輸入的文字儲存起來，並讓 Label 印出它。<br>緊接著，我再刪除了 LineEdit 的顯示文字。</p>
<p>效果大致上如下：</p>
<figure class="wp-block-image"><a href="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-14.png?ssl=1"><img loading="lazy" width="799" height="633" src="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-14.png?resize=799%2C633&#038;ssl=1" alt class="wp-image-427 jetpack-lazy-image" data-recalc-dims="1" data-lazy-srcset="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-14.png?w=799&amp;ssl=1 799w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-14.png?resize=300%2C238&amp;ssl=1 300w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-14.png?resize=768%2C608&amp;ssl=1 768w" data-lazy-sizes="(max-width: 799px) 100vw, 799px" data-lazy-src="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-14.png?resize=799%2C633&amp;is-pending-load=1#038;ssl=1" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"><noscript><img loading="lazy" width="799" height="633" src="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-14.png?resize=799%2C633&#038;ssl=1" alt="" class="wp-image-427" srcset="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-14.png?w=799&amp;ssl=1 799w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-14.png?resize=300%2C238&amp;ssl=1 300w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-14.png?resize=768%2C608&amp;ssl=1 768w" sizes="(max-width: 799px) 100vw, 799px" data-recalc-dims="1" /></noscript></a><figcaption>這是一開始。</figcaption></figure>
<figure class="wp-block-image"><a href="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-15.png?ssl=1"><img loading="lazy" width="800" height="637" src="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-15.png?resize=800%2C637&#038;ssl=1" alt class="wp-image-428 jetpack-lazy-image" data-recalc-dims="1" data-lazy-srcset="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-15.png?w=800&amp;ssl=1 800w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-15.png?resize=300%2C239&amp;ssl=1 300w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-15.png?resize=768%2C612&amp;ssl=1 768w" data-lazy-sizes="(max-width: 800px) 100vw, 800px" data-lazy-src="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-15.png?resize=800%2C637&amp;is-pending-load=1#038;ssl=1" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"><noscript><img loading="lazy" width="800" height="637" src="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-15.png?resize=800%2C637&#038;ssl=1" alt="" class="wp-image-428" srcset="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-15.png?w=800&amp;ssl=1 800w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-15.png?resize=300%2C239&amp;ssl=1 300w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-15.png?resize=768%2C612&amp;ssl=1 768w" sizes="(max-width: 800px) 100vw, 800px" data-recalc-dims="1" /></noscript></a><figcaption>然後我輸入文字。</figcaption></figure>
<figure class="wp-block-image"><a href="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-16.png?ssl=1"><img loading="lazy" width="800" height="636" src="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-16.png?resize=800%2C636&#038;ssl=1" alt class="wp-image-429 jetpack-lazy-image" data-recalc-dims="1" data-lazy-srcset="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-16.png?w=800&amp;ssl=1 800w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-16.png?resize=300%2C239&amp;ssl=1 300w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-16.png?resize=768%2C611&amp;ssl=1 768w" data-lazy-sizes="(max-width: 800px) 100vw, 800px" data-lazy-src="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-16.png?resize=800%2C636&amp;is-pending-load=1#038;ssl=1" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"><noscript><img loading="lazy" width="800" height="636" src="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-16.png?resize=800%2C636&#038;ssl=1" alt="" class="wp-image-429" srcset="https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-16.png?w=800&amp;ssl=1 800w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-16.png?resize=300%2C239&amp;ssl=1 300w, https://i1.wp.com/clay-atlas.com/wp-content/uploads/2019/08/image-16.png?resize=768%2C611&amp;ssl=1 768w" sizes="(max-width: 800px) 100vw, 800px" data-recalc-dims="1" /></noscript></a><figcaption>按下按鈕。</figcaption></figure>
<p>如何？是不是按照我們設定的流程走呢？</p>
<p>那麼，今天的心得筆記就紀錄到這裡。</p>
<hr class="wp-block-separator has-text-color has-background has-very-dark-gray-background-color has-very-dark-gray-color is-style-wide" />
<h2 class="has-text-align-center">Read More</h2>
<ul id="block-9c89c5bc-4b3b-4bef-ac79-7cf418cfee3c"><li><a href="https://clay-atlas.com/python-chinese-pyqt5-tutorial-install/">[PyQt5] 基本教學(1) 安裝 PyQt5，印出 Hello World!</a></li><li><a href="https://clay-atlas.com/pyqt5-%E5%9F%BA%E6%9C%AC%E6%95%99%E5%AD%B8-2-qlabel-qlineedit-qpushbutton/">[PyQt5] 基本教學(2) QLabel, QLineEdit, QPushButtom</a></li><li><a href="https://clay-atlas.com/python-chinese-pyqt5-tutorial-mainwindow-icon-pixmap-palette/">[PyQt5] 基本教學(3) QMainWindow, QIcon, QPixmap, QPalette</a></li><li><a href="https://clay-atlas.com/pyqt5-%E5%9F%BA%E6%9C%AC%E6%95%99%E5%AD%B8-4-%E8%8F%9C%E5%96%AE%E3%80%81%E5%B7%A5%E5%85%B7%E6%AC%84/">[PyQt5] 基本教學(4) 菜單、工具欄</a></li><li><a href="https://clay-atlas.com/python-chinese-tutorial-pyqt5-progressbar-sliderbar-dial/">[PyQt5] 基本教學(5) 進度條、滑動條、旋轉鈕</a></li><li><a href="https://clay-atlas.com/python-chinese-tutorial-%E4%B8%8B%E6%8B%89%E5%BC%8F%E9%81%B8%E5%96%AE%E3%80%81%E5%B8%83%E5%B1%80%E5%85%83%E4%BB%B6/">[PyQt5] 基本教學(6) 下拉選單、BoxLayout</a></li><li><a href="https://clay-atlas.com/python-chinese-tutorial-pyqt5-hide-show-windowresize/">[PyQt5] 基本教學(7) hide, show, 自動適應窗口大小</a></li><li><a href="https://clay-atlas.com/python-chinese-tutorial-pyqt5-qtimer-qlcdnumber/">[PyQt5] 基本教學(8) QTimer, QlcdNumber</a></li><li><a href="https://clay-atlas.com/pyqt5-%E5%9F%BA%E6%9C%AC%E6%95%99%E5%AD%B8-9-qcaledar%EF%BC%8C%E4%BD%BF%E7%94%A8-python-%E8%BC%95%E9%AC%86%E5%89%B5%E9%80%A0%E6%97%A5%E6%9B%86%E5%85%83%E4%BB%B6/">[PyQt5] 基本教學(9) QCaledar，使用 Python 輕鬆創造日曆元件</a></li><li><a href="https://clay-atlas.com/blog/2019/11/12/pyqt5-chinese-tutorial-keyboard-mouse/">[PyQt5] 基本教學(10) 使用鍵盤輸入指令、判斷滑鼠點擊位置</a></li><li><a href="https://clay-atlas.com/blog/2019/11/15/python-chinese-tutorial-pyqt5-qcolordialog/">[PyQt5] 基本教學(11) 使用 QColorDialog 調色盤來進行顏色的設定</a></li></ul>
<figure class="likecoin-embed likecoin-button"><iframe scrolling="no" frameborder="0" style="height: 212px; width: 100%;" src="https://button.like.co/in/embed/ccs96307/button?type=wp&integration=wordpress_plugin&referrer=https%3A%2F%2Fclay-atlas.com%2Fblog%2F2019%2F08%2F27%2Fpyqt5-%25e5%259f%25ba%25e6%259c%25ac%25e6%2595%2599%25e5%25ad%25b8-2-qlabel-qlineedit-qpushbutton%2F"></iframe></figure><div class="sharedaddy sd-sharing-enabled"><div class="robots-nocontent sd-block sd-social sd-social-icon sd-sharing"><h3 class="sd-title">分享此文：</h3><div class="sd-content"><ul><li class="share-twitter"><a rel="nofollow noopener noreferrer" data-shared="sharing-twitter-422" class="share-twitter sd-button share-icon no-text" href="https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/?share=twitter" target="_blank" title="分享到 Twitter"><span></span><span class="sharing-screen-reader-text">分享到 Twitter(在新視窗中開啟)</span></a></li><li class="share-facebook"><a rel="nofollow noopener noreferrer" data-shared="sharing-facebook-422" class="share-facebook sd-button share-icon no-text" href="https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/?share=facebook" target="_blank" title="按一下以分享至 Facebook"><span></span><span class="sharing-screen-reader-text">按一下以分享至 Facebook(在新視窗中開啟)</span></a></li><li class="share-linkedin"><a rel="nofollow noopener noreferrer" data-shared="sharing-linkedin-422" class="share-linkedin sd-button share-icon no-text" href="https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/?share=linkedin" target="_blank" title="分享到 LinkedIn"><span></span><span class="sharing-screen-reader-text">分享到 LinkedIn(在新視窗中開啟)</span></a></li><li class="share-reddit"><a rel="nofollow noopener noreferrer" data-shared="" class="share-reddit sd-button share-icon no-text" href="https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/?share=reddit" target="_blank" title="分享到 Reddit"><span></span><span class="sharing-screen-reader-text">分享到 Reddit(在新視窗中開啟)</span></a></li><li class="share-end"></li></ul></div></div></div>
<div id='jp-relatedposts' class='jp-relatedposts'>
<h3 class="jp-relatedposts-headline"><em>Maybe you want to read:</em></h3>
</div></div><div class="nv-tags-list"><span>Tags:</span><a href=https://clay-atlas.com/blog/tag/pyqt5/ title="PyQt5" class=pyqt5 rel="tag">PyQt5</a><a href=https://clay-atlas.com/blog/tag/python/ title="Python" class=python rel="tag">Python</a> </div>
<div id="comments" class="comments-area">
<div class="nv-comments-wrap">
<div class="nv-comments-title-wrap">
<h2 class="comments-title">2 thoughts on &ldquo;[PyQt5] 基本教學(2) QLabel, QLineEdit, QPushButton&rdquo;</h2> </div>
<ol class="nv-comments-list">
<li class="comment even thread-even depth-1" id="comment-item-2118">
<article id="comment-2118" class="nv-comment-article">
<div class="nv-comment-header">
<div class="nv-comment-avatar"><img alt src="https://secure.gravatar.com/avatar/227a7281ab1b5f9d5fd74196600801a5?s=50&#038;d=retro&#038;r=g" class="avatar avatar-50 photo jetpack-lazy-image" height="50" width="50" loading="lazy" data-lazy-srcset="https://secure.gravatar.com/avatar/227a7281ab1b5f9d5fd74196600801a5?s=100&#038;d=retro&#038;r=g 2x" data-lazy-src="https://secure.gravatar.com/avatar/227a7281ab1b5f9d5fd74196600801a5?s=50&amp;is-pending-load=1#038;d=retro&#038;r=g" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"><noscript><img alt='' src='https://secure.gravatar.com/avatar/227a7281ab1b5f9d5fd74196600801a5?s=50&#038;d=retro&#038;r=g' srcset='https://secure.gravatar.com/avatar/227a7281ab1b5f9d5fd74196600801a5?s=100&#038;d=retro&#038;r=g 2x' class='avatar avatar-50 photo' height='50' width='50' loading='lazy'/></noscript></div> <div class="comment-author vcard">
<span class="fn author">WilliamXiao</span>
<a href="https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/#comment-2118">
<time class="entry-date published" datetime="2021-03-14T05:22:25+00:00" content="2021-03-14">
2021-03-14 at 05:22 </time>
</a>
</div>
</div>
<div class="nv-comment-content comment nv-content-wrap">
<p>感谢你的教学！<br />
另外我想知道自建py文件后撰写逻辑程序的部分应该从哪里系统地学习呢，我在初步的时候会clone你的代码照猫画虎hhh。我想自己写逻辑的part应该在哪里学习呢？<br />
谢谢</p>
<div class="edit-reply">
<span class="nv-reply-link"><a rel='nofollow' class='comment-reply-link' href='#comment-2118' data-commentid="2118" data-postid="422" data-belowelement="comment-2118" data-respondelement="respond" data-replyto="回覆給「WilliamXiao」" aria-label='回覆給「WilliamXiao」'>Reply</a></span> </div>
</div>
</article>
</li>
<li class="children" role="listitem"><ol> <li class="comment byuser comment-author-ccs96307 bypostauthor odd alt depth-2" id="comment-item-2119">
<article id="comment-2119" class="nv-comment-article">
<div class="nv-comment-header">
<div class="nv-comment-avatar"><img alt src="https://secure.gravatar.com/avatar/fb7c6baee50bb79acc3afb91e8e5a545?s=50&#038;d=retro&#038;r=g" class="avatar avatar-50 photo jetpack-lazy-image" height="50" width="50" loading="lazy" data-lazy-srcset="https://secure.gravatar.com/avatar/fb7c6baee50bb79acc3afb91e8e5a545?s=100&#038;d=retro&#038;r=g 2x" data-lazy-src="https://secure.gravatar.com/avatar/fb7c6baee50bb79acc3afb91e8e5a545?s=50&amp;is-pending-load=1#038;d=retro&#038;r=g" srcset="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7"><noscript><img alt='' src='https://secure.gravatar.com/avatar/fb7c6baee50bb79acc3afb91e8e5a545?s=50&#038;d=retro&#038;r=g' srcset='https://secure.gravatar.com/avatar/fb7c6baee50bb79acc3afb91e8e5a545?s=100&#038;d=retro&#038;r=g 2x' class='avatar avatar-50 photo' height='50' width='50' loading='lazy'/></noscript></div> <div class="comment-author vcard">
<span class="fn author"><a href='https://clay-atlas.com' rel='external nofollow ugc' class='url'>ccs96307</a></span>
<a href="https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/#comment-2119">
<time class="entry-date published" datetime="2021-03-14T05:38:51+00:00" content="2021-03-14">
2021-03-14 at 05:38 </time>
</a>
</div>
</div>
<div class="nv-comment-content comment nv-content-wrap">
<p>很高興能夠替你提供幫助。<br />
關於邏輯部分的程式，我想每個專案、每個開發者想要的功能都不盡相同，很難說有什麼比較完整的教學。<br />
這方面或許可以參考官方文件、或是網路上前輩們所提供的專案原始碼。</p>
<div class="edit-reply">
<span class="nv-reply-link"><a rel='nofollow' class='comment-reply-link' href='#comment-2119' data-commentid="2119" data-postid="422" data-belowelement="comment-2119" data-respondelement="respond" data-replyto="回覆給「ccs96307」" aria-label='回覆給「ccs96307」'>Reply</a></span> </div>
</div>
</article>
</li>
</ol></li> </ol>
</div>
<div id="respond" class="comment-respond">
<h3 id="reply-title" class="comment-reply-title">Leave a Reply <small><a rel="nofollow" id="cancel-comment-reply-link" href="/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/#respond" style="display:none;">取消回覆</a></small>
</h3>
<form id="commentform" class="comment-form">
<iframe title="留言表單" src="https://jetpack.wordpress.com/jetpack-comment/?blogid=164929906&#038;postid=422&#038;comment_registration=0&#038;require_name_email=0&#038;stc_enabled=0&#038;stb_enabled=0&#038;show_avatars=1&#038;avatar_default=retro&#038;greeting=Leave+a+Reply&#038;greeting_reply=%E5%B0%8D+%25s+%E7%99%BC%E8%A1%A8%E8%BF%B4%E9%9F%BF&#038;color_scheme=light&#038;lang=zh_TW&#038;jetpack_version=10.1&#038;show_cookie_consent=10&#038;has_cookie_consent=0&#038;token_key=%3Bnormal%3B&#038;sig=6c476fb6af05da089736e61af088d49fd11c224a#parent=https%3A%2F%2Fclay-atlas.com%2Fblog%2F2019%2F08%2F27%2Fpyqt5-%25e5%259f%25ba%25e6%259c%25ac%25e6%2595%2599%25e5%25ad%25b8-2-qlabel-qlineedit-qpushbutton%2F" name="jetpack_remote_comment" style="width:100%; height: 430px; border:0;" class="jetpack_remote_comment" id="jetpack_remote_comment" sandbox="allow-same-origin allow-top-navigation allow-scripts allow-forms allow-popups">
									</iframe>
<!--[if !IE]><!-->
<script>
						document.addEventListener('DOMContentLoaded', function () {
							var commentForms = document.getElementsByClassName('jetpack_remote_comment');
							for (var i = 0; i < commentForms.length; i++) {
								commentForms[i].allowTransparency = false;
								commentForms[i].scrolling = 'no';
							}
						});
					</script>
<!--<![endif]-->
</form>
</div>
<input type="hidden" name="comment_parent" id="comment_parent" value="" />
</div>
</article>
<div class="nv-sidebar-wrap col-sm-12 nv-right blog-sidebar">
<aside id="secondary" role="complementary">
<div id="polylang-3" class="widget widget_polylang"><p class="widget-title">Language</p><ul>
<li class="lang-item lang-item-29 lang-item-zh current-lang lang-item-first"><a lang="zh-TW" hreflang="zh-TW" href="https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAMAAABBPP0LAAAAVFBMVEUAILQAGrEAEazhAAD5AADwAACBot+5ued2mNv6aWv7X1/5UVHoAACWltz5+fz+/v5ahNPyRkv5QkL5OTn2MTH3Kir1JiZOe87rOkb1Hh70FRXyDQ3JFHMOAAAAU0lEQVR4AQXBgQ3CMBAAMV8+Iuy/LKhUgB0kRchDfksRbU59R1Xd14If51QNK3Ndc6im7Hg63DVhr/kct2pSr8WRahIWUk1i2XrHo7tYbB8IL/AHd28PeH6kKkoAAAAASUVORK5CYII=" alt="中文 (台灣)" width="16" height="11" style="width: 16px; height: 11px;" /><span style="margin-left:0.3em;">中文 (台灣)</span></a></li>
<li class="lang-item lang-item-36 lang-item-us"><a lang="en-US" hreflang="en-US" href="https://clay-atlas.com/us/blog/2019/09/17/python-english-tutorial-pyqt5-label-lineedit-pushbutton/"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAALCAMAAABBPP0LAAAAmVBMVEViZsViZMJiYrf9gnL8eWrlYkjgYkjZYkj8/PujwPybvPz4+PetraBEgfo+fvo3efkydfkqcvj8Y2T8UlL8Q0P8MzP9k4Hz8/Lu7u4DdPj9/VrKysI9fPoDc/EAZ7z7IiLHYkjp6ekCcOTk5OIASbfY/v21takAJrT5Dg6sYkjc3Nn94t2RkYD+y8KeYkjs/v7l5fz0dF22YkjWvcOLAAAAgElEQVR4AR2KNULFQBgGZ5J13KGGKvc/Cw1uPe62eb9+Jr1EUBFHSgxxjP2Eca6AfUSfVlUfBvm1Ui1bqafctqMndNkXpb01h5TLx4b6TIXgwOCHfjv+/Pz+5vPRw7txGWT2h6yO0/GaYltIp5PT1dEpLNPL/SdWjYjAAZtvRPgHJX4Xio+DSrkAAAAASUVORK5CYII=" alt="English" width="16" height="11" style="width: 16px; height: 11px;" /><span style="margin-left:0.3em;">English</span></a></li>
</ul>
</div><div id="search-2" class="widget widget_search"><p class="widget-title">Search</p>
<form role="search" method="get" class="search-form" action="https://clay-atlas.com/">
<label>
<span class="screen-reader-text">Search for...</span>
</label>
<input type="search" class="search-field" placeholder="Search for..." value="" name="s" />
<button type="submit" class="search-submit" aria-label="Search">
<span class="nv-search-icon-wrap">
<div class="nv-icon nv-search">
<svg width="15" height="15" viewBox="0 0 1792 1792" xmlns="http://www.w3.org/2000/svg"><path d="M1216 832q0-185-131.5-316.5t-316.5-131.5-316.5 131.5-131.5 316.5 131.5 316.5 316.5 131.5 316.5-131.5 131.5-316.5zm512 832q0 52-38 90t-90 38q-54 0-90-38l-343-342q-179 124-399 124-143 0-273.5-55.5t-225-150-150-225-55.5-273.5 55.5-273.5 150-225 225-150 273.5-55.5 273.5 55.5 225 150 150 225 55.5 273.5q0 220-124 399l343 343q37 37 37 90z" /></svg>
</div> </span>
</button>
</form>
</div><div id="categories-4" class="widget widget_categories"><p class="widget-title">Categories</p><form action="https://clay-atlas.com" method="get"><label class="screen-reader-text" for="cat">Categories</label><select name='cat' id='cat' class='postform'>
<option value='-1'>選取分類</option>
<option class="level-0" value="85">Android Studio&nbsp;&nbsp;(5)</option>
<option class="level-0" value="403">Apple&nbsp;&nbsp;(37)</option>
<option class="level-1" value="561">&nbsp;&nbsp;&nbsp;AppleScript&nbsp;&nbsp;(6)</option>
<option class="level-1" value="404">&nbsp;&nbsp;&nbsp;iPad&nbsp;&nbsp;(3)</option>
<option class="level-1" value="456">&nbsp;&nbsp;&nbsp;MacOS&nbsp;&nbsp;(34)</option>
<option class="level-0" value="424">C/C++&nbsp;&nbsp;(52)</option>
<option class="level-1" value="649">&nbsp;&nbsp;&nbsp;C&nbsp;&nbsp;(10)</option>
<option class="level-1" value="464">&nbsp;&nbsp;&nbsp;C++&nbsp;&nbsp;(43)</option>
<option class="level-0" value="555">CSS&nbsp;&nbsp;(3)</option>
<option class="level-0" value="517">Dart&nbsp;&nbsp;(2)</option>
<option class="level-0" value="73">Database&nbsp;&nbsp;(9)</option>
<option class="level-1" value="74">&nbsp;&nbsp;&nbsp;MySQL&nbsp;&nbsp;(6)</option>
<option class="level-1" value="520">&nbsp;&nbsp;&nbsp;SQLite&nbsp;&nbsp;(2)</option>
<option class="level-0" value="492">Excel&nbsp;&nbsp;(1)</option>
<option class="level-0" value="71">Flutter&nbsp;&nbsp;(43)</option>
<option class="level-1" value="83">&nbsp;&nbsp;&nbsp;Intellij IDEA&nbsp;&nbsp;(2)</option>
<option class="level-0" value="7">Game&nbsp;&nbsp;(20)</option>
<option class="level-1" value="88">&nbsp;&nbsp;&nbsp;NS&nbsp;&nbsp;(6)</option>
<option class="level-1" value="103">&nbsp;&nbsp;&nbsp;PS4&nbsp;&nbsp;(13)</option>
<option class="level-1" value="96">&nbsp;&nbsp;&nbsp;PS5&nbsp;&nbsp;(2)</option>
<option class="level-0" value="496">Git&nbsp;&nbsp;(7)</option>
<option class="level-1" value="539">&nbsp;&nbsp;&nbsp;Github&nbsp;&nbsp;(6)</option>
<option class="level-0" value="105">HTML&nbsp;&nbsp;(8)</option>
<option class="level-0" value="109">JavaScript&nbsp;&nbsp;(3)</option>
<option class="level-0" value="500">LeetCdoe&nbsp;&nbsp;(29)</option>
<option class="level-0" value="26">Linux&nbsp;&nbsp;(123)</option>
<option class="level-0" value="6">Machine Learning&nbsp;&nbsp;(76)</option>
<option class="level-1" value="90">&nbsp;&nbsp;&nbsp;Keras&nbsp;&nbsp;(7)</option>
<option class="level-1" value="28">&nbsp;&nbsp;&nbsp;PyTorch&nbsp;&nbsp;(49)</option>
<option class="level-1" value="66">&nbsp;&nbsp;&nbsp;Scikit-Learn&nbsp;&nbsp;(7)</option>
<option class="level-1" value="439">&nbsp;&nbsp;&nbsp;Tensorflow&nbsp;&nbsp;(3)</option>
<option class="level-0" value="22">Movie&nbsp;&nbsp;(1)</option>
<option class="level-0" value="5">NLP&nbsp;&nbsp;(26)</option>
<option class="level-0" value="24">Novel&nbsp;&nbsp;(9)</option>
<option class="level-0" value="59">Others&nbsp;&nbsp;(7)</option>
<option class="level-0" value="557">PHP&nbsp;&nbsp;(1)</option>
<option class="level-0" value="4">Python&nbsp;&nbsp;(281)</option>
<option class="level-1" value="114">&nbsp;&nbsp;&nbsp;Flask&nbsp;&nbsp;(4)</option>
<option class="level-1" value="68">&nbsp;&nbsp;&nbsp;Others&nbsp;&nbsp;(4)</option>
<option class="level-1" value="62">&nbsp;&nbsp;&nbsp;Packages&nbsp;&nbsp;(56)</option>
<option class="level-1" value="80">&nbsp;&nbsp;&nbsp;PyCharm&nbsp;&nbsp;(11)</option>
<option class="level-1" value="946">&nbsp;&nbsp;&nbsp;Pygame&nbsp;&nbsp;(2)</option>
<option class="level-1" value="17">&nbsp;&nbsp;&nbsp;PyQt5&nbsp;&nbsp;(35)</option>
<option class="level-1" value="851">&nbsp;&nbsp;&nbsp;PySide6&nbsp;&nbsp;(4)</option>
<option class="level-1" value="63">&nbsp;&nbsp;&nbsp;Python Tutorial&nbsp;&nbsp;(19)</option>
<option class="level-0" value="515">Ruby&nbsp;&nbsp;(1)</option>
<option class="level-0" value="448">Tools&nbsp;&nbsp;(10)</option>
<option class="level-0" value="1">Uncategorized&nbsp;&nbsp;(4)</option>
<option class="level-0" value="452">Windows&nbsp;&nbsp;(12)</option>
<option class="level-0" value="14">Word&nbsp;&nbsp;(5)</option>
<option class="level-0" value="99">WordPress&nbsp;&nbsp;(41)</option>
<option class="level-0" value="3">圍棋&nbsp;&nbsp;(3)</option>
<option class="level-0" value="112">漫畫&nbsp;&nbsp;(2)</option>
</select>
</form>
<script type="text/javascript">
/* <![CDATA[ */
(function() {
	var dropdown = document.getElementById( "cat" );
	function onCatChange() {
		if ( dropdown.options[ dropdown.selectedIndex ].value > 0 ) {
			dropdown.parentNode.submit();
		}
	}
	dropdown.onchange = onCatChange;
})();
/* ]]> */
</script>
</div><div id="archives-4" class="widget widget_archive"><p class="widget-title">Archives</p> <label class="screen-reader-text" for="archives-dropdown-4">Archives</label>
<select id="archives-dropdown-4" name="archive-dropdown">
<option value="">選取月份</option>
<option value='https://clay-atlas.com/blog/2021/09/'> 2021 年 9 月 &nbsp;(7)</option>
<option value='https://clay-atlas.com/blog/2021/08/'> 2021 年 8 月 &nbsp;(20)</option>
<option value='https://clay-atlas.com/blog/2021/07/'> 2021 年 7 月 &nbsp;(24)</option>
<option value='https://clay-atlas.com/blog/2021/06/'> 2021 年 6 月 &nbsp;(24)</option>
<option value='https://clay-atlas.com/blog/2021/05/'> 2021 年 5 月 &nbsp;(32)</option>
<option value='https://clay-atlas.com/blog/2021/04/'> 2021 年 4 月 &nbsp;(26)</option>
<option value='https://clay-atlas.com/blog/2021/03/'> 2021 年 3 月 &nbsp;(31)</option>
<option value='https://clay-atlas.com/blog/2021/02/'> 2021 年 2 月 &nbsp;(14)</option>
<option value='https://clay-atlas.com/blog/2021/01/'> 2021 年 1 月 &nbsp;(18)</option>
<option value='https://clay-atlas.com/blog/2020/12/'> 2020 年 12 月 &nbsp;(17)</option>
<option value='https://clay-atlas.com/blog/2020/11/'> 2020 年 11 月 &nbsp;(25)</option>
<option value='https://clay-atlas.com/blog/2020/10/'> 2020 年 10 月 &nbsp;(24)</option>
<option value='https://clay-atlas.com/blog/2020/09/'> 2020 年 9 月 &nbsp;(21)</option>
<option value='https://clay-atlas.com/blog/2020/08/'> 2020 年 8 月 &nbsp;(17)</option>
<option value='https://clay-atlas.com/blog/2020/07/'> 2020 年 7 月 &nbsp;(21)</option>
<option value='https://clay-atlas.com/blog/2020/06/'> 2020 年 6 月 &nbsp;(19)</option>
<option value='https://clay-atlas.com/blog/2020/05/'> 2020 年 5 月 &nbsp;(28)</option>
<option value='https://clay-atlas.com/blog/2020/04/'> 2020 年 4 月 &nbsp;(31)</option>
<option value='https://clay-atlas.com/blog/2020/03/'> 2020 年 3 月 &nbsp;(24)</option>
<option value='https://clay-atlas.com/blog/2020/02/'> 2020 年 2 月 &nbsp;(25)</option>
<option value='https://clay-atlas.com/blog/2020/01/'> 2020 年 1 月 &nbsp;(32)</option>
<option value='https://clay-atlas.com/blog/2019/12/'> 2019 年 12 月 &nbsp;(39)</option>
<option value='https://clay-atlas.com/blog/2019/11/'> 2019 年 11 月 &nbsp;(53)</option>
<option value='https://clay-atlas.com/blog/2019/10/'> 2019 年 10 月 &nbsp;(34)</option>
<option value='https://clay-atlas.com/blog/2019/09/'> 2019 年 9 月 &nbsp;(15)</option>
<option value='https://clay-atlas.com/blog/2019/08/'> 2019 年 8 月 &nbsp;(18)</option>
<option value='https://clay-atlas.com/blog/2019/07/'> 2019 年 7 月 &nbsp;(15)</option>
</select>
<script type="text/javascript">
/* <![CDATA[ */
(function() {
	var dropdown = document.getElementById( "archives-dropdown-4" );
	function onSelectChange() {
		if ( dropdown.options[ dropdown.selectedIndex ].value !== '' ) {
			document.location.href = this.options[ this.selectedIndex ].value;
		}
	}
	dropdown.onchange = onSelectChange;
})();
/* ]]> */
</script>
</div><div id="text-4" class="widget widget_text"><p class="widget-title">系列文章</p> <div class="textwidget"><ul>
<li><a href="https://clay-atlas.com/essay-series/">隨筆散記</a></li>
<li><a href="https://clay-atlas.com/machine-learning-notes/">機器學習筆記</a></li>
</ul>
</div>
</div><div id="tag_cloud-3" class="widget widget_tag_cloud"><p class="widget-title">TAGS</p><div class="tagcloud"><a href="https://clay-atlas.com/blog/tag/android-studio/" class="tag-cloud-link tag-link-84 tag-link-position-1" style="font-size: 12pt;" aria-label="Android Studio (5 個項目)">Android Studio<span class="tag-link-count"> (5)</span></a>
<a href="https://clay-atlas.com/blog/tag/apple/" class="tag-cloud-link tag-link-406 tag-link-position-2" style="font-size: 12pt;" aria-label="Apple (28 個項目)">Apple<span class="tag-link-count"> (28)</span></a>
<a href="https://clay-atlas.com/blog/tag/applescript/" class="tag-cloud-link tag-link-563 tag-link-position-3" style="font-size: 12pt;" aria-label="AppleScript (6 個項目)">AppleScript<span class="tag-link-count"> (6)</span></a>
<a href="https://clay-atlas.com/blog/tag/c/" class="tag-cloud-link tag-link-425 tag-link-position-4" style="font-size: 12pt;" aria-label="C++ (43 個項目)">C++<span class="tag-link-count"> (43)</span></a>
<a href="https://clay-atlas.com/blog/tag/css/" class="tag-cloud-link tag-link-556 tag-link-position-5" style="font-size: 12pt;" aria-label="CSS (3 個項目)">CSS<span class="tag-link-count"> (3)</span></a>
<a href="https://clay-atlas.com/blog/tag/cpl/" class="tag-cloud-link tag-link-651 tag-link-position-6" style="font-size: 12pt;" aria-label="C 語言 (10 個項目)">C 語言<span class="tag-link-count"> (10)</span></a>
<a href="https://clay-atlas.com/blog/tag/database/" class="tag-cloud-link tag-link-86 tag-link-position-7" style="font-size: 12pt;" aria-label="Database (9 個項目)">Database<span class="tag-link-count"> (9)</span></a>
<a href="https://clay-atlas.com/blog/tag/flask/" class="tag-cloud-link tag-link-115 tag-link-position-8" style="font-size: 12pt;" aria-label="Flask (4 個項目)">Flask<span class="tag-link-count"> (4)</span></a>
<a href="https://clay-atlas.com/blog/tag/flutter/" class="tag-cloud-link tag-link-72 tag-link-position-9" style="font-size: 12pt;" aria-label="Flutter (42 個項目)">Flutter<span class="tag-link-count"> (42)</span></a>
<a href="https://clay-atlas.com/blog/tag/game/" class="tag-cloud-link tag-link-110 tag-link-position-10" style="font-size: 12pt;" aria-label="Game (17 個項目)">Game<span class="tag-link-count"> (17)</span></a>
<a href="https://clay-atlas.com/blog/tag/git/" class="tag-cloud-link tag-link-497 tag-link-position-11" style="font-size: 12pt;" aria-label="Git (5 個項目)">Git<span class="tag-link-count"> (5)</span></a>
<a href="https://clay-atlas.com/blog/tag/github/" class="tag-cloud-link tag-link-538 tag-link-position-12" style="font-size: 12pt;" aria-label="Github (6 個項目)">Github<span class="tag-link-count"> (6)</span></a>
<a href="https://clay-atlas.com/blog/tag/html/" class="tag-cloud-link tag-link-106 tag-link-position-13" style="font-size: 12pt;" aria-label="HTML (8 個項目)">HTML<span class="tag-link-count"> (8)</span></a>
<a href="https://clay-atlas.com/blog/tag/ipad/" class="tag-cloud-link tag-link-405 tag-link-position-14" style="font-size: 12pt;" aria-label="iPad (3 個項目)">iPad<span class="tag-link-count"> (3)</span></a>
<a href="https://clay-atlas.com/blog/tag/javascript/" class="tag-cloud-link tag-link-108 tag-link-position-15" style="font-size: 12pt;" aria-label="JavaScript (3 個項目)">JavaScript<span class="tag-link-count"> (3)</span></a>
<a href="https://clay-atlas.com/blog/tag/keras/" class="tag-cloud-link tag-link-91 tag-link-position-16" style="font-size: 12pt;" aria-label="Keras (7 個項目)">Keras<span class="tag-link-count"> (7)</span></a>
<a href="https://clay-atlas.com/blog/tag/kotlin/" class="tag-cloud-link tag-link-675 tag-link-position-17" style="font-size: 12pt;" aria-label="Kotlin (3 個項目)">Kotlin<span class="tag-link-count"> (3)</span></a>
<a href="https://clay-atlas.com/blog/tag/leetcode/" class="tag-cloud-link tag-link-501 tag-link-position-18" style="font-size: 12pt;" aria-label="LeetCode (29 個項目)">LeetCode<span class="tag-link-count"> (29)</span></a>
<a href="https://clay-atlas.com/blog/tag/linux/" class="tag-cloud-link tag-link-27 tag-link-position-19" style="font-size: 12pt;" aria-label="Linux (122 個項目)">Linux<span class="tag-link-count"> (122)</span></a>
<a href="https://clay-atlas.com/blog/tag/machine-learning/" class="tag-cloud-link tag-link-12 tag-link-position-20" style="font-size: 12pt;" aria-label="Machine Learning (71 個項目)">Machine Learning<span class="tag-link-count"> (71)</span></a>
<a href="https://clay-atlas.com/blog/tag/macos/" class="tag-cloud-link tag-link-455 tag-link-position-21" style="font-size: 12pt;" aria-label="MacOS (34 個項目)">MacOS<span class="tag-link-count"> (34)</span></a>
<a href="https://clay-atlas.com/blog/tag/microsoft/" class="tag-cloud-link tag-link-95 tag-link-position-22" style="font-size: 12pt;" aria-label="Microsoft (6 個項目)">Microsoft<span class="tag-link-count"> (6)</span></a>
<a href="https://clay-atlas.com/blog/tag/mysql/" class="tag-cloud-link tag-link-75 tag-link-position-23" style="font-size: 12pt;" aria-label="MySQL (6 個項目)">MySQL<span class="tag-link-count"> (6)</span></a>
<a href="https://clay-atlas.com/blog/tag/nlp/" class="tag-cloud-link tag-link-10 tag-link-position-24" style="font-size: 12pt;" aria-label="NLP (27 個項目)">NLP<span class="tag-link-count"> (27)</span></a>
<a href="https://clay-atlas.com/blog/tag/novel/" class="tag-cloud-link tag-link-25 tag-link-position-25" style="font-size: 12pt;" aria-label="Novel (9 個項目)">Novel<span class="tag-link-count"> (9)</span></a>
<a href="https://clay-atlas.com/blog/tag/ns/" class="tag-cloud-link tag-link-87 tag-link-position-26" style="font-size: 12pt;" aria-label="NS (6 個項目)">NS<span class="tag-link-count"> (6)</span></a>
<a href="https://clay-atlas.com/blog/tag/others/" class="tag-cloud-link tag-link-60 tag-link-position-27" style="font-size: 12pt;" aria-label="Others (9 個項目)">Others<span class="tag-link-count"> (9)</span></a>
<a href="https://clay-atlas.com/blog/tag/ps4/" class="tag-cloud-link tag-link-104 tag-link-position-28" style="font-size: 12pt;" aria-label="PS4 (13 個項目)">PS4<span class="tag-link-count"> (13)</span></a>
<a href="https://clay-atlas.com/blog/tag/pycharm/" class="tag-cloud-link tag-link-81 tag-link-position-29" style="font-size: 12pt;" aria-label="PyCharm (11 個項目)">PyCharm<span class="tag-link-count"> (11)</span></a>
<a href="https://clay-atlas.com/blog/tag/pyqt5/" class="tag-cloud-link tag-link-18 tag-link-position-30" style="font-size: 12pt;" aria-label="PyQt5 (34 個項目)">PyQt5<span class="tag-link-count"> (34)</span></a>
<a href="https://clay-atlas.com/blog/tag/python/" class="tag-cloud-link tag-link-9 tag-link-position-31" style="font-size: 12pt;" aria-label="Python (267 個項目)">Python<span class="tag-link-count"> (267)</span></a>
<a href="https://clay-atlas.com/blog/tag/python-packages/" class="tag-cloud-link tag-link-65 tag-link-position-32" style="font-size: 12pt;" aria-label="Python Packages (54 個項目)">Python Packages<span class="tag-link-count"> (54)</span></a>
<a href="https://clay-atlas.com/blog/tag/python-tutorial/" class="tag-cloud-link tag-link-64 tag-link-position-33" style="font-size: 12pt;" aria-label="Python Tutorial (17 個項目)">Python Tutorial<span class="tag-link-count"> (17)</span></a>
<a href="https://clay-atlas.com/blog/tag/pytorch/" class="tag-cloud-link tag-link-16 tag-link-position-34" style="font-size: 12pt;" aria-label="PyTorch (49 個項目)">PyTorch<span class="tag-link-count"> (49)</span></a>
<a href="https://clay-atlas.com/blog/tag/scikit-learn/" class="tag-cloud-link tag-link-67 tag-link-position-35" style="font-size: 12pt;" aria-label="Scikit-Learn (7 個項目)">Scikit-Learn<span class="tag-link-count"> (7)</span></a>
<a href="https://clay-atlas.com/blog/tag/tensorflow/" class="tag-cloud-link tag-link-441 tag-link-position-36" style="font-size: 12pt;" aria-label="Tensorflow (3 個項目)">Tensorflow<span class="tag-link-count"> (3)</span></a>
<a href="https://clay-atlas.com/blog/tag/tools/" class="tag-cloud-link tag-link-449 tag-link-position-37" style="font-size: 12pt;" aria-label="Tools (10 個項目)">Tools<span class="tag-link-count"> (10)</span></a>
<a href="https://clay-atlas.com/blog/tag/unity/" class="tag-cloud-link tag-link-715 tag-link-position-38" style="font-size: 12pt;" aria-label="Unity (25 個項目)">Unity<span class="tag-link-count"> (25)</span></a>
<a href="https://clay-atlas.com/blog/tag/vim/" class="tag-cloud-link tag-link-754 tag-link-position-39" style="font-size: 12pt;" aria-label="VIM (6 個項目)">VIM<span class="tag-link-count"> (6)</span></a>
<a href="https://clay-atlas.com/blog/tag/windows/" class="tag-cloud-link tag-link-419 tag-link-position-40" style="font-size: 12pt;" aria-label="Windows (9 個項目)">Windows<span class="tag-link-count"> (9)</span></a>
<a href="https://clay-atlas.com/blog/tag/word/" class="tag-cloud-link tag-link-15 tag-link-position-41" style="font-size: 12pt;" aria-label="Word (5 個項目)">Word<span class="tag-link-count"> (5)</span></a>
<a href="https://clay-atlas.com/blog/tag/wordpress/" class="tag-cloud-link tag-link-98 tag-link-position-42" style="font-size: 12pt;" aria-label="WordPress (40 個項目)">WordPress<span class="tag-link-count"> (40)</span></a>
<a href="https://clay-atlas.com/blog/tag/go/" class="tag-cloud-link tag-link-77 tag-link-position-43" style="font-size: 12pt;" aria-label="圍棋 (3 個項目)">圍棋<span class="tag-link-count"> (3)</span></a>
<a href="https://clay-atlas.com/blog/tag/%e8%bb%8c%e8%b7%a1/" class="tag-cloud-link tag-link-13 tag-link-position-44" style="font-size: 12pt;" aria-label="軌跡 (4 個項目)">軌跡<span class="tag-link-count"> (4)</span></a>
<a href="https://clay-atlas.com/blog/tag/computer/" class="tag-cloud-link tag-link-670 tag-link-position-45" style="font-size: 12pt;" aria-label="電腦 (4 個項目)">電腦<span class="tag-link-count"> (4)</span></a></div>
</div>
<div id="recent-posts-2" class="widget widget_recent_entries">
<p class="widget-title">Recent Posts</p>
<ul>
<li>
<a href="https://clay-atlas.com/blog/2021/09/10/python-en-determine-variable-function/">[Python] 判斷一個變數是否為函式</a>
</li>
<li>
<a href="https://clay-atlas.com/blog/2021/09/09/pygame-cn-input-box/">[Pygame] 簡單的文字輸入框製作筆記</a>
</li>
<li>
<a href="https://clay-atlas.com/blog/2021/09/07/pygame-cn-download-install-hello-world/">[Pygame] 下載並執行 Hello World 程式</a>
</li>
<li>
<a href="https://clay-atlas.com/blog/2021/09/06/machine-learning-cn-mean-absolute-error/">[Machine Learning] MAE 指標介紹與程式實作</a>
</li>
<li>
<a href="https://clay-atlas.com/blog/2021/09/02/tool-cn-imatheq-introduction/">[工具] 線上的數學公式編輯器 iMathEQ</a>
</li>
</ul>
</div><div id="calendar-3" class="widget widget_calendar"><p class="widget-title">Calender</p><div id="calendar_wrap" class="calendar_wrap"><table id="wp-calendar" class="wp-calendar-table">
<caption>2019 年 8 月</caption>
<thead>
<tr>
<th scope="col" title="星期一">一</th>
<th scope="col" title="星期二">二</th>
<th scope="col" title="星期三">三</th>
<th scope="col" title="星期四">四</th>
<th scope="col" title="星期五">五</th>
<th scope="col" title="星期六">六</th>
<th scope="col" title="星期日">日</th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="3" class="pad">&nbsp;</td><td>1</td><td><a href="https://clay-atlas.com/blog/2019/08/02/" aria-label="文章發佈於 2019 年 8 月 2 日">2</a></td><td><a href="https://clay-atlas.com/blog/2019/08/03/" aria-label="文章發佈於 2019 年 8 月 3 日">3</a></td><td>4</td>
</tr>
<tr>
<td><a href="https://clay-atlas.com/blog/2019/08/05/" aria-label="文章發佈於 2019 年 8 月 5 日">5</a></td><td>6</td><td>7</td><td><a href="https://clay-atlas.com/blog/2019/08/08/" aria-label="文章發佈於 2019 年 8 月 8 日">8</a></td><td><a href="https://clay-atlas.com/blog/2019/08/09/" aria-label="文章發佈於 2019 年 8 月 9 日">9</a></td><td><a href="https://clay-atlas.com/blog/2019/08/10/" aria-label="文章發佈於 2019 年 8 月 10 日">10</a></td><td>11</td>
</tr>
<tr>
<td>12</td><td><a href="https://clay-atlas.com/blog/2019/08/13/" aria-label="文章發佈於 2019 年 8 月 13 日">13</a></td><td>14</td><td>15</td><td>16</td><td><a href="https://clay-atlas.com/blog/2019/08/17/" aria-label="文章發佈於 2019 年 8 月 17 日">17</a></td><td>18</td>
</tr>
<tr>
<td><a href="https://clay-atlas.com/blog/2019/08/19/" aria-label="文章發佈於 2019 年 8 月 19 日">19</a></td><td><a href="https://clay-atlas.com/blog/2019/08/20/" aria-label="文章發佈於 2019 年 8 月 20 日">20</a></td><td>21</td><td>22</td><td><a href="https://clay-atlas.com/blog/2019/08/23/" aria-label="文章發佈於 2019 年 8 月 23 日">23</a></td><td>24</td><td><a href="https://clay-atlas.com/blog/2019/08/25/" aria-label="文章發佈於 2019 年 8 月 25 日">25</a></td>
</tr>
<tr>
<td><a href="https://clay-atlas.com/blog/2019/08/26/" aria-label="文章發佈於 2019 年 8 月 26 日">26</a></td><td><a href="https://clay-atlas.com/blog/2019/08/27/" aria-label="文章發佈於 2019 年 8 月 27 日">27</a></td><td><a href="https://clay-atlas.com/blog/2019/08/28/" aria-label="文章發佈於 2019 年 8 月 28 日">28</a></td><td>29</td><td>30</td><td><a href="https://clay-atlas.com/blog/2019/08/31/" aria-label="文章發佈於 2019 年 8 月 31 日">31</a></td>
<td class="pad" colspan="1">&nbsp;</td>
</tr>
</tbody>
</table><nav aria-label="上個月及下個月" class="wp-calendar-nav">
<span class="wp-calendar-nav-prev"><a href="https://clay-atlas.com/blog/2019/07/">&laquo; 7 月</a></span>
<span class="pad">&nbsp;</span>
<span class="wp-calendar-nav-next"><a href="https://clay-atlas.com/blog/2019/09/">9 月 &raquo;</a></span>
</nav></div></div><div id="email-subscribers-form-2" class="widget widget_email-subscribers-form"><p class="widget-title"> Subscription </p>
<div class="emaillist" id="es_form_f1-n1">
<form action="/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/#es_form_f1-n1" method="post" class="es_subscription_form es_shortcode_form" id="es_subscription_form_613adbf0b4a51" data-source="ig-es">
<div class="es-field-wrap"><label>Name*<br /><input type="text" name="esfpx_name" class="ig_es_form_field_name" placeholder="" value="" required="required" /></label></div><div class="es-field-wrap"><label>Email*<br /><input class="es_required_field es_txt_email ig_es_form_field_email" type="email" name="esfpx_email" value="" placeholder="" required="required" /></label></div><input type="hidden" name="esfpx_lists[]" value="0aa0bef661d5" /><input type="hidden" name="esfpx_form_id" value="1" /> <input type="hidden" name="es" value="subscribe" />
<input type="hidden" name="esfpx_es_form_identifier" value="f1-n1" />
<input type="hidden" name="esfpx_es_email_page" value="422" />
<input type="hidden" name="esfpx_es_email_page_url" value="https://clay-atlas.com/blog/2019/08/27/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton/" />
<input type="hidden" name="esfpx_status" value="Unconfirmed" />
<input type="hidden" name="esfpx_es-subscribe" id="es-subscribe" value="3a6b13e04e" />
<label style="position:absolute;top:-99999px;left:-99999px;z-index:-99;"><input type="email" name="esfpx_es_hp_email" class="es_required_field" tabindex="-1" autocomplete="-1" value="" /></label>
<input type="submit" name="submit" class="es_subscription_form_submit es_submit_button es_textbox_button" id="es_subscription_form_submit_613adbf0b4a51" value="Subscribe" />
<span class="es_spinner_image" id="spinner-image"><img src="https://clay-atlas.com/wp-content/plugins/email-subscribers/lite/public/images/spinner.gif" alt="Loading" /></span>
</form>
<span class="es_subscription_message " id="es_subscription_message_613adbf0b4a51">
</span>
</div>
</div><div id="block-9" class="widget widget_block">
<div class="wp-block-group alignwide"><div class="wp-block-group__inner-container">
<p class="has-medium-font-size"><strong>Instagram</strong></p>
<div class="wp-block-columns alignwide">
<div class="wp-block-column" style="flex-basis:100%"> <div class="wp-block-jetpack-instagram-gallery wp-block-jetpack-instagram-gallery__grid wp-block-jetpack-instagram-gallery__grid-columns-3 is-stacked-on-mobile" style="grid-gap: 10px; --latest-instagram-posts-spacing: 10px;">
<a class="wp-block-jetpack-instagram-gallery__grid-post" href="https://www.instagram.com/p/CTfD7kYpYNA/" rel="noopener noreferrer" target="_blank">
<img alt="#cat #catlover #meow #blackcat #kitty" src="https://scontent-lax3-1.cdninstagram.com/v/t51.29350-15/241390868_1003775583777376_1723088239752021424_n.jpg?_nc_cat=105&#038;ccb=1-5&#038;_nc_sid=8ae9d6&#038;_nc_ohc=2dzoCkNHQaoAX_wP2ri&#038;_nc_ht=scontent-lax3-1.cdninstagram.com&#038;edm=ANo9K5cEAAAA&#038;oh=6833309a50b8c92e4688dbe1ff489ab7&#038;oe=6140AF47" />
</a>
<a class="wp-block-jetpack-instagram-gallery__grid-post" href="https://www.instagram.com/p/CTZt77vJMV7/" rel="noopener noreferrer" target="_blank">
<img alt="#travel #adventure #outdoor #explorer #naturelover #clouds #landscapes #traveltheworld" src="https://scontent-lax3-2.cdninstagram.com/v/t51.29350-15/241426308_245202220817307_4044494931991250804_n.jpg?_nc_cat=103&#038;ccb=1-5&#038;_nc_sid=8ae9d6&#038;_nc_ohc=y2NRGRUTV4UAX9ieiqL&#038;_nc_ht=scontent-lax3-2.cdninstagram.com&#038;edm=ANo9K5cEAAAA&#038;oh=2f7871300db82963ca9d4df0367c8ee5&#038;oe=613EE097" />
</a>
<a class="wp-block-jetpack-instagram-gallery__grid-post" href="https://www.instagram.com/p/CTMuBSoJ0ul/" rel="noopener noreferrer" target="_blank">
<img alt="You need to exercise more!" src="https://scontent-lax3-1.cdninstagram.com/v/t51.29350-15/240944082_352631393129306_8140257280431992790_n.jpg?_nc_cat=104&#038;ccb=1-5&#038;_nc_sid=8ae9d6&#038;_nc_ohc=pKzFXded4awAX9ClfWy&#038;_nc_ht=scontent-lax3-1.cdninstagram.com&#038;edm=ANo9K5cEAAAA&#038;oh=ab9c92e1136892f4a859a7b3fdd36e2a&#038;oe=613F81FF" />
</a>
<a class="wp-block-jetpack-instagram-gallery__grid-post" href="https://www.instagram.com/p/CTKJ7qlJvBk/" rel="noopener noreferrer" target="_blank">
<img alt="One day. " src="https://scontent-lax3-1.cdninstagram.com/v/t51.29350-15/240649604_210654647623561_4995680592818599419_n.jpg?_nc_cat=110&#038;ccb=1-5&#038;_nc_sid=8ae9d6&#038;_nc_ohc=czyZM8pRLY8AX88peI2&#038;_nc_ht=scontent-lax3-1.cdninstagram.com&#038;edm=ANo9K5cEAAAA&#038;oh=4e4d86f8dfda0e0ac45140ffe35c10ef&#038;oe=61402714" />
</a>
<a class="wp-block-jetpack-instagram-gallery__grid-post" href="https://www.instagram.com/p/CTHxqw0p82x/" rel="noopener noreferrer" target="_blank">
<img alt="The magic that attract the cat&#039;s attention." src="https://scontent-lax3-1.cdninstagram.com/v/t51.29350-15/240819280_382518803314078_6859955951202642167_n.jpg?_nc_cat=110&#038;ccb=1-5&#038;_nc_sid=8ae9d6&#038;_nc_ohc=jDuwy-1VFRoAX8KgYsS&#038;_nc_ht=scontent-lax3-1.cdninstagram.com&#038;edm=ANo9K5cEAAAA&#038;oh=5f15e5dcf4515c9b67ae7ebf9a1a1556&#038;oe=613FB178" />
</a>
<a class="wp-block-jetpack-instagram-gallery__grid-post" href="https://www.instagram.com/p/CTE0Me4pI14/" rel="noopener noreferrer" target="_blank">
<img alt="The last one is a larger white cat." src="https://scontent-lax3-1.cdninstagram.com/v/t51.29350-15/240519957_233510605354985_8314218512302661472_n.jpg?_nc_cat=109&#038;ccb=1-5&#038;_nc_sid=8ae9d6&#038;_nc_ohc=fs8yUjigt6IAX-LBcqv&#038;_nc_ht=scontent-lax3-1.cdninstagram.com&#038;edm=ANo9K5cEAAAA&#038;oh=f3effc1eb0ca9ac6f8b43003b5d447ad&#038;oe=613F2F66" />
</a>
<a class="wp-block-jetpack-instagram-gallery__grid-post" href="https://www.instagram.com/p/CTCxdAyp8mf/" rel="noopener noreferrer" target="_blank">
<img alt="#travel #outdoor #adventure #explorer #naturelover #landscapes #mountains" src="https://scontent-lax3-2.cdninstagram.com/v/t51.29350-15/240466164_614991186549570_1708026473853621237_n.jpg?_nc_cat=111&#038;ccb=1-5&#038;_nc_sid=8ae9d6&#038;_nc_ohc=1y8xvk9UNmEAX-1UtnU&#038;_nc_ht=scontent-lax3-2.cdninstagram.com&#038;edm=ANo9K5cEAAAA&#038;oh=62504cc68196fee58bbf07eec1c01be4&#038;oe=613EE671" />
</a>
<a class="wp-block-jetpack-instagram-gallery__grid-post" href="https://www.instagram.com/p/CGHKLThJNqv/" rel="noopener noreferrer" target="_blank">
<img alt="https://www.instagram.com/p/CGHKLThJNqv/" src="https://scontent-lax3-1.cdninstagram.com/v/t51.29350-15/120955043_156667206090883_150268462061461543_n.jpg?_nc_cat=109&#038;ccb=1-5&#038;_nc_sid=8ae9d6&#038;_nc_ohc=x8HXSTc59vAAX8kCBP2&#038;_nc_ht=scontent-lax3-1.cdninstagram.com&#038;edm=ANo9K5cEAAAA&#038;oh=0584856f68e1f44b2eabf380b3de721c&#038;oe=61406CDE" />
</a>
</div>
</div>
</div>
</div></div>
</div>
</aside>
</div>
</div>
</div>
</main>
<footer class="site-footer" id="site-footer" next-page-hide>
<div class="hfg_footer">
<div class="footer--row footer-top layout-full-contained" id="cb-row--footer-top" data-row-id="top" data-show-on="desktop">
<div class="footer--row-inner footer-top-inner footer-content-wrap">
<div class="container">
<div class="hfg-grid nv-footer-content hfg-grid-top row--wrapper row " data-section="hfg_footer_layout_top">
<div class="builder-item hfg-item-last hfg-item-first col-7 desktop-left tablet-left mobile-left hfg-item-v-middle offset-5"><div class="item--inner builder-item--footer-one-widgets" data-section="neve_sidebar-widgets-footer-one-widgets" data-item-id="footer-one-widgets">
<div class="widget-area">
<div id="text-2" class="widget widget_text"><p class="widget-title">聯絡我</p> <div class="textwidget"><p>電子信箱: <a href="/cdn-cgi/l/email-protection" class="__cf_email__" data-cfemail="90f3f3e3a9a6a3a0a7d0f7fdf1f9fcbef3fffd">[email&#160;protected]</a></p>
</div>
</div> </div>
</div>
</div> </div>
</div>
</div>
</div>
<div class="footer--row footer-bottom layout-full-contained" id="cb-row--footer-bottom" data-row-id="bottom" data-show-on="desktop">
<div class="footer--row-inner footer-bottom-inner footer-content-wrap">
<div class="container">
<div class="hfg-grid nv-footer-content hfg-grid-bottom row--wrapper row " data-section="hfg_footer_layout_bottom">
<div class="builder-item hfg-item-last hfg-item-first col-12 mobile-center tablet-center desktop-center hfg-item-v-middle"><div class="item--inner builder-item--footer_copyright" data-section="footer_copyright" data-item-id="footer_copyright">
<div class="component-wrap">
<a style="color: white">© </a><a href="https://clay-atlas.com">clay-atlas.com</a> <a style="color: white">Copyright 2021 | </a><a href="https://themeisle.com/themes/neve/" rel="nofollow">Neve</a></div>
</div>
</div> </div>
</div>
</div>
</div>
</div>
</footer>
</div>
<div style="display:none">
<div class="grofile-hash-map-227a7281ab1b5f9d5fd74196600801a5">
</div>
<div class="grofile-hash-map-fb7c6baee50bb79acc3afb91e8e5a545">
</div>
</div>
<script data-cfasync="false" src="/cdn-cgi/scripts/5c5dd728/cloudflare-static/email-decode.min.js"></script><script type="text/javascript">
		window.WPCOM_sharing_counts = {"https:\/\/clay-atlas.com\/blog\/2019\/08\/27\/pyqt5-%e5%9f%ba%e6%9c%ac%e6%95%99%e5%ad%b8-2-qlabel-qlineedit-qpushbutton\/":422};
	</script>
<link rel='stylesheet' id='jetpack-block-instagram-gallery-css' href='https://c0.wp.com/p/jetpack/10.1/_inc/blocks/instagram-gallery/view.min.css' type='text/css' media='all' />
<script type='text/javascript' src='https://c0.wp.com/p/jetpack/10.1/_inc/build/photon/photon.min.js' id='jetpack-photon-js'></script>
<script type='text/javascript' src='https://secure.gravatar.com/js/gprofiles.js?ver=202136' id='grofiles-cards-js'></script>
<script type='text/javascript' id='wpgroho-js-extra'>
/* <![CDATA[ */
var WPGroHo = {"my_hash":""};
/* ]]> */
</script>
<script type='text/javascript' src='https://c0.wp.com/p/jetpack/10.1/modules/wpgroho.js' id='wpgroho-js'></script>
<script type='text/javascript' id='neve-script-js-extra'>
/* <![CDATA[ */
var NeveProperties = {"ajaxurl":"https:\/\/clay-atlas.com\/wp-admin\/admin-ajax.php","nonce":"4e82d195a4","isRTL":"","isCustomize":""};
/* ]]> */
</script>
<script type='text/javascript' src='https://clay-atlas.com/wp-content/themes/neve/assets/js/build/modern/frontend.js?ver=3.0.3' id='neve-script-js' async></script>
<script type='text/javascript' src='https://c0.wp.com/c/5.8.1/wp-includes/js/comment-reply.min.js' id='comment-reply-js'></script>
<script type='text/javascript' src='https://clay-atlas.com/wp-content/plugins/jetpack/vendor/automattic/jetpack-lazy-images/src/../dist/intersection-observer.js?ver=1.1.3' id='jetpack-lazy-images-polyfill-intersectionobserver-js'></script>
<script type='text/javascript' id='jetpack-lazy-images-js-extra'>
/* <![CDATA[ */
var jetpackLazyImagesL10n = {"loading_warning":"Images are still loading. Please cancel your print and try again."};
/* ]]> */
</script>
<script type='text/javascript' src='https://clay-atlas.com/wp-content/plugins/jetpack/vendor/automattic/jetpack-lazy-images/src/../dist/lazy-images.js?ver=1.1.3' id='jetpack-lazy-images-js'></script>
<script type='text/javascript' src='https://clay-atlas.com/wp-content/plugins/wp-featherlight/js/wpFeatherlight.pkgd.min.js?ver=1.3.4' id='wp-featherlight-js'></script>
<script type='text/javascript' src='https://c0.wp.com/c/5.8.1/wp-includes/js/wp-embed.min.js' id='wp-embed-js'></script>
<script defer type='text/javascript' src='https://clay-atlas.com/wp-content/plugins/akismet/_inc/form.js?ver=4.1.12' id='akismet-form-js'></script>
<script type='text/javascript' src='https://c0.wp.com/c/5.8.1/wp-includes/js/dist/vendor/regenerator-runtime.min.js' id='regenerator-runtime-js'></script>
<script type='text/javascript' src='https://c0.wp.com/c/5.8.1/wp-includes/js/dist/vendor/wp-polyfill.min.js' id='wp-polyfill-js'></script>
<script type='text/javascript' id='jetpack-block-instagram-gallery-js-extra'>
/* <![CDATA[ */
var Jetpack_Block_Assets_Base_Url = {"url":"https:\/\/clay-atlas.com\/wp-content\/plugins\/jetpack\/_inc\/blocks\/"};
/* ]]> */
</script>
<script type='text/javascript' src='https://c0.wp.com/p/jetpack/10.1/_inc/blocks/instagram-gallery/view.min.js' id='jetpack-block-instagram-gallery-js'></script>
<script type='text/javascript' id='sharing-js-js-extra'>
/* <![CDATA[ */
var sharing_js_options = {"lang":"en","counts":"1","is_stats_active":"1"};
/* ]]> */
</script>
<script type='text/javascript' src='https://c0.wp.com/p/jetpack/10.1/_inc/build/sharedaddy/sharing.min.js' id='sharing-js-js'></script>
<script type='text/javascript' id='sharing-js-js-after'>
var windowOpen;
			( function () {
				function matches( el, sel ) {
					return !! (
						el.matches && el.matches( sel ) ||
						el.msMatchesSelector && el.msMatchesSelector( sel )
					);
				}

				document.body.addEventListener( 'click', function ( event ) {
					if ( ! event.target ) {
						return;
					}

					var el;
					if ( matches( event.target, 'a.share-twitter' ) ) {
						el = event.target;
					} else if ( event.target.parentNode && matches( event.target.parentNode, 'a.share-twitter' ) ) {
						el = event.target.parentNode;
					}

					if ( el ) {
						event.preventDefault();

						// If there's another sharing window open, close it.
						if ( typeof windowOpen !== 'undefined' ) {
							windowOpen.close();
						}
						windowOpen = window.open( el.getAttribute( 'href' ), 'wpcomtwitter', 'menubar=1,resizable=1,width=600,height=350' );
						return false;
					}
				} );
			} )();
var windowOpen;
			( function () {
				function matches( el, sel ) {
					return !! (
						el.matches && el.matches( sel ) ||
						el.msMatchesSelector && el.msMatchesSelector( sel )
					);
				}

				document.body.addEventListener( 'click', function ( event ) {
					if ( ! event.target ) {
						return;
					}

					var el;
					if ( matches( event.target, 'a.share-facebook' ) ) {
						el = event.target;
					} else if ( event.target.parentNode && matches( event.target.parentNode, 'a.share-facebook' ) ) {
						el = event.target.parentNode;
					}

					if ( el ) {
						event.preventDefault();

						// If there's another sharing window open, close it.
						if ( typeof windowOpen !== 'undefined' ) {
							windowOpen.close();
						}
						windowOpen = window.open( el.getAttribute( 'href' ), 'wpcomfacebook', 'menubar=1,resizable=1,width=600,height=400' );
						return false;
					}
				} );
			} )();
var windowOpen;
			( function () {
				function matches( el, sel ) {
					return !! (
						el.matches && el.matches( sel ) ||
						el.msMatchesSelector && el.msMatchesSelector( sel )
					);
				}

				document.body.addEventListener( 'click', function ( event ) {
					if ( ! event.target ) {
						return;
					}

					var el;
					if ( matches( event.target, 'a.share-linkedin' ) ) {
						el = event.target;
					} else if ( event.target.parentNode && matches( event.target.parentNode, 'a.share-linkedin' ) ) {
						el = event.target.parentNode;
					}

					if ( el ) {
						event.preventDefault();

						// If there's another sharing window open, close it.
						if ( typeof windowOpen !== 'undefined' ) {
							windowOpen.close();
						}
						windowOpen = window.open( el.getAttribute( 'href' ), 'wpcomlinkedin', 'menubar=1,resizable=1,width=580,height=450' );
						return false;
					}
				} );
			} )();
</script>
<!--[if IE]>
		<script type="text/javascript">
			if ( 0 === window.location.hash.indexOf( '#comment-' ) ) {
				// window.location.reload() doesn't respect the Hash in IE
				window.location.hash = window.location.hash;
			}
		</script>
		<![endif]-->
<script type="text/javascript">
			(function () {
				var comm_par_el = document.getElementById( 'comment_parent' ),
					comm_par = ( comm_par_el && comm_par_el.value ) ? comm_par_el.value : '',
					frame = document.getElementById( 'jetpack_remote_comment' ),
					tellFrameNewParent;

				tellFrameNewParent = function () {
					if ( comm_par ) {
						frame.src = "https://jetpack.wordpress.com/jetpack-comment/?blogid=164929906&postid=422&comment_registration=0&require_name_email=0&stc_enabled=0&stb_enabled=0&show_avatars=1&avatar_default=retro&greeting=Leave+a+Reply&greeting_reply=%E5%B0%8D+%25s+%E7%99%BC%E8%A1%A8%E8%BF%B4%E9%9F%BF&color_scheme=light&lang=zh_TW&jetpack_version=10.1&show_cookie_consent=10&has_cookie_consent=0&token_key=%3Bnormal%3B&sig=6c476fb6af05da089736e61af088d49fd11c224a#parent=https%3A%2F%2Fclay-atlas.com%2Fblog%2F2019%2F08%2F27%2Fpyqt5-%25e5%259f%25ba%25e6%259c%25ac%25e6%2595%2599%25e5%25ad%25b8-2-qlabel-qlineedit-qpushbutton%2F" + '&replytocom=' + parseInt( comm_par, 10 ).toString();
					} else {
						frame.src = "https://jetpack.wordpress.com/jetpack-comment/?blogid=164929906&postid=422&comment_registration=0&require_name_email=0&stc_enabled=0&stb_enabled=0&show_avatars=1&avatar_default=retro&greeting=Leave+a+Reply&greeting_reply=%E5%B0%8D+%25s+%E7%99%BC%E8%A1%A8%E8%BF%B4%E9%9F%BF&color_scheme=light&lang=zh_TW&jetpack_version=10.1&show_cookie_consent=10&has_cookie_consent=0&token_key=%3Bnormal%3B&sig=6c476fb6af05da089736e61af088d49fd11c224a#parent=https%3A%2F%2Fclay-atlas.com%2Fblog%2F2019%2F08%2F27%2Fpyqt5-%25e5%259f%25ba%25e6%259c%25ac%25e6%2595%2599%25e5%25ad%25b8-2-qlabel-qlineedit-qpushbutton%2F";
					}
				};

				
				if ( 'undefined' !== typeof addComment ) {
					addComment._Jetpack_moveForm = addComment.moveForm;

					addComment.moveForm = function ( commId, parentId, respondId, postId ) {
						var returnValue = addComment._Jetpack_moveForm( commId, parentId, respondId, postId ),
							cancelClick, cancel;

						if ( false === returnValue ) {
							cancel = document.getElementById( 'cancel-comment-reply-link' );
							cancelClick = cancel.onclick;
							cancel.onclick = function () {
								var cancelReturn = cancelClick.call( this );
								if ( false !== cancelReturn ) {
									return cancelReturn;
								}

								if ( ! comm_par ) {
									return cancelReturn;
								}

								comm_par = 0;

								tellFrameNewParent();

								return cancelReturn;
							};
						}

						if ( comm_par == parentId ) {
							return returnValue;
						}

						comm_par = parentId;

						tellFrameNewParent();

						return returnValue;
					};
				}

				
				// Do the post message bit after the dom has loaded.
				document.addEventListener( 'DOMContentLoaded', function () {
					var iframe_url = "https:\/\/jetpack.wordpress.com";
					if ( window.postMessage ) {
						if ( document.addEventListener ) {
							window.addEventListener( 'message', function ( event ) {
								var origin = event.origin.replace( /^http:\/\//i, 'https://' );
								if ( iframe_url.replace( /^http:\/\//i, 'https://' ) !== origin ) {
									return;
								}
								frame.style.height = event.data + 'px';
							});
						} else if ( document.attachEvent ) {
							window.attachEvent( 'message', function ( event ) {
								var origin = event.origin.replace( /^http:\/\//i, 'https://' );
								if ( iframe_url.replace( /^http:\/\//i, 'https://' ) !== origin ) {
									return;
								}
								frame.style.height = event.data + 'px';
							});
						}
					}
				})

			})();
		</script>
<script src='https://stats.wp.com/e-202136.js' defer></script>
<script>
	_stq = window._stq || [];
	_stq.push([ 'view', {v:'ext',j:'1:10.1',blog:'164929906',post:'422',tz:'0',srv:'clay-atlas.com'} ]);
	_stq.push([ 'clickTrackerInit', '164929906', '422' ]);
</script>
</body>
</html>


'''

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.label1.setText('Hello World!')
        self.ui.textBrowser.setHtml(data)
        self.ui.textBrowser.moveCursor(QtGui.QTextCursor.End)
        self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.updateContent)
        self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).clicked.connect(self.exitApp)
    
    def updateContent(self):
        self.ui.textBrowser.setHtml('Run...')

    def exitApp(self):
        sys.exit(0) 


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

