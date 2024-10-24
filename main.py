import argparse
from graph import Graph

from parser import parse_siteswap

parser = argparse.ArgumentParser(description='Process siteswap.')
parser.add_argument('mode', nargs='?', default='visual', help='Mode to run the script: "visual" or "no-visual"')
args = parser.parse_args()

siteswap = input("Enter the siteswap you want to learn: ")

graph = Graph()
graph.build_graph(parse_siteswap(siteswap), siteswap)
subsiteswap_list = graph.get_subsiteswap_list()
subsiteswap_list.reverse()
siteswaps = []
for ss in subsiteswap_list:
    siteswaps.append(''.join([str(value) for value in ss]))
print(ss)

if args.mode != 'no-visual':
    from scraper import input_siteswap_and_click
    
if args.mode != 'no-visual':
    input_siteswap_and_click(siteswaps, "ss", "input[type='submit'][value='Go']")
