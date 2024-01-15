**Prompt:**
Write a bash terminal command to achieve the following task.
Be concise, but include as much code as needed. Do not write anything else. Ever.

**TASK**
**for i in {1..4}; do for tip in {"20 (TWENTY)","200 (TWO HUNDRED)","20000 (TWENTY THOUSAND)"}; do llm -m 4t -t tip-test "Just tell me how to extract the tip amount?" -p tip "$tip"  > "output_$i.txt"; done; done


**Response:**
for i in {1..4}; do for tip in "20 (TWENTY)" "200 (TWO HUNDRED)" "20000 (TWENTY THOUSAND)"; do llm -m 4t -t tip-test "Just tell me how to extract the tip amount?" -p tip "$tip" > "output_$i.txt"; done; done

<details><summary>Metadata</summary>

- Duration: 7460 ms
- Datetime: 2024-01-09T14:42:42.447365
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{"temperature": 0.0}
```

**Prompt:**
make it none-blocking so they are called in parrallel?

**Response:**
for i in {1..4}; do for tip in "20 (TWENTY)" "200 (TWO HUNDRED)" "20000 (TWENTY THOUSAND)"; do llm -m 4t -t tip-test "Just tell me how to extract the tip amount?" -p tip "$tip" > "output_${i}_${tip//[^0-9]/}.txt" & done; done

<details><summary>Metadata</summary>

- Duration: 7256 ms
- Datetime: 2024-01-09T14:44:26.538845
- Model: gpt-4-1106-preview

</details>

**Options:**
```json
{}
```

