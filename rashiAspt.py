movable = [1,4,7,10]                                   fixed = [2,5,8,11]
mutables = [3,6,9,12]                  
#get a sign                                    a_lord_sign = kona_s[2] #11

#we want to creat the list for all kendra rashi aspects [1, 4, 7],[6, 9, 12],[11, 2, 5]                                                      asptList = []
kendraList = []
        #is_it_fixed_or_mut_or_mov
        for numm in kendras_s:
            for listt, name in ((movable,'movable'),(fixed,'fixed'),(mutables,'mutables')):
                if numm in listt:
                    if name == 'movable':
                       asptList.append([numm,numm + 4,numm + 7,numm + 10])
                    elif name == 'fixed':
                       asptList.append([numm,numm + 2,numm + 5,numm + 8])
                    elif name == 'mutables':
                       asptList.append([numm,numm + 3,numm + 6,numm + 9])
                    break
        print(asptList)
        #join the list
        s_list = asptList[0] + asptList[1] + asptList[2]
        #reduce big nums
        for num in s_list:
            if num >= 13:
                nnum = num - 12
                kendraList.append(nnum)
            else:
                kendraList.append(num)
        #get a kona planet sign and search for it in kendra list
        print('kendraList = ',kendraList)
