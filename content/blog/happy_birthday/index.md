---
title: "Happy Birthday!"
date: 2024-05-22
tags: ["code", "celebration", "appreciation of tian"]
summary: "Read here for how to take over this website"
draft: true
---

### How website?
All the code for the site is on [this Github repo](https://github.com/EWol234/ewol234.github.io), which is also where I'm hosting it. You can copy this and put it on your own `username.github.io` repo to host, and it should just work (I think).

I used a static-site generator called [Pelican](https://docs.getpelican.com/en/4.9.1/index.html), the Github repo can be set up to run this whenever you push some changes so it automatically recreates your pages. You'll just need to tell it to use the custom build action that's already in the repo, you can see the docs for that [here](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow).

### How domain?
I got the domain from Squarespace, if you want to keep it you can make an account and I'll add you as an administrator so you can point to your repo, or you can get your own domain and point it to your repo yourself.

### How content?
Content-wise, you add posts by adding a new file to the `content/` directory, and pages like "About" go in the `content/pages/` directory. There are two settings files: `pelicanconf.py` and `publishconf.py`, usually you only need to change the first one, the second one imports everything from the first one and adds some stuff for the official published version.

Style-wise I added a theme in `themes/pelican-hyde` which I did some customization on, you would edit the templates or CSS files there to change the look. I had to hard-code the "Acting, Travel, Software Engineering" into that to get the icon in the middle lol.

The stuff in the sidebar can be configured in `pelicanconf.py`, you can extra links that aren't pages (like the "Home" link) via `MENUITEMS`, and you can add links to your socials via `SOCIAL`.

