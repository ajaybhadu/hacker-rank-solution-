import sys

nums = ['twelve', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve',
        'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty one',
       'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 
       'twenty nine']

H = int(sys.stdin.readline())
M = int(sys.stdin.readline())

if M==0:
    print nums[H] + " o' clock"
elif M==15:
    print "quarter past " + nums[H]
elif M==30:
    print "half past " + nums[H]
elif M==45:
    print "quarter to " + nums[(H+1)%12]
elif M==1:
    print "one minute past " + nums[H]
elif M==59:
    print "one minute to " + nums[(H+1)%12]
elif M < 30:
    print nums[M] + " minutes past " + nums[H]
elif M > 30:
    print nums[60-M] + " minutes to " + nums[(H+1)%12]
    
