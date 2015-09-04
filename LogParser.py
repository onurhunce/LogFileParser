# coding=utf-8
import argparse
import operator
from itertools import islice
import os


def log_parser(file_to_read):
    """
    Reads file, splits into data, return desired outputs.
    """
    url_dict = {}
    with open(file_to_read) as f:
        temp_time = None
        temp_url = None
        url_time = None
        size = os.path.getsize(file_to_read)
        for element in islice(f, size):
            temp = (element.split(" "))
            if temp[-1:] > temp_time:
                temp_time = temp[-1:]
                url_time = ''.join(temp[-1:])[:-1]
                temp_url = temp[6]

            if temp[6] in url_dict:
                url_dict[temp[6]] += 1
            else:
                url_dict[temp[6]] = 1

    most_request_url = max(url_dict.iteritems(), key=operator.itemgetter(1))[0]

    return len(url_dict.keys()), most_request_url, temp_url, url_time


"""
Prints distinct url count, most requested url, most time consuming url,
and time of that url.
"""


def print_results(parser_results="There is no result."):
    distinct_url_count, most_requested_url, biggest_url_time, biggest_time = \
        parser_results
    print "Distinct url count: %s" % distinct_url_count
    print "Most requested url: %s" % most_requested_url
    print "Most time consuming url:%s time: %s" % (biggest_url_time,
                                                   biggest_time)


if __name__ == "__main__":

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("file_to_read")
        args = parser.parse_args()
        if args.file_to_read:
            print_results(log_parser(args.file_to_read))
    except ValueError:
        print("Error in reading file!")
