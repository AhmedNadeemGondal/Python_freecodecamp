text = "X-DSPAM-Confidence:    0.8475"
white_space = text.find(' ')
after_white_space = text[white_space:]
final_string = after_white_space.strip()
final_string = float(final_string)

print(final_string)