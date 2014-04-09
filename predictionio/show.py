import predictionio

client = predictionio.Client(appkey="9p8iicV4jQPFrh9aP9Xf2JMpA4Gv8JGv7CVgQI4X9dSLbIclWVetjbaikJbt9lca")

# Recommend 5 items to each user
user_ids = [str(x) for x in range(1, 6)]
for user_id in user_ids:
    print "Retrieve top 5 recommendations for user", user_id
    try:
        client.identify(user_id)
        rec = client.get_itemrec_topn("engine1", 5)
        print rec
    except predictionio.ItemRecNotFoundError as e:
        print 'Caught exception:', e
