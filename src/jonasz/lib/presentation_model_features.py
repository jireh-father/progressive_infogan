"""
Full summary of featuers isolated in a run of exp_consistency_300.
"""

_descriptions = {
  79: ('Size of the irises', ', face redness'),
  78: ('Eyelids', ', face redness'),
  77: ('Nostrils & eyelids', ''),
  76: ('Shape of the nostrils, wrinkles', ''),
  75: ('Wrinkles', ''),
  74: ('Eyelids (subtle)', ', wrinkles'),
  73: ('Wrinkles', ', skin redness'),
  72: ('Lower eyelid', ''),
  71: ('Shape of the eyes', ''),
  70: ('Face redness', ''),
  69: ('Wrinkles', ''),
  68: ('Hair texture', ''),
  67: ('Shape of the nostrils', ''),
  66: ('Hair texture', ''),
  65: ('Size of the irises', ''),
  64: ('Color of the irises', ''),

  63: ('Skin color, face geometry', ''),
  62: ('Look direction', ''),
  61: ('Nose tip: left / right, eyebrows', ''),
  60: ('Vertical face stretch', ''),
  59: ('Nose geometry (subtle)', ''),
  58: ('Upper lip + face geometry', ''),
  57: ('Look direction', ''),
  56: ('Nose: vertical position', ''),
  55: ('Eyebrows shape', ''),
  54: ('Nose position', ', look direction'),
  53: ('Age', ''),
  52: ('Nose: upturned tip', ''),
  51: ('Cheeckbones and nose, subtle', ''),
  50: ('Nose tip shape', ', hair texture'),
  49: ('Nose length', ''),
  48: ('Eyebrows up / down', ''),

  47: ('Face oval: chin', ''),
  46: ('Subtle head inclination', ''),
  45: ('Hair: curly / straight', ''),
  44: ('Mouth open / closed', ', man / woman'),
  43: ('Forward / backward inclination', ', hair texture'),
  42: ('Face oval, smile, chin size', ''),
  41: ('Man / woman', ', slight nod'),
  40: ('Smile, chin size', ''),
  39: ('Lower jaw width', ''),
  38: ('Mouth position: up / down', ''),
  37: ('Face oval: width', ''),
  36: ('Lower jaw length', ''),
  35: ('Head size', ''),
  34: ('Jaw size', ''),
  33: ('Smile: upper lip', ''),
  32: ('Lower jaw size', ''),

  31: ('Face oval: width', ''),
  30: ('Hairstyle', ''),
  29: ('Hairstyle: left side', ''),
  28: ('Hairstyle', ''),
  27: ('Hairstyle', ''),
  26: ('Hairstyle: right side', ''),
  25: ('Neck width', ''),
  24: ('Hairstyle: background size', ''),
  23: ('Hairstyle', ''),
  22: ('Hairstyle', ''),
  21: ('Skin: pale / red', ''),
  20: ('Hairstyle', ''),
  19: ('Hairstyle: forhead right size, overall size', ''),
  18: ('Hairstyle', ''),
  17: ('Hairstyle', ''),
  16: ('Face oval: size', ''),

  15: ('Rotation + hair color', ''),
  14: ('Rotation + hairstyle', ''),
  13: ('Skin paleness + hair color', ''),
  12: ('Rotation + hairstyle', ''),
  11: ('Rotation + hair color', ''),
  10: ('Blond / black hair', ', slight rotation'),
  9: ('Hairstyle: color, bangs', ''),
  8: ('Hair color', ''),
  7: ('Hairstyle: color, bangs', ''),
  6: ('Lighting, hair color', ''),
  5: ('Hairstyle', ''),
  4: ('Hair length & color', ''),
  3: ('Left / right rotation', ''),
  2: ('Hairstyle, light', ''),
  1: ('Light bright / dark', ''),
  0: ('Head rotation + hairstyle', ''),
}

descriptions = {
  key: desc1 + '.' for key, (desc1, desc2) in _descriptions.items()
}

descriptions_full = {
  key: desc1 + desc2 + '.' for key, (desc1, desc2) in _descriptions.items()
}