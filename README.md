# pee

## (p)ython fr(ee) 
### the Linux free command but for MacOS and built in Python

`pee` displays stats about `total`, `used`, `free`, and `available` memory in the system. By default (no flag), it returns the stts as bytes.

`time` also returns `buffer` and `cache` info which is not available from the MacOS kernal. 

## Installation
`pip install pee`

## Usage
`pee <metric>` where `metric` is a data metric.  

### flags
```
-h, --help          show this help message and exit
-g, --gigabytes     display memory info in gigabytes
-m, --megabytes     display memory info in megabytes
-k, --kilobytes     display memory info in kilobytes
-b, --bytes         display memory info in bytes (default)
-V, --version       display version info
```

## Dependencies
[psutil](https://github.com/giampaolo/psutil)

## More Info
I am currently working through [Operating System: Three Easy Steps](http://pages.cs.wisc.edu/~remzi/OSTEP/) and the exercises at the end of chapter 13 require the use of `free`. I am using MacOS so I don't have access to it.

Yes, I could have just booted up Virtual Box for Ubuntu, but instead I built a tool similar to `free` for use on MacOS, because there should be one anyways.

## Contributing
feel free to raise an issue or pull request if you find a bug
