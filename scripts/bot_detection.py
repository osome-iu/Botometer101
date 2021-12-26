"""
This script checks the bot scores of the accounts in the input file

argv[1]: filename of input, should be a csv file with just the user_ids
argv[-1:]: filename of output
"""
import sys
import json
import utils
import json
import botometer

if __name__ == "__main__":
    logger = utils.get_logger(__name__)

    # parse the input parameters
    input_filename = sys.argv[1]
    output_filename = sys.argv[-1]

    # load the Twitter app keys
    with open("keys.json") as f:
        keys = json.load(f)

    # initialize Botometer class
    rapidapi_key = keys['rapidapi_key']
    twitter_app_auth = {
        'consumer_key': keys['consumer_key'],
        'consumer_secret': keys['consumer_secret'],
        'access_token': keys['access_token'],
        'access_token_secret': keys['access_token_secret']
    }

    bom = botometer.Botometer(
        wait_on_ratelimit=True,
        rapidapi_key=rapidapi_key,
        **twitter_app_auth
        )

    # load the input
    user_ids = []
    with open(input_filename) as f:
        for line in f:
            user_ids.append(int(line))

    # start to check the bot scores
    logger.info(f"Check bot scores for {len(user_ids)} users")
    bot_scores = []
    for index, user_id in enumerate(user_ids):
        logger.info(f"Checking user {user_id}, {index} / {len(user_ids)}...")
        try:
            result = bom.check_account(user_id)
            bot_scores.append(result)
        except KeyboardInterrupt:
            sys.exit()
        except Exception as e:
            err_msg = 'Error handling account {}\n{}: {}'.format(
                user_id,
                type(e).__name__,
                getattr(e, 'msg', '') or getattr(e, 'reason', ''),
                )
            logger.info(err_msg)
            with open(f"{output_filename}.error", "a") as ef:
                ef.write(f"{user_id}\n")

    logger.info(f"Fetched bot scores for {len(bot_scores)} / {len(user_ids)} accounts")

    if len(bot_scores) < len(user_ids):
        logger.info(f"Error log file: {output_filename}.error")

    logger.info("Start to dump the bot scores")
    with open(output_filename, "w") as f:
        for bot_score in bot_scores:
            bot_score_str = json.dumps(bot_score) + "\n"
            f.write(bot_score_str)