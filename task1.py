
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df= pd.read_csv("C:/Users/Sri/Contacts/Downloads/cards_data.csv")
# Set style for plots
sns.set(style="whitegrid")

# ---- Clean and convert 'acct_open_date' safely to datetime ----
df['acct_open_date'] = pd.to_datetime(df['acct_open_date'], errors='coerce')
df['acct_open_year'] = df['acct_open_date'].dt.year
df = df.dropna(subset=['acct_open_year'])

# ---- Create a 2x3 grid layout for subplots ----
fig, axes = plt.subplots(2, 3, figsize=(10, 6))

# Plot 1: Card Brand Distribution (Bar Plot)
sns.countplot(data=df, x='card_brand', palette='muted', ax=axes[0, 0])
axes[0, 0].set_title('Card Brand Distribution')
axes[0, 0].set_xlabel('Card Brand')
axes[0, 0].set_ylabel('Count')

# Plot 2: Card Type by Brand (Stacked Bar Plot)
sns.countplot(data=df, x='card_brand', hue='card_type', palette='Set2', ax=axes[0, 1])
axes[0, 1].set_title('Card Type by Brand')
axes[0, 1].set_xlabel('Card Brand')
axes[0, 1].set_ylabel('Count')

# Plot 3: Has Chip vs Card Type (Count Plot)
sns.countplot(data=df, x='card_type', hue='has_chip', palette='coolwarm', ax=axes[0, 2])
axes[0, 2].set_title('Has Chip vs Card Type')
axes[0, 2].set_xlabel('Card Type')
axes[0, 2].set_ylabel('Count')

# Plot 4: Account Open Year Trends (Bar Plot)
sns.countplot(data=df, x='acct_open_year', palette='Blues', ax=axes[1, 0])
axes[1, 0].set_title('Account Open Year Trends')
axes[1, 0].set_xlabel('Year')
axes[1, 0].set_ylabel('Number of Accounts Opened')
axes[1, 0].tick_params(axis='x', rotation=45)

# Plot 5: Average Credit Limit by Card Type (Box Plot)
sns.boxplot(data=df, x='card_type', y='credit_limit', palette='pastel', ax=axes[1, 1])
axes[1, 1].set_title('Average Credit Limit by Card Type')
axes[1, 1].set_xlabel('Card Type')
axes[1, 1].set_ylabel('Credit Limit')

# Plot 6: Number of Cards Issued vs Credit Limit (Scatter Plot)
sns.scatterplot(data=df, x='num_cards_issued', y='credit_limit', hue='card_type', palette='coolwarm', ax=axes[1, 2])
axes[1, 2].set_title('Number of Cards Issued vs Credit Limit')
axes[1, 2].set_xlabel('Number of Cards Issued')
axes[1, 2].set_ylabel('Credit Limit')

# Add a main title for the whole figure
fig.suptitle('Credit Card Data Analysis', fontsize=18, fontweight='bold', y=0.99)

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()
