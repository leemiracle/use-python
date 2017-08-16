#!/usr/bin/env python
# coding=utf8

from tensorflow.tensorboard.backend.event_processing import event_file_loader
from tensorflow.python.summary.writer import event_file_writer
import sys
from collections import defaultdict
import argparse

MAX_EVENT_NUM = 2000
EVENT_SPACING = 100
min_field_num = 2


def find_largest_public_contract(number):
    """
    找所有能整除number的数
    :param number:
    :return:
    """
    import math
    array = []
    sqrt_n = int(math.sqrt(number))
    for i in range(1, sqrt_n+1):
        if number % i == 0:
            array.append(i)
            array.append(number/i)
    return sorted(list(set(array)))


def main():
    global MAX_EVENT_NUM, EVENT_SPACING
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help="Input file name", required=True)
    parser.add_argument('-o', '--output', help="Output file name", required=True)
    parser.add_argument("-max", "--max_event_number", help="the limit number of event log to save",
                        action="store", type=int)
    parser.add_argument("-space", "--max_space", help="the setting of event space",
                        action="store", type=int)
    args = parser.parse_args()
    if args.max_event_number:
        MAX_EVENT_NUM = args.max_event_number
    if args.max_space:
        EVENT_SPACING = args.max_space
    inputfile = args.input
    outputfile = args.output
    # inputfile = '/data/dlp_test/mao_tbs/491/train/events.out.tfevents.1501763386.ai-work-2'
    # outputfile = '/data/dlp_test/mao_tbs/491/test'

    _generator = event_file_loader.EventFileLoader(inputfile)
    i = 0
    # image_values = []
    indexes = []
    file_versions = []
    graph_defs = []
    meta_graph_defs = []
    tagged_run_metadatas = []
    for event in _generator.Load():
        records = defaultdict(int)
        if event.HasField('summary'):
            count = 0
            for value in event.summary.value:
                if value.HasField('image'):
                    records['image'] += 1
                    value.ClearField('image')
                    # print event.ListFields()
                elif value.HasField('simple_value'):
                    records['simple_value'] += 1
                    # print value.tag
                elif value.HasField('histo'):
                    records['histo'] += 1
                elif value.HasField('obsolete_old_style_histogram'):
                    records['old_style_histo'] += 1
                elif value.HasField('audio'):
                    records['audio'] += 1
                elif value.HasField('tensor'):
                    # almost no data
                    records['tensor'] += 1
                    # print value.tag
                count += 1
        elif event.HasField('file_version'):
            file_versions.append(i)
        elif event.HasField('graph_def'):
            graph_defs.append(i)
        elif event.HasField('meta_graph_def'):
            meta_graph_defs.append(i)
        elif event.HasField('tagged_run_metadata'):
            tagged_run_metadatas.append(i)
        indexes.append(len(records.keys()))
        i += 1

    # for k in image_values:
    #     print k, image_values[k]["id"], image_values[k]["count"]
    #     events[image_values[k]["id"]].summary.value[image_values[k]["count"]].image.CopyFrom(image_values[k]["value"])
    # print indexes
    print 'file_versions:', file_versions
    print 'graph_defs:', graph_defs
    print 'meta_graph_defs:', meta_graph_defs
    print 'tagged_run_metadatas:', tagged_run_metadatas
    meta_events = file_versions + graph_defs + meta_graph_defs+tagged_run_metadatas
    print "events:", len(indexes)
    # 结尾索引
    max_field_len = max(indexes)
    max_index = list(reversed(indexes)).index(max_field_len)
    max_index = len(indexes) - max_index
    # indexes = [i for i in range(len(indexes)) if indexes[i] == max_field_len]
    # print "信息量多的event:", len(indexes)
    # store_list = find_max_equal_diffence_array(indexes)
    # print "event的最大等差数列:", store_list
    # compression_ratio = int(len(store_list) / MAX_EVENT_NUM)

    # 开头索引
    index = 0
    for i in range(len(indexes)):
        if indexes[i] >= min_field_num:
            index = i
            break
    # 算法基本假设： 所有信息量多event是以MAX_EVENT_NUM为间隔增长的,默认100
    store_list = [i for i in range(index, max_index)]
    compression_ratio = int(len(store_list)/MAX_EVENT_NUM)
    compression_ratio = compression_ratio if compression_ratio else 1
    print "数列的压缩率:", compression_ratio
    if compression_ratio > 1:
        spacing_public_contract = find_largest_public_contract(EVENT_SPACING)
        rate = int(compression_ratio/EVENT_SPACING)
        if rate > 1:
            setup_num = rate*EVENT_SPACING
        else:
            setup_num = filter(lambda x: x <= compression_ratio, spacing_public_contract)[-1]
        store_list = store_list[::setup_num]
    # for k in last_image:
    #     events[store_list[-1]].summary.value[last_image[k]["count"]].image.CopyFrom(last_image[k]["value"])
    # events = [events[i] for i in store_list]
    ew = event_file_writer.EventFileWriter(outputfile)
    out_json = defaultdict(list)
    i = 0
    event_count = 1
    _generator = event_file_loader.EventFileLoader(inputfile)
    for event in _generator.Load():
        # 清除图片
        if event.HasField('summary'):
            for value in event.summary.value:
                # 不删除最后一张图片
                if value.HasField('image') and (i != store_list[-1]):
                    value.ClearField('image')
        if i in store_list:
            event_count += 1
            ew.add_event(event)
            for v in event.summary.value:
                if v.HasField('simple_value'):
                    out_json[v.tag].append(v.simple_value)
        elif i in meta_events:
            event_count += 1
            ew.add_event(event)

        i += 1
    ew.flush()
    ew.close()
    print event_count
    # print out_json


def find_max_equal_diffence_array(array):
    length = 2
    a = array
    n = len(a)-1
    l = dict()
    key = [a[-2], a[-1]]
    times = 0
    for j in range(n-1, 0, -1):
        i = j-1
        k = j+1
        while(i >= 0 and k <= n):
            times += 1
            if times % 1000 == 0:
                print "times:", times
            if a[i] + a[k] < 2*a[j]:
                k += 1
            elif a[i] + a[k] > 2*a[j]:
                l[(i, j)] = 2
                i = i-1
            else:
                if (j, k) not in l:
                    l[(j, k)] = 2
                l[(i, j)] = l[(j, k)]+1
                for ke in l:
                    if l[ke] > length:
                        length = l[ke]
                        key = [ke[0], ke[1]]
                i = i-1
                k = k+1
    setup = int(a[key[1]]-a[key[0]])
    return [(a[key[0]] + i*setup) for i in range(length)]


if __name__ == '__main__':
    from sys import argv

    script, user_name = argv
    print(script, user_name)