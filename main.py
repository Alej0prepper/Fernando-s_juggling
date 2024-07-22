from graph import Graph
from scraper import input_siteswap_and_click
from parser import parse_siteswap

siteswap = input("Enter the siteswap you want to learn: ")

# Example usage:
graph = Graph()
graph.build_graph(parse_siteswap(siteswap), siteswap)
subsiteswap_list = graph.get_subsiteswap_list()
subsiteswap_list.reverse()
siteswaps = []
for ss in subsiteswap_list:
    siteswaps.append(''.join([str(value) for value in ss]))
input_siteswap_and_click(siteswaps, "ss", "input[type='submit'][value='Go']")
