
llm_wrapper() {
    command="$@"
    models=("3.5" "4t")
    # create a command for each model, and send it to the model
    filenames=()
    for i in {0..1}; do
        model_name="model_$i"
        model=${models[$i]}
        # filename from datetime
        filename="$(date '+%Y-%m-%d-%H-%M-%S')-$model_name.md"
        llm -m $model "$command" > "$filename" &
        filenames+=("$filename")
    done
}


llm_wrapper "$@"
for filename in "${filenames[@]}"; do
    code "$filename"
done