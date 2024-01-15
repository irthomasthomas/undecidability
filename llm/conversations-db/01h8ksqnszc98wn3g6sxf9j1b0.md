**Prompt:**
title:	Search conversation topics and continue
state:	OPEN
author:	irthomasthomas
labels:	
comments:	1
assignees:	
projects:	
milestone:	
number:	4
--
I want to quickly search my conversation history by topic and select conversations to continue.

Create vector embeddings of conversations.
Search topics
Continue conversations

-i interactive mode with Terminal menu to select conversations
 Which tools mentioned in the linked article might be relevant to the issue thread below? Article: "\n\n\n\n29th April 2023\n\nI shipped openai-to-sqlite 0.3 yesterday with a fun new feature: you can now use the command-line tool to enrich data in a SQLite database by running values through an OpenAI model and saving the results, all in a single SQL query.\nThe idea for this came out of a conversation in a Datasette Office Hours session. I was asked if there was a way to do sentiment analysis using Datasette. There isn’t, yet—and the feature I’ve been planning that would enable that (which I’m calling “enrichments”) is still a fair way out.\nBut it got me to thinking... what’s the simplest possible way to run sentiment analysis on a column of data in a SQLite database using the tools I’ve already built?\nI ended up adding a small new feature to my openai-to-sqlite tool: the ability to call the OpenAI API (currently just the ChatGPT / gpt-3.5-turbo model) with a SQL query, plus a new chatgpt(prompt) SQL function for executing prompts.\nThis means you can do sentiment analysis something like this:\nopenai-to-sqlite query database.db \"\n  update messages set sentiment = chatgpt(\n    'Sentiment analysis for this message: ' || message ||\n    ' - ONLY return a lowercase string from: positive, negative, neutral, unknown'\n  )\n  where sentiment not in ('positive', 'negative', 'neutral', 'unknown')\n    or sentiment is null\n\"\nRunning this command causes the sentiment column on the messages table to be populated with one of the following values: positive, negative, neutral or unknown.\nIt also prints out a cost estimate at the end. To run against 400 rows of data (each the length of a group chat message, so pretty short) cost me 20,000 tokens, which was about 4 cents. gpt-3.5-turbo is cheap.\nThe command uses an OpenAI API key from the OPENAI_API_KEY environment variable, or you can pass it in using the --token option to the command.\nThe tool also displays a progress bar while it’s running, which looks like this:\n\nSentiment analysis with ChatGPT\nHere’s the SQL query that I ran, with extra inline comments:\nupdate messages\n  -- we're updating rows in the messages table\n  set sentiment = chatgpt(\n    -- Construct the ChatGPT prompt\n    'Sentiment analysis for this message: ' ||\n    message ||\n    ' - ONLY return a lowercase string from:' ||\n    'positive, negative, neutral, unknown'\n)\nwhere\n  -- Don't update rows that already have a sentiment\n  sentiment not in (\n    'positive', 'negative', 'neutral', 'unknown'\n  ) or sentiment is null\nAnd here’s the prompt I’m using:\n\nSentiment analysis for this message: {message}—ONLY return a lowercase string from: positive, negative, neutral, unknown\n\nAs usual with prompt engineering, you end up having to practically BEG the model to stick to the rules. My first version of this prompt produced all kinds of unexpected output—this version mostly does what I want, but still ends up spitting out the occasional Positive. or Sentiment: Negative result despite my pleas for just those four strings.\nI’m sure there are better prompts for this. I’d love to see what they are!\n(The most likely improvement would be to include some examples in the prompt, to help nail down the expected outputs—an example of few-shot training.)\nRunning prompts with a SELECT\nI have other tools for running prompts from the command-line, but if you want to use this to execute a prompt directly without writing to a database you can execute against the :memory: SQLite in-memory database like this:\nopenai-to-sqlite query :memory: \\\n  \"select chatgpt('Surprising names for a horse')\"\n\n\nHow the progress bar works\nWhen I first implemented this, it didn’t have a progress bar.\nThis turned out to be a pretty big problem!\nA SQL update that affects 400 rows, each one involving an API call to OpenAI, can take a few minutes to run.\nDuring that time, there is no feedback at all to show you that it’s working, or indicate how far it’s gone.\nThe UPDATE statement itself runs inside a transaction, so you can’t even peak in the database to see how it’s going—all 400 rows will appear once, at the end of the query.\nI really wanted a progress bar. But how could I implement that? I need it to update as the query progresses, and I also need to know how many API calls it’s going to make in advance in order to correctly display it.\nI figured out a neat way of doing this.\nThe trick is to run the SQL query twice. The first time, implement a dummy chatgpt() function that counts how many times it has been called but doesn’t make an API call.\nThen, at the end of that query... rollback the transaction! This means that the dummy chatgpt() function will have been called the correct number of times, but the database will be left unchanged.\nNow register the “real” chatgpt() function and run the query a second time.\nThat second chatgpt() Python function can increment the counter used by the progress bar each time it’s called.\nThe result is a progress bar that knows how many API calls are going to be made and updates as the query progresses.\nHere’s the code that makes that happen.\nIs this a good way of doing things?\nEven though I managed to get the progress bar working, there are still some big limitations in using a SQL query to do this.\nThe first is that any query which triggers external API calls via a custom SQL function is inherently time-consuming. This means running a really long transaction, and since SQLite only accepts a single write at a time this means locking the database for writes for a very long time.\nThat’s OK for a command-line script like this when you’re the only user of the database, but it’s not a good idea for databases that are serving other queries—as I frequently do with SQLite and Datasette.\nA much bigger problem though is what happens when something goes wrong. An update ... set col1 = chatgpt(...) query executes in a single transaction. If you’re running it against 400 rows and something causes an error at row 399, the transaction will rollback and you’ll lose all of the work that DID succeed!\nAs such, while this is a fun tool for ad-hoc experiments with OpenAI data enrichment, I don’t think it’s a good long-term solution. A better mechanism would enable each individual API call to be written to storage such that problems in later calls don’t discard data collected earlier on.\n\n\n\n\n"

**Response:**
The tools mentioned in the article that might be relevant to the issue thread are:

1. openai-to-sqlite: This tool allows you to enrich data in a SQLite database by running values through an OpenAI model and saving the results, all in a single SQL query. It can be used to perform sentiment analysis on a column of data in a SQLite database by calling the OpenAI API.

2. ChatGPT / gpt-3.5-turbo model: This is the OpenAI model used for sentiment analysis in the example provided. It can be accessed using the openai-to-sqlite tool and can return sentiment values such as positive, negative, neutral, or unknown.

3. chatgpt() SQL function: This is a custom SQL function added to the openai-to-sqlite tool that allows you to execute prompts for the ChatGPT model directly within SQL queries. It can be used to construct prompts for sentiment analysis and update the sentiment column in the messages table.

4. Progress bar implementation: The author describes a custom implementation of a progress bar for long-running SQL queries that involve API calls. This allows the user to track the progress of the query and know how many API calls are going to be made.

It's important to note that these tools are specific to enriching data in a SQLite database using the OpenAI models and might not be directly related to searching conversation history or continuing conversations. However, they can be adapted and extended to suit the requirements of searching conversation topics and continuing conversations.

<details><summary>Metadata</summary>

- Duration: 13214 ms
- Datetime: 2023-08-24T12:53:46.016152
- Model: gpt-3.5-turbo-0613

</details>

**Options:**
```json
{}
```

