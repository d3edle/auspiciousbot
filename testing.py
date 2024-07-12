import datetime
 
now = datetime.datetime.now()
# print(now.hour * 12)
print(now.day)
# later = datetime.datetime(2024,6,9,19,30)
# difference = later-now
# print(difference.seconds)



# def hour_parse(rawtime):
#     #4:30pm
#     #4pm
#     #430pm
#     isam,ispm = False, False
    
#     if ':' in rawtime:
#         rawtime = rawtime[:rawtime.find(':')] + rawtime[rawtime.find(':')+1:]
        
#     if 'am' in rawtime:
#         isam = True
#         rawtime = rawtime[:rawtime.find('am')]
#     elif 'pm' in rawtime:
#         ispm = True
#         rawtime = rawtime[:rawtime.find('pm')]

#     if len(rawtime) == 4:
#         hour = int(rawtime[:2])
#         min = int(rawtime[2:])
#     if len(rawtime) == 3:
#         hour = int(rawtime[:1])
#         min = int(rawtime[1:])
#     if len(rawtime) == 1:
#         hour =int(rawtime)
#         min = 0
    
#     if isam != True and ispm != True:  #operating on the assumpation that if i say 7, it's likely 7pm
#         ispm = True
    
#     if ispm:
#         hour += 12
    
#     return hour, min
