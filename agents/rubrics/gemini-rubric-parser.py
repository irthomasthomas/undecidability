import xml.etree.ElementTree as ET

tree = ET.parse("conversation_output.xml")
root = tree.getroot()

for response in root.findall("response"):
    text = response.find("text").text
    relevance = response.find("relevance").text
    # ... extract other criteria ...
    print(f"Response: {text}\nRelevance: {relevance}\n")

overall = root.find("overall")
goal_completion = overall.find("goal_completion").text
# ... extract other criteria ...
print(f"\nOverall Goal Completion: {goal_completion}")
