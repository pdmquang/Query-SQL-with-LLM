from langchain_ollama import OllamaEmbeddings
import pandas as pd
import time
from scipy.spatial.distance import cosine

start = time.time()
t_user_df = pd.read_csv("./data/T_USER.csv")
ct_user_level_df = pd.read_csv("./data/CT_USER_LEVEL.csv")

embed = OllamaEmbeddings(
    model="llama3:8b"
)

end = time.time()
print(f"Load model {end - start}")

def cosine_similarity(x, y):
    return 1 - cosine(x,y)

def get_embedding(text):
    text = text.replace("\n", " ")
    return embed.embed_query(text)

# ct_user_level_df["embedding"] = ct_user_level_df.apply(lambda row: row)

embeds_dict = dict()
col_names = ct_user_level_df.columns
# embeds = [get_embedding(f"{col_names[index]} + {row}") for index, row in ct_user_level_df.iterrows()]

start = time.time()
for index, row in ct_user_level_df.iterrows():
    embeds_dict[row.to_json()] = get_embedding(row.to_json())

end = time.time()
print(f"Get Embedding for {len(ct_user_level_df)} rows in {(end - start) % 60}")

customer_query = "Get payment limit of this user id = INLABLB"
query_embed = get_embedding(customer_query)

scores = dict()
for text, embedding in embeds_dict.items():
    scores[text] = cosine_similarity(query_embed, embedding)

sorted_scores = dict(sorted(
                        scores.items(), 
                        key=lambda item: item[1], 
                        reverse=True)
                    )

print(sorted_scores)


# import ollama

# response = ollama.chat(
#     model="llama3:8b",
#     messages=[
#         {
#             "role": "user",
#             "content": "Tell me an interesting fact about elephants",
#         },
#     ],
# )
# print(response["message"]["content"])