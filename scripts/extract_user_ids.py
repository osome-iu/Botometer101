"""
This script extracts the unique user_ids from the tweet collection

argv[1]: filename of input
argv[-1]: filename of output
"""
import sys
import utils
import json

if __name__ == "__main__":
    logger = utils.get_logger(__name__)

    # parse the input parameters
    input_filename = sys.argv[1]
    output_filename = sys.argv[-1]

    logger.info(f"Start to extract user_ids from {input_filename}")
    user_ids = set()
    with open(input_filename) as f:
        for line in f:
            tweet = json.loads(line)
            user_ids.add(tweet['user']['id_str'])

    logger.info("Start to dump the user_ids")
    with open(output_filename, "w") as f:
        for user_id_str in user_ids:
            f.write(f"{user_id_str}\n")