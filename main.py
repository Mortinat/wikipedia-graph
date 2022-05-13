import wikipediaapi
import networkx as nx

G = nx.Graph()


def add_nodes(page):
    G.add_node(page.title)
    links = page.links
    for title in sorted(links.keys()):
        if not (
            title.startswith("Category:")
            or title.startswith("File:")
            or title.startswith("Template:")
            or title.startswith("User:")
            or title.startswith("Wikipedia:")
            or title.startswith("Help:")
            or title.startswith("Template talk:")
            or title.startswith("Module:")
        ):
            G.add_node(title)
            G.add_edge(page.title, title)


wiki_wiki = wikipediaapi.Wikipedia("en")
page = wiki_wiki.page("Tubize")
add_nodes(page)
links = page.links
for title in sorted(links.keys()):
    if not (
        title.startswith("Category:")
        or title.startswith("File:")
        or title.startswith("Template:")
        or title.startswith("User:")
        or title.startswith("Wikipedia:")
        or title.startswith("Help:")
        or title.startswith("Template talk:")
        or title.startswith("Module:")
    ):
        page = wiki_wiki.page(title)
        add_nodes(page)
        links_2 = page.links
        for title in sorted(links_2.keys()):
            if not (
                title.startswith("Category:")
                or title.startswith("File:")
                or title.startswith("Template:")
                or title.startswith("User:")
                or title.startswith("Wikipedia:")
                or title.startswith("Help:")
                or title.startswith("Template talk:")
                or title.startswith("Module:")
            ):
                page = wiki_wiki.page(title)
                add_nodes(page)

nx.write_gexf(G, "tubize.gexf")
