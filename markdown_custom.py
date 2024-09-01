from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor
from markdown.inlinepatterns import LinkInlineProcessor, LINK_RE

import re
import xml.etree.ElementTree as etree


class TailwindLink(LinkInlineProcessor):
    # Modification of default handleMatch
    def handleMatch(self, m: re.Match[str], data: str) -> tuple[etree.Element | None, int | None, int | None]:
        """ Return an `a` [`Element`][xml.etree.ElementTree.Element] or `(None, None, None)`. """
        text, index, handled = self.getText(data, m.end(0))

        if not handled:
            return None, None, None

        href, title, index, handled = self.getLink(data, index)
        if not handled:
            return None, None, None

        el = etree.Element("a")
        el.text = text

        el.set("href", href)

        if title is not None:
            el.set("title", title)

        el.set("class", "text-yellow-800 hover:underline")

        return el, m.start(0), index


# Replacements will be applied in order
TAILWIND_REPLACEMENTS = {
    "p": {
        "tag": "p",
        "class": "pb-4",
    },
    "h1": {
        "tag": "p",
        "class": "font-bold text-slate-800 text-3xl py-6"
    },
    "h2": {
        "tag": "p",
        "class": "font-bold text-slate-800 text-2xl py-4"
    },
    "h3": {
        "tag": "p",
        "class": "font-bold text-slate-800 text-xl py-2"
    },
}


class TailwindCSS(Treeprocessor):
    def run(self, root):
        for target_tag, replacement in TAILWIND_REPLACEMENTS.items():
            elements = root.findall(f".//{target_tag}")
            for element in elements:
                element.tag = replacement["tag"]
                element.attrib["class"] = replacement["class"]


class TianExtension(Extension):
    def extendMarkdown(self, md):
        md.treeprocessors.register(TailwindCSS(md.parser), 'tailwind', 175)

        md.inlinePatterns.deregister('link')
        md.inlinePatterns.register(TailwindLink(LINK_RE, md), 'link', 160)


