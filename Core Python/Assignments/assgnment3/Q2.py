#Write a program to input any alphabet and check whether it is vowel or consonant.
alpha = input('Enter the alpha:')
#alpha = 'a'
if (alpha in ('aeiouAEIOU')):
    print('vowel')
else: 
    print('consonat')
