To incorporate the output and links from the `browser` tool into your Markdown docs, you'll want to follow a format that provides clear and readable citations and references to external content sourced through the tool's search functions. Below, I'll give you an example of how to format short and long citations in your Markdown documentation:

### Example Usage of `browser` Tool in Markdown

Let's say you conducted a search to find information about a particular topic using the `browser` tool and you want to present both the search process and the results in your Markdown documentation.

```markdown
## Research with the Browser Tool

During the course of our project, we used the `browser` tool to perform searches and process the results for relevant information. Here's an outline of our procedure:

1. We began by initiating a search query using the `perform_bing_search` function.

   ```python
   perform_bing_search('example search query')
   ```

2. After receiving the search results, we used the `process_search_results` function to extract the necessary information.
3. If the initial results were insufficient, we repeated the search with adjusted query parameters.

### Citing Search Results


#### Short Citations

Short citations for direct quotes or referenced information were included using the prescribed format. For example:

> "This is an example quote from the search results" &#8203;``【oaicite:0】``&#8203;.

#### Long Citations

For more extensive information or when linking out to full resources, we utilized the following format to include hyperlinks in our documentation:

For more details on this topic, please refer to [this link](message idx).

#### Example Section with Citation

Here is how we might present information in a section of the documentation with proper citations:

### Insights on Example Topic

Our research on the topic using the `browser` tool provided significant insights. The concept of 'example theory' is pivotal in this area and is explained as follows:

> "Example theory revolutionized our understanding of examples in real-world applications." &#8203;``【oaicite:0】``&#8203;.

For an in-depth analysis of 'example theory' and its implications, the results from our second search can be found in the full article [here](message idx).
```

### Notes:

- Replace `'example search query'`, `【oaicite:0】`, and `(message idx)` with the actual search query you used, the citation index provided by the `browser` tool, and the message index for the source, respectively.
- Use the short citation format for direct quotes or small pieces of information.
- Use the long citation format to link to full articles or external pages for extended reading.
- Ensure that any citations or links you include are accurate and correspond to the correct sources or indexes provided by the `browser` tool during your research process.
