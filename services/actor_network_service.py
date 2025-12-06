from .data_loader import credits_data
from itertools import combinations
from collections import Counter
import json
import networkx as nx


def get_actor_network():
    actor_pairs = []

    for credit in credits_data:
        cast = credit.get("cast", "[]")
        cast = json.loads(cast)
        actors = [actor.get("name") for actor in cast[:100] if actor.get("name")]

        if len(actors) >= 2:
            pairs = combinations(sorted(actors), 2)
            actor_pairs.extend(pairs)

    pair_counts = Counter(actor_pairs)

    G = nx.Graph()

    for (actor1, actor2), weight in pair_counts.items():
        G.add_edge(actor1, actor2, weight=weight)

    top_pairs = sorted(pair_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    return {
        "nodes": G.number_of_nodes(),
        "edges": G.number_of_edges(),
        "density": nx.density(G),
        "top_actor_pairs": [
            {
                "actor1": pair[0],
                "actor2": pair[1],
                "collaborations": count
            }
            for pair, count in top_pairs
        ],
        "top_central_actors": [
            {"actor": actor, "centrality": round(centrality, 4)}
            for actor, centrality in sorted(
                nx.degree_centrality(G).items(),
                key=lambda x: x[1],
                reverse=True
            )[:10]
        ]
    }
