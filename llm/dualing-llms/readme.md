use a wrapper around llm to make it run dual llm requests in parallel
1. llm -t man-terminator -m 4t "Tell me how to create two terminals and create a command in both of them at once."
2. llm -t man-terminator -m 4t "Broadcast to all terminals"
3. explain 'git init && git branch -M main && gh repo create llm-templates --source=. --public'
4. llm -m gorilla 'Convert audio to text'
5. llm -m gorilla 'Convert audio to text' -o temperature 1
6. llm -m gorilla 'load a peft ' -o temperature 1
7. llm -m gorilla 'run inference on a peft adapter' -o temperature 1
8. llm -m gorilla 'load a model and PEFT adapter' -o temperature 1
   
