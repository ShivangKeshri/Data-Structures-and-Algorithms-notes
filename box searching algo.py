def key_search(main_box):
    pile = main_box.make_a_pile_to_look_through
    while pile > 0:
        box = pile.grab_a_box()
        for item in box:
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print("found the key")


# recursion implementation in pile of boxes

def key_search(box):
    for item in box:
        if item.is_a_box():
            key_search(item)    #--> recursion implementation as we call the main function back.
        elif item.is_a_key():
            print("found the key")
            
