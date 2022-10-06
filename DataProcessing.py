import pandas as pd
import rsa

start_df = pd.read_json('data.json', lines=True)
initial_rows = len(start_df)
print("initial rows: " + str(initial_rows))

dedupe_df = start_df.drop_duplicates(subset=['id','created_at'])
deduped_rows = len(dedupe_df)
print("deduped rows: " + str(deduped_rows))
print("Duplicate rows removed " + str(initial_rows-deduped_rows))

dedupe_df['age_group_rank'] = dedupe_df.groupby('age_group')['user_score'].rank(ascending=True)
dedupe_df['age_group_rank'] = dedupe_df['age_group_rank'].astype(int)

firsts_df = dedupe_df.loc[dedupe_df['age_group_rank']==1]
firsts_df = firsts_df[['id','email','age_group']].sort_values(by=['age_group'])
print(firsts_df)

dedupe_df = dedupe_df.explode('widget_list')
print("Exploded Widget List Rows: " + str(len(dedupe_df)))

#expand the widget list
dedupe_df = pd.concat([dedupe_df, dedupe_df['widget_list'].apply(pd.Series)], axis = 1,)
dedupe_df = dedupe_df.drop(columns=["widget_list"])
dedupe_df = dedupe_df.iloc[: , :-1]
dedupe_df.dropna(axis=1, how='all')

dedupe_df = dedupe_df.rename(columns={"name":"widget_name", "amount":"widget_amount"})

#encrypt email
publicKey, privateKey = rsa.newkeys(512)
dedupe_df['email'] = [rsa.encrypt(x.encode(),publicKey) for x in dedupe_df['email']] 
dedupe_df.to_parquet('dedupe_data.parquet')

#dataframe of location and ids
inverse_df = dedupe_df[['location','id']]
inverse_df = inverse_df.groupby('location')['id'].apply(list).reset_index()
inverse_df = inverse_df.rename(columns={"id":"ids"})
inverse_df.to_parquet('inverse_data.parquet')
