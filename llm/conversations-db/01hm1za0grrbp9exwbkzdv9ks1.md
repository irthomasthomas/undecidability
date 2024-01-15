**Prompt:**
diff --git a/agents/vision/GPT4-vision-toolkit.py b/agents/vision/GPT4-vision-toolkit.py
index 04be120..5d7ffb0 100644
--- a/agents/vision/GPT4-vision-toolkit.py
+++ b/agents/vision/GPT4-vision-toolkit.py
@@ -7,14 +7,19 @@ import base64
 from PIL import Image
 from openai import OpenAI
 
+# Define some global variables so I can use them in the functions below
+STREAM = False
 devtty = "/dev/tty"
 if os.path.exists(devtty):
-    logging.basicConfig(filename=devtty, level=logging.DEBUG)
+    logging.basicConfig(filename=devtty, level=logging.ERROR)
 
 # Client instantiation, moved from individual functions to reduce duplication
 client = OpenAI()
 
 def openai_completion(prompt, system_prompt, max_tokens=2000, model='gpt-4-vision-preview', base64_image=None):
+    """Generate a completion from OpenAI's API."""
+    
+    #Todo: refactor to use streaming completion.
     response = client.chat.completions.create(
         model=model,
         messages=[
@@ -35,9 +40,19 @@ def openai_completion(prompt, system_prompt, max_tokens=2000, model='gpt-4-visio
             },
         ],
         max_tokens=max_tokens,
+        stream=STREAM,
     )
-    result = response.choices[0].message.content
-    return result
+    if not STREAM:
+        result = response.choices[0].message.content
+        return result
+    else:
+        for chunk in response:
+            if len(chunk.choices) > 0:
+                delta = chunk.choices[0].delta
+                if delta.role:
+                    print(delta.role + ": ", end="", flush=True)
+                if delta.content:
+                    print(delta.content, end="", flush=True)
 
 def convert_image_to_base64(image):
     buffered = io.BytesIO()
@@ -63,11 +78,16 @@ def generate_output(image, prompt, output_type):
 def cli():
     pass
 
+# add a streaming option.
 @cli.command()
 @click.argument('image_path', type=click.Path(exists=True), required=False)
 @click.argument('prompt', required=False)
 @click.option('--output', type=click.Choice(['text', 'json', 'md'], case_sensitive=False), default='describe')
-def describe(image_path, prompt, output):
+@click.option('--stream', is_flag=True, default=False) # use this like: cat image.png | python3 GPT4-vision-toolkit.py --stream
+def describe(image_path, prompt, output, stream):
+    """Describe an image."""
+    global STREAM # I'm sure there's a better way to do this, but I'm not sure what it is. < copilot generated this comment for me.
+    STREAM = stream
     if not image_path:
         if sys.stdin.isatty():
             raise click.UsageError("No image provided. You must provide an image path or pipe in an image.")
diff --git a/agents/writer/guide-to-writing-documentation.md b/agents/writer/guide-to-writing-documentation.md
new file mode 100644
index 0000000..7c3d6c4
--- /dev/null
+++ b/agents/writer/guide-to-writing-documentation.md
@@ -0,0 +1,65 @@
+# What makes documentation good
+
+Documentation puts useful information inside other people’s heads. Follow these tips to write better documentation.
+
+### Make docs easy to skim
+
+Few readers read linearly from top to bottom. They’ll jump around, trying to assess which bit solves their problem, if any. To reduce their search time and increase their odds of success, make docs easy to skim.
+
+**Split content into sections with titles.** Section titles act as signposts, telling readers whether to focus in or move on.
+
+**Prefer titles with informative sentences over abstract nouns.** For example, if you use a title like “Results”, a reader will need to hop into the following text to learn what the results actually are. In contrast, if you use the title “Streaming reduced time to first token by 50%”, it gives the reader the information immediately, without the burden of an extra hop.
+
+**Include a table of contents.** Tables of contents help readers find information faster, akin to how hash maps have faster lookups than linked lists. Tables of contents also have a second, oft overlooked benefit: they give readers clues about the doc, which helps them understand if it’s worth reading.
+
+**Keep paragraphs short.** Shorter paragraphs are easier to skim. If you have an essential point, consider putting it in its own one-sentence paragraph to reduce the odds it’s missed. Long paragraphs can bury information.
+
+**Begin paragraphs and sections with short topic sentences that give a standalone preview.** When people skim, they look disproportionately at the first word, first line, and first sentence of a section. Write these sentences in a way that don’t depend on prior text. For example, consider the first sentence “Building on top of this, let’s now talk about a faster way.” This sentence will be meaningless to someone who hasn’t read the prior paragraph. Instead, write it in a way that can understood standalone: e.g., “Vector databases can speed up embeddings search.”
+
+**Put topic words at the beginning of topic sentences.** Readers skim most efficiently when they only need to read a word or two to know what a paragraph is about. Therefore, when writing topic sentences, prefer putting the topic at the beginning of the sentence rather than the end. For example, imagine you’re writing a paragraph on vector databases in the middle of a long article on embeddings search. Instead of writing “Embeddings search can be sped up by vector databases” prefer “Vector databases speed up embeddings search.” The second sentence is better for skimming, because it puts the paragraph topic at the beginning of the paragraph.
+
+**Put the takeaways up front.** Put the most important information at the tops of documents and sections. Don’t write a Socratic big build up. Don’t introduce your procedure before your results.
+
+**Use bullets and tables.** Bulleted lists and tables make docs easier to skim. Use them frequently.
+
+**Bold important text.** Don’t be afraid to bold important text to help readers find it.
+
+### Write well
+
+Badly written text is taxing to read. Minimize the tax on readers by writing well.
+
+**Keep sentences simple.** Split long sentences into two. Cut adverbs. Cut unnecessary words and phrases. Use the imperative mood, if applicable. Do what writing books tell you.
+
+**Write sentences that can be parsed unambiguously.** For example, consider the sentence “Title sections with sentences.” When a reader reads the word “Title”, their brain doesn’t yet know whether “Title” is going to be a noun or verb or adjective. It takes a bit of brainpower to keep track as they parse the rest of the sentence, and can cause a hitch if their brain mispredicted the meaning. Prefer sentences that can be parsed more easily (e.g., “Write section titles as sentences”) even if longer. Similarly, avoid noun phrases like “Bicycle clearance exercise notice” which can take extra effort to parse.
+
+**Avoid left-branching sentences.** Linguistic trees show how words relate to each other in sentences. Left-branching trees require readers to hold more things in memory than right-branching sentences, akin to breadth-first search vs depth-first search. An example of a left-branching sentence is “You need flour, eggs, milk, butter and a dash of salt to make pancakes.” In this sentence you don’t find out what ‘you need’ connects to until you reach the end of the sentence. An easier-to-read right-branching version is “To make pancakes, you need flour, eggs, milk, butter, and a dash of salt.” Watch out for sentences in which the reader must hold onto a word for a while, and see if you can rephrase them.
+
+**Avoid demonstrative pronouns (e.g., “this”), especially across sentences.** For example, instead of saying “Building on our discussion of the previous topic, now let’s discuss function calling” try “Building on message formatting, now let’s discuss function calling.” The second sentence is easier to understand because it doesn’t burden the reader with recalling the previous topic. Look for opportunities to cut demonstrative pronouns altogether: e.g., “Now let’s discuss function calling.”
+
+**Be consistent.** Human brains are amazing pattern matchers. Inconsistencies will annoy or distract readers. If we use Title Case everywhere, use Title Case. If we use terminal commas everywhere, use terminal commas. If all of the Cookbook notebooks are named with underscores and sentence case, use underscores and sentence case. Don’t do anything that will cause a reader to go ‘huh, that’s weird.’ Help them focus on the content, not its inconsistencies.
+
+**Don’t tell readers what they think or what to do.** Avoid sentences like “Now you probably want to understand how to call a function” or “Next, you’ll need to learn to call a function.” Both examples presume a reader’s state of mind, which may annoy them or burn our credibility. Use phrases that avoid presuming the reader’s state. E.g., “To call a function, …”
+
+### Be broadly helpful
+
+People come to documentation with varying levels of knowledge, language proficiency, and patience. Even if we target experienced developers, we should try to write docs helpful to everyone.
+
+**Write simply.** Explain things more simply than you think you need to. Many readers might not speak English as a first language. Many readers might be really confused about technical terminology and have little excess brainpower to spend on parsing English sentences. Write simply. (But don’t oversimplify.)
+
+**Avoid abbreviations.** Write things out. The cost to experts is low and the benefit to beginners is high. Instead of IF, write instruction following. Instead of RAG, write retrieval-augmented generation (or my preferred term: the search-ask procedure).
+
+**Offer solutions to potential problems.** Even if 95% of our readers know how to install a Python package or save environment variables, it can still be worth proactively explaining it. Including explanations is not costly to experts—they can skim right past them. But excluding explanations is costly to beginners—they might get stuck or even abandon us. Remember that even an expert JavaScript engineer or C++ engineer might be a beginner at Python. Err on explaining too much, rather than too little.
+
+**Prefer terminology that is specific and accurate.** Jargon is bad. Optimize the docs for people new to the field, instead of ourselves. For example, instead of writing “prompt”, write “input.” Or instead of writing “context limit” write “max token limit.” The latter terms are more self-evident, and are probably better than the jargon developed in base model days.
+
+**Keep code examples general and exportable.** In code demonstrations, try to minimize dependencies. Don’t make users install extra libraries. Don’t make them have to refer back and forth between different pages or sections. Try to make examples simple and self-contained.
+
+**Prioritize topics by value.** Documentation that covers common problems—e.g., how to count tokens—is magnitudes more valuable than documentation that covers rare problems—e.g., how to optimize an emoji database. Prioritize accordingly.
+
+**Don’t teach bad habits.** If API keys should not be stored in code, never share an example that stores an API key in code.
+
+**Introduce topics with a broad opening.** For example, if explaining how to program a good recommender, consider opening by briefly mentioning that recommendations are widespread across the web, from YouTube videos to Amazon items to Wikipedia. Grounding a narrow topic with a broad opening can help people feel more secure before jumping into uncertain territory. And if the text is well-written, those who already know it may still enjoy it.
+
+### Break these rules when you have a good reason
+
+Ultimately, do what you think is best. Documentation is an exercise in empathy. Put yourself in the reader’s position, and do what you think will help them the most.
diff --git a/nyxt/auto-config.3.lisp b/nyxt/auto-config.3.lisp
index cd98a6b..1a068e3 100644
--- a/nyxt/auto-config.3.lisp
+++ b/nyxt/auto-config.3.lisp
@@ -1,6 +1,3 @@
-(defmethod customize-instance ((document-buffer document-buffer) &key)
-  (setf (slot-value document-buffer 'zoom-ratio-default) 1.1))
-
 (defmethod customize-instance ((buffer buffer) &key)
   (setf (slot-value buffer 'default-modes)
           '(nyxt/mode/certificate-exception:certificate-exception-mode
@@ -20,3 +17,4 @@
 
 (defmethod customize-instance ((browser browser) &key)
   (setf (slot-value browser 'remote-execution-p) t))
+
diff --git a/nyxt/config.lisp b/nyxt/config.lisp
index 0a17395..e6385fe 100644
--- a/nyxt/config.lisp
+++ b/nyxt/config.lisp
@@ -1,30 +1,22 @@
-(define-command-global pipe-selection ()
-    "Send selection to named pipe"
-  (let ((selection (ps-eval (ps:chain window (get-selection) (to-string)))))
-    (uiop:launch-program (list "sh" "-c" (concatenate 'string "echo " "'" selection "'" " > /tmp/nyxt_selection_pipe")))))
+(in-package #:nyxt-user)
 
+;;; Loading files from the same directory.
+(define-nyxt-user-system-and-load nyxt-user/basic-config
+  :components ("gh-selection-to-issue


**Response:**
Refactor OpenAI completion function to use streaming option

<details><summary>Metadata</summary>

- Duration: 735 ms
- Datetime: 2024-01-13T17:53:24.280193
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{"temperature": 0.6}
```

