from psutil import virtual_memory, swap_memory
from argparse import ArgumentParser
import sys

from .__init__ import __version__

mem = virtual_memory()
swap = swap_memory()
version_info = f"pee version: {__version__}"

def metric_info(flag):
    '''get appropriate number for math for metric based on flag'''
    m = 0
    if flag == 'b':
        m = 1
        return m
    metrics = {
            'gb': 1073741824,
            'kb': 1024,
            'mb': 1048576
            }
    if flag not in metrics.keys():
        print("problem with metric")
        exit(1)
    else:
        m = metrics.get(flag)
    return m


def vm_metrics(item, m):
    '''do the math for the appropriate metric'''
    try:
        if m == 1: # if measured in bytes, return without decimals
            result = item/m
            return int(result)
        elif m == 1073741824: # if GB, return with 2 decimal places
            result  = round(item/m,2)
            return result
        else:
            result = round(item/m)
            return result
    except:
        return None


def print_info(metric, unit):
    '''print info about virtual memory based on flag'''
    # MEM info
    print("Mem:")
    total = vm_metrics(mem.total, metric)
    used = vm_metrics(mem.used, metric)
    free = vm_metrics(mem.free, metric)
    available = vm_metrics(mem.available, metric)
    
    print(f"\ttotal: {total} {unit}")
    print(f"\tused: {used} {unit}")
    print(f"\tfree: {free} {unit}")
    print(f"\tavailable: {available} {unit}")

    # SWAP info
    print("Swap:")
    total = vm_metrics(swap.total, metric)
    used = vm_metrics(swap.used, metric)
    free = vm_metrics(swap.free, metric)

    print(f"\ttotal: {total} {unit}")
    print(f"\tused: {used} {unit}")
    print(f"\tfree: {free} {unit}")


def main():

    ap = ArgumentParser(description="Display amount of free and used memory in the system")
    ap.add_argument("-g", "--gigabytes", action="store_true", 
            help="display memory info in gigabytes")
    ap.add_argument("-m", "--megabytes", action="store_true",
            help="display memory info in megabytes")
    ap.add_argument("-k", "--kilobytes", action="store_true",
            help="display memory info in kilobytes")
    ap.add_argument("-b", "--bytes", action="store_true",
            help="display memory info in bytes")
    ap.add_argument("-V", "--version", action="store_true", 
            help="display version info")

    args = ap.parse_args()

    ####### only allow one flag at a time
    true_count = 0
    vals = vars(args)

    for i in vals.values():
        if i == True:
            true_count+=1
    
    if true_count > 1:
        print("only one argument at a time")
        exit(1)


    if args.gigabytes:
        metric = metric_info('gb')
        print_info(metric, "GB")

    elif args.megabytes:
        metric = metric_info('mb')
        print_info(metric, "MB") 
    
    elif args.kilobytes:
        metric = metric_info('kb')
        print_info(metric, 'KB')
    
    elif args.bytes:
        metric = metric_info('b')
        print_info(metric, "")

    elif args.version:
        print(version_info)
    
    else: # show in bytes by default
        metric = metric_info('b')
        print_info(metric, "")

if __name__ == '__main__':
    main()
