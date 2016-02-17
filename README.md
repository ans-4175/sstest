# README
## Problem 1
`python prob1.py [filename]`
It will produce file output with name `[filename].out`
> If you need a seeding file execute this `python seeding.py [filename] [number_of_lines]`

## Problem 2
I believe my script will solve it, but maybe take more time. I would like to split parallelism wisely based on CPU cores, find suitable tuning. I would like to find tuning how many I should split input files into chunks, and number of parallelism.
> Based on my benchmark and shitty use of multiprocessing (first time using Python's Pool). With my laptop (i5 with 8GB memory, I use pool's count same as my cores' count and chunked files into 1024 * CPU cores' count), I need around ~2GB for processing 7 million entries. It must be my mistakes not patiently try better tuning or good use of multiprocessing

## Problem 3
`python prob3.py [filename] [name_to_find] [phone_to_find]`
It will print in console True|False whether your arguments exists
> If you need a seeding file execute this `python seeding3.py [filename] [number_of_lines]`