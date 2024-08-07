import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Apply a custom theme for better aesthetics
sns.set_theme(style="whitegrid")

# Reading the CSV files
conversation_df = pd.read_csv('/home/ShellLM/Projects/undecidability/agents/rubrics/conversation_eval.csv')
response_df = pd.read_csv('/home/ShellLM/Projects/undecidability/agents/rubrics/response_eval.csv')

# Plotting the data for conversation evaluations
plt.figure(figsize=(15, 8))
sns.barplot(data=conversation_df.melt(id_vars=['evaluation_id', 'model_judge', 'group_id', 'total_prompts', 'overall_justification']), 
            x='variable', y='value', hue='model_judge', palette="viridis")
plt.title('Scores from Conversation Evaluations', fontsize=20)
plt.xlabel('Evaluation Metrics', fontsize=15)
plt.ylabel('Scores', fontsize=15)
plt.legend(title='Model Judge', fontsize=12)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig('/home/ShellLM/Projects/undecidability/agents/rubrics/conversation_eval_scores.png')

# Plotting the data for response evaluations
plt.figure(figsize=(15, 8))
sns.barplot(data=response_df.melt(id_vars=['evaluation_id', 'group_id', 'response_number', 'justification']), 
            x='variable', y='value', hue='group_id', palette="viridis")
plt.title('Scores from Response Evaluations', fontsize=20)
plt.xlabel('Evaluation Metrics', fontsize=15)
plt.ylabel('Scores', fontsize=15)
plt.legend(title='Group ID', fontsize=12)
plt.xticks(rotation=45, fontsize=12)
plt.yticks(fontsize=12)
plt.tight_layout()
plt.savefig('/home/ShellLM/Projects/undecidability/agents/rubrics/response_eval_scores.png')

print("Charts have been successfully created and saved.")
