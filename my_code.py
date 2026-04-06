import pytest

def fix_phone_num(phone_num_to_fix):
  
  if len(phone_num_to_fix) != 10:
    raise ValueError("Can only format numbers that are exactly 10 digits long")
  
  # add an additional test that fails with a specific message if the phone number is longer than 10 digits but starts with '+1'
  if len(phone_num_to_fix) >= 10 and phone_num_to_fix[0:2] = '+1':
    raise ValueError("Can only format numbers that are exactly 10 digits long")
      
  if not phone_num_to_fix.isdigit():
    raise ValueError("Phone number must only contain digits")
      
  area_code = phone_num_to_fix[0:3]
  three_part = phone_num_to_fix[3:6]
  four_part = phone_num_to_fix[6:]
      
  fixed_num = "(" + area_code + ")" + " " + three_part + " " + four_part 
  return fixed_num
