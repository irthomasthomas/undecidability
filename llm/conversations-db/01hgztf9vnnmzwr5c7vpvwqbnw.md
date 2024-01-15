**Prompt:**
(defun save-github-labels ()
  "Save the labels of the repository https://api.github.com/repos/irthomasthomas/undecidability/labels."
  (let* ((url "https://api.github.com/repos/irthomasthomas/undecidability/labels")
         (response (dex:get url)))
    (with-open-file (file "labels.txt" :direction :output)
      (format file "~a" response))))

This produces a file like:
[{"id":5935764687,"node_id":"LA_kwDOKNgf3c8AAAABYcyUzw","url":"https://api.github.com/repos/irthomasthomas/undecidability/labels/Agents","name":"Agents","color":"fef2c0","default":false,"description":"Autonomous AI agents using LLMs"},{"id":5976028723,"node_id":"LA_kwDOKNgf3c8AAAABZDL2Mw","url":"https://api.github.com/repos/irthomasthomas/undecidability/labels/Algorithms","name":"Algorithms","color":"bfd4f2","default":false,"description":"Sorting, Learning or Classifying. All algorithms go here."}]

Save the id, name and description to a list and make this available to other nyxt functions.

Notes on njson:
start parsing right away, be it from file:

(njson:decode #p"/path/to/njson/checkout/tests/test.json")
;; => #(1 3.8 T NIL :NULL "foo" #(1 2 3) #("bar" T :NULL 1000000)
;;      #<HASH-TABLE :TEST EQUAL :COUNT 1 {100EAB1383}>
;;      #<HASH-TABLE :TEST EQUAL :COUNT 3 {100EAB16D3}>)

or from string:

(njson:decode "[\"hello\", 5]")
;; => #("hello", 5)

or other specializeable types. Default methods support:

    pathnames,
    strings,
    streams.

 The types NJSON returns from its methods (and that your own methods extending NJSON should expect/return) are:

    Lisp real-s for JSON numbers.
    Lisp strings for JSON strings.
    :null for JSON null.
    t for true and nil for false.
    Vectors for JSON arrays.
    Hash-tables for JSON objects.

(defvar data (njson:decode "{\"key\": 5, \"second-key\": [1, 2, false]}"))
(njson:jget "key" data)
;; => 5, T

;; Index using sequence:
(njson:jget '("second-key" 1) data)
;; => 2, T

;; Index using JSON Pointer (as pathname):
(njson:jget #p"/second-key/0" data)
;; => 1, T

;; Modify the element in place:
(setf (njson:jget #p"/second-key/0" data) 3)
;; Another indexing syntax, for no particular reason:
(njson:jget #("second-key" 0) data)
;; => 3, T

(defvar data (njson:jget "key" (njson:decode "{\"key\": 5}")))
;; => 5, T
(njson:jget "key" (njson:jcopy data))
;; => 5, T

(njson:jkeys (njson:decode "{\"a\": 1, \"b\": 2}"))
;; ("a" "b")
(njson:jkeys (njson:decode "[\"a\", \"b\"]"))
;; (0 1)

(njson:ensure-array #(1 2 3))
;; #(1 2 3)
(njson:ensure-array 3)
;; #(3)
(njson:ensure-array (njson:decode "{\"a\": 3}"))
;; #(#<hash-table>)
(njson:ensure-array (njson:decode "{\"a\": 3}") :convert-objects t)
;; #(3)

(njson:ensure-object "key" #<hash-table>)
;; #<hash-table>
(njson:ensure-object "key" 3)
;; #<hash-table> with "key": 3
(njson:ensure-object "key" #(1 2 3))
;; #<hash-table> with "key": #(1 2 3)

(njson:jmatch
 parsed-api-data
 (("ok" :true "result" result)
  (values t result))
 (("ok" :false "error_code" _ "description" description)
  (values nil description))
 (t (error "Malformed data!")))


**Response:**
To save the `id`, `name`, and `description` of the GitHub labels to a list and make it available to other Nyxt functions, you can modify the `save-github-labels` function to use `njson:decode` to parse the JSON response and then extract the required fields. Here's how you can do it:

```lisp
(defvar *github-labels-list* nil) ; Global variable to store the labels list

(defun save-github-labels ()
  "Save the id, name, and description of the labels of the repository https://api.github.com/repos/irthomasthomas/undecidability/labels."
  (let* ((url "https://api.github.com/repos/irthomasthomas/undecidability/labels")
         (response (dex:get url)))
    (setf *github-labels-list* ; Update the global variable
          (mapcar (lambda (label)
                    (list (njson:jget "id" label)
                          (njson:jget "name" label)
                          (njson:jget "description" label)))
                  (njson:decode response))))) ; Parse the JSON response and extract fields

(defun get-github-labels-list ()
  "Return the list of GitHub labels."
  *github-labels-list*)
```

In this code, we have:

1. Defined a global variable `*github-labels-list*` to store the list of labels.
2. Modified the `save-github-labels` function to parse the JSON response using `njson:decode` and then extract the `id`, `name`, and `description` fields from each label using `njson:jget`.
3. Used `mapcar` to apply the extraction process to each label in the parsed JSON array and update the global variable with the resulting list.
4. Added a `get-github-labels-list` function that returns the list of labels stored in the global variable.

Now, other Nyxt functions can access the list of GitHub labels by calling `get-github-labels-list`. Remember to call `save-github-labels` first to populate the list before attempting to access it.

<details><summary>Metadata</summary>

- Duration: 41077 ms
- Datetime: 2023-12-06T15:02:40.127198
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.2}
```

**Prompt:**
Now write an example function that could use the labels

**Response:**
Certainly! Below is an example function that uses the labels list called `print-github-label-details`. This function iterates over each label that we earlier stored in the global variable `*github-labels-list*` and prints its `id`, `name`, and `description` to the standard output:

```lisp
(defun print-github-label-details ()
  "Print details of GitHub labels stored in *github-labels-list*."
  (unless *github-labels-list*
    (error "No data available. Please run save-github-labels first."))

  (format t "~&%-10s %-30s %-50s" "ID" "Name" "Description") ; Print table header
  (format t "~&------------------------------------------------------------------------------")
  
  (dolist (label *github-labels-list*)
    (destructuring-bind (id name description) label
      (format t "~&%-10d %-30s %-50s" id name description)))) ; Print each label details
```

To call this function and see the results, make sure you have first called `save-github-labels` to fetch and save the labels. Here’s how you would use it:

```lisp
(save-github-labels) ; Fetch and save the labels
(print-github-label-details) ; Print the details of the labels
```

This would result in an output similar to the following if there are any labels:

```
ID         Name                           Description                                           
------------------------------------------------------------------------------
5935764687 Agents                         Autonomous AI agents using LLMs                       
5976028723 Algorithms                     Sorting, Learning or Classifying. All algorithms go here.
```

This is a simple illustrative function. In a practical scenario, you might have functions that filter labels, update them, or sync them with other systems, based on your needs.

<details><summary>Metadata</summary>

- Duration: 33949 ms
- Datetime: 2023-12-06T15:07:28.545234
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

**Prompt:**
Too many arguments (3) to FORMAT "~&%-10d %-30s %-50s": uses at most 0.

**Response:**
Apologies for the confusion. The `FORMAT` function in Common Lisp can take an arbitrary number of arguments after the control string, depending on the directives used within the control string itself. The error message you encountered suggests that the format directives may not correspond to the provided arguments.

Let's correct the `print-github-label-details` function to use the `FORMAT` function properly, taking into account the number and types of arguments we are passing:

```lisp
(defun print-github-label-details ()
  "Print details of GitHub labels stored in *github-labels-list*."
  (unless *github-labels-list*
    (error "No data available. Please run save-github-labels first."))

  ;; Print the table header
  (format t "~&~%-10s ~%-30s ~%-50s~%" "ID" "Name" "Description")
  (format t "~&~%-10s~%-30s~%-50s~%" "----------" "------------------------------" "--------------------------------------------------")
  
  ;; Iterate over the list and print each label's details
  (dolist (label *github-labels-list*)
    (let ((id (first label))
          (name (second label))
          (description (third label)))
      (format t "~&~%-10A ~%-30A ~%-50A~%" id name description)))) ; Use ~A for aesthetic output
```

In this corrected function, the format control string `~&~%-10A ~%-30A ~%-50A~%` is used. The `~A` directive is for printing an object "aesthetically," and it works for most Lisp objects. I also added `~%` directives to insert newlines after the header and each label's details. The `~&` directive ensures we start on a fresh line.

Now you should be able to run the `print-github-label-details` function without encountering the `FORMAT` error. Make sure `*github-labels-list*` is populated by first running `save-github-labels`.

<details><summary>Metadata</summary>

- Duration: 39980 ms
- Datetime: 2023-12-06T15:25:33.646195
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

