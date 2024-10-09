import xml.etree.ElementTree as ET
import numpy as np


# Function to parse XML and generate web graph
def parse_xml(xml_data):
    """
    Parse XML and create a web graph.

    Args:
        xml_data (str): XML string containing web page information.

    Returns:
        dict: A dictionary representing the web graph (adjacency list).
        set: A set of URLs related to the topic of interest.
    """
    graph = {}
    topic_specific_pages = set()

    # Parse XML
    root = ET.fromstring(xml_data)

    # Iterate over each page element
    for page in root.findall('page'):
        url = page.find('url').text
        links = [link.text for link in page.findall('links/link')]
        topic = page.find('topic').text

        # Add links to the graph (adjacency list)
        graph[url] = links

        # Add the page to topic-specific set if it matches the desired topic
        if topic == "AI":  # You can change this to any specific topic
            topic_specific_pages.add(url)

    return graph, topic_specific_pages


# Function to compute topic-specific PageRank
def topic_specific_pagerank(graph, topic_pages, num_iterations=100, d=0.85):
    """
    Compute topic-specific PageRank.

    Args:
        graph (dict): Adjacency list representing the web graph.
        topic_pages (set): Set of topic-specific pages to bias the rank towards.
        num_iterations (int): Number of iterations to run the algorithm.
        d (float): Damping factor.

    Returns:
        dict: PageRank scores for each page.
    """
    # Initialize variables
    nodes = list(graph.keys())
    N = len(nodes)
    ranks = np.ones(N) / N  # Initialize ranks uniformly

    # Create link matrix
    link_matrix = np.zeros((N, N))
    for i, node in enumerate(nodes):
        if len(graph[node]) == 0:  # Handle dangling pages (no out-links)
            link_matrix[:, i] = 1 / N
        else:
            for target in graph[node]:
                if target in nodes:
                    j = nodes.index(target)
                    link_matrix[j, i] = 1 / len(graph[node])

    # Teleport vector for topic-specific bias (bias towards topic pages)
    teleport = np.array([1.0 if node in topic_pages else 0.0 for node in nodes])
    teleport = teleport / teleport.sum()  # Normalize teleport vector

    # Iteratively calculate topic-specific PageRank
    for _ in range(num_iterations):
        ranks = (1 - d) * teleport + d * link_matrix.dot(ranks)

    return {nodes[i]: ranks[i] for i in range(N)}


# Example XML Data
xml_data = """
<web>
    <page>
        <url>https://example.com/ai</url>
        <links>
            <link>https://example.com/machine-learning</link>
            <link>https://example.com/deep-learning</link>
        </links>
        <topic>AI</topic>
    </page>
    <page>
        <url>https://example.com/machine-learning</url>
        <links>
            <link>https://example.com/ai</link>
        </links>
        <topic>AI</topic>
    </page>
    <page>
        <url>https://example.com/deep-learning</url>
        <links>
            <link>https://example.com/ai</link>
        </links>
        <topic>AI</topic>
    </page>
    <page>
        <url>https://example.com/healthcare</url>
        <links>
            <link>https://example.com/ai</link>
        </links>
        <topic>Healthcare</topic>
    </page>
</web>
"""

# Main logic
if __name__ == "__main__":
    # Step 1: Parse XML and generate web graph
    web_graph, topic_specific_pages = parse_xml(xml_data)

    # Step 2: Compute topic-specific PageRank (biased towards AI-related pages)
    pageranks = topic_specific_pagerank(web_graph, topic_specific_pages, num_iterations=100, d=0.85)

    # Output the PageRank scores
    print("Topic-Specific PageRank Scores:")
    for page, rank in sorted(pageranks.items(), key=lambda item: -item[1]):
        print(f"{page}: {rank:.4f}")
