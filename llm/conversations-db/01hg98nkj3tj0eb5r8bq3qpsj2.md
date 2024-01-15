**Prompt:**


**Response:**
const express = require("express");
const bodyParser = require("body-parser");

const PORT = 3000;
const app = express();

app.use(bodyParser.json({ extended: false }));

app.use(bodyParser.urlencoded({ extended: true }));

app.use(express.static("View"));

require('./routes')(app);

app.get('/',function(req, res) {
    res.sendFile('/templates/index.html',{root: __dirname });
});

app.listen(PORT, function() {
    console.log("Server is running on http://localhost:" + PORT);
});

<details><summary>Metadata</summary>

- Duration: 1595 ms
- Datetime: 2023-11-27T20:48:54.279336
- Model: gpt-3.5-turbo-instruct

</details>

**Options:**
```json
{"temperature": 1.0}
```

