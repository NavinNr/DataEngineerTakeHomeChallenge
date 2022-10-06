# Answers
These are my answers to the questions that require an output.

1. Original number of rows: 1000
3. Rows removed: 6
5. Users ranked 1 in their age group:
 
| id                                   | email                      | age_group |
|--------------------------------------|----------------------------|-----------|
| 64c1dc80-0d62-4b19-910b-9f08ca275eaf | jpatricheph@stanford.edu   | 1         |
| e5179ee6-baa2-44f4-9202-3c04019518d3 | tlewington1g@pcworld.com   | 2         |
| d85e4e4b-bf84-47ab-9c04-8ab668d9b055 | ukillcrossj2@xinhuanet.com | 3         |
| 198854aa-3b04-468c-aeae-947922981eda | rthorleyi0@buzzfeed.com    | 4         |

7. New total number of rows: 1781

# Solution Thoughts

The script to process the data is in DataProcessing.py. Please have data.json in the same folder or modify the path of the data in the script accordingly. The script will print the output to the questions in the console and generate the required parquet files in the same folder.

Decided to use Python as Pandas and other libraries like RSA provided a good way to process the data without having to write custom methods.

Total time taken was approximately 1 hour with most of the time spent on finding a solution to the anonymizing email problem. Went with RSA as it can be encrypted and decrypted once the key has been stored.

Overall, it was a fun exercise and a good opportunity to refresh some data processing skills that I don't do on a day to day basis.
