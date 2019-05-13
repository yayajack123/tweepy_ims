import tweepy
import time
# NOTE: I put my keys in the keys.py to separate them
# from this main file.
# Please refer to keys_format.py to see the format.
from db_con import *
from keys import *

# NOTE: flush=True is just for running this script
# with PythonAnywhere's always-on task.
# More info: https://help.pythonanywhere.com/pages/AlwaysOnTasks/
# print('this is my twitter bot', flush=True)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

FILE_NAME = 'last_seen_id.txt'
FILE_NAME1 = 'last_seen_id_mentions.txt'


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def retrieve_last_seen_id_mentions(file_name):
    f_read = open(file_name, 'r')
    last_seen_id_mentions = int(f_read.read().strip())
    f_read.close()
    return last_seen_id_mentions

def store_last_seen_id_mentions(last_seen_id_mentions, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id_mentions))
    f_write.close()
    return

def check_update():
    print('check data mahasiswa...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    check_id = 'select max(tb_mahasiswa.id) from tb_mahasiswa'
    cursor_db.execute(check_id)
    test=cursor_db.fetchone()[0]
    if test > last_seen_id :
        print("ada data baru\n")
        get_new_data = 'select *from tb_mahasiswa where id>%d' %(last_seen_id)
        cursor_db.execute(get_new_data)
        hasil = cursor_db.fetchall()
        for data in hasil:
            print("nim " + data[1] + "total harus bayar %d" %(data[3]))
            api.update_status('@ImsBot' + ' #'+data[1] +'-'+data[2] +'-%d' %(data[3]))
            print("data has been sent\n")


        last_seen_id = data[0]
        store_last_seen_id(last_seen_id,FILE_NAME)
        # get_new_data='select *from tb_mahasiswa where id=%s'%(test)
        # cursor_db.execute(get_new_data)
        # results = cursor_db.fetchone()

        # last_seen_id = test
        # store_last_seen_id(last_seen_id, FILE_NAME)
        # api.update_status('@widianapw' + ' #'+results[1] +' #%d' %(results[2]))
        # print("data has been sent")

    else:
        print("tidak ada data baru..\n")
    db.commit()

def check_message():
    last_seen_id_mentions = retrieve_last_seen_id_mentions(FILE_NAME1)
    mentions = api.mentions_timeline(last_seen_id_mentions, tweet_mode='extended')
    for mention in reversed(mentions):
        print("Mendapat data kiriman dari bank")
        print(mention.full_text.lower(), flush=True)
        hasil1 = (mention.full_text.lower().split("#"))[1]
        nim = (hasil1.split("-"))[0]
        status = int((hasil1.split("-"))[1])
        print(nim)
        print(status)
        update = "update tb_mahasiswa set status_pembayaran = '%s' where nim = %s" %(status,nim)
        print("data sudah diupdate\n")
        cursor_db.execute(update)
        db.commit()
        last_seen_id_mentions = mention.id
        store_last_seen_id_mentions(last_seen_id_mentions, FILE_NAME1)

# def reply_to_tweets():
#     print('retrieving and replying to tweets...', flush=True)
#     # DEV NOTE: use 1060651988453654528 for testing.
#     last_seen_id = retrieve_last_seen_id(FILE_NAME)
#     # NOTE: We need to use tweet_mode='extended' below to show
#     # all full tweets (with full_text). Without it, long tweets
#     # would be cut off.
#     mentions = api.mentions_timeline(
#                         last_seen_id,
#                         tweet_mode='extended')
#
#     for mention in reversed(mentions):
#         print(str(mention.id) + ' - ' + mention.full_text, flush=True)
#         last_seen_id = mention.id
#         store_last_seen_id(last_seen_id, FILE_NAME)
#         sql_select = "select * from tb_chat"
#         cursor_db.execute(sql_select)
#         results = cursor_db.fetchall()
#         flag=0
#         for row in results:
#             if row[1] in mention.full_text.lower():
#                 text=row[2]
#                 flag=flag+1
#         if flag == 0:
#             text = "Semangat kak!"
#
#         flag = 0
#         api.update_status('@' + mention.user.screen_name + ' ' + text, mention.id)
#         print("reply has been sent")
#
#         # if results is not None:
#         #     api.update_status('@' + mention.user.screen_name +'#bos back to you!', mention.id)
#         # else :
#         #     api.update_status('@' + mention.user.screen_name + '#bos is not back!', mention.id)
#             # if row[0] in mention.full_text.lower():
#             #     print(1)
#         # if '#bos' in mention.full_text.lower():
#         #     print('found #bos!', flush=True)
#         #     print('responding back...', flush=True)
#         #     api.update_status('@' + mention.user.screen_name +
#         #             '#bos back to you!', mention.id)

while True:
    check_update()
    check_message()
    time.sleep(3)
