https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
# CMT114 Coursework
# student number:

import docx
import os, sys

def change_style(filepath, style='IEEE'):
    pass # remove this when you add your code
    # YOUR CODE HERE
    # YOUR CODE HERE
    # YOUR CODE HERE

# ---- DO NOT CHANGE THE CODE BELOW ----
if __name__ == "__main__":
    if len(sys.argv)<3: raise ValueError('Provide filename and style as input arguments')
    filepath, style = sys.argv[1], sys.argv[2]
    print('filepath is "{}"'.format(filepath))
    print('target style is "{}"'.format(style))
    change_style(filepath, style)
